from ping3 import ping

def getNetworkData(index):
    network_ping = pingTime()
    network_speedDownload = networkSpeed(1)
    network_speedUpload = networkSpeed(2)

    if index == 1:
        return "{:.2f}".format(network_ping)
    if index == 2: 
        return network_speedDownload
    if index == 3: 
        return network_speedUpload

def pingTime():
    pingTest = ping('8.8.8.8')
    return pingTest * 1000

def networkSpeed(index):
    if index == 1:
        return '1'
    if index == 2:
        return '1'
   
networkSpeed(1)
