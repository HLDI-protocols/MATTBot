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
        print("MATTbot: sir, its getting late")

    elif(current_time=="00:00:00"):
        HLEngine_audioProcess.playsound("voice/12am.wav")
        print("MATTbot: time update 12am")

    elif(current_time=="01:00:00"):
        HLEngine_audioProcess.playsound("voice/1am.wav")
        print("MATTbot: time update 1am")

    elif(current_time=="02:00:00"):
        HLEngine_audioProcess.playsound("voice/2am.wav")
        print("MATTbot: time update 2am")

    elif(current_time=="03:00:00"):
        HLEngine_audioProcess.playsound("voice/3am.wav")
        print("MATTbot: time update 3am")

    elif(current_time=="04:00:00"):
        HLEngine_audioProcess.playsound("voice/4am.wav")
        print("MATTbot: time update 4am")

    elif(current_time=="05:00:00"):
        HLEngine_audioProcess.playsound("voice/5am.wav")
        print("MATTbot: time update 5am")

    elif(current_time=="06:00:00"):
        HLEngine_audioProcess.playsound("voice/6am.wav")
        print("MATTbot: time update 6am")

    elif(current_time=="07:00:00"):
        HLEngine_audioProcess.playsound("voice/7am.wav")
        print("MATTbot: time update 7am")

    elif(current_time=="08:00:00"):
        HLEngine_audioProcess.playsound("voice/8am.wav")
        print("MATTbot: time update 8am")

    elif(current_time=="09:00:00"):
        HLEngine_audioProcess.playsound("voice/9am.wav")
        print("MATTbot: time update 9am")

    elif(current_time=="10:00:00 "):
        HLEngine_audioProcess.playsound("voice/10am.wav")
        print("MATTbot: time update 10am")

    elif(current_time=="11:00:00"):
        HLEngine_audioProcess.playsound("voice/11am.wav")
        print("MATTbot: time update 11am")

    elif(current_time=="12:00:00"):
        HLEngine_audioProcess.playsound("voice/12pm.wav")
        print("MATTbot: time update 12pm")

    elif(current_time=="13:00:00"):
        HLEngine_audioProcess.playsound("voice/1pm.wav")
        print("MATTbot: time update 1pm")

    elif(current_time=="14:00:00"):
        HLEngine_audioProcess.playsound("voice/2pm.wav")
        print("MATTbot: time update 2pm")

    elif(current_time=="15:00:00"):
        HLEngine_audioProcess.playsound("voice/3pm.wav")
        print("MATTbot: time update 3pm")

    elif(current_time=="16:00:00"):
        HLEngine_audioProcess.playsound("voice/4pm.wav")
        print("MATTbot: time update 4pm")

    elif(current_time=="17:00:00"):
        HLEngine_audioProcess.playsound("voice/5pm.wav")
        print("MATTbot: time update 5pm")

    elif(current_time=="18:00:00"):
        HLEngine_audioProcess.playsound("voice/6pm.wav")
        print("MATTbot: time update 6pm")

    elif(current_time=="19:00:00"):
        HLEngine_audioProcess.playsound("voice/7pm.wav")
        print("MATTbot: time update 7pm")

    elif(current_time=="20:00:00"):
        HLEngine_audioProcess.playsound("voice/8pm.wav")
        print("MATTbot: time update 8pm")

    elif(current_time=="21:00:00"):
        HLEngine_audioProcess.playsound("voice/9pm.wav")
        print("MATTbot: time update 9pm")

    elif(current_time=="22:00:00"):
        HLEngine_audioProcess.playsound("voice/10pm.wav")
        print("MATTbot: time update 10pm")

    elif(current_time=="23:00:00"):
        HLEngine_audioProcess.playsound("voice/11pm.wav")
        print("MATTbot: time update 11pm")


while(True):
    runner()
    
        
