#!/bin/sh
cd System
#KDE uncomment konsole
konsole -e python3 MATTAutomata.py & 
konsole -e python3 console.py &
#UBUNTU/other gnome distro uncomment gnome
#gnome-terminal -e 'python3 MATTAutomata.py &'
#gnome-terminal -e 'python3 console.py &'
wait
exit


 


