# Прикрутить бота к задачам с предыдущего семинара:
    # 1) Создать калькулятор для работы с рациональными и комплексными числами,
    #    организовать меню, добавив в неё систему логирования
    # 2) Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import logging
from CALC_development import *
from Phone_book_project import *

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola, compadre! At your service!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(InlineQueryResultArticle(id=query.upper(), title='Caps',
                   input_message_content=InputTextMessageContent(query.upper())))
    await context.bot.answer_inline_query(update.inline_query.id, results)
# ___________________________
# async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# async def phonebook(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
# ___________________________

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, unknown command.")

if __name__ == '__main__':
    application = ApplicationBuilder().token('5711638068:AAFergmX5gtya3X4L0o9DtGQbF-mK__M-l8').build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    inline_caps_handler = InlineQueryHandler(inline_caps)
    # calc_handler = CommandHandler('calc', calc)
    # phonebook_handler = CommandHandler('phonebook', phonebook)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(inline_caps_handler)
    # application.add_handler(calc_handler)
    # application.add_handler(phonebook_handler)
    application.add_handler(unknown_handler)


    application.run_polling()