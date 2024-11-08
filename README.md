# Ticket Hint

Ticket Hint adalah Mini AI Project menggunakan Flask yang menerima input pertanyaan dan memberikan respons yang sudah diproses supaya memberikan output yang diharapkan.

## 📋 Fitur
- Menerima input pertanyaan (ticket) melalui endpoint API.
- Mengembalikan saran dari ticket yang diinputkan dengan respons JSON.

## 🛠️ Teknologi yang Digunakan
- Python 3.10
- Flask (Framework web Python)

## 📦 Instalasi

### 1. Clone Repository
Clone repository ini ke komputer Anda:
```
git clone https://github.com/rizkymileapp/testing-ticket.git
cd testing-ticket
```

### 2. Buat dan Aktifkan Virtual Environment
Buat virtual environment untuk mengisolasi proyek:
```
python -m venv venv
venv\Scripts\activate
```

### 3. Instal Dependencies
Instal Flask dan dependencies lainnya:
```
pip install -r requirements.txt
```

### 4. Menjalankan Aplikasi
Jalankan aplikasi Flask dengan perintah berikut:
```
python app.py
```
Aplikasi akan berjalan di http://127.0.0.1:5000/.

### 5. Menggunakan cURL
Anda dapat menguji API menggunakan cURL atau Postman.
```
curl -X POST http://127.0.0.1:5000/ticket-response \
-H "Content-Type: application/json" \
-d "{\"question\": \"Saya tidak bisa login ke akun saya\"}"
```



