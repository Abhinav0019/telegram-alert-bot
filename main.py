
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace this with your Telegram User ID to restrict who receives the alert
AUTHORIZED_USER_ID = 766100254

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id == AUTHORIZED_USER_ID:
        await update.message.reply_text("🔔 Bot is active! You’ll now receive breakout & swing alerts here.")
    else:
        await update.message.reply_text("❌ Unauthorized user. Access denied.")

# Sample alert function (replace this with real alert logic)
async def send_alert(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=AUTHORIZED_USER_ID, text="🚨 Sample Alert: HINDUNILVR - HTF OB Rejection + LTF CHoCH Entry")

def main() -> None:
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()

    application.add_handler(CommandHandler("start", start))

    # To test a scheduled alert (optional)
    # job_queue = application.job_queue
    # job_queue.run_once(send_alert, when=10)

    application.run_polling()

if __name__ == '__main__':
    main()
