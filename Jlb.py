import logging
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Kuweka log level kwenye INFO
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)



async def start(update, context):
    """Send a message when the command /start is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a Telegram bot. Type /echo to see an echo of your message.")

async def echo(update, context):
    """Echo the user message."""
    await context.bot.copy_message(
    chat_id=update.effective_chat.id,
    from_chat_id=update.effective_chat.id,
    message_id=update.message.id
)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:

	application = Application.builder().token("6555046105:AAExFhj03molfJGTheCyAumCvz0o2JlfTIk").build()
	
	start_handler = CommandHandler('start', start)
	echo_handler = MessageHandler(filters.ALL, echo)
	application.add_handler(start_handler)
	application.add_handler(echo_handler)
	
	application.add_error_handler(error_handler)

	application.run_polling(allowed_updates=Update.ALL_TYPES)
	



if __name__ == '__main__':
    main()
