# Reddit Userbot Basic (PRAW)         <a href='https://ko-fi.com/parthprolegend' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi6.png?v=6' border='0' alt="Buy Me a Bo'oh'o'wa'er at ko-fi.com" /></a>

![Python](https://img.shields.io/badge/Python-3.12.6-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

This project is a Reddit userbot built using the Python Reddit API Wrapper (PRAW). The bot is designed to interact with Reddit by upvoting and replying to comments in a specific subreddit. It demonstrates basic usage of the PRAW library and serves as a starting point for building more advanced Reddit bots.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)
- [Notices](#notices)
  - [Reddit API Usage](#reddit-api-usage)
  - [License and Acknowledgements](#license-and-acknowledgements)
- [Example Output](#example-output)
- [Troubleshooting](#troubleshooting)
- [Contribution Guidelines](#contribution-guidelines)

## Features

- 🚀 Automatically upvotes and replies to comments in a specified subreddit.
- ⚙️ Configurable through an `.env` file.
- 🔗 Uses PRAW for seamless interaction with Reddit's API.

## Prerequisites

- Python 3.12.6 (NOT test for other versions)
- A Reddit account
- Reddit API credentials (client ID, client secret, username, password, and user agent)

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

3. Create a `.env` file in the root directory and add your Reddit API credentials:
   ```ini
   [account_reddit]
   client_id = YOUR_CLIENT_ID
   client_secret = YOUR_CLIENT_SECRET
   username = YOUR_USERNAME
   password = YOUR_PASSWORD
   user_agent = YOUR_USER_AGENT
   subreddit = YOUR_SUBREDDIT
   ```

   Note: For Setting Up the **[PRAW](https://github.com/praw-dev/praw)** interface to obtain client_id and client_secret, check out **[OAuth2 Quick Start:First Steps](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)**

## Usage

1. Run the bot:
   ```bash
   python main.py
   ```

2. The bot will upvote and reply to comments in the specified subreddit.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/parthprolegend)

## Notes

- The bot clears upvotes after a short delay to comply with Reddit's rules.
- Ensure that your bot's actions comply with Reddit's API terms of service.

## Notices

This project uses the PRAW library to interact with Reddit's API. PRAW is developed and maintained by the PRAW Dev Team. For more information, visit the [PRAW GitHub repository](https://github.com/praw-dev/praw).

### Reddit API Usage

- This bot interacts with Reddit's API and must comply with [Reddit's API Terms of Service](https://www.redditinc.com/policies/data-api-terms-of-service).
- Ensure that your bot's actions do not violate Reddit's rules or result in account suspension.

### License and Acknowledgements

- This project is licensed under the GNU Affero General Public License v3.0. See the [LICENSE](LICENSE) file for details.
- PRAW is licensed under the BSD 2-Clause License. See the [PRAW License](https://github.com/praw-dev/praw/blob/master/LICENSE.txt) for details.
- Reddit and the Reddit logo are registered trademarks of Reddit, Inc. This project is not affiliated with Reddit, Inc.

PRAW, an acronym for "Python Reddit API Wrapper", is a Python package that allows for simple access to Reddit's API. PRAW aims to be easy to use and internally follows all of **[Reddit's API rules](https://github.com/reddit/reddit/wiki/API)**. With PRAW there's no need to introduce `sleep` calls in your code. Give your client an appropriate user agent and you're set.

## Example Output

When the bot runs successfully, you might see output like this:

```
Successfully upvoted the comment: https://www.reddit.com/r/example/comments/abc123/comment/xyz456
Successfully replied to the comment: https://www.reddit.com/r/example/comments/abc123/comment/xyz456
```

## Troubleshooting

- **Issue**: `Invalid credentials` error.
  - **Solution**: Double-check your `.env` file for correct Reddit API credentials.
- **Issue**: Bot does not upvote or reply.
  - **Solution**: Ensure the subreddit exists and has new posts.
- **Issue**: Rate limit errors.
  - **Solution**: Reduce the bot's activity or add delays between actions.

## Contribution Guidelines

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/parthprolegend)