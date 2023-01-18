from socket import *
servername = "192.168.170.128"
serverport = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Please enter loewercase sentence:")
clientSocket.sendto(message.encode(),(servername,serverport))
modifiedMessage , serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
