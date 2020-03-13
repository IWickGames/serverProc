import serverProc

active = True
while active:
    msg = input("Enter something to send: ")
    
    if msg == "exit":
        active = False
    else:
        serverProc.client("127.0.0.1", 3333, msg)