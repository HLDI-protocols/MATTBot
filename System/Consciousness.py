import random
import string
import MATTbot_Engine
import os
from HLEngine import HLEngine_Progressbar
from HLEngine import HLEngine_wordX
from HLEngine import HLEngine_audioProcess
from HLEngine import HLEngine_communications
from HLEngine import HLEngine_camSnap


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

SIGNING_INPUT=("bye","poweroff","tata","goodbye","adios")
SIGNING_OUTPUT=("bye","good bye","tata","adios amigo","thanks")

SERIAL_MODE=("connected devices","search devices","devices","connect to device")

EMOTIONS=("wait","sad","well","terrified","confused","confusion","bad","love","sleep","happy","ha","great","awesome","dump","not well","stupid","mm","mmm","ok","okay","ya","thats fine","mmmm",":P",":)",";p",";)","oh yea")

EMOTION_OUT_SAD=("its okay","you can overcome it","you are amazing guy bro","dont be sad, I am with you","you are cute bro","its okay, things can go wrong. Nobody is perfect")

EMOTION_OUT_HAPPY=("thats cool","wow","you are awesome","i am happy to see you happy","great dude. keep on pushing")

EMOTIONS_NO=("mm","okay","ya","thats fine","mmmm",":P",":)",";p",";)","oh yea")

BAD_Words=("fuck","fuck you","fuckyou","asshole","you rubbish","fuck off","jack ass","jerk")

questions=("what","how","who","when","which","may","learn","study")

STUDY_NEW=("learn","study")

MUSIC=("music","song","play")

MUSIC_LIST=("music/1.mp3","music/2.mp3","music/3.mp3","music/theme.mp3")

SHUTDOWN=("shutdown","poweroff","turnoff","turn off","init 0")

REBOOT=("reboot","restart","init 6")

CAMERA_SER=("camserver","spy","eye")

STOP_CAMERA_SER=("kill_spy","terminate_spy","pluck_eye","murder_spy")

IP=("ip","address","network","gateway")

SECURITY=("iris")

KILL_SECURITY=("kill_security","terminate_security")

PURPOSE=("purpose","detail","capable")

INTRODUCTION=("yourself","introduce","name")

AUTOMATA=("automation","auto","takeover")

MOTION=("motion_reference","spy_reference","camera_server_reference")

SOUND_CLOUD_HITS=("soundcloud","sound cloud", "favourites","favourite","cloud","songs")
SOUND_CLOUD=("https://soundcloud.com/datastream1986/star-racer","https://soundcloud.com/ageofvolt/supreme-delight-free-download","https://soundcloud.com/ageofvolt/volts-theme","https://soundcloud.com/theundeadaudio/a-love-letter","https://soundcloud.com/time-travel-beats/sunny","https://soundcloud.com/miamisunsets/dark-city-ft-emilio-asstevez","https://soundcloud.com/juno-dreams/be-with-me-remastered-2018","https://soundcloud.com/spaceinvaderspaceinvader/ocean-drive-avenue-dont-you-like-it-spaceinvader-remix","https://soundcloud.com/morgan-willis-1982/professor-omega-feat-paradise-walk-supernova-album","https://soundcloud.com/moter-gr/vortex","https://soundcloud.com/ageofvolt/wunderbar","https://soundcloud.com/chill/digy-tragedy-ft-kirsch")

def introduction(sentence):
    for word in sentence.split():
        if word.lower() in INTRODUCTION:
            HLEngine_audioProcess.playsound("voice/myself.wav")
            HLEngine_audioProcess.playsound("voice/purpose1.wav")


def purpose(sentence):
    for word in sentence.split():
        if word.lower() in PURPOSE:
            HLEngine_audioProcess.playsound("voice/purpose2.wav")




def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            HLEngine_audioProcess.playsound("voice/service.wav")
            return random.choice(GREETING_RESPONSES)



def bye(sentence):
 
    for word in sentence.split():
        if word.lower() in SIGNING_INPUT:
            HLEngine_Progressbar.progress("MATT down")
            HLEngine_audioProcess.playsound("voice/bye.wav")
            return ("off")

