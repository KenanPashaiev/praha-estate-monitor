from enum import auto, IntFlag

layoutFilterName = "Layout"

class LayoutFilter(IntFlag):
    L1_KT = auto()
    L1_1 = auto()
    L2_KT = auto()
    L2_1 = auto()
    L3_KT = auto()
    L3_1 = auto()
    L4_KT = auto()
    L4_1 = auto()
    L5_KT = auto()
    L5_1 = auto()
    L6_1 = auto()

    def toString(self) -> str:
        values = [member for member in LayoutFilter._member_names_ if member in str(self)]
        result = ', '.join(values)

        result = result.replace('L6_1', '6 and more')
        result = result.replace('L', '')
        result = result.replace('_', '+')
        result = result.replace('|', ', ')
        return result.lower()
    
    def toParams(self) -> str:
        flagValues = LayoutFilter._member_names_
        values = [member for member in flagValues if member in str(self)]
        result = []
        
        for value in values:
            result.append(str(flagValues.index(value) + 2))

        return '|'.join(result)
    
    def equalOrContains(self, value):
        return value in self
    
    def label(self = None):
        return "Layout"