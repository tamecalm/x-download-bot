
import tweepy
import os
from config.config import *

# Authenticate Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Initialize Telegram bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Bot commands
def start(update, context):
    update.message.reply_text(
        "Welcome to Twitter Downloader Bot! You can download tweets by using the /download command followed by the tweet ID."
    )

def download_tweet(update, context):
    if not context.args:
        update.message.reply_text("Please provide a tweet ID after the /download command.")
        return

    tweet_id = context.args[0]
    
    try:
        tweet = api.get_status(tweet_id)
        tweet_text = f"Tweet ID: {tweet_id}\n\n{tweet.text}"
        bot.send_message(chat_id=update.message.chat_id, text=tweet_text)
    except tweepy.TweepError as e:
        update.message.reply_text(f"Error: {e}")

def donate(update, context):
    update.message.reply_text(
        "Please enter the amount you would like to donate and the currency code separated by a space. For example: '10 USD' for 10 US dollars."
    )

    # Add a handler to wait for user input after the donation command
    return "WAITING_AMOUNT"

def handle_donation_amount(update, context):
    amount, currency = context.message.text.split()
    
    response = requests.post(
        "https://api.chippercash.com/v1/payments/send",
        headers={"Authorization": f"Bearer {CHIPPER_CASH_API_KEY}"},
        json={
            "amount": float(amount),
            "currency": currency.upper(),
            "recipient": "your_chipper_cash_account_id",
        }
    )

    if response.status_code == 200:
        update.message.reply_text("Thank you for your donation!")
    else:
        update.message.reply_text("Failed to process donation. Please try again later.")

def help_command(update, context):
    update.message.reply_text(
        "Commands:\n"
        "/start - Start the bot\n"
        "/download [tweet_id] - Download a tweet\n"
        "/donate - Donate to support the bot\n"
        "/help - Show available commands"
    )

def unknown_command(update, context):
    update.message.reply_text(
        "Sorry, I don't understand that command. Please use /help to see available commands."
    )

if __name__ == "__main__":
    # Initialize Updater and Dispatcher
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download_tweet))
    dispatcher.add_handler(CommandHandler("donate", donate))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_donation_amount))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))

    # Start the bot
    updater.start_polling()
    updater.idle()
