from enum import auto, IntFlag

class DistrictFilter(IntFlag):
    Praha_1 = auto()
    Praha_2 = auto()
    Praha_3 = auto()
    Praha_4 = auto()
    Praha_5 = auto()
    Praha_6 = auto()
    Praha_7 = auto()
    Praha_8 = auto()
    Praha_9 = auto()
    Praha_10 = auto()

    def toString(self) -> str:
        if self.name == None:
            return ''

        result = self.name
        result = result.replace('|', ', ')
        result = result.replace('_', ' ')
        return result
    
    def toParams(self) -> str:
        if self.name == None:
            return ''

        result = self.name
        result = result.replace('Praha_10', '5010')
        result = result.replace('Praha_', '500')
        return result
    
    def equalOrContains(self, value):
        return value in self
    
    def label(self = None):
        return "Districts"
