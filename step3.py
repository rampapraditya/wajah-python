import cv2
import os

# Load model Haar Cascade untuk deteksi wajah
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Membuat folder untuk menyimpan wajah jika belum ada
if not os.path.exists('wajah_tersimpan'):
    os.makedirs('wajah_tersimpan')

# Buka kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Tidak dapat membuka kamera.")
    exit()

print("Kamera berhasil dibuka. Tekan 'q' untuk keluar dan 's' untuk menyimpan wajah.")

face_id = 0  # ID untuk setiap wajah yang disimpan
saved_count = 0  # Jumlah wajah yang disimpan

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal menangkap frame.")
        break

    # Ubah ke grayscale (dibutuhkan untuk Haar)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Gambar kotak di sekitar wajah
    for (x, y, w, h) in faces:
        # Crop wajah dari frame
        face = frame[y:y+h, x:x+w]

        # Gambar kotak hijau di sekitar wajah
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Tampilkan hasil
    cv2.imshow('Deteksi Wajah', frame)

    # Cek jika tombol 's' ditekan untuk menyimpan wajah
    if cv2.waitKey(1) & 0xFF == ord('s') and len(faces) > 0:
        for (x, y, w, h) in faces:
            # Crop wajah dari frame
            face = frame[y:y+h, x:x+w]

            # Simpan wajah ke file
            file_name = f'wajah_tersimpan/wajah_{face_id}.jpg'
            cv2.imwrite(file_name, face)
            print(f"Wajah {face_id} disimpan: {file_name}")

            face_id += 1
            saved_count += 1

    # Keluar jika pengguna menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan
cap.release()
cv2.destroyAllWindows()
print(f"Total wajah yang disimpan: {saved_count}")
