import serverProc

while True:
    rawPacket = serverProc.server("127.0.0.1", 3333)
    print(rawPacket)