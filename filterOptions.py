from chatData import *
from ioUtils import *
from chatOperations import *
from layoutFilter import LayoutFilter
from districtFilter import DistrictFilter
from offerTypeFilter import OfferTypeFilter
from propertyTypeFilter import PropertyTypeFilter

def getLayoutOptions(chatId):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)

    arr = [
        [ ( "1+kt", LayoutFilter.L1_KT ), ( "1+1", LayoutFilter.L1_1 )],
        [ ( "2+kt", LayoutFilter.L2_KT ), ( "2+1", LayoutFilter.L2_1 ) ],
        [ ( "3+kt", LayoutFilter.L3_KT ), ( "3+1", LayoutFilter.L3_1 ) ],
        [ ( "4+kt", LayoutFilter.L4_KT ), ( "4+1", LayoutFilter.L4_1 ) ],
        [ ( "5+kt", LayoutFilter.L5_KT ), ( "5+1", LayoutFilter.L5_1 ) ],
        [ ( "6 and more", LayoutFilter.L6_1 ) ],
    ]

    return chatData.monitoringFilters.layout, arr

def getDistrictOptions(chatId):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)

    arr = [
        [ ( "Praha 1", DistrictFilter.Praha_1 ), ( "Praha 2", DistrictFilter.Praha_2 )],
        [ ( "Praha 3", DistrictFilter.Praha_3 ), ( "Praha 4", DistrictFilter.Praha_4 ) ],
        [ ( "Praha 5", DistrictFilter.Praha_5 ), ( "Praha 6", DistrictFilter.Praha_6 ) ],
        [ ( "Praha 7", DistrictFilter.Praha_7 ), ( "Praha 8", DistrictFilter.Praha_8 ) ],
        [ ( "Praha 9", DistrictFilter.Praha_9 ), ( "Praha 10", DistrictFilter.Praha_10 ) ]
    ]

    return chatData.monitoringFilters.district, arr
    
def getOfferTypeOptions(chatId):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)

    arr = [
        [( "Sale", OfferTypeFilter.SALE )], 
        [( "Rent", OfferTypeFilter.RENT )],
        [( "Auction", OfferTypeFilter.AUCTION )]
    ]

    return chatData.monitoringFilters.offerType, arr

def getPropertyTypeOptions(chatId):
    data = readFromFile(fname)
    chatData = getChatData(data, chatId)

    arr = [
        [( "Apartment", PropertyTypeFilter.APARTMENT )], 
        [( "House", PropertyTypeFilter.HOUSE )],
        [( "Land", PropertyTypeFilter.LAND )]
    ]

    return chatData.monitoringFilters.type, arr
