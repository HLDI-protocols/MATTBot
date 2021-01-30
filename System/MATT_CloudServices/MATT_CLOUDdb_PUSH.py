def CLOUDDB_PUSH(PATH,SUBPATH,direction,id,DATA):
    try:

        import firebase_admin
        from firebase_admin import credentials, firestore
        cred = credentials.Certificate("mattbot.json")
        firebase_admin.initialize_app(cred)

        firestore_db = firestore.client()
        firestore_db.collection(PATH).document(str(id)).set({SUBPATH: DATA})
        return('[uploaded to MATTcloud]')
    except:
        return('[ERROR in CLOUDDB_PUSH]')

