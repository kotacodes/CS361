# sends message to outpost
# main.py

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.60" 
port = 8000
s.connect((host, port))

def ts(str):
    s.send('Message From CS361'.encode())
    data = '' 
    while data == '':
        data = s.recv(1024).decode() 
        if data != '':
            print(data) 
    
    s.close() 
ts(s)


