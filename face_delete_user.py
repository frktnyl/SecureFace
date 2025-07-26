import pymongo
import getpass 
from hashlib import sha256

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.secure_face_db

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = sha256("admin123".encode()).hexdigest()

def verify_admin():
    print("🔐 Admin Girişi Gerekiyor")
    username = input("👤 Admin Kullanıcı Adı: ")
    password = getpass.getpass("🔑 Admin Şifresi: ")

    if username == ADMIN_USERNAME and sha256(password.encode()).hexdigest() == ADMIN_PASSWORD_HASH:
        print("✅ Doğrulama başarılı.\n")
        return True
    else:
        print("❌ Hatalı kullanıcı adı veya şifre.")
        return False

def delete_user(user_id):
    result = db.user_records.delete_many({"user_id": user_id})
    if result.deleted_count > 0:
        print(f"🗑️ {user_id} adlı kullanıcı başarıyla silindi.")
    else:
        print(f"⚠️ {user_id} kullanıcı bulunamadı.")

if __name__ == "__main__":
    if verify_admin():
        user_to_delete = input("Silinecek kullanıcı adını girin: ")
        confirm = input(f"⚠️ Emin misiniz? '{user_to_delete}' adlı kullanıcı silinecek (y/n): ")
        if confirm.lower() == "y":
            delete_user(user_to_delete)
        else:
            print("🚫 İşlem iptal edildi.")
