"""
AI Prompt Şablonları
Her özellik için optimize edilmiş prompt'lar
"""

class AIPrompts:
    @staticmethod
    def ozet_prompt(konu: str) -> str:
        """Konu özetleme prompt'u"""
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
        """Soru üretme prompt'u"""
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
        """Çalışma planı oluşturma prompt'u"""
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
        """PDF/Metin açıklama prompt'u"""
        return f"""Sen karmaşık akademik metinleri basitleştiren bir öğretmensin.

Aşağıdaki metni:
- Günlük dile çevir
- Örneklerle açıkla
- Kısa bir özet ile bitir

Metin:
{metin}"""

    @staticmethod
    def anlamadim_prompt(konu: str) -> str:
        """'Anlamadım' butonu için prompt"""
        return f"""Öğrenci bu konuyu anlamadığını söylüyor.

Konuyu:
- Daha basit
- Günlük hayattan örneklerle
- Kısa ve net

şekilde tekrar anlat.

Konu:
{konu}"""
