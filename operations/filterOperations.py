from filters.districtFilter import DistrictFilter
from filters.estateTypeFilter import EstateTypeFilter
from filters.layoutFilter import LayoutFilter
from filters.offerTypeFilter import OfferTypeFilter
from ranges.priceRange import PriceRange
from ranges.areaRange import AreaRange
from ranges.moveInDateRange import MoveInDateRange
from entities.monitoringFilters import MonitoringFilters
from operations.chatOperations import getChatData, updateChatData

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
    chatData.monitoringFilters.estateType = estateType
    updateChatData(chatId, chatData)


def updatePriceForChat(chatId: int, priceRange: PriceRange):
    chatData = getChatData(chatId)
    chatData.monitoringFilters.priceRange = priceRange
    updateChatData(chatId, chatData)

def updateAreaForChat(chatId: int, areaRange: AreaRange):
    chatData = getChatData(chatId)
    chatData.monitoringFilters.areaRange = areaRange
    updateChatData(chatId, chatData)

def updateMoveInDateForChat(chatId: int, moveInDateRange: MoveInDateRange):
    chatData = getChatData(chatId)
    chatData.monitoringFilters.moveInDateRange = moveInDateRange
    updateChatData(chatId, chatData)
