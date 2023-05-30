import psutil

def memory_data():
    memory_usage = psutil.virtual_memory().percent
    print (f"{memory_usage}")
    return memory_usage 


memory_data()