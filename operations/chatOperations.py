import logging

from entities.chatData import ChatData
from utils.ioUtils import writeData, readFromFile

def startNewChat(chatId: int):
    existingChatData = getChatData(chatId)
    if existingChatData != None:
        return

    chatData = ChatData(chatId=chatId)
    updateChatData(chatId, chatData)

def markEstateForChat(chatId: int, estateId: int):
    chatData = getChatData(chatId)
    chatData.properties.append(estateId)
    updateChatData(chatId, chatData)

def estateIsMarkedForChat(chatId: int, estateId: int) -> bool:
    chatData = getChatData(chatId)

    return estateId in chatData.properties

def setIsMonitoringForChat(chatId: int, isMonitoring: bool):
    chatData = getChatData(chatId)
    chatData.isMonitoring = isMonitoring
    updateChatData(chatId, chatData)

def getMonitoredChats():
    data = readFromFile()
    for item in data:
        if item.isMonitoring:
            yield item

def getChatData(chatId: int) -> ChatData:
    data = readFromFile()
    chatData = None
    for item in data:
        if item.chatId == str(chatId):
            chatData = item

    return chatData

def updateChatData(chatId: int, chatData: ChatData):
    data = readFromFile()
    for index, item in enumerate(data):
        if item.chatId == str(chatId):
            data[index] = chatData
            writeData(data)
            return
        
    logging.log(logging.INFO, f"New chat {str(chatId)} created.")
    data.append(chatData)
    writeData(data)

    
