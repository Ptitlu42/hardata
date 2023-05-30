import psutil

def getCpuData():
    cpu_percent = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq()
    cpu_number = psutil.cpu_count()

    return cpu_percent, cpu_freq, cpu_number

