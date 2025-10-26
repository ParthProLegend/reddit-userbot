# Reddit Userbot (PRAW) v.0.2.0         <a href='https://ko-fi.com/parthprolegend' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi6.png?v=6' border='0' alt="Buy Me a Bo'oh'o'wa'er at ko-fi.com" /></a>

![Python](https://img.shields.io/badge/Python-3.12.6-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
<a href="https://cla-assistant.io/ParthProLegend/reddit-userbot-praw-basic"><img src="https://cla-assistant.io/readme/badge/ParthProLegend/reddit-userbot-praw-basic" alt="CLA assistant" /></a>

### ```⚠️ Project is in Alpha phase so bugs and functionality limitations are there.```
#### ```I have worked hard to fix the ones I found but still feel free to raise any issues. All contributions are welcome.```

This project is a Reddit userbot built using the Python Reddit API Wrapper (PRAW). The bot is designed to interact with Reddit by upvoting and replying to comments in a specific subreddit. It demonstrates basic usage of the PRAW library and serves as a starting point for building more advanced Reddit bots.

## Table of Contents

- [Changelog](#changelog)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)
- [Notices](#notices)
  - [Reddit API Usage](#reddit-api-usage)
  - [License and Acknowledgements](#license-and-acknowledgements)
  - [Liability and Warranty Disclaimer](#liability-and-warranty-disclaimer)
- [Example Output](#example-output)
- [Troubleshooting](#troubleshooting)
- [Contribution Guidelines](#contribution-guidelines)

## Changelog

### v.0.2.0 (Latest)
- Enhanced userbot functionality with improved logging, error handling, and colored terminal output.
- Integrated Google GenAI (Gemini) for generating intelligent replies to comments.
- Added configurable options for upvoting, replying, and clearing votes.
- Introduced `output.py` for color formatting and cycling.
- Updated dependencies and added comprehensive API usage notes.
- Improved documentation with detailed setup instructions and troubleshooting.

### v.0.1.0 (Initial Release)
- Basic Reddit userbot using PRAW for upvoting and replying to comments.
- Simple configuration via `.ini` file.
- Basic error handling and logging.

## Features

- 🚀 Automatically upvotes and replies to comments in a specified subreddit.
- ⚙️ Configurable through an `.ini` file.
- 🔗 Uses PRAW for seamless interaction with Reddit's API.
- 🛠️ Improved logging and error handling for better debugging.
- 🎨 Colored output in the terminal for enhanced visibility.
- 🆕 Enhanced userbot functionality with options for upvoting, replying, and clearing votes.
- 🤖 Integrated Google GenAI (Gemini) for generating intelligent replies.
- 💻 (Upcoming) local model support via REST API
- 🖥️ (Upcoming) local model support via OpenAI API
- 📂 `output.py` file for handling output colour formatting and color cycling (looked fun in hindsight)

## Prerequisites

- Python 3.12.6 (NOT tested for other versions)
- A Reddit account
- Reddit API credentials (client ID, client secret, username, password, and user agent)
- Google account to obtain API key (from Google AI Studio) for replies
- Required Python packages (see `requirements.txt` for full list):
  - `praw==7.8.1`
  - `google-genai==1.44.0`

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/parthprolegend)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ParthProLegend/reddit-userbot-praw-basic.git
   cd reddit-userbot-praw-basic
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: It is recommended to use a virtual environment to avoid conflicts with system packages. Create and activate one with:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. Create a `.ini` file in the root directory and add your Reddit API credentials:
   ```ini
   [account_reddit]
   client_id = YOUR_CLIENT_ID
   client_secret = YOUR_CLIENT_SECRET
   username = YOUR_USERNAME
   password = YOUR_PASSWORD
   user_agent = YOUR_USER_AGENT
   subreddit = YOUR_SUBREDDIT
   number_of_submissions_to_check = NUMBER (default:20 if not provided)
   ```

   **Note**: The `.ini` file contains sensitive information (API keys, credentials) and is not tracked by Git (see `.gitignore`). Do not commit it to version control to avoid exposing your credentials.

   Note: For Setting Up the **[PRAW](https://github.com/praw-dev/praw)** interface to obtain client_id and client_secret, check out **[OAuth2 Quick Start:First Steps](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)**

4. (optional) Generate your own API key from **[Google AI Studio](https://aistudio.google.com/api-keys)** and here's the Guide to generate API key on **[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key)**

5. Additional configuration in the `.ini` file is required for logging and Google GenAI integration.
   ```ini
   [logging]
   level = INFO
   file = app.log

   [google_api]
   google-genai = 1.44.0
   GEMINI_API_KEY = YOUR_API_KEY
   system_instruction = YOUR_SYSTEM_INTRUCTIONS (like:"Always be friendly and polite.", etc.)
   response_base = RESPONSE_BASE {having 3 entries as "{comment_body}", "{submission_title}" and "{submission_selftext}"}
                  (like: 'Respond to \"{comment_body}\" which was a response to \"Title: {submission_title} and Content: {submission_selftext}\"'.)
    ```

## Usage

1. Run the bot:
   ```bash
   python main.py
   ```

2. The bot will upvote and reply to comments in the specified subreddit.

3. (Pending Implementation) Configure the bot's behavior in the `.ini` file:
   ```ini
   [bot_settings]
   upvote_comments = True
   reply_to_comments = True
   clear_votes = True
   ```

4. To use Google GenAI (Gemini) for replies, set up the `GOOGLE_API_KEY` in the `.ini` file.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/parthprolegend)

## Notes

- The bot clears upvotes after a short delay to comply with Reddit's rules.
- Ensure that your bot's actions comply with Reddit's API terms of service.
- For detailed output logs, check the `app.log` file or whatever is defined in your .ini.
- The logging configuration can be adjusted in the `main.py` and `.ini` file. By default, it logs to `app.log` with a log level of `INFO`.
- The `ColorCycler` class is used for cycling colors in terminal output. Ensure your terminal supports ANSI colors.

## Example .ini file

The bot need .ini file to run successfully, like this sample (with auto-replying enabled):

For Setting Up the **[PRAW](https://github.com/praw-dev/praw)** interface to obtain client_id and client_secret, check out **[OAuth2 Quick Start:First Steps](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)**

```ini
[account_reddit]
client_id = YOUR_CLIENT_ID
client_secret = YOUR_CLIENT_SECRET
password = YOUR_ACCOUNT_PASSWORD
user_agent = PythonDesktop:PRAW:0.0.2 (by /u/RedditUsername for Testing Purposes)
username = YOUR_ACCOUNT_USERNAME
subreddit = SUBREDDIT_NAME_WHERE_YOU_WANT_TO_RUN_THE_BOT
number_of_submissions_to_check = NUMBER_OF_SUBMISSIONS_TO_CHECK_IN_THE_SUB_USING_NEW_SORTING

[google_api]
google-genai = 1.44.0
GEMINI_API_KEY = YOUR_GEMINI_API_KEY
system_instruction = YOUR_SYSTEM_INSTRUCTION (like: You are a human. Always be family friendly and polite, do not lie, do not respond professionally like a bot. You are not OP, and you does not refer to you.)
response_base = YOUR_RESPONSE_BASE (like: Give a short response to "{comment_body}" in response to a reddit with \"Title: {submission_title} and Content: {submission_selftext}\" in about 20 words.)

[logging]
enabled = True ; (Not Implemented Yet, planned)
level = INFO (Choose between DEBUG/INFO)
file = app.log (or any FILE_NAME.log)

[configuration]
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
PROXY = None
REQUEST_DELAY = 15
MAX_RETRIES = 10
ERROR_TIMEOUT = 60
```

## Notices

This project uses the PRAW library to interact with Reddit's API. PRAW is developed and maintained by the PRAW Dev Team. For more information, visit the [PRAW GitHub repository](https://github.com/praw-dev/praw).

### Reddit API Usage

- This bot interacts with Reddit's API and complies with [Reddit's API Terms of Service](https://www.redditinc.com/policies/data-api-terms-of-service).
- Ensure that the bot's actions do not violate Reddit's rules resulting in your account suspension.
- **Important Notes**:
  - Reddit API access requires a properly configured app. Follow the OAuth setup guide linked in Installation.
  - Be aware of Reddit's rate limits; excessive requests may lead to temporary bans. The bot includes built-in delays to mitigate this.

### Google Gemini API Usage

- This bot interacts with Google's API and complies with [Google's Gemini API Terms of Service](https://ai.google.dev/gemini-api/terms).
- For more information, visit the [Google Gemini API documentation](https://ai.google.dev/gemini-api/docs).
- **Important Notes**:
  - Google Gemini API usage may incur costs beyond the free tier limits. Check [Google's pricing](https://ai.google.dev/pricing) for details.
  - Keep your `GEMINI_API_KEY` secure and do not share it publicly to avoid unauthorized usage and potential charges.
  - The bot uses the "gemini-2.5-flash" model; ensure your API key has access to this model or adjust in the code if needed.

### License and Acknowledgements

- This project is licensed under the GNU Affero General Public License v3.0. See the [LICENSE](LICENSE) file for details.
- PRAW is licensed under the BSD 2-Clause License. See the [PRAW License](https://github.com/praw-dev/praw/blob/master/LICENSE.txt) for details.
- Google GenAI (Gemini) is integrated into this project for enhanced reply generation. For more information, visit the [Google Gemini API documentation](https://ai.google.dev/gemini-api/docs).
- Google and Gemini are trademarks of Google LLC. This project is not affiliated with Google, LLC or any of their partners.
- Reddit and the Reddit logo are registered trademarks of Reddit, Inc. This project is not affiliated with Reddit, Inc or any of their partners.

PRAW, an acronym for "Python Reddit API Wrapper", is a Python package that allows for simple access to Reddit's API. PRAW aims to be easy to use and internally follows all of **[Reddit's API rules](https://github.com/reddit/reddit/wiki/API)**. With PRAW there's no need to introduce `sleep` calls in your code. Give your client an appropriate user agent and you're set.

### Liability and Warranty Disclaimer

- This project is provided "as is" without any warranties or guarantees. Use it at your own risk.
- The author is not liable for any damages or issues arising from the use of this project.
- It is your responsibility to ensure that your use of this project complies with Reddit's API terms and any other applicable laws.

## Example Output

When the bot runs at INFO level logging successfully, you might see colored output like this (colors depend on your terminal support):

```h
ID: abc123	Title: Example Title	Score: 42
URL: https://www.reddit.com/r/example/comments/abc123
Post: This is the post content.

https://www.reddit.com/r/example/comments/abc123/comment/xyz456

Comment: This is a comment.

✅ Userbot upvoted and cleared vote successfully.
✅ Userbot replied successfully.

🤖🎯 Check out my GitHub at https://github.com/ParthProLegend
🤖🎯 and this project is located at https://github.com/ParthProLegend/reddit-userbot-praw-basic

Remember to star the repository if you find it useful! 🌟

Buy me a coffee at https://ko-fi.com/parthprolegend to support my work. ☕️
```

## Troubleshooting

- **Issue**: `Invalid credentials` error.
  - **Solution**: Double-check your `.ini` file for correct Reddit API credentials.
- **Issue**: Bot does not upvote or reply.
  - **Solution**: Ensure the subreddit exists and has new posts.
- **Issue**: Rate limit errors.
  - **Solution**: Reduce the bot's activity or add delays between actions.
- **Issue**: Google GenAI integration problems.
  - **Solution**: Verify `GOOGLE_API_KEY` in the `.ini` file and check your Google Cloud project settings.
- **Issue**: Colored terminal output not working.
  - **Solution**: Ensure your terminal supports ANSI colors. If using Windows, consider using Windows Terminal or enabling ANSI support in the command prompt.

## Contribution Guidelines

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

For bug reports or feature requests, please open an issue on the [GitHub repository](https://github.com/ParthProLegend/reddit-userbot-praw-basic/issues).

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/parthprolegend)
