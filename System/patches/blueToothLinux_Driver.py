import bluetooth
import time

bd_addr = "FC:A8:9A:00:34:F0"
port = 1
sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
sock.connect((bd_addr,port))

while 1:
    tosend = input('entersome stuff')
    if tosend != 'q':
        sock.send(tosend)
    