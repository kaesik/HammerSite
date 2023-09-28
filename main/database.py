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

db_items = db.child('items').get()
db_ammunition = [item for item in db.child('items').child('ammunition').get()]
db_armor = [item for item in db.child('items').child('armors').get()]
db_weapons = [item for item in db.child('items').child('weapons').get()]