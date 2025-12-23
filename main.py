import os
import cv2
from ultralytics import YOLO

# 1. Modeli Yükle
model = YOLO("best.pt")

# 2. Kayıt Klasörünü Oluştur
# Eğer 'Prediction_Results' diye bir klasör yoksa oluşturur.
output_folder = "Prediction_Results"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 3. Tahmin Yap (test klasöründeki tüm resimler için)
results = model.predict(source="test", conf=0.50, stream=True)

print("İşlem başlıyor... Fotoğraflar hem gösterilecek hem kaydedilecek.")
print("Çıkmak için resim penceresindeyken 'q' tuşuna basabilirsin.")

for result in results:
    # --- A. Çizilmiş Resmi Al ---
    im_array = result.plot()

    # --- B. Dosya İsmini Bul ---
    filename = os.path.basename(result.path)

    # --- C. Kaydet ---
    save_path = os.path.join(output_folder, filename)
    cv2.imwrite(save_path, im_array)
    print(f"Kaydedildi: {save_path}")

    # --- D. Ekranda Göster ---
    cv2.imshow("Sonuc (Gecmek icin bir tusa bas)", im_array)

    # Tuşa basana kadar bekle (q'ya basarsa komple çıkar)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print("Tüm işlemler bitti! 'Prediction_Results' klasörünü kontrol et.")