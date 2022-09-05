
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='main_bot-log.py', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print('Event: /start')
    update.message.reply_text(text='Hi User Bot. You called the /start command')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    bot = Updater(token=settings.API_KEY, use_context=True)
    bot_dp = bot.dispatcher
    bot_dp.add_handler(handler=CommandHandler("start", greet_user))
    bot_dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info(msg='Bot launched')

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()




