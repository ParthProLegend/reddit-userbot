import praw
from time import sleep
import configparser


class RedditUserbotClass():
    def __init__(self):

        self.config = configparser.ConfigParser()
        self.config.read('.env')

        self.client_id_value = str(self.config['account_reddit']['client_id'])
        self.client_secret_value = str(self.config['account_reddit']['client_secret'])
        self.password_value = str(self.config['account_reddit']['password'])
        self.user_agent_value = str(self.config['account_reddit']['user_agent'])
        self.username_value = str(self.config['account_reddit']['username'])
        self.subreddit_value = str(self.config['account_reddit']['subreddit'])

        # print(self.client_id_value, self.client_secret_value, self.password_value, self.user_agent_value, self.username_value, self.subreddit_value)

        del self.config

        self.reddit = praw.Reddit(
            client_id=self.client_id_value,
            client_secret=self.client_secret_value,
            password=self.password_value,
            user_agent=self.user_agent_value,
            username=self.username_value,
        )

        del self.client_id_value, self.client_secret_value, self.password_value, self.user_agent_value, self.username_value

        self.reddit = self.reddit
        self.i = 0
        self.nth_comment_to_reply = 4

        print(self.reddit.user.me())

    def userbot(self):
        for self.submission in self.reddit.subreddit(self.subreddit_value).new(limit=self.nth_comment_to_reply):
            if self.i < self.nth_comment_to_reply - 1:
                self.i += 1
                continue
            # print(self.submission.title, self.submission.score, self.submission.id, self.submission.url, self.submission)
            self.submission.comment_sort = "new"
            self.top_comments = list(self.submission.comments)
            if len(self.top_comments) > 1:
                    self.comment = self.reddit.comment(str(self.top_comments[1]))
                    try:
                        self.comment.upvote()
                        sleep(5)
                        self.comment.clear_vote()  # Clear the upvote to avoid account ban as it's against Reddit rules
                        print(f"Successfully upvoted the comment: https://www.reddit.com{self.comment.permalink}")
                    except Exception as e:
                        print(f"Error upvoting comment: {e}")

                    try:
                        self.comment.reply("Hi man")
                        print(f"Successfully replied to the comment: https://www.reddit.com{self.comment.permalink}")
                    except Exception as e:
                        print(f"Error replying to comment: {e}")

if __name__ == "__main__":
    RedditUserbot = RedditUserbotClass()
    RedditUserbot.userbot()