"""
PDF okuma ve işleme modülü
"""
from pypdf import PdfReader
from typing import Optional

class PDFReader:
    @staticmethod
    def extract_text(file_path: str) -> Optional[str]:
        """PDF dosyasından metin çıkarır"""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                text = ""
                
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                
                return text.strip()
        except Exception as e:
            print(f"PDF okuma hatası: {e}")
            return None
    
    @staticmethod
    def extract_text_from_bytes(file_bytes: bytes) -> Optional[str]:
        """Byte array'den metin çıkarır (upload için)"""
        try:
            from io import BytesIO
            pdf_file = BytesIO(file_bytes)
            pdf_reader = PdfReader(pdf_file)
            text = ""
            
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            return text.strip()
        except Exception as e:
            print(f"PDF okuma hatası: {e}")
            return None
