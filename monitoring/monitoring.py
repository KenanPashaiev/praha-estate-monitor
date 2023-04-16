import asyncio
import logging
from telegram import ReplyKeyboardMarkup, Update, Bot
from telegram.ext import ContextTypes

from handlers.states import MONITORING, FILTERS
from handlers.baseHandlers import filterReplyMarkup
from operations.chatOperations import getMonitoredChats, setIsMonitoringForChat
from operations.filterOperations import getFiltersForChat
from monitoring.srealityClient import fetchEstates

tasks = {}

replyMarkup = ReplyKeyboardMarkup([[ "Stop monitoring" ]], resize_keyboard=True)


async def startMonitoring(update: Update = None, context: ContextTypes.DEFAULT_TYPE = None):
    chatId = str(update.effective_chat.id)

    initializeMonitor(chatId, context.bot)
    setIsMonitoringForChat(chatId, True)
    logging.log(logging.INFO, "Started monitoring")
    await context.bot.send_message(chat_id=chatId, 
                                   text="Started monitoring\n",
                                   reply_markup=replyMarkup)
    return MONITORING


def initializeMonitors(token: str):
    monitoredChats = getMonitoredChats()
    bot = Bot(token)
    for chat in monitoredChats:
        initializeMonitor(chat.chatId, bot)


def initializeMonitor(chatId: str, bot: Bot):
    global tasks
    monitoringFilters = getFiltersForChat(chatId)
    tasks[chatId] = asyncio.get_event_loop().create_task(monitorEstates(bot, chatId, monitoringFilters))


async def stopMonitoring(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = str(update.effective_chat.id)
    tasks[chatId].cancel()

    setIsMonitoringForChat(chatId, False)
    await context.bot.send_message(chat_id=chatId, 
                                   text="Stopped monitoring\n", 
                                   reply_markup=filterReplyMarkup)

    return FILTERS


async def monitorEstates(bot: Bot, chatId: str, monitoringFilters):
    while True:
        await fetchEstates(bot, chatId, monitoringFilters)
        await asyncio.sleep(15)
