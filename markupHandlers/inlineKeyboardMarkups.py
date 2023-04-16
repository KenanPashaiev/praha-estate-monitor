from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from operations.filterOperations import getFiltersForChat
from filters.layoutFilter import LayoutFilter
from filters.districtFilter import DistrictFilter
from filters.offerTypeFilter import OfferTypeFilter
from filters.estateTypeFilter import EstateTypeFilter

def getLayoutKeyboardMarkup(chatId: int) -> InlineKeyboardMarkup:
    filters = getFiltersForChat(chatId)

    arr = [
        [ LayoutFilter.L1_KT, LayoutFilter.L1_1 ],
        [ LayoutFilter.L2_KT, LayoutFilter.L2_1 ],
        [ LayoutFilter.L3_KT, LayoutFilter.L3_1 ],
        [ LayoutFilter.L4_KT, LayoutFilter.L4_1 ],
        [ LayoutFilter.L5_KT, LayoutFilter.L5_1 ],
        [ LayoutFilter.L6_1 ],
    ]
    
    return InlineKeyboardMarkup(applyOptions(arr, filters.layout))

def getDistrictKeyboardMarkup(chatId: int) -> InlineKeyboardMarkup:
    filters = getFiltersForChat(chatId)

    arr = [
        [ DistrictFilter.Praha_1, DistrictFilter.Praha_2 ],
        [ DistrictFilter.Praha_3, DistrictFilter.Praha_4 ],
        [ DistrictFilter.Praha_5, DistrictFilter.Praha_6 ],
        [ DistrictFilter.Praha_7, DistrictFilter.Praha_8 ],
        [ DistrictFilter.Praha_9, DistrictFilter.Praha__10 ]
    ]

    return InlineKeyboardMarkup(applyOptions(arr, filters.district))
    
def getOfferTypeKeyboardMarkup(chatId: int) -> InlineKeyboardMarkup:
    filters = getFiltersForChat(chatId)

    arr = [
        [ OfferTypeFilter.SALE ], 
        [ OfferTypeFilter.RENT ],
        [ OfferTypeFilter.AUCTION ]
    ]

    return InlineKeyboardMarkup(applyOptions(arr, filters.offerType))

def getEstateTypeKeyboardMarkup(chatId: int) -> InlineKeyboardMarkup:
    filters = getFiltersForChat(chatId)

    arr = [
        [ EstateTypeFilter.APARTMENT ], 
        [ EstateTypeFilter.HOUSE ],
        [ EstateTypeFilter.LAND ]
    ]

    return InlineKeyboardMarkup(applyOptions(arr, filters.estateType))


#private
def applyOptions(arr, currentFilterValue: int) -> InlineKeyboardMarkup:
    options = arr
    for i, subArr in enumerate(options):
        for j, item in enumerate(subArr):
            options[i][j] = getOption(item, currentFilterValue)

    return options


def getOption(filterOption, currentValue) -> InlineKeyboardButton:
    text = filterOption.toString() + (" ☑️" if currentValue.equalOrContains(filterOption) else "")

    return InlineKeyboardButton(text = text, callback_data = filterOption.label()+str(int(filterOption)))

