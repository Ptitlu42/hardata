import psutil

def getCpuData(index):
    cpu_percent = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq().current
    cpu_number = psutil.cpu_count()

    if index == 1:
        return cpu_percent
    if index == 2:
         return "{:.2f}".format(cpu_freq)
    if index == 3: 
        return cpu_number

