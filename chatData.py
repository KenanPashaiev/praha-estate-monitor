import json

from monitoringFilters import MonitoringFilters

class ChatData:
    def __init__(self, chatId = "", monitoringFilters = MonitoringFilters(), properties = []):
        self.chatId = chatId
        self.monitoringFilters = monitoringFilters
        self.properties = properties
