try:
    import praw
    from time import sleep
    import configparser
    import logging
    from output import *
except ImportError as e:
    print(f"Error importing module: {e}. Please ensure all required packages are installed. Run 'pip install -r requirements.txt' to install missing packages.")
    raise

class RedditUserbotClass():
    def __init__(self, logging_enabled=True):

        try:
            print("Importing .env configuration file.")
            self.config = configparser.ConfigParser()
            self.config.read('.env')
            print("✅ Configuration successfully read from .env file.")
        except Exception as e:
            print(f"❌ Error reading .env file: {e}. Please ensure the file exists and is properly formatted.")
            raise

        if logging_enabled:
            level_str = self.config['logging']['level'].upper()
            level = getattr(logging, level_str)
            filename = self.config['logging']['file']
            logging.basicConfig(level=level, filename=filename, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.info("Logging is enabled. Check the app.log file for details.")
        else:
            filename = self.config['logging']['file']
            logging.basicConfig(level=logging.CRITICAL, filename=filename, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.info("⚠️ Logging is disabled, only critical errors will be logged. Check the app.log file for details.")

        try:
            self.client_id_value = str(self.config['account_reddit']['client_id']).strip()
            self.client_secret_value = str(self.config['account_reddit']['client_secret']).strip()
            self.password_value = str(self.config['account_reddit']['password']).strip()
            self.user_agent_value = str(self.config['account_reddit']['user_agent']).strip()
            self.username_value = str(self.config['account_reddit']['username']).strip()
            self.subreddit_value = str(self.config['account_reddit']['subreddit']).strip()
            self.last_n_submissions_to_check = int(self.config['account_reddit'].get('number_of_submissions_to_check', 10))
            logging.info(f"✅ Reddit API credentials located and initialized.")
        except KeyError as e:
            logging.error(f"❌ Missing configuration for {e}. Please check your .env file.")
            raise

        try:
            reddit = praw.Reddit(
                client_id=self.client_id_value,
                client_secret=self.client_secret_value,
                password=self.password_value,
                user_agent=self.user_agent_value,
                username=self.username_value,
            )
            logging.info("✅ Reddit API client initialized.")
        except Exception as e:
            logging.error(f"❌ Error initializing Reddit client: {e}")
            raise

        self.reddit = reddit
        del self.client_id_value, self.client_secret_value, self.password_value, self.user_agent_value, self.username_value
        del reddit

    def userbot(self, upvote=False, upvote_clear=False, reply=False):
        logging.info("Starting userbot process.")
        for self.submission in self.reddit.subreddit(self.subreddit_value).new(limit=self.last_n_submissions_to_check):
            self.i = 0
            logging.info(f"Processing submission: {self.submission.title}")
            if self.i < self.last_n_submissions_to_check - 1:
                self.i += 1
                logging.info(f"Current submission {self.i} has {self.submission.num_comments} comments.")
                if self.submission.num_comments > 3 and self.submission.locked != True and self.submission.is_self == True:
                    pass
                else:
                    continue

            prBrightGray(f"ID: {self.submission.id}\tTitle: {self.submission.title}\tScore: {self.submission.score}\nURL: {self.submission.url}\nPost:", end = "\t")
            logging.info(f"ID: {self.submission.id}\tTitle: {self.submission.title}\tScore: {self.submission.score}\nURL: {self.submission.url}\nPost:")
            prBlue(f"{self.submission.selftext.strip()}",end="\n")
            logging.info(f"{self.submission.selftext.strip()}")
            self.submission.comment_sort = "new"
            self.top_comments = list(self.submission.comments)

            if len(self.top_comments) > 2:
                self.comment = self.reddit.comment(str(self.top_comments[1]))
                prBrightGray(f"https://www.reddit.com{self.comment.permalink}",end="\n\n")
                logging.info(f"https://www.reddit.com{self.comment.permalink}")
                prGreen(f"Comment: {self.comment.body}",end="\n")
                logging.info(f"Comment: {self.comment.body}")

                if upvote == True:
                    upvote_status = self.upvote_comment(upvote_clear)
                    if upvote_status == 0:
                        prBrightGray("✅ Userbot upvoted and cleared vote successfully.",end="\n")
                        logging.info("Userbot upvoted and cleared the vote successfully.")
                    elif upvote_status == 1:
                        prYellow("⚠️ Userbot upvoted successfully but did not clear the vote as per configuration. This might lead to an account ban as it's against Reddit TOS.",end="\n")
                        logging.info("⚠️ Userbot upvoted successfully but did not clear the vote as per configuration. This might lead to an account ban as it's against Reddit TOS.")
                    else:
                        prRed(f"Error upvoting to comment: {upvote_status}",end="\n")
                        logging.error(f"Error upvoting to comment: {upvote_status}")

                if reply == True:
                    reply_status = self.reply_comment()
                    if reply_status == 0:
                        prBrightGray("✅ Userbot replied successfully.",end="\n")
                        logging.info("✅ Successfully replied to the comment.")
                    else:
                        prRed(f"Error replying to comment: {reply_status}", end="\n")
                        logging.error(f"❌ Error replying to comment: {reply_status}")

                return 0

            else:
                continue

    def upvote_comment(self, upvote_clear=True):
        try:
            prBrightGray(f"Upvoting comment.", end="\n")
            logging.info(f"Upvoting comment.")
            self.comment.upvote()
            sleep(5)
            if upvote_clear:
                try:
                    self.comment.clear_vote() # Clearing the upvote by default to avoid account ban as it's against Reddit rules
                    return 0
                except Exception as e:
                    logging.error(f"Error clearing upvote: {e}")
                    return e
            else:
                prYellow(f"⚠️ Please clear the upvote to avoid account ban as it's against Reddit TOS.", end="\n")
                logging.info(f"⚠️ Please clear the upvote to avoid account ban as it's against Reddit TOS.")
                return 1

        except Exception as e:
            return e

    def reply_comment(self):
        try:
            from google import genai
            logging.info("✅ Google GenAI module imported successfully.")
        except ImportError as e:
            prRed(f"Error importing Google GenAI module: {e}. Please ensure the package is installed. Run 'pip install google-genai=={str(self.config['google_api']['google-genai']).strip()}' to install the missing package.", end="\n")
            logging.error(f"❌ Error importing Google GenAI module: {e}. Please ensure the package is installed. Run 'pip install google-genai=={str(self.config['google_api']['google-genai']).strip()}' to install the missing package.")
            raise

        try:
            self.response_base = str(self.config['google_api']['response_base']).strip()
            self.system_instruction = str(self.config['google_api']['system_instruction']).strip()
            logging.info(f"✅ Google Gemini API credentials located and initialized.")
        except KeyError as e:
            logging.error(f"❌ Missing configuration for {e}. Please check your .env file.")
            raise

        try:
            self.GEMINI_API_KEY = str(self.config['google_api']['GEMINI_API_KEY'])
            self.client = genai.Client(api_key=self.GEMINI_API_KEY)
            logging.info("✅ Google Gemini client initialized.")
        except Exception as e:
            logging.error(f"❌ Error initializing Google Gemini client: {e}")
            raise

        del self.GEMINI_API_KEY

        try:
            prBrightGray("Generating response...",end="\n")
            logging.info("Generating response...")
            self.response_base = str(self.response_base.format(
                comment_body=self.comment.body,
                submission_title=self.submission.title,
                submission_selftext=self.submission.selftext
            ))
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                config=genai.types.GenerateContentConfig(
                    system_instruction=self.system_instruction),
                contents=self.response_base
            )
            prBrightGray("Generated response:",end="\t")
            prPurple(f"{response.text}",end="\n")
            logging.info(f"✅ Generated response: {response.text}")
        except Exception as e:
            logging.error(f"❌ Error generating response: {e}")
            return e

        try:
            self.comment.reply(str(response.text))
            return 0
        except Exception as e:
            return e

if __name__ == "__main__":
    print("Program started. Initializing RedditUserbot.")
    RedditUserbot = RedditUserbotClass(True)
    success = RedditUserbot.userbot(True, True, True)
    if success == 0:
        logging.info("✅ Userbot ran successfully. Check the log file for details. 🥳 🎉")
        prGreen("✅ Userbot ran successfully. 🥳 🎉", end="\n")
    else:
        logging.error("❌ Userbot encountered an error. Check the log file for details.😭")
        prRed("❌ Userbot encountered an error. 😭", end="\n")

    prBrightPurple("🤖🎯 Check out my GitHub at ")
    prPurple("https://github.com/ParthProLegend")
    prBrightPurple(" and this project is located at ")
    prPurple("https://github.com/ParthProLegend/reddit-userbot-praw-basic")

    prCyan("\nRemember to star the repository if you find it useful! 🌟\n")

    Colour = ColorCycler()
    Colour.cycling_colors_print("Buy me a coffee at ")
    prPurple("https://ko-fi.com/parthprolegend")
    Colour.cycling_colors_print(" to support my work. ☕️")