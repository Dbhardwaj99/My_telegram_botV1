import API_KEY as keys
from telegram.ext import *
import responses as res

print("Bot started..")


def start_command(update):
    update.message.reply_text("Type your username to get started.")


def help_command(update):
    update.message.reply_text("Google your doubts")


def handle_message(update):
    text = str(update.message.text).lower()
    response = res.sample_response(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("Start", start_command))
    dp.add_handler(CommandHandler("Help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()
