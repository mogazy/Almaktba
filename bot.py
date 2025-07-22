import os, logging
from flask import Flask, request
import telegram

TOKEN   = os.getenv("8105420365:AAHOTbafGjhiWtr9UE3BJFXZF-4MybdJv1c")
PORT    = int(os.environ.get("PORT", 5000))
bot     = telegram.Bot(TOKEN)
app     = Flask(__name__)

@app.route("/" + TOKEN, methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    if update.message and update.message.text == "/start auto":
        chat_id = update.message.chat.id
        bot.send_message(chat_id, "مرحباً! هذه رسالتك التلقائية 🎉")

    return "ok"

if __name__ == "__main__":
    # (اختياري) لتشغيل Webhook تلقائيًا عند الإقلاع
    webhook_url = f"https://your-app.onrender.com/{TOKEN}"
    bot.set_webhook(webhook_url)
    app.run(host="0.0.0.0", port=PORT)
