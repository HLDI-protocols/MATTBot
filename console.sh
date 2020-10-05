#!/bin/sh
#gif-for-cli "Prop/HLD.gif"
python3 -m gif_for_cli "Prop/HLD.gif"
wait
#gif-for-cli "Prop/MATTBot.gif"
python3 -m gif_for_cli "Prop/MATTBot.gif"
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
echo "last updated on 12th AUGUST 2020"
#gif-for-cli "Prop/HLD.gif"
python3 -m gif_for_cli "Prop/MATTBot.gif"

exit


 


 
