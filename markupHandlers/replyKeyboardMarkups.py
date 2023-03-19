from telegram import ReplyKeyboardMarkup

from filters.districtFilter import DistrictFilter
from filters.layoutFilter import LayoutFilter
from filters.estateTypeFilter import EstateTypeFilter
from filters.offerTypeFilter import OfferTypeFilter

startMonitoringMessageText = "Start monitoring"
stopMonitoringMessageText = "Stop monitoring"
cancelMessageText = "Cancel"

filterReplyMarkup = ReplyKeyboardMarkup([
    [ startMonitoringMessageText ],
    [ EstateTypeFilter.label(), OfferTypeFilter.label() ],
    [ LayoutFilter.label(), DistrictFilter.label() ], 
    [ "Price range", "Area", "Move in dates" ]
    ], resize_keyboard=True)

cancelReplyMarkup = ReplyKeyboardMarkup([[cancelMessageText]], resize_keyboard=True)
