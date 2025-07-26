import pymongo
import hashlib
import numpy as np
from datetime import datetime

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
database = mongo_client.secure_face_db

def generate_hash(embedding_vector):
    return hashlib.sha256(embedding_vector.tobytes()).hexdigest()

def save_user_embedding(user_id, embedding_vec):
    record = {
        "user_id": user_id,
        "embedding_hash": generate_hash(embedding_vec),
        "embedding_data": embedding_vec.tolist()
    }
    database.user_records.insert_one(record)

def search_best_match(embedding_vec, similarity_threshold=0.5):
    all_users = list(database.user_records.find())
    best_candidate = (None, float('inf'))  # (user_id, distance)
    for user in all_users:
        stored_embedding = np.array(user["embedding_data"])
        distance = np.linalg.norm(stored_embedding - embedding_vec)
        if distance < best_candidate[1]:
            best_candidate = (user["user_id"], distance)
    if best_candidate[1] < similarity_threshold:
        return best_candidate
    return None

def log_failed_attempt(ip_address, timestamp=None):
    log_entry = {
        "ip_address": ip_address,
        "attempt_time": timestamp or datetime.utcnow()
    }
    database.access_logs.insert_one(log_entry)
