from entities.monitoringFilters import MonitoringFilters

class ChatData:
    def __init__(self, chatId:str = "", monitoringFilters:MonitoringFilters = MonitoringFilters(), properties = [], isMonitoring:bool = False):
        self.chatId:str = chatId
        self.monitoringFilters:str = monitoringFilters
        self.properties = properties
        self.isMonitoring:bool = isMonitoring
