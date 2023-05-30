from ping3 import ping
import time
import psutil

def getNetworkData():
    network_ping = pingTime()
    network_speedSent = networkSpeed(2)
    network_speedReceived = networkSpeed(1)

def pingTime():
    pingTest = ping('8.8.8.8')
    return pingTest * 1000

def networkSpeed(index):

    old_values = psutil.net_io_counters()
    time.sleep(1)
    new_values = psutil.net_io_counters()

    sent_bytes = new_values.bytes_sent - old_values.bytes_sent
    recv_bytes = new_values.bytes_recv - old_values.bytes_recv

    if index == 1:
        return sent_bytes
    if index == 2:
        return recv_bytes