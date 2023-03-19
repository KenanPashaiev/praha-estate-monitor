import re
import logging
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from filterOptions import *
from filterOptions import *
from operations.chatOperations import *
from operations.filterOperations import *
from markupHandlers.replyKeyboardMarkups import *
from handlers.states import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chatId = update.effective_chat.id
    logging.log(logging.INFO, f"Chat '{str(chatId)}' started interacting with the bot")
    startNewChat(str(update.effective_chat.id))

    await context.bot.send_message(chat_id=chatId,
                                   text="Hey, I'm a bot that monitors SReality and Bezrealitky to find any apartments that suit you. You can start using me by specifying the filters and pressing 'Start monitoring'.", 
                                   reply_markup=filterReplyMarkup)
    return FILTERS

async def filters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    filters = getFiltersForChat(chatId)

    logging.log(logging.INFO, "User with ID "+str(chatId)+" is settings filters")
    await context.bot.send_message(chat_id=chatId,
                                   text="Your current filters are following:\n"+
                                   f"*Operation type*: {filters.offerType.toString()}\n" +
                                   f"*Estate Type*: {filters.estateType.toString()}\n" +
                                   f"*Layout*: {filters.layout.toString()}\n" +
                                   f"*District*: {filters.district.toString()}\n" +
                                   f"*Price*: {filters.priceRange.toString()} CZK\n" +
                                   f"*Area* : {filters.areaRange.toString()} m²\n" +
                                   f"*Move in date*: {filters.moveInDateRange.toString()}\n", 
                                   parse_mode='markdown')
    
async def layout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    replyMarkup = getLayoutKeyboardMarkup(chatId)
    await optionsBase(context, chatId, replyMarkup, LayoutFilter.label())
    
async def district(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    replyMarkup = getDistrictKeyboardMarkup(chatId)
    await optionsBase(context, chatId, replyMarkup, DistrictFilter.label())
    
async def offerType(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    replyMarkup = getOfferTypeKeyboardMarkup(chatId)
    await optionsBase(context, chatId, replyMarkup, OfferTypeFilter.label())

async def estateTypeOptions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    replyMarkup = getEstateTypeKeyboardMarkup(chatId)
    await optionsBase(context, chatId, replyMarkup, EstateTypeFilter.label())
    
async def optionsBase(context: ContextTypes.DEFAULT_TYPE, chatId: int, replyMarkup: InlineKeyboardMarkup, optionName: str):
    logging.log(logging.INFO, f"Chat '{str(chatId)}' is selecting {optionName}")
    await context.bot.send_message(chat_id=chatId, 
                                   text=f"Select {optionName}:\n", 
                                   reply_markup=replyMarkup)






