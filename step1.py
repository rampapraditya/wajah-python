import cv2

# Inisialisasi kamera (0 = default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Tidak dapat membuka kamera.")
    exit()

print("✅ Kamera berhasil dibuka. Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal menangkap frame.")
        break

    # Tampilkan frame ke jendela
    cv2.imshow('Kamera', frame)

    # Keluar jika pengguna menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan
cap.release()
cv2.destroyAllWindows()
