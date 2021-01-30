def RTDB_PUSH(PATH,SUBPATH,Message):

    try:
 
        from firebase import firebase
        firCon="https://mattbot-2d336.firebaseio.com/"

        firebase = firebase.FirebaseApplication(firCon, None)
        firebase.put(PATH,SUBPATH,Message)
        #firebase.put('/REMOTE_ACTION/','action',Message)
        return('[UPDATED to MATTcloud]')

    except:

        return('[ERROR IN FIRE RTDB_PUSH]')
