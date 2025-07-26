import streamlit as st
import cv2
from face_utils import get_embedding as calculate_embedding, extract_faces as detect_faces
from db import enroll_user as register_user, find_match as search_match, log_fail as log_failure
import numpy as np

st.title("SecureFace")

selected_mode = st.sidebar.selectbox("İşlem Seçiniz", ["Oturum Aç", "Yeni Kayıt"])

camera = cv2.VideoCapture(0)
success, img = camera.read()
camera.release()

detected_faces = detect_faces(img)
if len(detected_faces) > 1:
    st.warning("Birden fazla yüz tespit edildi! Lütfen tek kişi olduğunuzdan emin olun.")
elif len(detected_faces) == 0:
    st.info("Yüz algılanamadı, lütfen kameraya doğru bakınız.")
else:
    single_face = detected_faces[0]
    embedding_vector = calculate_embedding(single_face)
    if selected_mode == "Yeni Kayıt":
        username = st.text_input("Kullanıcı İsmi Giriniz")
        if st.button("Kaydet"):
            for _ in range(10):
                register_user(username, embedding_vector)
            st.success(f"{username} başarıyla kaydedildi.")
    else:
        if st.button("Oturum Aç"):
            matched_user = search_match(embedding_vector)
            if matched_user:
                st.success(f"{matched_user[0]} sisteme giriş yaptı, hoş geldiniz!")
            else:
                log_failure(st.session_state.get('client_ip', 'bilinmeyen_ip'))
                st.error("Giriş başarısız oldu! Yetkilendirme sağlanamadı.")
