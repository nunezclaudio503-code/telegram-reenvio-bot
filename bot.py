from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

GROUP_IDS = [
    # -1001234567890,
    # -1009876543210,
]

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    for group_id in GROUP_IDS:
        try:
            await context.bot.forward_message(
                chat_id=group_id,
                from_chat_id=update.effective_chat.id,
                message_id=update.message.message_id
            )
        except Exception as e:
            print(f"Error enviando a {group_id}: {e}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, forward_message))

print("Bot iniciado...")
app.run_polling()
