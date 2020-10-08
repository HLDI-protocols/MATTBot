
from HLEngine import HLEngine_audioProcess
from Seeker import timeMapper
def automata(current_time,reminder):

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

    elif(current_time==timeMapper.twentyfour):
        HLEngine_audioProcess.playsound("voice/12am.wav")
        print("MATTbot: time update 12am")

    elif(current_time==timeMapper.one):
        HLEngine_audioProcess.playsound("voice/1am.wav")
        print("MATTbot: time update 1am")

    elif(current_time==timeMapper.two):
        HLEngine_audioProcess.playsound("voice/2am.wav")
        print("MATTbot: time update 2am")

    elif(current_time==timeMapper.three):
        HLEngine_audioProcess.playsound("voice/3am.wav")
        print("MATTbot: time update 3am")

    elif(current_time==timeMapper.four):
        HLEngine_audioProcess.playsound("voice/4am.wav")
        print("MATTbot: time update 4am")

    elif(current_time==timeMapper.five):
        HLEngine_audioProcess.playsound("voice/5am.wav")
        print("MATTbot: time update 5am")

    elif(current_time==timeMapper.six):
        HLEngine_audioProcess.playsound("voice/6am.wav")
        print("MATTbot: time update 6am")

    elif(current_time== timeMapper.seven):
        HLEngine_audioProcess.playsound("voice/7am.wav")
        print("MATTbot: time update 7am")

    elif(current_time==timeMapper.eight):
        HLEngine_audioProcess.playsound("voice/8am.wav")
        print("MATTbot: time update 8am")

    elif(current_time==timeMapper.nine):
        HLEngine_audioProcess.playsound("voice/9am.wav")
        print("MATTbot: time update 9am")

    elif(current_time==timeMapper.ten):
        HLEngine_audioProcess.playsound("voice/10am.wav")
        print("MATTbot: time update 10am")

    elif(current_time==timeMapper.eleven):
        HLEngine_audioProcess.playsound("voice/11am.wav")
        print("MATTbot: time update 11am")

    elif(current_time==timeMapper.twelve):
        HLEngine_audioProcess.playsound("voice/12pm.wav")
        print("MATTbot: time update 12pm")

    elif(current_time==timeMapper.thirteen):
        HLEngine_audioProcess.playsound("voice/1pm.wav")
        print("MATTbot: time update 1pm")

    elif(current_time==timeMapper.fourteen):
        HLEngine_audioProcess.playsound("voice/2pm.wav")
        print("MATTbot: time update 2pm")

    elif(current_time==timeMapper.fifteen):
        HLEngine_audioProcess.playsound("voice/3pm.wav")
        print("MATTbot: time update 3pm")

    elif(current_time==timeMapper.sixteen):
        HLEngine_audioProcess.playsound("voice/4pm.wav")
        print("MATTbot: time update 4pm")

    elif(current_time==timeMapper.seventeen):
        HLEngine_audioProcess.playsound("voice/5pm.wav")
        print("MATTbot: time update 5pm")

    elif(current_time==timeMapper.eighteen):
        HLEngine_audioProcess.playsound("voice/6pm.wav")
        print("MATTbot: time update 6pm")

    elif(current_time==timeMapper.nineteen):
        HLEngine_audioProcess.playsound("voice/7pm.wav")
        print("MATTbot: time update 7pm")

    elif(current_time==timeMapper.twenty):
        HLEngine_audioProcess.playsound("voice/8pm.wav")
        print("MATTbot: time update 8pm")

    elif(current_time==timeMapper.twentyone):
        HLEngine_audioProcess.playsound("voice/9pm.wav")
        print("MATTbot: time update 9pm")

    elif(current_time==timeMapper.twentytwo):
        HLEngine_audioProcess.playsound("voice/10pm.wav")
        print("MATTbot: time update 10pm")

    elif(current_time==timeMapper.twentythree):
        HLEngine_audioProcess.playsound("voice/11pm.wav")
        print("MATTbot: time update 11pm")
