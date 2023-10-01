import pyrebase
import os

firebaseConfig = {
    'apiKey': os.environ.get('FIREBASE_API_KEY'),
    'authDomain': "wh-db-72f36.firebaseapp.com",
    'databaseURL': 'https://wh-db-72f36-default-rtdb.europe-west1.firebasedatabase.app/',
    'projectId': "wh-db-72f36",
    'storageBucket': "wh-db-72f36.appspot.com",
    'messagingSenderId': "334358927008",
    'appId': "1:334358927008:web:700f4e34f27aa06df6dbc5",
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

#ITEMS
db_items = []
for group in [
        group.val() for group in
        db.child('en').child('wfrp').child('items').get()
]:
    for type in group:
        if type == 'melee' or type == 'ranged':
            for subtype in group[type]:
                for item in group[type][subtype]:
                    db_items.append(group[type][subtype][item])
        else:
            for item in group[type]:
                db_items.append(group[type][item])


# db_armor = [item for item in db.child('items').child('armors').get()]
# db_weapons = [item for item in db.child('items').child('weapons').get()]