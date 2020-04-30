#!/bin/sh
cd System
#konsole -e python3 MATTAutomata.py & 
#konsole -e python3 console.py &
gnome-terminal -e 'python3 MATTAutomata.py &'
gnome-terminal -e 'python3 console.py &'
wait
exit
 


