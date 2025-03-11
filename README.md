# Dynamic Wallpaper with Calendar Events Overlay

Bu proje, herkese açık bir Google Takvim veya iCal URL'sinden çekilen etkinlikleri alıp, Windows masaüstü arka planınıza sağ üst köşede dinamik olarak ekleyen bir Python script'idir. Etkinlikler Türkiye saat dilimine (Europe/Istanbul) göre biçimlendirilir ve her güncellemede otomatik olarak yenilenir.

## Özellikler

- **Herkese Açık Takvim Entegrasyonu:**  
  Takviminizden iCal URL'si ile etkinlik verilerini çekin.
  
- **Dinamik Wallpaper Güncelleme:**  
  Etkinlikleri sağ üst köşede, "dd.mm.yyyy HH:MM - Etkinlik Adı" formatında gösterir.
  
- **Zaman Dilimi Dönüşümü:**  
  Etkinlik zamanı UTC'den Türkiye saatine çevrilir.

- **Görsel Çıktı:**  
  Güncellenmiş masaüstü resmi **masaustu_modified.jpg** olarak kaydedilir ve sistem arka planı otomatik olarak değiştirilir.

- **Örnek Çıktı:**  
  Proje ile oluşturulan ekran görüntüsü `screen.png` dosyasında yer almaktadır.

## Gereksinimler

- Python 3.9 veya üstü (zoneinfo modülü için)
- [Pillow](https://pillow.readthedocs.io/)  
- [ics](https://pypi.org/project/ics/)  
- [requests](https://pypi.org/project/requests/)

Gerekli paketleri yüklemek için:

```bash
pip install Pillow ics requests
```

## Kurulum

1. Bu depoyu klonlayın:

   ```bash
   git clone https://github.com/metinciris/Dynamic-Wallpaper-with-Calendar-Events-Overlay
   cd dynamic-wallpaper-calendar
   ```

2. **iCal URL'nizi** `takvimwallpaper.py` dosyasında `ical_url` değişkenine ekleyin:

   ```python
   ical_url = "YOUR_PUBLIC_ICAL_URL"  # Takviminizin iCal URL'si
   ```

3. Masaüstü resminizi `C:\Users\User\Pictures\masaustu.jpg` yoluna yerleştirin ya da dosya yolunu güncelleyin.

## Kullanım

Script'i çalıştırdığınızda:
- iCal URL'sinden etkinlik verileri çekilir.
- Etkinlikler, Türkiye saatine göre biçimlendirilip sağ üst köşede gösterilir.
- Oluşturulan yeni resim masaüstü arka planı olarak ayarlanır.

Script'i çalıştırmak için:

```bash
python takvimwallpaper.py
```

## Ekran Görüntüsü

Aşağıda oluşturulan masaüstü arka planının örnek görüntüsü bulunmaktadır:

![Screen](screen.png)

## Zamanlayıcı ile Güncelleme

Script'i Windows Görev Zamanlayıcısı gibi araçlar kullanarak belirli aralıklarla otomatik olarak çalıştırabilir, masaüstü arka planınızın sürekli güncel kalmasını sağlayabilirsiniz.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. 
