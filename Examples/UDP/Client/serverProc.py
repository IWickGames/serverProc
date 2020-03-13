import os
from socket import *

#Client
def client(ipAddress, portSocket, strMessage):
    #Encode a string then send it in a packet
    addr = (ipAddress, portSocket)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.sendto(strMessage.encode(encoding="utf-8", errors='strict'), addr)
    UDPSock.close()

#Server
def server(ipAddress, portSocket, buffer=1024):
    #Wait untill a packet is resieved and then decode it and output it
    try:
        decode = ''
        addr = (ipAddress, portSocket)
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.bind(addr)
        while decode == '':
            (data, addr) = UDPSock.recvfrom(buffer)
            decode = data.decode(encoding='utf-8', errors='strict')
        UDPSock.close()
    except KeyboardInterrupt:
        pass

    return decode;