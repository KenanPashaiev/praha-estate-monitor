import pickle

fname = "data.pkl"

def readFromFile():
    global fname
    
    data = []
    try:
        with open(fname, "rb") as f:
            data = pickle.load(f)

    except Exception as e:
        pass

    return data

def writeData(data):
    global fname

    with open(fname, "wb") as f:
        pickle.dump(data, f)
        f.close()