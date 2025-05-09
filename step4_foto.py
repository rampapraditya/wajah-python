import cv2

# Load model Haar Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Baca gambar dari file
image_path = 'foto_input.jpg'  # ganti dengan nama file gambar kamu
image = cv2.imread(image_path)

if image is None:
    print("Gambar '{image_path}' tidak ditemukan.")
    exit()

# Konversi ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Deteksi wajah
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Gambar kotak di sekitar wajah
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Tampilkan gambar
cv2.imshow('Deteksi Wajah dari Gambar', image)
cv2.waitKey(0)
cv2.destroyAllWindows()