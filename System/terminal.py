import Consciousness_Proto
from HLEngine import HLEngine_audioProcess
from HLEngine import HLEngine_communications

def terminalAccess(request):
    
        
        fetchGr=Consciousness_Proto.greeting(request)
        fetchBy=Consciousness_Proto.bye(request)   
        Fight=Consciousness_Proto.fight(request)
        #responser=Consciousness_Proto.superLogic(request)
        playBoy=Consciousness_Proto.playSome(request)
        shutdown=Consciousness_Proto.down(request)
        reboot=Consciousness_Proto.reboot(request)
        spy=Consciousness_Proto.spy(request)
        kill=Consciousness_Proto.killSpy(request)
        reminder=Consciousness_Proto.create_reminder(request)
        Consciousness_Proto.soundCloud(request)
        Consciousness_Proto.introduction(request)
        Consciousness_Proto.purpose(request)    
        Consciousness_Proto.automata(request)
        Consciousness_Proto.motionRef(request)
        Consciousness_Proto.vectorBot(request)
        Consciousness_Proto.analog_Controller(request)
        Consciousness_Proto.facebook(request)
        Consciousness_Proto.youtube(request)
        Consciousness_Proto.leave(request)
        Consciousness_Proto.target_identification(request)
        Consciousness_Proto.wakeup(request)
        Consciousness_Proto.radioMango(request)
        Consciousness_Proto.clubFM(request)
        Consciousness_Proto.akashavani(request)
        
        #Consciousness_Proto.IRIS(request)
def terminalSubroutine(HOST,NAME,MESSAGE):
        data=Consciousness_Proto.chatClient(HOST,NAME,MESSAGE)
        return(data)
def terminalSubroutine_2(HOST,NAME,MESSAGE):
        data=Consciousness_Proto.chatServer(HOST,NAME,MESSAGE)
        return(data)
        
    

 
    
  
    
