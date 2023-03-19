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
    if estateId in chatData.properties:
        logging.log(logging.INFO, f"{str(estateId)} estate already marked for chat {str(chatId)}")

    return estateId in chatData.properties

def getChatData(chatId: int) -> ChatData:
    data = readFromFile()
    chatData = None
    for item in data:
        if item.chatId == str(chatId):
            # logging.log(logging.INFO, f"Chat '{str(chatId)}' found, loading.")
            chatData = item

    return chatData

def updateChatData(chatId: int, chatData: ChatData):
    data = readFromFile()
    for index, item in enumerate(data):
        if item.chatId == chatId:
            data[index] = chatData
            writeData(data)
            return
        
    logging.log(logging.INFO, f"New chat {str(chatId)} created.")
    data.append(chatData)
    writeData(data)

    
