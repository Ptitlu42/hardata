import psutil
import subprocess

def getMemoryData(index):
    memory_data = psutil.virtual_memory()
    memory_total = memory_data.total
    memory_available = memory_data.available
    memory_percent = memory_data.percent
    memory_freq = get_memory_frequency()

    if index == 1:
        return "{:.2f}".format(memory_available / (1024 ** 3))
    if index == 2:
        return "{:.2f}".format(memory_percent)
    if index == 3: 
        return "{:.2f}".format(memory_total / (1024 ** 3))
    if index == 4:
        return memory_freq

def get_memory_frequency():
    output = subprocess.check_output("sudo dmidecode --type 17", shell=True)
    lines = output.decode().split("\n")
    for line in lines:
        if "Speed" in line and "Configured" not in line:
            speed = line.split(":")[1].strip()
            memory_freq = int(speed.replace("MHz", "").replace("MT/s", ""))
            return memory_freq
