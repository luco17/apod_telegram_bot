import os
from telegram.ext import Updater, CommandHandler
from apod import fetchAPOD
from datetime import date
from datetime import datetime

TGM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
DEFAULT_DATE = datetime.strftime(date.today(), "%Y-%m-%d")


def send_photo(update, context):
    title, url = fetchAPOD(context.args[0])
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=title)
    context.bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater(token=TGM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("nasa", send_photo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
