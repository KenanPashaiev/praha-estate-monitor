import re
from telegram import Update
from telegram.ext import ContextTypes

from filterOptions import getLayoutKeyboardMarkup, getDistrictKeyboardMarkup, getOfferTypeKeyboardMarkup, getEstateTypeKeyboardMarkup
from operations.filterOperations import toggleLayoutCheckbox, toggleDistrictCheckbox, toggleOfferType, toggleEstateType
from filters.layoutFilter import LayoutFilter
from filters.districtFilter import DistrictFilter
from filters.offerTypeFilter import OfferTypeFilter
from filters.estateTypeFilter import EstateTypeFilter

async def layoutOptionsCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await optionsCallbackBase(update, context, toggleLayoutCheckbox, LayoutFilter, getLayoutKeyboardMarkup)

async def districtOptionsCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await optionsCallbackBase(update, context, toggleDistrictCheckbox, DistrictFilter, getDistrictKeyboardMarkup)

async def offerTypeOptionsCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await optionsCallbackBase(update, context, toggleOfferType, OfferTypeFilter, getOfferTypeKeyboardMarkup)

async def estateTypeOptionsCallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await optionsCallbackBase(update, context, toggleEstateType, EstateTypeFilter, getEstateTypeKeyboardMarkup)

async def optionsCallbackBase(update: Update, context: ContextTypes.DEFAULT_TYPE, toggleOption, optionClass, getReplyMarkup ):
    call_back_data = re.sub("\D", "", update.callback_query.data) # remove all non-digit characters from string 
    chatId = update.effective_chat.id
    messageId = update.effective_message.id

    toggleOption(chatId, optionClass(int(call_back_data)))
    replyMarkup = getReplyMarkup(chatId)

    await context.bot.edit_message_reply_markup(chatId, messageId, reply_markup=replyMarkup)

