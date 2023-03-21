import re

from handlers.states import SETPRICE

class PriceRange:
    defaultMinPrice = 0
    defaultMaxPrice = 10000000

    def __init__(self, minPrice = defaultMinPrice, maxPrice = defaultMaxPrice):
        self.minPrice = minPrice
        self.maxPrice = maxPrice


    def label(self = None) -> str:
        return "Price"
    
    def state(self = None) -> int:
        return SETPRICE
    
    def exampleString(self = None) -> str:
        return ("'10000-35000' to specify both min and max. \n" +
                "'10000-' to specify only min. \n"+
                "'-35000' to specify only max.")
    
    
    
    def isValidString(str: str) -> bool:
        if not "-" in str:
            return False
        
        validatedStr = str.replace(" ", "")

        pattern = re.compile("^(\d+)?-?(\d+)?$")
        return pattern.fullmatch(validatedStr)
    
    def toString(self) -> str:
        minPriceStr = self.minPrice if self.minPrice > self.defaultMinPrice else ""
        maxPriceStr = self.maxPrice if self.maxPrice < self.defaultMaxPrice else ""
        return f"{minPriceStr} - {maxPriceStr}"
    
    def toParams(self) -> str:
        minPriceStr = self.minPrice if self.minPrice > self.defaultMinPrice else self.defaultMinPrice
        maxPriceStr = self.maxPrice if self.maxPrice < self.defaultMaxPrice else self.defaultMaxPrice
        return f"{minPriceStr}|{maxPriceStr}"

    def toRange(str: str):
        splittedString = str.replace(" ", "").split('-')
        minPrice = int(splittedString[0]) if splittedString[0] != "" else PriceRange.defaultMinPrice
        maxPrice = int(splittedString[1]) if splittedString[1] != "" else PriceRange.defaultMaxPrice
        return PriceRange(minPrice, maxPrice)
    