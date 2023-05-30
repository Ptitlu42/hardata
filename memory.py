import psutil

def getMemoryData():
    memory_data = psutil.virtual_memory()
    memory_total = memory_data.total
    memory_available = memory_data.available
    memory_percent = memory_data.percent

    return memory_available, memory_percent, memory_total


getMemoryData()