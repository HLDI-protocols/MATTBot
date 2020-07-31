#!/bin/sh
gif-for-cli "System/HLEngine/HL_Flags/updating_HLEngine.gif"

wait
cd System
#KDE uncomment konsole
#konsole -e python3 MATTAutomata.py & 
#konsole -e python3 console.py &
#UBUNTU/other gnome distro uncomment gnome
#gnome-terminal -e 'python3 MATTAutomata.py &'
#gnome-terminal -e 'python3 console.py &'
./OUL.sh
wait
cd ..
clear
echo "MATTBot 2020 activated"
echo "designed and developed by Akhil P Jacob"
echo "last updated on 31st July 2020"
gif-for-cli "System/HLEngine/HL_Flags/updating_HLEngine.gif"
exit


 


 