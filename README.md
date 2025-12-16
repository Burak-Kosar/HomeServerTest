# 🚀 End-to-End DevOps CI/CD Pipeline (Self-Hosted)

Bu proje, yerel bir Linux sunucusu üzerinde çalışan, **GitHub Actions Self-Hosted Runner** kullanılarak otomatize edilmiş uçtan uca (End-to-End) bir CI/CD boru hattı simülasyonudur.

Basit bir Python (Flask) web uygulaması, GitHub'a yapılan her "push" işleminden sonra otomatik olarak derlenmekte, test edilmekte ve yerel sunucuda Docker konteyneri olarak yayına alınmaktadır.

## 🏗️ Mimari ve Akış

Sistem şu adımları otomatik olarak gerçekleştirir:
1.  **Code:** Geliştirici kodu `main` dalına gönderir (Push).
2.  **Trigger:** GitHub Actions tetiklenir ve yerel ağdaki (Home Lab) sunucuya sinyal gönderir.
3.  **Build:** Self-Hosted Runner, Docker imajını inşa eder.
4.  **Deploy:** Eski konteyner durdurulur/silinir ve yeni sürüm ayağa kaldırılır.
5.  **Proxy:** Nginx Proxy Manager, trafiği karşılar ve `app.local` adresi üzerinden sunar.

## 🛠️ Kullanılan Teknolojiler

* **Dil & Framework:** Python, Flask
* **Containerization:** Docker, Docker Compose
* **CI/CD:** GitHub Actions (Self-Hosted Runner)
* **Reverse Proxy:** Nginx Proxy Manager
* **OS:** Linux (Debian/Ubuntu)
* **Monitoring:** (Opsiyonel) Grafana & Prometheus

## 📂 Proje Yapısı

```bash
.
├── .github/workflows/deploy.yml  # CI/CD Konfigürasyonu
├── app.py                        # Flask Uygulaması
├── Dockerfile                    # Docker İmaj Tanımı
├── requirements.txt              # Python Bağımlılıkları
└── README.md                     # Dokümantasyon
