import os
import tweepy
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Import configuration variables from config.py
from config.config import *

# Authenticate Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Initialize Telegram bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Bot commands
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to VidSpice Xplorer Bot! You can download videos from X (formerly known as Twitter) by sending the tweet URL."
    )

def download_video(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("Please provide a tweet URL after the /download command.")
        return

    tweet_url = context.args[0]
    
    try:
        # Get tweet details
        tweet_id = tweet_url.split("/")[-1]
        tweet = api.get_status(tweet_id)
        # Check if media is a video
        if "video_info" in tweet.extended_entities["media"][0]:
            video_url = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
            # Download video
            video_file = requests.get(video_url)
            # Save video locally
            with open("downloaded_video.mp4", "wb") as file:
                file.write(video_file.content)
            # Send video to user
            bot.send_video(chat_id=update.message.chat_id, video=open("downloaded_video.mp4", "rb"))
            # Delete the local video file
            os.remove("downloaded_video.mp4")
        else:
            update.message.reply_text("The provided tweet does not contain a video.")
    except tweepy.TweepError as e:
        update.message.reply_text(f"Error: {e}")

def donate(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Please enter the amount you would like to donate and the currency code separated by a space. For example: '10 USD' for 10 US dollars."
    )

    # Add a handler to wait for user input after the donation command
    return "WAITING_AMOUNT"

def handle_donation_amount(update: Update, context: CallbackContext):
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

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Commands:\n"
        "/start - Start the bot\n"
        "/download [tweet_url] - Download a video from X (formerly known as Twitter)\n"
        "/donate - Donate to support the bot\n"
        "/help - Show available commands"
    )

def unknown_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry, I don't understand that command. Please use /help to see available commands."
    )

if __name__ == "__main__":
    # Initialize Updater and Dispatcher
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download_video))
    dispatcher.add_handler(CommandHandler("donate", donate))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_donation_amount))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))

    # Start the bot
    updater.start_polling()
    updater.idle()
