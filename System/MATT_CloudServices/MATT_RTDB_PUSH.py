def fireRTDB_push(Message):
 
    from firebase import firebase
    firCon="https://mattbot-2d336.firebaseio.com/"

    firebase = firebase.FirebaseApplication(firCon, None)
    firebase.put('/REMOTE_ACTION/','action',Message)
    return('[Record Updated]')

fireRTDB_push("LIZZ")
