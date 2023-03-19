import re
import logging
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from filterOptions import *
from operations.chatOperations import *
from operations.filterOperations import *
from markupHandlers.replyKeyboardMarkups import *
from handlers.states import *
from ranges.areaRange import AreaRange
from ranges.moveInDateRange import MoveInDateRange
from ranges.priceRange import PriceRange

async def moveInDateReply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await replyBase(update, context, MoveInDateRange, updateMoveInDateForChat)

async def priceReply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await replyBase(update, context, PriceRange, updatePriceForChat)

async def areaReply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await replyBase(update, context, AreaRange, updateAreaForChat)

async def replyBase(update: Update, context: ContextTypes.DEFAULT_TYPE, rangeClass, updateRangeForChat):
    chatId = update.effective_chat.id
    messageText = update.effective_message.text
    if messageText == cancelMessageText:
        await context.bot.send_message(chat_id=chatId, 
                                       text=f"Canceling {rangeClass.label()} range edit", 
                                       reply_markup=filterReplyMarkup)
        return FILTERS
    
    if not rangeClass.isValidString(messageText):
        await context.bot.send_message(chat_id=chatId, 
                                       text=f"Provided {rangeClass.label()} range format is not correct.\n"+
                                       f"Required format: {rangeClass.exampleString()}")
        return rangeClass.state()
        
    range = rangeClass.toRange(messageText)
    updateRangeForChat(chatId, range)
    await context.bot.send_message(chat_id=chatId, 
                                   text=f"{rangeClass.label()} range set to {range.toString()}",
                                   reply_markup=filterReplyMarkup)
    
    return FILTERS
