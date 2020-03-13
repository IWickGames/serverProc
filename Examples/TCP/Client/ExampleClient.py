import serverProc

IP = "127.0.0.1"
PORT = 1111
BUFFER = 1024

#This sends "Send Message" to the server in IP on the port PORT
#If the server responds you will get a message back and it will be stored in returnMessage
returnMessage = serverProc.TCPClient(IP, PORT, "Send Message", BUFFER)