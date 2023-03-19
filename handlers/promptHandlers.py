

import logging
from telegram import Update
from telegram.ext import ContextTypes

from markupHandlers.replyKeyboardMarkups import cancelReplyMarkup
from operations.filterOperations import getFiltersForChat


async def pricePrompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    currentValue = getFiltersForChat(chatId).priceRange
    return await promptBase(context, chatId, currentValue)

async def areaPrompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    currentValue = getFiltersForChat(chatId).areaRange
    return await promptBase(context, chatId, currentValue)

async def moveInDatePrompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    currentValue = getFiltersForChat(chatId).moveInDateRange
    return await promptBase(context, chatId, currentValue)

async def promptBase(context: ContextTypes.DEFAULT_TYPE, chatId: int, currentValue):
    logging.log(logging.INFO, f"Chat {str(chatId)} is specifying {currentValue.label()}")
    await context.bot.send_message(chat_id=chatId, 
                                   text=f"Specify the {currentValue.label()} range.\n"+
                                   f"Current value: {currentValue.toString()}.\n" +
                                   f"For example: {currentValue.exampleString()}.\n",
                                   reply_markup=cancelReplyMarkup)
    
    return currentValue.state()