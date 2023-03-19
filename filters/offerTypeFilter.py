from enum import IntEnum

class OfferTypeFilter(IntEnum):
    SALE = 1
    RENT = 2
    AUCTION = 3

    def toString(self) -> str:
        return self.name.title()
    
    def equalOrContains(self, value):
        return value == self
    
    def label(self = None):
        return "Offer type"
