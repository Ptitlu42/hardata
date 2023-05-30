import psutil

def getMemoryData():
    memory_usage = psutil.virtual_memory().percent
    print (f"{memory_usage}")
    return memory_usage 


getMemoryData()