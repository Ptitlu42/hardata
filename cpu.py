import psutil

def getCpuData():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq().current
    print (f"{cpu_usage} \n {cpu_freq}")
    return cpu_usage, cpu_freq


getCpuData()