from pyrogram import Client
from Handler import app
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

app = Client("my_bot")

@app.on_message(filters.command("start"))
def start(client, message):
    # Information about the developer
    developer_info = "Bot developed by [Developer's Name](https://github.com/developer_profile)"

    # Hosting information
    hosting_info = "Hosted on [Hosting Service](https://hosting_provider.com)"

    # Version of the bot
    version_info = "Bot Version: 1.0.0"

    # Source code information
    source_code_info = "Source code available at [GitHub](https://github.com/bot_repository)"

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Developer", url="https://github.com/developer_profile"),
                InlineKeyboardButton("Hosting", url="https://hosting_provider.com"),
            ],
            [
                InlineKeyboardButton("Source Code", url="https://github.com/bot_repository")
            ]
        ]
    )

    message.reply_text(
        f"{developer_info}\n\n{hosting_info}\n\n{version_info}\n\n{source_code_info}",
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

if __name__ == "__main__":
    app.run()
