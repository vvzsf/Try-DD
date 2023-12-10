from pyrogram import Client filters
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to handle the welcome message
@app.on_chat_member_updated()
def welcome(client, message):
    chat_id = message.chat.id
    new_member = message.new_chat_member

    if new_member:
        username = new_member.username if new_member.username else new_member.first_name
        welcome_message = f"Welcome, @{username}! Thanks for joining."

        # Send welcome message
        app.send_message(chat_id, welcome_message)

# Command to set a custom thumbnail
@app.on_message(filters.command("thumbnail"))
def set_thumbnail(client, message):
    # Handle logic to set a custom thumbnail
    pass

# Command to upload a file
@app.on_message(filters.command("upload"))
def upload_file(client, message):
    # Handle logic to upload a file
    pass

# Command for using ffmpeg support
@app.on_message(filters.command("dl"))
def ffmpeg_support(client, message):
    # Handle logic with ffmpeg support
    pass

# Run the bot
app.run()
