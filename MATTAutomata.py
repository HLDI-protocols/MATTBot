import time
from HLEngine import HLEngine_audioProcess
from HLEngine import HLEngine_Progressbar
print("HL Robotics and Intelligence Presents")
HLEngine_Progressbar.progress("MATTAutomata")
print("MATTbot:Automata is ARMED")
def runner():
    
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    if(current_time=="10:00:10"):
        HLEngine_audioProcess.playsound("voice/breakfast.wav")
        print("MATTbot:sir, Breakfast time")
    elif(current_time=="13:00:10"):
        HLEngine_audioProcess.playsound("voice/lunch.wav")
        print("MATTbot:sir, Lunch time")
    elif(current_time=="16:00:10"):
        HLEngine_audioProcess.playsound("voice/tea.wav")
        print("MATTbot:sir, Tea time")
    elif(current_time=="22:00:10"):
        HLEngine_audioProcess.playsound("voice/late.wav")
        print("MATTbot:sir, its getting late")


while(True):
    runner()
    
        
