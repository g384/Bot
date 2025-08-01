from pyrogram import Client, filters
import os
import subprocess

API_ID = 290666113
API_HASH = "cc5ba8ec50937aee6f4a8784a180d95b"
BOT_TOKEN = "8399264656:AAEGpfI_NC_8qKUh8N1xQGVndLWq2SnNSAs"

app = Client("media_downloader_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("👋 أهلًا بيك!\nأرسل رابط فيديو من (يوتيوب، فيسبوك، إنستا، تيك توك أو بينترست)، وأنا أحمله لك 🎬")

@app.on_message(filters.text & ~filters.command("start"))
def download_video(client, message):
    url = message.text.strip()
    output_filename = "video.%(ext)s"

    message.reply("⏳ جاري تحميل الفيديو...")

    try:
        subprocess.run(["yt-dlp", "-f", "best", "-o", output_filename, url], check=True)

        for file in os.listdir():
            if file.startswith("video.") and not file.endswith(".py"):
                message.reply_video(file)
                os.remove(file)
                break
    except Exception as e:
        message.reply(f"❌ خطأ أثناء التحميل:\n{e}")

app.run()