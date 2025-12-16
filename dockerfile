# 1. Zemin: Python yüklü hafif bir Linux sürümü kullan
FROM python:3.9-slim

# 2. Çalışma klasörünü ayarla
WORKDIR /app

# 3. Önce gereksinimleri kopyala ve kur (Cache performansı için)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Kalan uygulama dosyalarını kopyala
COPY . .

# 5. Uygulama 5000 portundan yayın yapacak
EXPOSE 5000

# 6. Başlatma komutu
CMD ["python", "app.py"]