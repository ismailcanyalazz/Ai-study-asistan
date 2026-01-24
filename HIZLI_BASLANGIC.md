# 🚀 Hızlı Başlangıç Kılavuzu

## ⚡ 3 Adımda Başlayın!

### 1️⃣ Python Kurulumu (Eğer kurulu değilse)

**Windows için:**
1. https://www.python.org/downloads/ adresine gidin
2. "Download Python 3.x.x" butonuna tıklayın
3. İndirilen dosyayı çalıştırın
4. ⚠️ **ÖNEMLİ**: "Add Python to PATH" kutucuğunu işaretleyin!
5. "Install Now" butonuna tıklayın

**Kurulumu test edin:**
```bash
python --version
```

### 2️⃣ Backend Kurulumu

**Terminal/PowerShell'i açın ve şu komutları çalıştırın:**

```bash
# Backend klasörüne gidin
cd c:\Users\yalaz\Desktop\Asistan\backend

# Bağımlılıkları yükleyin
python -m pip install -r requirements.txt
```

### 3️⃣ OpenAI API Key Ayarlayın

**API Key almak için:**
1. https://platform.openai.com/ adresine gidin
2. Hesap oluşturun (ilk kullanıcılara $5 ücretsiz kredi!)
3. Sağ üstteki profil ikonuna tıklayın
4. "View API Keys" seçeneğine tıklayın
5. "Create new secret key" butonuna tıklayın
6. Key'i kopyalayın (bir daha gösterilmeyecek!)

**`.env` dosyası oluşturun:**

`backend` klasöründe `.env` adında yeni bir dosya oluşturun ve içine şunu yazın:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

(sk-xxx... yerine kendi API key'inizi yapıştırın)

## 🎯 Uygulamayı Çalıştırma

### Backend'i Başlatın

```bash
cd c:\Users\yalaz\Desktop\Asistan\backend
python main.py
```

✅ Şu mesajı görmelisiniz:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Frontend'i Açın

**Yöntem 1: Doğrudan Tarayıcıda**
- `c:\Users\yalaz\Desktop\Asistan\frontend\index.html` dosyasına çift tıklayın

**Yöntem 2: Local Server ile (Önerilen)**

Yeni bir terminal açın:
```bash
cd c:\Users\yalaz\Desktop\Asistan\frontend
python -m http.server 3000
```

Tarayıcıda açın: http://localhost:3000

## 🎨 İlk Kullanım

1. **Konu Özetleme** kartına bir konu yazın
   - Örnek: "Osmanlı İmparatorluğu'nun kuruluş dönemi"
2. "📝 Özet Oluştur" butonuna tıklayın
3. Birkaç saniye bekleyin
4. AI tarafından oluşturulan özeti görün! 🎉

## ❗ Sık Karşılaşılan Sorunlar

### "Python bulunamadı" hatası
➡️ Python'u PATH'e ekleyin veya yeniden kurun

### "pip bulunamadı" hatası
➡️ `python -m pip` kullanın

### "API hatası" alıyorum
➡️ `.env` dosyasındaki API key'i kontrol edin
➡️ OpenAI hesabınızda kredi olduğundan emin olun

### Backend'e bağlanamıyor
➡️ Backend'in çalıştığından emin olun (http://localhost:8000)
➡️ Tarayıcı konsolunu kontrol edin (F12)

### CORS hatası
➡️ Frontend'i `file://` yerine `http://localhost:3000` üzerinden açın

## 💰 Maliyet Bilgisi

- GPT-3.5 Turbo kullanıyor (en ucuz model)
- Ortalama maliyet: ~$0.002 per istek
- İlk kullanıcılara $5 ücretsiz kredi
- ~2500 istek yapabilirsiniz!

## 🎓 Kullanım Örnekleri

### Konu Özetleme
```
Konu: "Fotosentez ve bitkilerde enerji üretimi"
```

### Soru Üretme
```
Konu: "İkinci Dünya Savaşı'nın nedenleri"
```

### Çalışma Planı
```
Konu: "Matematik - İntegral"
Seviye: Üniversite
Günlük Süre: 2 saat
Sınava Kalan Gün: 15 gün
```

## 📞 Yardım

Sorun yaşıyorsanız:
1. README.md dosyasını okuyun
2. Terminal'deki hata mesajlarını kontrol edin
3. Backend loglarını kontrol edin
4. Tarayıcı konsolunu kontrol edin (F12)

---

**Başarılar! 🚀 İyi çalışmalar! 📚**
