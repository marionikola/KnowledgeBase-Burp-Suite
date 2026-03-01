# Quick Start Guide - Burp Suite

## Daftar Isi

1. [Mengapa Burp Suite?](#mengapa-burp-suite)
2. [Konsep Dasar](#konsep-dasar)
3. [Setup Pertama Kali](#setup-pertama-kali)
4. [Proxy Configuration](#proxy-configuration)
5. [Menavigasi Interface](#menavigasi-interface)
6. [First Test - Intercept Request](#first-test---intercept-request)
7. [Common Use Cases](#common-use-cases)
8. [Tips untuk Pemula](#tips-untuk-pemula)

---

## Mengapa Burp Suite?

Burp Suite adalah tools keamanan aplikasi web yang paling populer dan powerful untuk:

- **Penetration Testing**: Menguji keamanan aplikasi web
- **Security Auditing**: Melakukan audit keamanan
- **Bug Bounty**: Menemukan vulnerability untuk program bug bounty
- **Development Testing**: Menguji keamanan selama development

---

## Konsep Dasar

### Apa itu Burp Proxy?
Burp Proxy memungkinkan Anda untuk:
- Melihat semua HTTP/HTTPS traffic antara browser dan server
- Memodifikasi request sebelum dikirim ke server
- Melihat response dari server
- Mengintercept dan manipulasi data

### Alur Kerja Dasar
```
Browser -> Burp Proxy -> Server Target
                |
                v
          Analysis & Testing
```

### Tools Utama dalam Burp Suite
| Tool | Fungsi |
|------|--------|
| Proxy | Intercept HTTP/HTTPS traffic |
| Spider | Crawl website untuk menemukan pages |
| Scanner | Automated vulnerability scanning |
| Repeater | Manual request manipulation |
| Intruder | Automated payload testing |
| Sequencer | Analyze token randomness |
| Decoder | Encode/Decode data |
| Comparer | Compare two responses |

---

## Setup Pertama Kali

### Step 1: Jalankan Burp Suite
```bash
# Dari terminal
java -jar burpsuite_community.jar

# Atau klik icon jika sudah di-install
```

### Step 2: Buat Project Baru
1. Klik "Next" pada wizard
2. Pilih "Create new project"
3. Klik "Next"
4. Pilih lokasi penyimpanan (opsional)
5. Klik "Start Burp"

### Step 3: Konfigurasi Proxy
1. Pergi ke tab **Proxy** > **Options**
2. Pastikan "Proxy Listeners" aktif
3. Default: `127.0.0.1:8080`
4. Jika port berbeda, catat untuk下一步

---

## Proxy Configuration

### Konfigurasi Browser

#### Chrome/Edge
1. Settings > Network and Internet > Proxy
2. Manual proxy setup
3. Address: `127.0.0.1`
4. Port: `8080`

#### Firefox
1. Settings > Network Settings
2. Manual proxy configuration
3. HTTP Proxy: `127.0.0.1`
4. Port: `8080`
5. Check "Use this proxy for all protocols"

### Install CA Certificate (untuk HTTPS)

#### Step 1: Export Certificate
1. Proxy > Options > Import/Export CA certificate
2. Click "Export" > "Certificate in DER format"
3. Simpan sebagai `burp.cer`

#### Step 2: Install ke Browser
**Chrome/Edge:**
1. Settings > Security > Manage certificates
2. Import > Select certificate
3. Trust SSL certificates

**Firefox:**
1. Settings > Privacy & Security > Certificates
2. View Certificates > Import
3. Select certificate > Trust SSL certificates

---

## Menavigasi Interface

### Main Tabs
```
┌─────────────────────────────────────────────────┐
│ Dashboard │ Target │ Proxy │ Intruder │ Repeater│
│           │ Spider │ Scanner │ Sequencer │      │
├─────────────────────────────────────────────────┤
│                                                 │
│              Content Area                       │
│                                                 │
├─────────────────────────────────────────────────┤
│ Proxy history │ HTTP history │ WebSockets      │
└─────────────────────────────────────────────────┘
```

### Dashboard Tab
- Overview of scanning activities
- Task management
- Event log

### Target Tab
- Scope management
- Site map
- Issue definitions

### Proxy Tab
- Intercept
- HTTP history
- WebSocket history
- Options

### Tools Shortcuts
| Shortcut | Action |
|----------|--------|
| Ctrl+Tab | Next tab |
| Ctrl+Shift+Tab | Previous tab |
| Ctrl+L | Go to URL |
| Ctrl+U | URL encode |
| Ctrl+Shift+U | URL decode |

---

## First Test - Intercept Request

### Step 1: Enable Intercept
1. Pergi ke **Proxy > Intercept**
2. Klik **"Intercept is off"** untuk mengaktifkan
3. Status akan berubah menjadi **"Intercept is on"**

### Step 2: Browse ke Website
1. Buka browser yang sudah dikonfigurasi
2. Kunjungi website target (misal: http://example.com)
3. Request akan muncul di Proxy Intercept

### Step 3: Analyze Request
Perhatikan bagian:
- **Request Line**: Method, Path, Protocol
- **Headers**: Host, User-Agent, Cookie
- **Body**: POST data, JSON, dll

### Step 4: Modify Request
1. Ubah parameter di body
2. Klik **"Forward"** untuk kirim ke server
3. Lihat response di Response area

### Step 5: View History
1. Pergi ke **Proxy > HTTP history**
2. Lihat semua request yang sudah ditangkap
3. Filter berdasarkan method, status, dll

---

## Common Use Cases

### 1. Testing SQL Injection
1. Intercept request dengan parameter
2. Ubah nilai parameter menjadi `' OR '1'='1`
3. Forward request
4. Lihat response untuk tanda error

### 2. Testing XSS
1. Intercept request
2. Masukkan payload XSS di parameter
3. Forward dan lihat response
4. Check apakah script di-render

### 3. Session Testing
1. Capture login request
2. Lihat cookie yang di-set
3. Replay dengan cookie berbeda
4. Test untuk session fixation

### 4. API Testing
1. Intercept API calls
2. Modify JSON/XML payload
3. Test untuk IDOR, injection, dll

---

## Tips untuk Pemula

### Productivity Tips
1. **Use Keyboard Shortcuts**: Lebih cepat dari mouse
2. **Set Scope Awal**: Jangan scan semua, tentukan target
3. **Use Filters**: Saring noise di HTTP history
4. **Save Work**: Rutin simpan project state

### Best Practices
1. **Always Get Permission**: Hanya test sistem yang diizinkan
2. **Document Findings**: Catat semua vulnerability
3. **Use Professional Version**: Untuk fitur lebih lengkap
4. **Learn Each Tool**: Pahami semua tools secara mendalam

### Common Mistakes to Avoid
1. ❌ Tidak menginstall CA certificate
2. ❌ Testing tanpa menentukan scope
3. ❌ Mengabaikan SSL/TLS errors
4. ❌ Tidak backup project state

---

## Next Steps

Sekarang Anda sudah siap untuk:
- [ ] [Installation Guide](installation.md) - Detail instalasi
- [ ] Proxy Configuration Tutorial - Detail Proxy
- [ ] Scanner Usage - Vulnerability scanning

---

## Referensi Tambahan

- [Official Burp Suite Docs](https://portswigger.net/burp/documentation)
- [Web Security Academy](https://portswigger.net/web-security)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

---

**Version**: 1.0.0-20260301-Minggu-0939-WIB  
**Last Updated**: 2026-03-01 - Minggu - 09:39 GMT+7 (WIB)  
**Author**: waktuberhenti
