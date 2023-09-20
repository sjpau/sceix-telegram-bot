from telegram import Update
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    ContextTypes, 
    PicklePersistence,
    filters, 
)
import chess
import logging
from secrets import TOKEN

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi! I am a chess bot!"
    )

async def newmatch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.chat_data['board'] = chess.Board()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Created new board!',
    )

async def board(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_text = "Board not found!"
    if 'board' in context.chat_data.keys():
        reply_text = str(context.chat_data['board'])
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=reply_text,
    )

def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('newmatch', newmatch))
    app.add_handler(CommandHandler('board', board))

    app.run_polling(poll_interval=5)

if __name__ == '__main__':
    main()