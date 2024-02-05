# Recieves and returns a message to the main sender. 
# outpost.py 

import socket 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.60"
port = 8000


serversocket.bind((host, port))

serversocket.listen(5) 
print('server started and listening') 
while 1: 
    (clientsocket, address) = serversocket.accept() 
    print("connection found!")
    data  = clientsocket.recv(1024).decode() 
    print(data) 
    
    clientsocket.send(data.encode()) 


