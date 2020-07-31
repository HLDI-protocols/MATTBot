'''
HLDynamic Integrations 2020
Author:Er.Akhil P Jacob
CONCIOUSNESS
last updated on 10/05/2020
'''
import random
import string
import MATTbot_Engine
import os
from HLEngine import HLEngine_Progressbar
from HLEngine import HLEngine_wordX
from HLEngine import HLEngine_audioProcess
from HLEngine import HLEngine_communications
from HLEngine import HLEngine_ImageProcessing
from Seeker import taskMapping
from Seeker import timeMapper
from MATT_Ware import Devices



def introduction(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.INTRODUCTION:
            HLEngine_audioProcess.playsound("voice/myself.wav")
            HLEngine_audioProcess.playsound("voice/purpose1.wav")


def purpose(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.PURPOSE:
            HLEngine_audioProcess.playsound("voice/purpose2.wav")




def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in taskMapping.GREETING_INPUTS:
            HLEngine_audioProcess.playsound("voice/service.wav")
            return random.choice(taskMapping.GREETING_RESPONSES)



def bye(sentence):
 
    for word in sentence.split():
        if word.lower() in taskMapping.SIGNING_INPUT:
            HLEngine_Progressbar.progress("MATT down")
            HLEngine_audioProcess.playsound("voice/bye.wav")
            return ("off")

def utilCOM(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.SERIAL_MODE:
            try:   
                HLEngine_audioProcess.playsound("voice/wait.wav")             
                PORT=MATTbot_Engine.commonProtocols()
                return(PORT)
            except:
                print("Consciousness ERROR")

def EmotionDetector(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.EMOTIONS:
            HLEngine_audioProcess.playsound("voice/wait.wav") 
            result=MATTbot_Engine.sentimentalAnalsys(sentence)
            if(result<0):
                HLEngine_audioProcess.playsound("voice/sad.wav")
                return random.choice(taskMapping.EMOTION_OUT_SAD)
            elif(result>0):
                HLEngine_audioProcess.playsound("voice/happy.wav")
                return random.choice(taskMapping.EMOTION_OUT_HAPPY)
            else:
                return random.choice(taskMapping.EMOTIONS_NO)

def fight(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.BAD_Words:
            return random.choice(taskMapping.BAD_Words)


def superLogic(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.questions:
            HLEngine_audioProcess.playsound("voice/wait.wav") 
            ans=MATTbot_Engine.analyst(sentence)            
            return(ans)
            

def hyperLogic(param):
    for word in param.split():
        if word.lower() in taskMapping.questions:
            HLEngine_Progressbar.progress("Gathering")
            data=HLEngine_wordX.EW(param)
            xlogic=MATTbot_Engine.gainWisdom(data)
            HLEngine_audioProcess.playsound("voice/dataHere.wav") 
            f=open("hiveMind/hiveMind.txt","a")
            f.write(xlogic)
            f.close()
            HLEngine_audioProcess.playsound("voice/burn.wav") 
            return(xlogic)

def playSome(param):

    for word in param.split():
        if word.lower() in taskMapping.MUSIC:   
        
            os.system("./playboy.sh")
            return("playing as requested")
        else:
            return("********")
            
def down(sentence): 
    for word in sentence.split():
        if word.lower() in taskMapping.SHUTDOWN:
            HLEngine_Progressbar.progress("shutting down System")
            HLEngine_audioProcess.playsound("voice/bye.wav")
            HLEngine_communications.linux_shutdown()
            return("shutdown")

def reboot(sentence): 
    for word in sentence.split():
        if word.lower() in taskMapping.REBOOT:
            HLEngine_Progressbar.progress("rebooting")
            HLEngine_audioProcess.playsound("voice/reboot.wav")
            HLEngine_communications.linux_boot()
            return("reboot")

def spy(sentence):    
    for word in sentence.split():
        if word.lower() in taskMapping.CAMERA_SER:
            HLEngine_audioProcess.playsound("voice/wait.wav")
            HLEngine_Progressbar.progress("arming spy")
            HLEngine_communications.ifconfig()
            HLEngine_communications.spy()
            return("spy")


def killSpy(sentence):
    for word in sentence.split():
            if word.lower() in taskMapping.STOP_CAMERA_SER:
                HLEngine_audioProcess.playsound("voice/wait.wav")
                HLEngine_Progressbar.progress("murdering spy")
                HLEngine_communications.stop_spy()
                return("spy")



def IRIS(sentence):
    
    for word in sentence.split():
            if word.lower() in taskMapping.SECURITY:
                ip=input("\nEnter the cam IP address (eg:http://192.168.0.1:8081/video)\n")
                cascade="Filters/i.xml"
                frameName="MATT_IRIS"
                HLEngine_audioProcess.playsound("voice/wait.wav")
                print("MATT_IRIS PROTOCOL ARMED")
                while(True):
                    action=HLEngine_ImageProcessing.liveCam_filter(cascade,ip,frameName)
                    print(action)
                    if(action==True):
                        print("MATTbot:intruder Detected")
                        HLEngine_audioProcess.playsound("voice/dataHere.wav")
                        


            
def soundCloud(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.SOUND_CLOUD_HITS: 
            HLEngine_Progressbar.progress("Opening Browser")           
            link=random.choice(taskMapping.SOUND_CLOUD)
            import webbrowser
            webbrowser.open(link, new=2)


def motionRef(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.MOTION: 
            print('MATTbot:Motion is already installed')
            HLEngine_Progressbar.progress("Opening Browser")           
            link="https://www.instructables.com/id/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/"
            import webbrowser
            webbrowser.open(link, new=2)


def automata(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.AUTOMATA: 
            HLEngine_Progressbar.progress("Automata Enabling")        
            HLEngine_communications.automatA()   
            

def create_reminder(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.REMINDER: 
            HLEngine_Progressbar.progress("Opening Reminder Console")        
            time=str(input("Enter time: "))
            data=str(input("Enter Data to be Reminded: "))
            timeMapper.ALERT.append(time)
            timeMapper.REMIND_ALERT.append(data)
           
            print("WARNING !!!!: Reminder works only for this Instance of MATTBOT.")
            return("Reminder Added to MATTbot")


def vectorBot(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.VECTOR: 
            HLEngine_Progressbar.progress("Initializing")  
            botAddress=Devices.robot_Vector_COM
            HLEngine_communications.botAccess(botAddress)


def analog_Controller(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.ANALOG_CONTROLLER: 
            HLEngine_Progressbar.progress("Initializing")
            HLEngine_communications.VECTORCONTROLLER_JOYSTICK()

def facebook(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.FACEBOOK:
            HLEngine_Progressbar.progress("Initializing")
            import webbrowser
            link="www.facebook.com"
            webbrowser.open(link, new=2)


def youtube(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.YOUTUBE:
            HLEngine_Progressbar.progress("Initializing")
            import webbrowser
            link="www.youtube.com"
            webbrowser.open(link, new=2)


def leave(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.SICK:
            HLEngine_Progressbar.progress("Initializing")
            reason=input("Enter reason ....\n")
            date=input("Date .....\n")
            print("\n")

            print("Subject: Leave Application due to "+reason)
            print("Dear Sir,\n")
            print("Greetings of the day.")
            print("Kindly grant me leave on "+date+", Since I am having "+reason+".")
            print("Thanks and Regards,\n")
            print("Er.Akhil P Jacob,\n")
            print("Senior Robotics Engineer\n")
            print("Inker Robotics Thrissur\n")

            link="https://mail.yandex.com/?uid=1130000042136080#inbox"
            import webbrowser
            webbrowser.open(link, new=2)

def target_identification(param):

    for word in param.split():
        if word.lower() in taskMapping.TARGETS:   
        
            os.system("./tracker.sh")
            return("Enabling Cams as requested.....")
        else:
            return("********")

def wakeup(param):
    for word in param.split():
        if word.lower() in taskMapping.WAKEUP:   
        
            os.system("./wakeup.sh")
            return("Enabling Cams as requested.....")
        else:
            return("********")

    






    



