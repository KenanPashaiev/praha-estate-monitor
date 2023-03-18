import pickle
import logging

from chatData import *

def readFromFile(path):
    data = []
    try:
        with open(path, "rb") as f:
            data = pickle.load(f)

    except IOError:
        # may complain to user as well
        pass

    return data

def writeData(path, data):
    with open(path, "wb") as f:
        pickle.dump(data, f)