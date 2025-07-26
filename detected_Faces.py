import cv2
import numpy as np
from mtcnn import MTCNN
from tensorflow.keras.models import load_model

face_detector = MTCNN()
face_embedding_model = load_model('models/facenet_keras.h5')

def detect_faces_from_frame(frame):
    detections = face_detector.detect_faces(frame)
    detected_faces = []
    for det in detections:
        x, y, w, h = det['box']
        detected_faces.append(frame[y:y+h, x:x+w])
    return detected_faces

def calculate_face_embedding(face_img):
    resized_face = cv2.resize(face_img, (160, 160))
    normalized_face = resized_face.astype('float32') / 255.0
    expanded_face = np.expand_dims(normalized_face, axis=0)
    embedding_vector = face_embedding_model.predict(expanded_face)[0]
    return embedding_vector
