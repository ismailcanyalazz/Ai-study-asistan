# 🧠 AI Study Assistant - Yapay Zeka Destekli Ders Çalışma Asistanı

Modern ve kullanıcı dostu bir yapay zeka destekli ders çalışma asistanı. Öğrencilerin daha verimli çalışmasına yardımcı olur.

## ✨ Özellikler

### MVP (İlk Versiyon)
- ✅ **Konu Özetleme**: Herhangi bir konuyu basit ve anlaşılır şekilde özetler
- ✅ **Soru Üretme**: Konudan çoktan seçmeli, klasik ve zorlayıcı sorular üretir
- ✅ **Çalışma Planı**: Kişiselleştirilmiş günlük çalışma planı oluşturur
- ✅ **Metin Açıklama**: Karmaşık akademik metinleri basitleştirir
- ✅ **PDF İşleme**: PDF dosyalarını yükleyip içeriğini açıklar

### Gelecek Versiyonlar
- 🔜 Kullanıcı hesabı ve giriş sistemi
- 🔜 Konu geçmişi ve favoriler
- 🔜 "Bugün ne çalışmalıyım?" önerisi
- 🔜 Not alma alanı
- 🔜 Mobil uygulama

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- OpenAI API Key
- Modern web tarayıcı

### 1. Bağımlılıkları Yükleyin

```bash
cd backend
pip install -r requirements.txt
```

### 2. API Key Ayarlayın

`backend/.env` dosyası oluşturun:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**OpenAI API Key almak için:**
1. https://platform.openai.com/ adresine gidin
2. Hesap oluşturun veya giriş yapın
3. API Keys bölümünden yeni bir key oluşturun
4. Key'i `.env` dosyasına yapıştırın

### 3. Backend'i Başlatın

```bash
cd backend
python main.py
```

Backend `http://localhost:8000` adresinde çalışacak.

### 4. Frontend'i Açın

`frontend/index.html` dosyasını tarayıcınızda açın veya bir local server kullanın:

```bash
# Python ile basit server
cd frontend
python -m http.server 3000
```

Tarayıcıda `http://localhost:3000` adresine gidin.

## 📂 Proje Yapısı

```
ai-study-assistant/
│
├── backend/
│   ├── main.py              # FastAPI ana dosyası
│   ├── ai_prompts.py        # AI prompt şablonları
│   ├── pdf_reader.py        # PDF işleme modülü
│   ├── requirements.txt     # Python bağımlılıkları
│   └── .env                 # API anahtarları (oluşturulacak)
│
├── frontend/
│   ├── index.html           # Ana sayfa
│   ├── style.css            # Modern tasarım
│   └── script.js            # Frontend mantığı
│
└── README.md
```

## 🎨 Tasarım Özellikleri

- 🌙 **Modern Dark Theme**: Göz yormayan karanlık tema
- ✨ **Glassmorphism**: Cam efektli modern kartlar
- 🎭 **Animasyonlar**: Yumuşak geçişler ve hover efektleri
- 📱 **Responsive**: Mobil ve masaüstü uyumlu
- 🎨 **Gradient Buttons**: Renkli gradient butonlar
- 💫 **Animated Background**: Hareketli arka plan efektleri

## 🔧 API Endpoints

### `POST /ozet`
Konu özetleme
```json
{
  "konu": "Osmanlı İmparatorluğu"
}
```

### `POST /soru-uret`
Soru üretme
```json
{
  "konu": "Fotosentez"
}
```

### `POST /calisma-plani`
Çalışma planı oluşturma
```json
{
  "konu": "Matematik - İntegral",
  "seviye": "Üniversite",
  "sure": "2 saat",
  "gun": "15 gün"
}
```

### `POST /metin-acikla`
Metin açıklama
```json
{
  "metin": "Karmaşık akademik metin..."
}
```

### `POST /pdf-yukle`
PDF yükleme (multipart/form-data)

## 💡 Kullanım İpuçları

1. **Detaylı Konu Girin**: Daha spesifik konular daha iyi sonuçlar verir
2. **Gerçekçi Planlar**: Çalışma planı için gerçekçi süreler belirleyin
3. **Soru Çeşitliliği**: Üretilen sorular farklı zorluk seviyelerinde olur
4. **PDF Boyutu**: Büyük PDF'lerin ilk 3000 karakteri işlenir
5. **API Limitleri**: OpenAI API limitlerini göz önünde bulundurun

## 🛠️ Teknoloji Stack

### Backend
- **FastAPI**: Modern, hızlı web framework
- **OpenAI API**: GPT-3.5 Turbo
- **PyPDF2**: PDF işleme
- **Uvicorn**: ASGI server

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling, animations
- **Vanilla JavaScript**: API entegrasyonu
- **Google Fonts**: Inter font family

## 📊 Performans

- ⚡ Hızlı yanıt süreleri (2-5 saniye)
- 🔄 Asenkron işlemler
- 💾 Hafif ve optimize kod
- 🎯 Minimal bağımlılıklar

## 🔒 Güvenlik

- API anahtarları `.env` dosyasında saklanır
- CORS koruması aktif
- Input validasyonu
- Error handling

## 🐛 Sorun Giderme

### Backend başlamıyor
- Python versiyonunu kontrol edin (3.8+)
- Bağımlılıkları tekrar yükleyin: `pip install -r requirements.txt`
- `.env` dosyasının doğru konumda olduğundan emin olun

### API hatası alıyorum
- OpenAI API key'inizin geçerli olduğunu kontrol edin
- API limitlerini kontrol edin
- İnternet bağlantınızı kontrol edin

### Frontend backend'e bağlanamıyor
- Backend'in çalıştığından emin olun (`http://localhost:8000`)
- CORS hatası varsa backend'i yeniden başlatın
- Tarayıcı konsolunu kontrol edin

## 📝 Lisans

Bu proje eğitim amaçlıdır ve özgürce kullanılabilir.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull request göndermekten çekinmeyin.

## 📧 İletişim

Sorularınız için issue açabilirsiniz.

---

**🧠 AI Study Assistant** - Yapay Zeka ile Daha Akıllı Çalış! ✨
