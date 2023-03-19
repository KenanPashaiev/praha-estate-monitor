from telegram import InlineKeyboardButton
from entities.chatData import *
from operations.chatOperations import *
from operations.filterOperations import *
from filters.layoutFilter import LayoutFilter
from filters.districtFilter import DistrictFilter
from filters.offerTypeFilter import OfferTypeFilter
from filters.estateTypeFilter import EstateTypeFilter

def getLayoutOptions(chatId: int):
    filters = getFiltersForChat(chatId)

    arr = [
        [ LayoutFilter.L1_KT, LayoutFilter.L1_1 ],
        [ LayoutFilter.L2_KT, LayoutFilter.L2_1 ],
        [ LayoutFilter.L3_KT, LayoutFilter.L3_1 ],
        [ LayoutFilter.L4_KT, LayoutFilter.L4_1 ],
        [ LayoutFilter.L5_KT, LayoutFilter.L5_1 ],
        [ LayoutFilter.L6_1 ],
    ]
    
    return applyOptions(arr, filters.layout)

def getDistrictOptions(chatId):
    filters = getFiltersForChat(chatId)

    arr = [
        [ DistrictFilter.Praha_1, DistrictFilter.Praha_2 ],
        [ DistrictFilter.Praha_3, DistrictFilter.Praha_4 ],
        [ DistrictFilter.Praha_5, DistrictFilter.Praha_6 ],
        [ DistrictFilter.Praha_7, DistrictFilter.Praha_8 ],
        [ DistrictFilter.Praha_9, DistrictFilter.Praha_10 ]
    ]

    return applyOptions(arr, filters.district)
    
def getOfferTypeOptions(chatId):
    filters = getFiltersForChat(chatId)

    arr = [
        [ OfferTypeFilter.SALE ], 
        [ OfferTypeFilter.RENT ],
        [ OfferTypeFilter.AUCTION ]
    ]

    return applyOptions(arr, filters.offerType)

def getEstateTypeOptions(chatId):
    filters = getFiltersForChat(chatId)

    arr = [
        [ EstateTypeFilter.APARTMENT ], 
        [ EstateTypeFilter.HOUSE ],
        [ EstateTypeFilter.LAND ]
    ]

    return applyOptions(arr, filters.type)


#private
def applyOptions(arr, currentFilterValue):
    options = arr
    for i, subArr in enumerate(options):
        for j, item in enumerate(subArr):
            options[i][j] = getOption(item, currentFilterValue)

    return options


def getOption(filterOption, currentValue):
    text = filterOption.toString() + (" ☑️" if currentValue.equalOrContains(filterOption) else "")

    return InlineKeyboardButton(text = text, callback_data = filterOption.label()+str(filterOption))

