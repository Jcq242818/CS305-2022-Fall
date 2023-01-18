from socket import *
serverport = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverport))
serverSocket.listen(1)
print('The server is listening on')
while True:
    connectionSocket , addr = serverSocket.accept()
    sentence  = connectionSocket.recv(1024).decode()
    cap = sentence.upper()
    connectionSocket.send(cap.encode)
    connectionSocket.close()
    