def utilCOM(sentence):
    for word in sentence.split():
        if word.lower() in SERIAL_MODE:
            try:   
                HLEngine_audioProcess.playsound("voice/wait.wav")             
                PORT=MATTbot_Engine.commonProtocols()
                return(PORT)
            except:
                print("Consciousness ERROR")

def EmotionDetector(sentence):
    for word in sentence.split():
        if word.lower() in EMOTIONS:
            HLEngine_audioProcess.playsound("voice/wait.wav") 
            result=MATTbot_Engine.sentimentalAnalsys(sentence)
            if(result<0):
                HLEngine_audioProcess.playsound("voice/sad.wav")
                return random.choice(EMOTION_OUT_SAD)
            elif(result>0):
                HLEngine_audioProcess.playsound("voice/happy.wav")
                return random.choice(EMOTION_OUT_HAPPY)
            else:
                return random.choice(EMOTIONS_NO)

def fight(sentence):
    for word in sentence.split():
        if word.lower() in BAD_Words:
            return random.choice(BAD_Words)


def superLogic(sentence):
    for word in sentence.split():
        if word.lower() in questions:
            HLEngine_audioProcess.playsound("voice/wait.wav") 
            ans=MATTbot_Engine.analyst(sentence)            
            return(ans)
            

def hyperLogic(param):
    for word in param.split():
        if word.lower() in questions:
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
    """for word in param.split():
        if word.lower() in MUSIC:
            HLEngine_audioProcess.playsound("voice/wait.wav") 
            location=str(random.choice(MUSIC_LIST))
            HLEngine_audioProcess.playsound(location)"""
    os.system("./playboy.sh")
    return("playing as requested")
            
def down(sentence): 
    for word in sentence.split():
        if word.lower() in SHUTDOWN:
            HLEngine_Progressbar.progress("shutting down System")
            HLEngine_audioProcess.playsound("voice/bye.wav")
            HLEngine_communications.linux_shutdown()
            return("shutdown")

def reboot(sentence): 
    for word in sentence.split():
        if word.lower() in REBOOT:
            HLEngine_Progressbar.progress("rebooting")
            HLEngine_audioProcess.playsound("voice/reboot.wav")
            HLEngine_communications.linux_boot()
            return("reboot")

def spy(sentence):    
    for word in sentence.split():
        if word.lower() in CAMERA_SER:
            HLEngine_audioProcess.playsound("voice/wait.wav")
            HLEngine_Progressbar.progress("arming spy")
            HLEngine_communications.ifconfig()
            HLEngine_communications.spy()
            return("spy")


def killSpy(sentence):
    for word in sentence.split():
            if word.lower() in STOP_CAMERA_SER:
                HLEngine_audioProcess.playsound("voice/wait.wav")
                HLEngine_Progressbar.progress("murdering spy")
                HLEngine_communications.stop_spy()
                return("spy")



def IRIS(sentence):
    
    for word in sentence.split():
            if word.lower() in SECURITY:
                ip=input("\nEnter the cam IP address (eg:http://192.168.0.1:8081/video)\n")
                cascade="i.xml"
                frameName="MATT_IRIS"
                HLEngine_audioProcess.playsound("voice/wait.wav")
                print("MATT_IRIS PROTOCOL ARMED")
                while(True):
                    action=HLEngine_camSnap.liveCam_filter(cascade,ip,frameName)
                    print(action)
                    if(action==True):
                        print("MATTbot:intruder Detected")
                        HLEngine_audioProcess.playsound("voice/dataHere.wav")
                        


            
def soundCloud(sentence):
    for word in sentence.split():
        if word.lower() in SOUND_CLOUD_HITS: 
            HLEngine_Progressbar.progress("Opening Browser")           
            link=random.choice(SOUND_CLOUD)
            import webbrowser
            webbrowser.open(link, new=2)


def motionRef(sentence):
    for word in sentence.split():
        if word.lower() in MOTION: 
            print('MATTbot:Motion is already installed')
            HLEngine_Progressbar.progress("Opening Browser")           
            link="https://www.instructables.com/id/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/"
            import webbrowser
            webbrowser.open(link, new=2)


def automata(sentence):
    for word in sentence.split():
        if word.lower() in AUTOMATA: 
            HLEngine_Progressbar.progress("Automata Enabling")        
            HLEngine_communications.automatA()   
            

            



