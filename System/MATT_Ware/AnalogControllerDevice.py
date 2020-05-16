import Devices
import bluetooth
import time
import serial

try:
    print("Connected to controller module ")
    controller_Address=Devices.analog_Controller_COM
    vector_Address=Devices.robot_Vector_COM
    ser = serial.Serial(controller_Address, 9600)
    bd_addr=vector_Address
    port = 1
    sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
    sock.connect((bd_addr,port))


    global count
    count=0

    while 1:
        b = ser.readline()         # read a byte string
        string_n = b.decode()  # decode byte string into Unicode  
        data = string_n.rstrip() # remove \n and \r
        #flt = float(string)        # convert string to float
        print(data+" sent")
        if (data=="Forward"):
            count+=1
            if (count>=5):
                sock.send(str(Devices.Vector_controlPattern[0]))
                #time.sleep(2)
                count=0
        elif (data=="Backward"):
            count+=1
            if (count>=5):
                sock.send(str(Devices.Vector_controlPattern[1]))
                #time.sleep(2)
                count=0
        elif (data=="Left"):
            count+=1
            if (count>=5):
                sock.send(str(Devices.Vector_controlPattern[2]))
                #time.sleep(2)
                count=0
        elif (data=="Right"):
            count+=1
            if (count>=5):
                sock.send(str(Devices.Vector_controlPattern[3]))
                #time.sleep(2)
                count=0

        elif (data=="Stop"):
            count+=1
            if (count>=5):
                sock.send(str(Devices.Vector_controlPattern[4]))
                #time.sleep(2)
                count=0

        
except:
    print("Cannot connect to the controller device. Check with the connections")        