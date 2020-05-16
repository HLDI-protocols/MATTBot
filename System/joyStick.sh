#!/bin/sh
#echo over to VECTOR Controller JOY STICK;
cd MATT_Ware
sudo chmod a+rw /dev/ttyUSB0
python3 AnalogControllerDevice.py 
