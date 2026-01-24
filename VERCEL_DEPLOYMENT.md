# 🚀 Vercel'de Deployment Talimatları

## Adım 1: Vercel Hesabı Oluşturma

1. [vercel.com](https://vercel.com) adresine gidin
2. "Sign Up" butonuna tıklayın
3. GitHub hesabınızla giriş yapın (önerilir)

## Adım 2: GitHub'a Projeyi Pushlama

```bash
# Git kullanıcı bilgilerini ayarlayın (sadece ilk kez)
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"

# Dosyaları ekleyin
git add .

# Commit yapın
git commit -m "Initial commit: AI Study Assistant"

# GitHub remote ekleyin
git remote add origin https://github.com/DevilsDen1/Ai-study-asistan.git

# Push yapın
git branch -M main
git push -u origin main
```

## Adım 3: Vercel'de Proje Oluşturma

1. Vercel dashboard'a gidin
2. "Add New..." > "Project" seçin
3. GitHub repository'nizi seçin: `Ai-study-asistan`
4. "Import" butonuna tıklayın

## Adım 4: Environment Variables Ekleme

Deploy etmeden önce:

1. "Environment Variables" bölümüne gidin
2. Şu değişkeni ekleyin:
   - **Name**: `GEMINI_API_KEY`
   - **Value**: (Gemini API anahtarınız)
   - **Environment**: Production, Preview, Development (hepsini seçin)

## Adım 5: Deploy Ayarları

Vercel otomatik olarak `vercel.json` dosyasını algılayacak. Sadece:

1. "Deploy" butonuna tıklayın
2. Deployment tamamlanana kadar bekleyin (2-3 dakika)

## Adım 6: Siteyi Test Etme

Deployment tamamlandığında:

1. Vercel size otomatik bir URL verecek: `https://ai-study-asistan.vercel.app` (veya benzeri)
2. Bu URL'yi tarayıcınızda açın
3. Tüm özellikleri test edin

## 🎯 Önemli Notlar

- **Ücretsiz Plan**: Vercel'in ücretsiz planı çoğu kullanım için yeterlidir
- **Otomatik Deploy**: GitHub'a her push yaptığınızda otomatik deploy olur
- **Custom Domain**: İsterseniz kendi domain'inizi bağlayabilirsiniz
- **SSL**: Otomatik HTTPS sertifikası gelir

## 🔧 Sorun Giderme

### API Çalışmıyorsa:
1. Vercel dashboard > Settings > Environment Variables
2. `GEMINI_API_KEY` değişkeninin doğru eklendiğinden emin olun
3. "Redeploy" yapın

### Build Hatası Alırsanız:
1. `requirements.txt` dosyasının doğru olduğundan emin olun
2. Vercel logs'ları kontrol edin
3. Python versiyonunu kontrol edin (Vercel Python 3.9 kullanır)

## 📞 Destek

Sorun yaşarsanız:
- Vercel documentation: https://vercel.com/docs
- GitHub Issues: Projenizde issue açın
