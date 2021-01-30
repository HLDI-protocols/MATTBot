
def CLOUDDB_FETCHER(PATH,SUBPATH):
    
    try:
        import firebase_admin
        from firebase_admin import credentials, firestore
        cred = credentials.Certificate("mattbot.json")
        firebase_admin.initialize_app(cred)

        usabledata=[]

        firestore_db = firestore.client()
        snapshots = list(firestore_db.collection(PATH).get())
        for snapshot in snapshots:
            data=snapshot.to_dict()
            a=data[SUBPATH]
            usabledata.append(str(a))
        print(usabledata)
        pos=len(usabledata)
        if(usabledata[pos-1]!=usabledata[pos-2]):
            return(usabledata[pos-1])
        else:
            print("[no change]")

    except:
        print('[ERROR IN EXECUTING CLOUDDB_FETCHER ]')
