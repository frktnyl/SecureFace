import os
import pickle
import numpy as np

class FaceDataStore:
    def __init__(self, filepath='user_faces.pkl'):
        self.filepath = filepath
        self.records = self._load_data()

    def _load_data(self):
        if os.path.isfile(self.filepath):
            with open(self.filepath, 'rb') as file:
                return pickle.load(file)
        return {}

    def persist(self):
        with open(self.filepath, 'wb') as file:
            pickle.dump(self.records, file)

    def insert_user(self, user_id, embeddings_list):
        if user_id in self.records:
            self.records[user_id].extend(embeddings_list)
        else:
            self.records[user_id] = embeddings_list
        self.persist()
        print(f"[BAŞARILI] {user_id} sisteme başarıyla eklendi.")

    def list_users(self):
        return list(self.records.keys())

    def fetch_user_embeddings(self, user_id):
        return self.records.get(user_id, [])
