import psutil
import subprocess

def getMemoryData():
    memory_data = psutil.virtual_memory()
    memory_total = memory_data.total
    memory_available = memory_data.available
    memory_percent = memory_data.percent
    memory_freq = get_memory_frequency()

    return memory_available, memory_percent, memory_total, memory_freq

def get_memory_frequency():
    output = subprocess.check_output("sudo dmidecode --type 17", shell=True)
    lines = output.decode().split("\n")
    for line in lines:
        if "Speed" in line and "Configured" not in line:
            speed = line.split(":")[1].strip()
            memory_freq = int(speed.replace("MHz", "").replace("MT/s", ""))
            return memory_freq
