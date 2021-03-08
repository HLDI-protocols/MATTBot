from King_Crypto import encode
from King_Crypto import decode


import socket 
HOST = input('[Enter the system ip Address here]:')  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
NAME=input('[Enter your chat name: ')
print('[Started]')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:                            
            message=input(NAME)
            if(message=='exit'):
                break
            message=(NAME+message) 
            encrypedMessage=encode.dataEncryption(message)           
            conn.sendall(bytes(encrypedMessage, encoding="ascii"))  
            data = conn.recv(1024).decode('utf-8')
            decrypedMessage=decode.dataDecryption(data)
            print(decrypedMessage)