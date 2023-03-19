from enum import IntEnum

class EstateTypeFilter(IntEnum):
    APARTMENT = 1
    HOUSE = 2
    LAND = 3

    def toString(self) -> str:
        return self.name.title()
    
    def equalOrContains(self, value):
        return value == self
    
    def label(self = None):
        return "Estate type"