# Tutorial Konfigurasi Proxy - Burp Suite

## Daftar Isi

1. [Apa itu Burp Proxy?](#apa-itu-burp-proxy)
2. [Menjalankan Burp Proxy](#menjalankan-burp-proxy)
3. [Konfigurasi Browser](#konfigurasi-browser)
4. [Install CA Certificate](#install-ca-certificate)
5. [Intercept Mode](#intercept-mode)
6. [HTTP History](#http-history)
7. [Filter dan Options](#filter-dan-options)
8. [Tips Lanjutan](#tips-lanjutan)

---

## Apa itu Burp Proxy?

Burp Proxy adalah fitur utama Burp Suite yang memungkinkan Anda untuk:
- **Mengintercept** semua HTTP/HTTPS traffic antara browser dan server
- **Memodifikasi** request dan response secara real-time
- **Menganalisa** pola komunikasi aplikasi web
- **Mengidentifikasi** vulnerability seperti SQL Injection, XSS, dan lainnya

---

## Menjalankan Burp Proxy

### Step 1: Aktifkan Proxy Listener
1. Buka Burp Suite
2. Pergi ke tab **Proxy** > **Options**
3. Pada **Proxy Listeners**, pastikan ada listener yang aktif
4. Default: `127.0.0.1:8080`

### Step 2: Konfigurasi Listener Baru
```
Proxy > Options > Proxy Listeners > Add
- Bind to port: 8080
- Bind to address: All interfaces
- Support invisible proxy: ✓ (jika diperlukan)
```

---

## Konfigurasi Browser

### Chrome/Chromium
```bash
# Buka Settings > Advanced > System > Open proxy settings
# Atau akses: chrome://settings/system

# Set:
HTTP Proxy: 127.0.0.1
Port: 8080
```

### Firefox
```
Settings > Network Settings > Settings
- Select: Manual proxy configuration
- HTTP Proxy: 127.0.0.1
- Port: 8080
- ✓ Use this proxy for all protocols
```

### Edge
```
Settings > System > Open your computer's proxy settings
# Sama seperti Chrome
```

---

## Install CA Certificate

### Mengapa Perlu?

Tanpa CA certificate, Burp tidak bisa mengintercept traffic HTTPS karena browser akan menolak sertifikat yang tidak dipercaya.

### Step 1: Export Certificate
1. Proxy > Options > Import/Export CA certificate
2. Pilih **Export** > **Certificate in DER format**
3. Simpan sebagai `burp_suite_ca.cer`

### Step 2: Install di Browser

**Firefox:**
```
Options > Privacy & Security > Certificates
- View Certificates > Import
- Pilih file .cer
- ✓ Trust this CA to identify websites
```

**Chrome/Edge:**
```
Settings > Security > Manage certificates
- Import > Next
- Browse file .cer
- ✓ Place all certificates in the following store: Trusted Root Certification Authorities
```

---

## Intercept Mode

### Mengaktifkan Intercept
```
Proxy > Intercept > Intercept is on/off
```

### Tombol Control
| Tombol | Fungsi |
|--------|--------|
| **Forward** | Kirim request/response ke server |
| **Drop** | Buang request |
| **Intercept on/off** | Toggle intercept |
| **Action** | Menu konteks untuk request |

### Contoh Penggunaan

#### Test SQL Injection
1. Intercept request login
2. Ubah parameter username: `admin'--`
3. Forward request
4. Lihat response

#### Test XSS
1. Intercept request dengan parameter search
2. Masukkan payload: `<script>alert(1)</script>`
3. Forward dan lihat apakah ter-reflect

---

## HTTP History

### Menggunakan HTTP History
```
Proxy > HTTP History
```

### Kolom Penting
| Kolom | Deskripsi |
|-------|-----------|
| # | Urutan request |
| Host | Domain target |
| Method | GET, POST, PUT, dll |
| URL | Path yang diakses |
| Status | Response code |
| Length | Ukuran response |
| MIME | Tipe konten |
| Time | Durasi request |
| Comment | Catatan user |

### Filter Options
```
Filter bar: Show only... 
- Request types
- Response codes
- MIME types
- Search patterns
```

---

## Filter dan Options

### Request Filtering
```regex
# Contoh regex filter
^https?://(www\.)?target\.com/.*
```

### Response Filtering
- Show only: 2xx, 3xx, 4xx, 5xx
- MIME type: HTML, JSON, XML, dll

### Proxy Options Penting
```
✓ Support invisible proxy (untuk non-proxy aware clients)
✓ Use HTTP/1.0 / HTTP/2
✓ Use keep-alive
✓ Strip Secure flag (jika perlu testing)
```

---

## Tips Lanjutan

### 1. Scope Management
```
Target > Scope > Add to scope
# Hanya tampilkan request yang sesuai scope
```

### 2. SSL Pass Through
```
Proxy > Options > SSL Pass Through
# Untuk domain yang tidak bisa diintercept
```

### 3. Match and Replace
```
Proxy > Options > Match and Replace
# Otomatis ubah header/value tertentu
```

### 4. Save Work
```
# Rutin simpan project
File > Save Project As
```

---

## Troubleshooting

### Masalah: Port 8080 Used
**Solusi:**
```bash
# Linux/Mac
lsof -i :8080
#atau
netstat -tulpn | grep 8080

# Windows
netstat -ano | findstr :8080
```

### Masalah: HTTPS Not Working
- Pastikan CA certificate sudah diinstall
- Restart browser setelah install certificate

### Masalah: Burp Tidak Merespons
- Coba restart Burp Suite
- Periksa Java heap memory

---

## Next Steps

Lanjutkan ke:
- [Scanner Usage](scanner-usage.md) - Automated vulnerability scanning
- [Quick Start Guide](../getting-started/quick-start.md) - Kembali ke basics

---

**Version**: 1.0.1-20260301-Minggu-0954-WIB  
**Last Updated**: 2026-03-01 - Minggu - 09:54 GMT+7 (WIB)  
**Author**: waktuberhenti
