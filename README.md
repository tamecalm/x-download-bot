# VidSpice Xplorer Bot

## Overview
VidSpice Xplorer Bot is a Telegram bot designed to download videos from X (formerly known as Twitter) based on tweet URLs. The bot also includes a donation feature powered by Chipper Cash to support its ongoing development and maintenance.

## Getting Started
1. Clone the repository to your local machine.
2. Set up your Vercel account and install the Vercel CLI.
3. Configure your environment variables in the Vercel dashboard or using Vercel CLI.
4. Update the `scripts/twitter_downloader.py` file with your Telegram bot token, Twitter API keys, Chipper Cash API key, and other configuration details.
5. Deploy the bot on Vercel using the Vercel CLI or Vercel dashboard.

## Configuration
### Environment Variables
Ensure the following environment variables are set in Vercel:
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
- Use the `/help` command to see available commands.

## Contributions
Contributions to the project are welcome! You can contribute by submitting bug reports, feature requests, or pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
