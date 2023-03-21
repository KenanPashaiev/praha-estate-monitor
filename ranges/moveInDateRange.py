from datetime import datetime
from handlers.states import SETMOVEINDATE

class MoveInDateRange:
    dateFormat = '%d.%m.%Y'

    defaultFromDate = None
    defaultToDate = None

    def __init__(self, fromDate: datetime = defaultFromDate, toDate: datetime = defaultToDate):
        self.fromDate: datetime = fromDate
        self.toDate: datetime = toDate

    def label(self = None) -> str:
        return "Move in date"
    
    def state(self = None) -> int:
        return SETMOVEINDATE
    
    def exampleString(self = None) -> str:
        return ("'01.03.2023 - 01.05.2023' to specify both from and to dates. \n" +
                "'01.03.2023 -' to specify only from date. \n"+
                "'- 01.05.2023' to specify only to date.")
    
    def isValidString(str: str) -> bool:
        if not "-" in str:
            return False
        
        splittedString = str.replace(" ", "").split('-')
        try:
            datetime.strptime(splittedString[0], MoveInDateRange.dateFormat) if splittedString[0] != "" else None
            datetime.strptime(splittedString[1], MoveInDateRange.dateFormat) if splittedString[1] != "" else None
        except:
            return False

        return True
    
    def toString(self) -> str:
        fromDateStr = self.fromDate.strftime(MoveInDateRange.dateFormat) if self.fromDate != self.defaultFromDate else ""
        toDateStr = self.toDate.strftime(MoveInDateRange.dateFormat) if self.toDate != self.defaultToDate else ""
        return f"{fromDateStr} - {toDateStr}"
    
    def toParams(self) -> str:
        fromDateStr = self.fromDate.strftime('%Y-%m-%d') if self.fromDate != self.defaultFromDate else ""
        toDateStr = self.toDate.strftime('%Y-%m-%d') if self.toDate != self.defaultToDate else ""
        return f"{fromDateStr}|{toDateStr}"
    
    def toRange(str: str):
        splittedString = str.replace(" ", "").split('-')
        fromDate = datetime.strptime(splittedString[0], MoveInDateRange.dateFormat) if splittedString[0] != "" else None
        toDate = datetime.strptime(splittedString[1], MoveInDateRange.dateFormat) if splittedString[1] != "" else None

        return MoveInDateRange(fromDate, toDate)
 