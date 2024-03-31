import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from remove_bg import remove_bg # Assuming you have a function for background removal

# Telegram Bot token
TOKEN = '6782152543:AAGjdIk48iNCy58AyisxoxmvTJ44OJJAeic'

# Define the function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me an image and I will remove its background.')

# Define the function to handle images
def handle_image(update: Update, context: CallbackContext) -> None:
    # Check if the message contains an image
    if update.message.photo:
        # Get the photo file id
        file_id = update.message.photo[-1].file_id
        # Download the photo
        photo = context.bot.get_file(file_id)
        filename = os.path.join('downloads', f'{file_id}.jpg')
        photo.download(filename)
        # Remove background
        processed_image = remove_background(filename)
        # Send the processed image
        update.message.reply_photo(photo=open(processed_image, 'rb'))
        # Delete the downloaded image file
        os.remove(filename)
    else:
        update.message.reply_text("Please send an image.")

# Define the function to remove the background
def remove_background(image_path):
    # Your code to remove background goes here
    # Example: remove_bg(image_path)
    # Return path to the processed image
    return image_path

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handler for the /start command
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the message handler for images
    dispatcher.add_handler(MessageHandler(Filters.photo & ~Filters.command, handle_image))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
