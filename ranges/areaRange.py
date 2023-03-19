import re

from handlers.states import SETAREA

class AreaRange:
    defaultMinArea = 0
    defaultMaxArea = 10000000

    def __init__(self, minArea = defaultMinArea, maxArea = defaultMaxArea):
        self.minArea = minArea
        self.maxArea = maxArea

    def label(self = None) -> str:
        return "Area"
    
    def state(self = None) -> int:
        return SETAREA
    
    def exampleString(self = None) -> str:
        return ("'45 - 80' to specify both min and max. \n" +
                "'45 -' to specify only min. \n"+
                "'- 80' to specify only max.")
    
    def toString(self) -> str:
        minAreaStr = self.minArea if self.minArea > self.defaultMinArea else ""
        maxAreaStr = self.maxArea if self.maxArea < self.defaultMaxArea else ""
        return f"{minAreaStr} - {maxAreaStr}"
    
    def isValidString(str: str) -> bool:
        if not "-" in str:
            return False
        
        validatedStr = str.replace(" ", "")

        pattern = re.compile("^(\d+)?-?(\d+)?$")
        return pattern.fullmatch(validatedStr)
    
    def toRange(str: str):
        splittedString = str.replace(" ", "").split('-')
        minArea = int(splittedString[0]) if splittedString[0] != "" else AreaRange.defaultMinArea
        maxArea = int(splittedString[1]) if splittedString[1] != "" else AreaRange.defaultMaxArea
        return AreaRange(minArea, maxArea)
 