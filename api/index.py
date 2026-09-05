"""
FastAPI Backend - AI Study Assistant (Vercel Serverless)
Yapay Zeka Destekli Ders Çalışma Asistanı
"""
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
from io import BytesIO
from mangum import Mangum

# .env dosyasını yükle (local geliştirme için)
load_dotenv()

# Gemini API yapılandırması
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set!")
client = genai.Client(api_key=api_key)

app = FastAPI(title="AI Study Assistant API")

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request modelleri
class KonuRequest(BaseModel):
    konu: str

class SoruRequest(BaseModel):
    konu: str

class CalismaPlaniRequest(BaseModel):
    konu: str
    seviye: str
    sure: str
    gun: str

class MetinRequest(BaseModel):
    metin: str

class AnlamadimRequest(BaseModel):
    konu: str

# AI Prompts
class AIPrompts:
    @staticmethod
    def ozet_prompt(konu: str) -> str:
        return f"""Sen bir üniversite düzeyinde ders anlatan deneyimli bir eğitmendsin.
Aşağıda verilen konuyu:

- Basit ve anlaşılır
- Madde madde
- Öğrencinin sınavda çıkabilecek yerleri anlayacağı şekilde
- Gereksiz detaylara girmeden

özetle.

Konu:
{konu}"""

    @staticmethod
    def soru_uret_prompt(konu: str) -> str:
        return f"""Sen bir üniversite hocasısın.

Aşağıdaki konudan:
- 5 adet çoktan seçmeli
- 3 adet klasik
- 2 adet zorlayıcı yorum sorusu

oluştur.

Soruların altına **cevap anahtarını** da ekle.

Konu:
{konu}"""

    @staticmethod
    def calisma_plani_prompt(konu: str, seviye: str, sure: str, gun: str) -> str:
        return f"""Sen bir akademik danışmansın.

Öğrencinin:
- Seviyesi: {seviye}
- Günlük ayırabileceği süre: {sure}
- Sınava kalan gün: {gun}

bilgilerine göre,
aşağıdaki konu için günlük çalışma planı hazırla.

Plan:
- Gün gün
- Net süreler
- Tekrar ve soru çözümü içerecek şekilde olsun.

Konu:
{konu}"""

    @staticmethod
    def metin_aciklama_prompt(metin: str) -> str:
        return f"""Sen karmaşık akademik metinleri basitleştiren bir öğretmensin.

Aşağıdaki metni:
- Günlük dile çevir
- Örneklerle açıkla
- Kısa bir özet ile bitir

Metin:
{metin}"""

    @staticmethod
    def anlamadim_prompt(konu: str) -> str:
        return f"""Öğrenci bu konuyu anlamadığını söylüyor.

Konuyu:
- Daha basit
- Günlük hayattan örneklerle
- Kısa ve net

şekilde tekrar anlat.

Konu:
{konu}"""

# PDF Reader
class PDFReader:
    @staticmethod
    def extract_text_from_bytes(file_bytes: bytes) -> Optional[str]:
        try:
            pdf_file = BytesIO(file_bytes)
            pdf_reader = PdfReader(pdf_file)
            text = ""
            
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            return text.strip()
        except Exception as e:
            print(f"PDF okuma hatası: {e}")
            return None

# Gemini API çağrısı
def get_ai_response(prompt: str) -> str:
    """Gemini API'den yanıt al"""
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=prompt
        )
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI hatası: {str(e)}")

# Endpoints
@app.get("/")
async def root():
    return {
        "message": "AI Study Assistant API",
        "version": "1.0.0",
        "endpoints": [
            "/ozet - Konu özetleme",
            "/soru-uret - Soru üretme",
            "/calisma-plani - Çalışma planı",
            "/metin-acikla - Metin açıklama",
            "/anlamadim - Basitleştirilmiş açıklama"
        ]
    }

@app.post("/ozet")
async def konu_ozet(request: KonuRequest):
    """Konu özetleme"""
    prompt = AIPrompts.ozet_prompt(request.konu)
    response = get_ai_response(prompt)
    return {
        "success": True,
        "konu": request.konu,
        "ozet": response
    }

@app.post("/soru-uret")
async def soru_uret(request: SoruRequest):
    """Soru üretme"""
    prompt = AIPrompts.soru_uret_prompt(request.konu)
    response = get_ai_response(prompt)
    return {
        "success": True,
        "konu": request.konu,
        "sorular": response
    }

@app.post("/calisma-plani")
async def calisma_plani(request: CalismaPlaniRequest):
    """Çalışma planı oluşturma"""
    prompt = AIPrompts.calisma_plani_prompt(
        request.konu,
        request.seviye,
        request.sure,
        request.gun
    )
    response = get_ai_response(prompt)
    return {
        "success": True,
        "plan": response
    }

@app.post("/metin-acikla")
async def metin_acikla(request: MetinRequest):
    """Metin açıklama"""
    prompt = AIPrompts.metin_aciklama_prompt(request.metin)
    response = get_ai_response(prompt)
    return {
        "success": True,
        "aciklama": response
    }

@app.post("/anlamadim")
async def anlamadim(request: AnlamadimRequest):
    """Basitleştirilmiş açıklama"""
    prompt = AIPrompts.anlamadim_prompt(request.konu)
    response = get_ai_response(prompt)
    return {
        "success": True,
        "basit_aciklama": response
    }

@app.post("/pdf-yukle")
async def pdf_yukle(file: UploadFile = File(...)):
    """PDF yükle ve metne çevir"""
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Sadece PDF dosyaları kabul edilir")
    
    try:
        contents = await file.read()
        text = PDFReader.extract_text_from_bytes(contents)
        
        if not text:
            raise HTTPException(status_code=400, detail="PDF'den metin çıkarılamadı")
        
        # Metni açıkla
        prompt = AIPrompts.metin_aciklama_prompt(text[:3000])  # İlk 3000 karakter
        response = get_ai_response(prompt)
        
        return {
            "success": True,
            "dosya_adi": file.filename,
            "metin_uzunlugu": len(text),
            "aciklama": response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF işleme hatası: {str(e)}")

# Vercel Serverless Handler
handler = Mangum(app)
