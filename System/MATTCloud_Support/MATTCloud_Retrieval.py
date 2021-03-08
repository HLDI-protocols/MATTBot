def GetIT():
    try:
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://mattbot-2d336.firebaseio.com/', None)
        result = firebase.get('/MESSAGE/', 'messages')
        return(result)
    except:
        return('[ERROR in MATTCloud_Retrieval]')