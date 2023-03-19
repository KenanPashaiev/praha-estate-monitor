import re
from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardMarkup

from filterOptions import *
from operations.filterOperations import *
from filters.layoutFilter import *
from filters.offerTypeFilter import *
from filters.estateTypeFilter import *

async def layoutSelectCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    call_back_data = re.sub("\D", "", update.callback_query.data)
    chatId = update.effective_chat.id
    messageId = update.effective_message.id

    toggleLayoutCheckbox(str(chatId), LayoutFilter(int(call_back_data)))

    keyboard = getLayoutOptions(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.edit_message_reply_markup(chatId, messageId, reply_markup=reply_markup)

async def districtSelectCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    call_back_data = re.sub("\D", "", update.callback_query.data)
    chatId = update.effective_chat.id
    messageId = update.effective_message.id

    toggleDistrictCheckbox(str(chatId), DistrictFilter(int(call_back_data)))

    keyboard = getDistrictOptions(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.edit_message_reply_markup(chatId, messageId, reply_markup=reply_markup)

async def offerTypeSelectCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    call_back_data = re.sub("\D", "", update.callback_query.data)
    chatId = update.effective_chat.id
    messageId = update.effective_message.id

    toggleOfferType(str(chatId), OfferTypeFilter(int(call_back_data)))

    keyboard = getOfferTypeOptions(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.edit_message_reply_markup(chatId, messageId, reply_markup=reply_markup)

async def estateTypeSelectCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    call_back_data = re.sub("\D", "", update.callback_query.data)
    chatId = update.effective_chat.id
    messageId = update.effective_message.id

    toggleEstateType(str(chatId), EstateTypeFilter(int(call_back_data)))

    keyboard = getEstateTypeOptions(update.effective_chat.id)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.edit_message_reply_markup(chatId, messageId, reply_markup=reply_markup)

