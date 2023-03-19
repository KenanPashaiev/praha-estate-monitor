import re
import logging
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from filterOptions import *
from operations.chatOperations import *
from operations.filterOperations import *
from markupHandlers.replyKeyboardMarkups import *

FILTERS, SETMOVEINDATE, SETPRICE, SETAREA, MONITORING = range(5)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logging.log(logging.INFO, "User with ID "+str(update.effective_chat.id)+" started interacting with the bot")
    startNewChat(str(update.effective_chat.id))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hey, I'm a bot that monitors SReality and Bezrealitky to find any apartments that suit you. You can start using me by specifying the filters and pressing 'Start monitoring'.", 
                                   reply_markup=filterReplyMarkup)
    return FILTERS

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = InlineKeyboardMarkup([])
    logging.log(logging.INFO, "User with ID "+str(update.effective_chat.id)+" is settings filters")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Your current filters are following:\n"+
                                   "/offerType - Estate operation type. Values: ['sale', 'rent', 'auction']\n" +
                                   "/type - Estate type. Values: ['apartment', 'house', 'land']\n" +
                                   "/layout - Layout of the estate, for example: '3+kt, 3+1, 4+kt, 4+1'\n" +
                                   "/location, for example: 'Praha 1, Praha 2, Czechia'\n" +
                                   "/minPrice, for example: '15000-25000', '-25000'\n" +
                                   "/maxPrice, for example: '15000-25000', '-25000'\n" +
                                   "/minArea, for example: '15000-25000', '-25000'\n" +
                                   "/maxArea, for example: '90'\n"
                                   , reply_markup=reply_markup)

async def filters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    filters = getFiltersForChat(update.effective_chat.id)

    logging.log(logging.INFO, "User with ID "+str(update.effective_chat.id)+" is settings filters")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Your current filters are following:\n"+
                                   "*Operation type*: " + filters.offerType.toString() + "\n" +
                                   "*Type*: " + filters.type.toString() + "\n" +
                                   "*Layout*: " + filters.layout.toString() + "\n" +
                                   "*District*: " + filters.district.toString() + "\n" +
                                   "*Price*: " + str(filters.minPrice if filters.minPrice > 0 else "") + " - " + str(filters.maxPrice if filters.maxPrice < 10000000 else "") + " CZK\n" +
                                   "*Move in date*: " + str(filters.moveInDateFrom if filters.moveInDateFrom is not None else "") + " - " + str(filters.moveInDateTo if filters.moveInDateTo is not None else "") + "\n" +
                                   "*Area* : " + str(filters.minArea if filters.minArea > 0 else "") + " - " + str(filters.maxArea if filters.maxArea < 10000000 else "") + " m²\n"
                                   , parse_mode='markdown')
    
async def layout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = getLayoutOptions(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    logging.log(logging.INFO, "User with ID "+str(update.effective_chat.id)+" is selecting layout")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Select layout", reply_markup=reply_markup)
    
async def district(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = getDistrictOptions(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    logging.log(logging.INFO, "User with ID "+str(update.effective_chat.id)+" is selecting district")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Select district", reply_markup=reply_markup)
    
async def offerType(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = getOfferTypeOptions(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    logging.log(logging.INFO, "User with ID "+str(update.effective_chat.id)+" is selecting operation type")
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Select operation type\n", reply_markup=reply_markup)

async def type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    keyboard = getEstateTypeOptions(chatId)
    reply_markup = InlineKeyboardMarkup(keyboard)

    logging.log(logging.INFO, "User with ID "+str(chatId)+" is selecting estate type")
    await context.bot.send_message(chat_id=chatId, 
                                   text="Select estate type\n", reply_markup=reply_markup)




async def moveInDate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    logging.log(logging.INFO, "User with ID "+str(chatId)+" is specifying price")
    await context.bot.send_message(chat_id=chatId, 
                                   text="Specify which move in date range.\n"
                                   "You can specify multiple locations separated with commas.\n"+
                                   "For example: 'Praha 1, Praha 5, Czechia' or 'Říčany u Prahy, Czechia'", 
                                   reply_markup=cancelReplyMarkup)
    
    return SETMOVEINDATE

async def setMoveInDate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    messageText = update.effective_message.text

    if messageText == cancelMessageText:
        await context.bot.send_message(chat_id=chatId, 
                                       text="Canceling move in date edit", 
                                       reply_markup=filterReplyMarkup)
        return FILTERS
    
    setMoveInDate(chatId, messageText)
    await context.bot.send_message(chat_id=chatId, 
                                   text="Move in date set to "+messageText,
                                   reply_markup=filterReplyMarkup)
    return FILTERS




async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    logging.log(logging.INFO, "User with ID "+str(chatId)+" is specifying price")
    await context.bot.send_message(chat_id=chatId, 
                                   text="Specify the price range.\n"+
                                   "For example: '10 000 - 35 000' to specify both min and max. \n'10 000 -' to specify only min. \n'- 35 000' to specify only max", reply_markup=cancelReplyMarkup)
    
    return SETPRICE


async def setPrice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    messageText = update.effective_message.text
    if messageText == cancelMessageText:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text="Canceling price range edit", 
                                       reply_markup=filterReplyMarkup)
        return FILTERS
    
    messageText = update.effective_message.text.replace(" ", "")
    pattern = re.compile("^(\d+)?-?(\d+)?$")
    
    if not (pattern.fullmatch(messageText) and "-" in messageText):
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text="Provided price range is not correct.\n"+
                                       "For example: '10 000 - 35 000' to specify both min and max. \n"+
                                       "'10 000 -' to specify only min. \n"+
                                       "'- 35 000' to specify only max")
        return SETPRICE
        
    setPriceForChat(chatId, messageText)
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Price range set to "+messageText,
                                   reply_markup=filterReplyMarkup)
    return FILTERS



async def area(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    logging.log(logging.INFO, "User with ID "+str(chatId)+" is specifying area")
    await context.bot.send_message(chat_id=chatId, 
                                   text="Specify the area range.\n"+
                                   "For example: '45 - 80' to specify both min and max. \n'45 -' to specify only min. \n'- 80' to specify only max", reply_markup=cancelReplyMarkup)
    
    return SETAREA


async def setArea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatId = update.effective_chat.id
    messageText = update.effective_message.text
    if messageText == cancelMessageText:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text="Canceling area range edit", 
                                       reply_markup=filterReplyMarkup)
        return FILTERS
    
    messageText = update.effective_message.text.replace(" ", "")
    pattern = re.compile("^(\d+)?-?(\d+)?$")
    
    if not (pattern.fullmatch(messageText) and "-" in messageText):
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text="Provided area range is not correct.\n"+
                                       "For example: '45 - 80' to specify both min and max. \n"+
                                       "'45 -' to specify only min. \n"+
                                       "'- 80' to specify only max")
        return SETAREA
        
    setAreaForChat(chatId, messageText)
    await context.bot.send_message(chat_id=chatId, 
                                   text="Area range set to "+messageText,
                                   reply_markup=filterReplyMarkup)
    return FILTERS



