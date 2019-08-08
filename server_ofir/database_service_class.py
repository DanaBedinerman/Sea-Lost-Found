import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import json


def history_item_to_json(history_item):
    timestamp = history_item['time']
    history_item['second'] = timestamp.second
    history_item['minute'] = timestamp.minute
    history_item['hour'] = timestamp.hour
    history_item['day'] = timestamp.day
    history_item['month'] = timestamp.month
    history_item['year'] = timestamp.year
    del history_item['time']

    return history_item


def history_item_builder(latitude=34, longitude=25, direction=0, speed=0, radius=5):
    history_item = {
        u'latitude': latitude,
        u'longitude': longitude,
        u'direction': direction,
        u'speed': speed,
        u'radius': radius,
        u'time': datetime.datetime.utcnow()

    }

    return history_item


class DatabaseServiceClass:
    def __init__(self):
        cred = credentials.Certificate('./sea-lost-and-found-firebase-adminsdk-y70sk-94f45494e2.json')
        default_app = firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def add_to_item_history(self, item_id, latitude=34, longitude=25, direction=0, speed=0, radius=5):
        item_ref = self.db.collection(u'lost objects').document(item_id)
        history_ref = item_ref.collection(u'history')
        data = history_item_builder(latitude, longitude, direction, speed, radius)
        history_ref.add(data)

    def create_new_item(self, latitude=34, longitude=25, direction=0, speed=0, radius=5):
        new_item_ref = self.db.collection(u'lost objects').document()
        new_item_ref.collection(u'history').add(history_item_builder(latitude, longitude, direction, speed, radius))
        new_item_ref.set({
            u'id': new_item_ref.id
        }, merge=True)

        return new_item_ref.id

    def get_item_history(self, item_id):
        item_ref = self.db.collection(u'lost objects').document(item_id)
        history_ref = item_ref.collection(u'history')
        json_item = '{"id": "' + item_id + '",'
        item_history = '['
        for doc in history_ref.stream():
            y = json.dumps(history_item_to_json(doc.to_dict()))
            item_history = item_history + y + ','
        item_history = item_history[:-1]
        item_history = item_history + ']'
        json_item = json_item + ' "history": ' + item_history + '}'

        return json_item

    # def get_all_items_history(self, ):
    #     items_ref = self.db.collection(u'lost objects')
    #     json_all_items = '['
    #     docs = self.db.collection(u'lost objects').stream()
    #
    #     for doc in docs:
    #         # history_ref = doc.collection(u'history')
    #         print(doc.id)
    #         print(self.get_item_history(doc.id))

    def get_item_latest_history(self, item_id):
        history_ref = self.db.collection(u'lost objects').document(item_id).collection(u'history') \
            .order_by(u'time', direction=firestore.Query.DESCENDING).limit(1)
        item_history = ''
        for doc in history_ref.stream():
            item_history=history_item_to_json(doc.to_dict())

        return item_history
