from socket import *
servername = "192.168.170.128"
serverport = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername, serverport))
sentence = input("Please enter loewercase sentence:")
clientSocket.send(sentence.encode)
modifiedSentence  = clientSocket.recvfrom(1024)
print('from server:', modifiedSentence.decode())
clientSocket.close()
