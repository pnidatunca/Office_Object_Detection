# Office_Object_Detection
Bu proje, kendi veri setimle eğittiğim YOLOv8 yapay zeka modelini (`best.pt`) test etmek için yazdığım bir Python otomasyonudur.
Modeli eğittikten sonra "Acaba gerçek fotoğraflarda nasıl çalışıyor?" diye tek tek bakmak yerine, bu scripti çalıştırıyorum. Kod, test klasöründeki tüm fotoğrafları alıyor, tahminlerini yapıyor, sonuçları çiziyor ve hem bana gösteriyor hem de bilgisayarıma kaydediyor.

## Neler Kullanıldı?

Bu projeyi çalıştırmak için bilgisayarınızda şu kütüphanelerin olması gerekiyor:

* **Ultralytics (YOLOv8):** Eğittiğim `.pt` modelini çalıştırmak ve nesne tespiti yapmak için.
* **OpenCV (cv2):** Görüntüleri işlemek, ekrana pencere açıp göstermek ve sonuçları kaydetmek için.
* **OS:** Klasör oluşturma ve dosya yollarını yönetmek için.

## Kod Nasıl Çalışıyor?
Sistem şu 4 temel adımı otomatik olarak yapıyor:

### 1. Modelin Yüklenmesi
Kod ilk açıldığında `best.pt` dosyasını arar. Bu benim kendi eğittiğim ağırlık dosyasıdır. (Eğer siz kullanacaksanız kendi .pt dosyanızın adını buraya yazmalısınız).

### 2. Klasör Hazırlığı
Sonuçları kaydetmek için otomatik olarak `Prediction_Results` adında bir klasör oluşturur. Eğer klasör zaten varsa hata vermez, onu kullanır.

### 3. Toplu Tahmin (Batch Prediction)
`test` klasörünün içindeki tüm görselleri (`.jpg`, `.png` vb.) sırayla modele gönderir. Güven skoru (confidence) **0.50** ve üzerindeki tespitleri kabul eder.

### 4. Kayıt ve Gösterim (Save & Show)
Her bir resim için:
* YOLO'nun çizdiği kutucukları alır (`result.plot()`).
* Resmi `Prediction_Results` klasörüne aynı isimle kaydeder.
* Ekranda bir pencere açarak sonucu bana gösterir. Ben bir tuşa basana kadar bekler, böylece sonucu inceleyebilirim.

## 📸 Örnek Sonuçlar

<img width="641" height="602" alt="image" src="https://github.com/user-attachments/assets/f6699441-4683-4a8d-a443-ddd1a0026c25" />

<img width="646" height="602" alt="image" src="https://github.com/user-attachments/assets/3c60ed64-49cc-4419-b396-55470e20c446" />

<img width="642" height="612" alt="image" src="https://github.com/user-attachments/assets/59ecccca-c34e-4c7c-a3bc-9c1ce4edabaa" />


## Nasıl Çalıştırılır?

1.  Proje klasörüne `best.pt` model dosyanızı koyun.
2.  `test` adında bir klasör oluşturun ve içine test edilecek fotoğrafları atın.
3.  Kodu çalıştırın:
    ```bash
    python main.py
    ```
4.  Açılan pencerede her bir sonraki resme geçmek için **herhangi bir tuşa** (boşluk, enter vb.) basın.
5.  Programdan tamamen çıkmak için resim penceresindeyken **'q'** tuşuna basın.


##  Notlar
* Bu kod **Local PC (Kendi bilgisayarınız)** üzerinde çalışmak için tasarlanmıştır. Google Colab'da `cv2.imshow` çalışmayabilir, onun yerine `cv2_imshow` kullanmak gerekir.
* Güven skorunu (conf) değiştirmek isterseniz kodun içindeki `conf=0.50` kısmını `0.25` veya `0.70` yapabilirsiniz.
