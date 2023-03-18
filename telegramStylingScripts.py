from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from filterOptions import *

def styleLayoutInlineButtons(chatId):
    value, arr = getLayoutOptions(chatId)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = InlineKeyboardButton(text = arr[i][j][0] + (" ☑️" if arr[i][j][1] in value else ""), callback_data = "layout"+str(int(arr[i][j][1])))

    return arr

def styleDistrictInlineButtons(chatId):
    value, arr = getDistrictOptions(chatId)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = InlineKeyboardButton(text = arr[i][j][0] + (" ☑️" if arr[i][j][1] in value else ""), callback_data = "district"+str(int(arr[i][j][1])))

    return arr

def styleOfferTypeInlineButtons(chatId):
    value, arr = getOfferTypeOptions(chatId)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            filter = arr[i][j][1]
            arr[i][j] = InlineKeyboardButton(text = arr[i][j][0] + (" ☑️" if filter == value else ""), callback_data = "offerType"+str(int(filter)))

    return arr

def stylePropertyTypeInlineButtons(chatId):
    value, arr = getPropertyTypeOptions(chatId)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            filter = arr[i][j][1]
            arr[i][j] = InlineKeyboardButton(text = arr[i][j][0] + (" ☑️" if filter == value else ""), callback_data = "propertyType"+str(int(filter)))

    return arr
