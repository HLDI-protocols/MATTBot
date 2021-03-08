def SendIT(Message):
    try:

        from firebase import firebase
        firCon="https://mattbot-2d336.firebaseio.com/"

        firebase = firebase.FirebaseApplication(firCon, None)
        firebase.put('/MESSAGE/','messages',Message)
        return('[Record Updated]')
    except:
        return('[ERROR in MATTCloud_Updates]')


