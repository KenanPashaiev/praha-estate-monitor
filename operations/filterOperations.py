import datetime
from filters.districtFilter import DistrictFilter
from filters.estateTypeFilter import EstateTypeFilter

from filters.layoutFilter import LayoutFilter
from filters.offerTypeFilter import OfferTypeFilter
from operations.chatOperations import getChatData, updateChatData
from entities.monitoringFilters import MonitoringFilters

def getFiltersForChat(chatId: int) -> MonitoringFilters:
    chatData = getChatData(chatId)
    return chatData.monitoringFilters


def toggleLayoutCheckbox(chatId: int, layout: LayoutFilter):
    chatData = getChatData(chatId)
    chatData.monitoringFilters.layout = chatData.monitoringFilters.layout ^ layout
    updateChatData(chatId, chatData)

def toggleDistrictCheckbox(chatId: int, district: DistrictFilter):
    chatData = getChatData(chatId)
    chatData.monitoringFilters.district = chatData.monitoringFilters.district ^ district
    updateChatData(chatId, chatData)

def toggleOfferType(chatId: int, offerType: OfferTypeFilter):
    chatData = getChatData(chatId)
    chatData.monitoringFilters.offerType = offerType
    updateChatData(chatId, chatData)

def toggleEstateType(chatId: int, estateType: EstateTypeFilter):
    chatData = getChatData(chatId)
    chatData.monitoringFilters.type = estateType
    updateChatData(chatId, chatData)


def setMoveInDateForChat(chatId: int, moveInDateText: str) -> bool:
    chatData = getChatData(chatId)

    splittedString = moveInDateText.split('-')
    try:
        chatData.monitoringFilters.moveInDateFrom = datetime.strptime(splittedString[0], '%d.%m.%y') if not splittedString[0].isspace() else None
        chatData.monitoringFilters.moveInDateTo = datetime.strptime(splittedString[1], '%d.%m.%y') if not splittedString[0].isspace() else None
    except:
        return False

    updateChatData(chatId, chatData)
    return True

def setPriceForChat(chatId: int, priceText: str):
    chatData = getChatData(chatId)
    
    splittedString = priceText.split('-')
    chatData.monitoringFilters.minPrice = int(splittedString[0]) if not splittedString[0].isspace() else 0
    chatData.monitoringFilters.maxPrice = int(splittedString[1]) if not splittedString[1].isspace() else 10000000

    updateChatData(chatId, chatData)

def setAreaForChat(chatId: int, areaText: str):
    chatData = getChatData(chatId)

    splittedString = areaText.split('-')
    chatData.monitoringFilters.minArea = int(splittedString[0]) if not splittedString[0].isspace() else 0
    chatData.monitoringFilters.maxArea = int(splittedString[1]) if not splittedString[1].isspace() else 10000000

    updateChatData(chatId, chatData)