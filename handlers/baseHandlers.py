import logging
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from operations.chatOperations import startNewChat
from operations.filterOperations import getFiltersForChat, LayoutFilter, DistrictFilter, OfferTypeFilter, EstateTypeFilter
from markupHandlers.replyKeyboardMarkups import filterReplyMarkup
from markupHandlers.inlineKeyboardMarkups import getLayoutKeyboardMarkup, getDistrictKeyboardMarkup, getOfferTypeKeyboardMarkup, getEstateTypeKeyboardMarkup
from monitoring.monitoring import stopMonitoring
from handlers.states import FILTERS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chatId = update.effective_chat.id
    stopMonitoring(update, context)
    logging.log(logging.INFO, f"Chat '{str(chatId)}' started interacting with the bot")
    startNewChat(str(update.effective_chat.id))

    await context.bot.send_message(chat_id=chatId,
                                   text="Hey, I'm a bot that monitors SReality and Bezrealitky to find any apartments that suit you. You can start using me by specifying the filters and pressing 'Start monitoring'.", 
                                   reply_markup=filterReplyMarkup)
    return FILTERS

async def filters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    filters = getFiltersForChat(chatId)

    if(filters == None):
        await context.bot.send_message(chat_id=chatId, text="Please start the bot first using /start command.")
        return

    logging.log(logging.INFO, "User with ID "+str(chatId)+" is settings filters")
    await context.bot.send_message(chat_id=chatId,
                                   text="Your current filters are following:\n"+
                                   f"*{filters.offerType.label()}*: {filters.offerType.toString()}\n" +
                                   f"*{filters.estateType.label()}*: {filters.estateType.toString()}\n" +
                                   f"*{filters.layout.label()}*: {filters.layout.toString()}\n" +
                                   f"*{filters.district.label()}*: {filters.district.toString()}\n" +
                                   f"*{filters.priceRange.label()}*: {filters.priceRange.toString()} CZK\n" +
                                   f"*{filters.areaRange.label()}*: {filters.areaRange.toString()} m²\n" +
                                   f"*{filters.moveInDateRange.label()}*: {filters.moveInDateRange.toString()}\n", 
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






