import logging
import datetime

from chatData import *
from ioUtils import *

fname = "data.pkl"


def startNewChat(chatId):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)

    if(chatData == None):
        chatData = ChatData(chatId=chatId)
        logging.log(logging.INFO, "User not found, creating new record.")
        data.append(chatData)

    writeData(fname, data)

def toggleLayoutCheckbox(chatId, layout):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    chatData.monitoringFilters.layout = chatData.monitoringFilters.layout ^ layout

    writeData(fname, data)

def toggleDistrictCheckbox(chatId, district):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    chatData.monitoringFilters.district = chatData.monitoringFilters.district ^ district

    writeData(fname, data)

def toggleOfferType(chatId, offerType):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    chatData.monitoringFilters.offerType = offerType

    writeData(fname, data)

def togglePropertyType(chatId, propertyType):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    chatData.monitoringFilters.type = propertyType

    writeData(fname, data)

def getFiltersForChat(chatId):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    return chatData.monitoringFilters

def setMoveInDateForChat(chatId, moveInDateText):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    splittedString = moveInDateText.split('-')

    try:
        chatData.monitoringFilters.moveInDateFrom = datetime.strptime(splittedString[0], '%d.%m.%y') if not splittedString[0].isspace() else None
        chatData.monitoringFilters.moveInDateTo = datetime.strptime(splittedString[1], '%d.%m.%y') if not splittedString[0].isspace() else None
    except:
        return False

    writeData(fname, data)

def setPriceForChat(chatId, priceText):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    splittedString = priceText.split('-')

    chatData.monitoringFilters.minPrice = int(splittedString[0]) if not splittedString[0].isspace() else 0
    chatData.monitoringFilters.maxPrice = int(splittedString[1]) if not splittedString[1].isspace() else 10000000

    writeData(fname, data)

def setAreaForChat(chatId, areaText):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    splittedString = areaText.split('-')

    chatData.monitoringFilters.minArea = int(splittedString[0]) if not splittedString[0].isspace() else 0
    chatData.monitoringFilters.maxArea = int(splittedString[1]) if not splittedString[1].isspace() else 10000000

    writeData(fname, data)

def markEstateForChat(chatId, estateId):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    chatData.properties.append(estateId)

    writeData(fname, data)

def estateIsMarkedForChat(chatId, estateId):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)
    if estateId in chatData.properties:
        print(str(estateId) + " estate already marked for chat " + str(chatId))

    return estateId in chatData.properties

#private
def getChatData(data, chatId):
    chatData = None
    for item in data:
        if(item.chatId == str(chatId)):
            logging.log(logging.INFO, "User found, loading.")
            chatData = item

    return chatData
