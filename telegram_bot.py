from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import os

# Telegram bot token
TOKEN = 'your_telegram_bot_token'

# Define the function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me an image and I will remove its background.')

# Define the function to handle images
def handle_image(update: Update, context: CallbackContext) -> None:
    # Check if the message contains an image
    if update.message.photo:
        # Get the photo file id
        file_id = update.message.photo[-1].file_id
        # Download the image
        file = context.bot.get_file(file_id)
        file.download('image.jpg')
        # Send image to backend server for background removal
        response = requests.post('https://www.remove.bg/', files={'image': open('image.jpg', 'rb')})
        # Send the processed image back to the user
        update.message.reply_photo(response.content)
        # Remove downloaded image
        os.remove('image.jpg')
    else:
        update.message.reply_text("Please send an image.")

# Set up the Telegram bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo & ~Filters.command, handle_image))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
