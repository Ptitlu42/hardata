from getData import cpu, memory, disk, network

cpu_percent = cpu.getCpuData(1)
cpu_freq = cpu.getCpuData(2)
cpu_number = cpu.getCpuData(3)

disk_totalSpace = disk.getDiskData(1)
disk_usedSpace = disk.getDiskData(2)
disk_freePercent = disk.getDiskData(3)
disk_usedPercent = disk.getDiskData(4)
disk_freeSpace = disk.getDiskData(5)

memory_available = memory.getMemoryData(1)
memory_percentUsed = memory.getMemoryData(2)
memory_total = memory.getMemoryData(3)
memory_freq = memory.getMemoryData(4)

network_ping = network.getNetworkData(1)
network_speedDownload = network.getNetworkData(2)
network_speedUpload = network.getNetworkData(3)

print (f"\n CPU: \n\n {cpu_number} cpu \n {cpu_freq} mHz fréquence \n {cpu_percent} % used")
print (f"\n DISK: \n\n {disk_totalSpace} GB total \n {disk_freeSpace} GB free \n {disk_usedSpace} GB used \n {disk_usedPercent} % used \n {disk_freePercent} % free")
print (f"\n RAM: \n\n {memory_total} GB total \n {memory_available} GB available \n {memory_percentUsed} % used \n {memory_freq} mHz fréquence")
print (f"\n NETWORK: \n\n {network_ping} ms ping \n {network_speedDownload} mb download \n {network_speedUpload} mb upload")