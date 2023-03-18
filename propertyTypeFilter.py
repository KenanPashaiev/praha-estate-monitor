from enum import auto, IntEnum

class PropertyTypeFilter(IntEnum):
    APARTMENT = 1
    HOUSE = 2
    LAND = 3

    def toString(self):
        if self == PropertyTypeFilter.APARTMENT:
            return "Apartment"
        if self == PropertyTypeFilter.HOUSE:
            return "House"
        if self == PropertyTypeFilter.LAND:
            return "Land"