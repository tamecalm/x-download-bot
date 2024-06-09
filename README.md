# VidSpice Xplorer Bot

## Overview
VidSpice Xplorer Bot is a Telegram bot designed to download videos from X (formerly known as Twitter) based on tweet URLs. The bot also includes a donation feature powered by Chipper Cash to support its ongoing development and maintenance.

## Features
- Download videos from X using tweet URLs
- Donation feature via Chipper Cash for supporting the bot

## Getting Started
1. Clone the repository to your local machine.
2. Configure your Twitter API keys, Telegram bot token, Chipper Cash API key, and other environment variables in the `config/config.py` file.
3. Install the required dependencies by running `pip install -r config/requirements.txt`.
4. Deploy the bot on Railway.app using the provided deployment configuration.

## Configuration
### Environment Variables (in config/config.py)
- `TWITTER_API_KEY`: Your Twitter API key
- `TWITTER_API_SECRET`: Your Twitter API secret key
- `TWITTER_ACCESS_TOKEN`: Your Twitter access token
- `TWITTER_ACCESS_TOKEN_SECRET`: Your Twitter access token secret
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `CHIPPER_CASH_API_KEY`: Your Chipper Cash API key

## Usage
- Start the bot by sending `/start` to initiate the bot.
- Download a video from X (formerly known as Twitter) by providing the tweet URL using the `/download [tweet_url]` command.
- Donate to support the bot's development using the `/donate` command.

## Contributions
Contributions to the project are welcome! You can contribute by submitting bug reports, feature requests, or pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
