from King_Crypto import encode
from King_Crypto import decode


import socket

HOST = input('[Enter the chatroom ip]:')  # The server's hostname or IP address
PORT = 65432        # The port used by the server
NAME = input('[Enter your chat name]:')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024).decode('utf-8')
        decrypedmessage=decode.dataDecryption(data)
        print(decrypedmessage)
        message=input(NAME)
        if(message=='exit'):
            break
        
        message=(NAME+message)  
        encrypedMessage=encode.dataEncryption(message)
        s.sendall(bytes(encrypedMessage, encoding="ascii"))