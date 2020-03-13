import serverProc

IP = '127.0.0.1'
PORT = 1111
BUFFER = 1024

#Wait untill a client sends a request and return it into Message and store there IP in IPAddress
#connect is the socket save. DO NOT CHANGE OR MESS WITH THAT VARIABLE
connect, IPAddress, Message = serverProc.TCPServerRecieve(IP, PORT, BUFFER)
#This will import the connect variable again and return strMessage to the client
#"Test Responce can be anything you want"
serverProc.TCPServerRespond(connect, "Test Responce")