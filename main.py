from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import time

TOKEN = '1683788665:AAF5TK7XXB395MOMhHVZsvn6Ic4jQgW5n84'


def time_now_now(update, context):
    time_now = time.localtime()
    time_now = time.strftime('%H:%M:%S', time_now)
    update.message.reply_text(time_now)


def data(update, context):
    data_now = time.localtime()
    data_now = time.strftime('%d-%m-%Y', data_now)
    update.message.reply_text(data_now)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("time", time_now_now))
    dp.add_handler(CommandHandler("data", data))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()