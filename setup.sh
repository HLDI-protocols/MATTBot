#!/bin/sh
echo 'Hyper Library Dynamic Integration 2020';
wait
sudo apt-get update
wait
sudo apt-get install idle3
wait
sudo apt-get install python3-pip
wait
sudo apt-get install python-pyaudio python3-pyaudio 
wait
sudo apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools
wait
sudo apt-get install motion
wait
sudo apt-get install sox
wait
sudo apt-get install sox libsox-fmt-all
wait
sudo apt install libespeak1
wait
sudo apt-get install python3-pygame
wait
sudo apt-get install python3-bluez
wait
cd System/HLEngine
python3 HLEngine_EnvironmentSetup.py &
wait
cd ..
cd patches
python3 nlpFix.py &
#echo 'Setting usb access to Linux'
#sudo chmod a+rw /dev/ttyACM0
wait
echo 'Hyper Library Dynamic Integration 2020 Environmenal setup completed SUCCESSFULLY';

cd ..
chmod +x playboy.sh
wait
chmod +x OUL.sh
wait
chmod +x tracker.sh
wait
chmod +x wakeup.sh
wait

cd ..

chmod +x launcher.sh
wait
chmod +x console.sh
wait
chmod +x updates.sh
wait

echo "[MATTBOT is ready to use.... ENJOY !!!!!!]";

