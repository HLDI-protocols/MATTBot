#Built by APJ
import string
def dataEncryption(data):

    keyLoader=open('/home/predator/HLDi/MATTBot/System/King_Crypto/key.txt','r')
    key=keyLoader.read()

    dataModel=[]
    ASCER=(string.printable)
    for i in ASCER:
        dataModel.append(i)
 
    
    keyModel=str(key)
    Position_Generator=[]

    Data=str(data)
    for i in Data:
        #print(i)
        if(i in Data):
            Position=dataModel.index(i)
            Position_Generator.append(Position)

    #print(Position_Generator)


    encrypt=[]
    stringer=""
    for i in Position_Generator:
        
        data=keyModel[i]
        encrypt.append(data)
        


    encrypted=stringer.join(encrypt)    
    return(encrypted)