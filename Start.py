from telegram.ext import Updater, CommandHandler
from Handler import start, set_thumbnail, handle_upload, handle_download
from queue import Queue  # Import the Queue class

def main():
    update_queue = Queue()  # Creating a Queue instance
    updater = Updater("6625459474:AAEWMFsJYWg8QDb5aO56BRUvS4Mpul98TF8", update_queue=update_queue)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("thumbnail", set_thumbnail))
    dp.add_handler(CommandHandler("upload", handle_upload))
    dp.add_handler(CommandHandler("dl", handle_download))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
