import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from apify_client import ApifyClient
import re

from telegramStylingScripts import *
from chatOperations import *
from layoutFilter import *
from offerTypeFilter import *
from propertyTypeFilter import *

async def layoutSelectCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    call_back_data = re.sub("\D", "", update.callback_query.data)
    chatId = update.effective_chat.id
    messageId = update.effective_message.id

    toggleLayoutCheckbox(str(chatId), LayoutFilter(int(call_back_data)))

    keyboard = styleLayoutInlineButtons(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.edit_message_reply_markup(chatId, messageId, reply_markup=reply_markup)

async def districtSelectCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    call_back_data = re.sub("\D", "", update.callback_query.data)
    chatId = update.effective_chat.id
    messageId = update.effective_message.id

    toggleDistrictCheckbox(str(chatId), DistrictFilter(int(call_back_data)))

    keyboard = styleDistrictInlineButtons(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.edit_message_reply_markup(chatId, messageId, reply_markup=reply_markup)

async def offerTypeSelectCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    call_back_data = re.sub("\D", "", update.callback_query.data)
    chatId = update.effective_chat.id
    messageId = update.effective_message.id

    toggleOfferType(str(chatId), OfferTypeFilter(int(call_back_data)))

    keyboard = styleOfferTypeInlineButtons(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.edit_message_reply_markup(chatId, messageId, reply_markup=reply_markup)

async def propertyTypeSelectCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    call_back_data = re.sub("\D", "", update.callback_query.data)
    chatId = update.effective_chat.id
    messageId = update.effective_message.id

    togglePropertyType(str(chatId), PropertyTypeFilter(int(call_back_data)))

    keyboard = stylePropertyTypeInlineButtons(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.edit_message_reply_markup(chatId, messageId, reply_markup=reply_markup)

