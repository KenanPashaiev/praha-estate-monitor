import asyncio

from handlers.baseHandlers import *
from operations.filterOperations import *
from filters.layoutFilter import *
from monitoring.srealityClient import *

tasks = {}

replyMarkup = ReplyKeyboardMarkup([[ "Stop monitoring" ]], resize_keyboard=True)

async def startMonitoring(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global tasks
    chatId = update.effective_chat.id
    monitoringFilters = getFiltersForChat(chatId)
    tasks[chatId] = asyncio.get_event_loop().create_task(monitorProperties(context, chatId, monitoringFilters))
    logging.log(logging.INFO, "Started monitoring")

    await context.bot.send_message(chat_id=chatId, 
                                   text="Started monitoring\n", 
                                   reply_markup=replyMarkup)
    return MONITORING


async def stopMonitoring(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    tasks[chatId].cancel()
    await context.bot.send_message(chat_id=chatId, 
                                   text="Stopped monitoring\n", 
                                   reply_markup=filterReplyMarkup)

    return FILTERS


async def monitorProperties(context, chatId, monitoringFilters):
    while True:
        await fetchEstates(context, chatId, monitoringFilters)
        await asyncio.sleep(15)

