from HLEngine import HLEngine_ImageProcessing
from HLEngine import HLEngine_audioProcess
import time
filters="Filters/i.xml"
count=0
while(True):
    data=HLEngine_ImageProcessing.liveCam_filter(filters,0,"MATTBot 2020 Sleep Killer")
    print(data)
    if(data==True):
        print('MATTBot:Master is Working :p') 
    elif(data==False):
        count+=1
        print('MATTBot:Master is Sleeping :p')
        if(count>5):            
            time.sleep(2)
            HLEngine_audioProcess.playsound('voice/wakeup.wav')


 