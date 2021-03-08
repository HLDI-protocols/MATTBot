#Built by APJ
import string
def dataDecryption(data):
    data=str(data)
    dataModel=[]
    ASCER=(string.printable)
    for i in ASCER:
        dataModel.append(i)
    keyLoader=open('/home/predator/HLDi/MATTBot/System/King_Crypto/key.txt','r')
    key=keyLoader.read()
    keyModel=str(key)
    decrypt=[]
    decryption=[]
    stringer=""
    for i in data:
        if(i in keyModel):
            position=keyModel.index(i)
            decrypt.append(position)
    for i in decrypt:
        decode=dataModel[i]
        decryption.append(decode)

    decrypted=stringer.join(decryption)
    return(decrypted)
        

        
        