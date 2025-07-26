# 🎭 SecureFace — Yüz Tanıma Tabanlı Kimlik Doğrulama Sistemi

## 📌 Proje Hakkında

**SecureFace**, Python ve modern yapay zeka teknolojileri kullanarak geliştirilmiş,  
gerçek zamanlı yüz tanıma tabanlı kimlik doğrulama uygulamasıdır.  

- MTCNN ile canlı kamera görüntüsünden yüz algılama  
- FaceNet modeli ile 128 boyutlu yüz embedding çıkarma  
- MongoDB’de yüz embeddinglerini güvenli ve hızlı yönetme  
- Streamlit arayüzü ile kullanıcı dostu deneyim  
- Başarılı ve başarısız girişlerin loglanması  

## ⚙️ Özellikler

- 🔹 Yeni kullanıcı kayıt ve yüz verisi ekleme (10 farklı poz)  
- 🔹 Canlı kamera ile yüz algılama ve doğrulama  
- 🔹 Yüz benzerlik oranına göre güvenilir giriş kontrolü  
- 🔹 Giriş başarısızlıklarında IP ve zaman kaydı  
- 🔹 Dosya veya veritabanı tabanlı yüz veri yönetimi opsiyonu  
- 🔹 Basit, sade ve modern kullanıcı arayüzü  

## 📁 Dosya Yapısı

├── detected_faces.py       # Yüz algılama ve embedding çıkarma
├── face_db_manager.py      # MongoDB işlemleri (kayıt, arama, loglama)
├── faceDataBase.py         # Dosya tabanlı yüz veri yönetimi (opsiyonel)
├── secureface_app.py       # Streamlit arayüzü ve uygulama akışı
└── README.md               # Proje açıklaması

## 🛠 Teknolojiler

- Python 3.8
- Streamlit
- OpenCV
- MTCNN
- TensorFlow / Keras
- MongoDB
- NumPy


