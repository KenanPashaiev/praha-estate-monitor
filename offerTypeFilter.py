from enum import auto, IntEnum

class OfferTypeFilter(IntEnum):
    SALE = 1
    RENT = 2
    AUCTION = 3

    def toString(self):
        if self == OfferTypeFilter.SALE:
            return "Sale"
        if self == OfferTypeFilter.RENT:
            return "Rent"
        if self == OfferTypeFilter.AUCTION:
            return "Auction"
