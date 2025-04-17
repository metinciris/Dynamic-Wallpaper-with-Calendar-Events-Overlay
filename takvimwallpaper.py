import ctypes
import datetime
import requests
from ics import Calendar
from PIL import Image, ImageDraw, ImageFont
from zoneinfo import ZoneInfo

# Herkese açık takviminizin iCal URL'sini buraya ekleyin.
ical_url = "https://calendar.google.com/calendar/ical/metin%40metinciris.com.tr/private-dbd80c7721cac91a1fc89cf278b8355b/basic.ics"

def fetch_events(ical_url):
    """
    iCal URL'sinden takvim verisini çekerek, şu andan sonraki etkinlikleri
    artan sırayla döndürür. Zamanlar UTC olarak gelir, dönüşüm sonrasında
    Türkiye saatine çevirilecektir.
    """
    response = requests.get(ical_url)
    response.raise_for_status()
    calendar = Calendar(response.text)
    
    now = datetime.datetime.now(datetime.timezone.utc)
    upcoming_events = [
        event for event in calendar.events
        if event.begin.datetime >= now
    ]
    upcoming_events.sort(key=lambda event: event.begin.datetime)
    return upcoming_events

def set_wallpaper(path):
    """
    Belirtilen dosya yolunu Windows masaüstü arka planı olarak ayarlar.
    """
    SPI_SETDESKWALLPAPER    = 20
    SPIF_UPDATEINIFILE      = 0x01
    SPIF_SENDWININICHANGE   = 0x02
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, path,
        SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )

def update_image_with_events(input_path, output_path, events):
    """
    Resmi açar, sağ üst köşeye Türkiye saatiyle biçimlendirilmiş
    etkinlik listesini ekler ve güncellenmiş resmi kaydeder.
    """
    img = Image.open(input_path)
    draw = ImageDraw.Draw(img)
    
    # Font ayarı: Arial kullanılmaya çalışılır, bulunamazsa varsayılan font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    
    # Türkiye saat dilimi
    tr_zone = ZoneInfo("Europe/Istanbul")
    
    # Etkinlik bilgilerini istenen formatta oluşturuyoruz.
    # Her satır: "dd.mm.yyyy HH:MM - Etkinlik Adı"
    event_lines = []
    for event in events:
        # Eğer event bir string ise (örn. "Yaklaşan etkinlik yok."), direkt ekle
        if isinstance(event, str):
            event_lines.append(event)
            continue
        # Aksi hâlde ICS Event objesi: zamanı dönüştür ve ekle
        event_time = event.begin.datetime.astimezone(tr_zone)
        formatted_time = event_time.strftime("%d.%m.%Y %H:%M")
        summary = event.name or "Etkinlik"
        event_lines.append(f"{formatted_time} - {summary}")
    
    event_text = "\n".join(event_lines)
    
    # Metnin boyutunu hesaplamak için textbbox kullanıyoruz
    bbox = draw.textbbox((0, 0), event_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Sağ üst köşeye yerleştirmek için
    margin = 20
    x = img.width - text_width - margin
    y = margin

    # Arka plan kutusu: biraz padding ile
    padding = 10
    rectangle_coords = [
        x - padding, y - padding,
        x + text_width + padding, y + text_height + padding
    ]
    draw.rectangle(rectangle_coords, fill="lightblue")
    
    # Metni ekleyelim (siyah renk)
    draw.text((x, y), event_text, fill="black", font=font)
    
    # Güncellenmiş resmi kaydet
    img.save(output_path)

if __name__ == "__main__":
    # Resim dosyası yolları:
    input_image_path  = r"C:\Users\User\Pictures\masaustu.jpg"
    output_image_path = r"C:\Users\User\Pictures\masaustu_modified.jpg"
    
    # Takvimden etkinlikleri çek
    events = fetch_events(ical_url)
    
    # Eğer etkinlik yoksa, uygun mesaj ekleyelim.
    if not events:
        events = ["Yaklaşan etkinlik yok."]
    
    # Etkinlik listesini resme ekleyip güncelle
    update_image_with_events(input_image_path, output_image_path, events)
    
    # Güncellenmiş resmi masaüstü arka planı olarak ayarla
    set_wallpaper(output_image_path)
