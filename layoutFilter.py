from enum import auto, IntFlag

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

    def toString(self):
        print(self.toParams())
        if self.name == None:
            return ''

        result = self.name
        result = result.replace('L6_1', '6 and more')
        result = result.replace('L', '')
        result = result.replace('_', '+')
        result = result.replace('|', ', ')
        return result.lower()
    
    def toParams(self):
        if self.name == None:
            return ''

        flagValues = LayoutFilter._member_names_
        values = [member for member in LayoutFilter._member_names_ if member in self.name]
        result = []
        print(flagValues)
        print(values)

        for value in values:
            result.append(str(flagValues.index(value) + 2))

        result = '|'.join(result)
        return result
    