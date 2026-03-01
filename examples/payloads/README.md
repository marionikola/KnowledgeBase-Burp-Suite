# Burp Suite Payload Collection

> Koleksi payload komprehensif untuk security testing menggunakan Burp Suite

## Overview

Direktori ini berisi kumpulan payload yang digunakan untuk menguji berbagai jenis kerentanan keamanan (vulnerability) pada aplikasi web. Payload dikelompokkan berdasarkan kategori untuk memudahkan penetration tester dalam melakukan security assessment.

## Struktur Folder

```
examples/payloads/
├── api/                    # API Testing Payloads
│   ├── graphql-*.txt      # GraphQL testing payloads
│   ├── jwt-*.txt          # JWT testing payloads
│   ├── oauth-*.txt        # OAuth testing payloads
│   └── rest-*.txt         # REST API testing payloads
├── authentication/         # Authentication Testing
│   ├── auth-*.txt         # General auth bypass
│   ├── jwt-*.txt          # JWT vulnerabilities
│   └── oauth-*.txt        # OAuth vulnerabilities
├── files/                  # File-Related Testing
│   └── lfi-*.txt          # Local File Inclusion
├── injection/              # Injection Payloads
│   ├── sqli-*.txt         # SQL Injection
│   ├── nosql-*.txt        # NoSQL Injection
│   ├── ldap-*.txt         # LDAP Injection
│   ├── xpath-*.txt        # XPath Injection
│   └── rfi-*.txt          # Remote File Inclusion
├── miscellaneous/           # Other Payloads
│   ├── csrf-*.txt         # CSRF testing
│   ├── deserialization-*.txt  # Deserialization
│   ├── ssti-*.txt         # Server Side Template Injection
│   └── race-condition-*.txt   # Race Condition
├── network/                 # Network-Based Testing
│   ├── ssrf-*.txt         # Server Side Request Forgery
│   └── http-*.txt         # HTTP smuggling/splitting
└── xss/                     # Cross-Site Scripting
    ├── xss-*.txt          # XSS payloads
    └── dom-*.txt          # DOM-based XSS
```

## Kategori Payload

### 1. Injection (`injection/`)

Berisi payload untuk berbagai jenis teknik injeksi:

| File | Deskripsi |
|------|-----------|
| `sqli-*.txt` | SQL Injection (Error-based, Blind, Union, Time-based) |
| `nosql-*.txt` | NoSQL Injection (MongoDB, dll) |
| `ldap-*.txt` | LDAP Injection |
| `xpath-*.txt` | XPath Injection |
| `xml-*.txt` | XML Injection/XXE |
| `rfi-*.txt` | Remote File Inclusion |

### 2. Cross-Site Scripting (`xss/`)

Payload XSS berbagai jenis:

| File | Deskripsi |
|------|-----------|
| `xss-basic.txt` | Basic XSS payloads |
| `xss-stored.txt` | Stored XSS |
| `xss-reflected.txt` | Reflected XSS |
| `xss-dom.txt` | DOM-based XSS |
| `xss-event.txt` | Event handler-based XSS |

### 3. Authentication (`authentication/`)

Pengujian autentikasi dan authorization:

| File | Deskripsi |
|------|-----------|
| `auth-bypass.txt` | Authentication bypass |
| `auth-sql.txt` | SQL-based auth bypass |
| `jwt-*.txt` | JWT vulnerabilities |
| `oauth-*.txt` | OAuth vulnerabilities |

### 4. File Inclusion (`files/`)

| File | Deskripsi |
|------|-----------|
| `lfi-basic.txt` | Basic LFI |
| `lfi-nullbyte.txt` | Null byte bypass |
| `lfi-wrapper.txt` | Protocol wrapper bypass |
| `lfi-*.txt` | Platform-specific LFI |

### 5. API Testing (`api/`)

| File | Deskripsi |
|------|-----------|
| `rest-*.txt` | REST API testing |
| `graphql-*.txt` | GraphQL testing |
| `jwt-*.txt` | JWT API testing |
| `oauth-*.txt` | OAuth/API security |

### 6. Network Attacks (`network/`)

| File | Deskripsi |
|------|-----------|
| `ssrf-*.txt` | Server-Side Request Forgery |
| `http-*.txt` | HTTP Request Smuggling |
| `websocket-*.txt` | WebSocket injection |

### 7. Miscellaneous (`miscellaneous/`)

| File | Deskripsi |
|------|-----------|
| `ssti-*.txt` | Server-Side Template Injection |
| `deserialization-*.txt` | Deserialization attacks |
| `csrf-*.txt` | CSRF testing |
| `race-condition-*.txt` | Race condition testing |
| `bypass-*.txt` | WAF/Filter bypass |

## Cara Penggunaan

### Menggunakan dengan Burp Intruder

1. Buka Burp Suite Professional/Community
2. Capture request yang ingin diuji
3. Send ke Intruder (Ctrl+I)
4. Pilih posisi payload (§placeholder§)
5. Load payload dari file yang sesuai:
   ```
   Payloads → Load → Select file
   ```

### Menggunakan dengan Repeater

1. Copy payload dari file yang sesuai
2. Paste ke parameter yang ingin diuji
3. Send request dan analisis response

### Menggunakan dengan Burp Scanner

1. Passive scan akan otomatis menggunakan payload internal
2. Untuk active scanning, configurasi secara manual

## Tips Penggunaan

### Pemilihan Payload yang Tepat

- **Gunakan sesuai target**: Pilih kategori yang relevan dengan aplikasi yang diuji
- **Test bertahap**: Mulai dari payload sederhana, lanjut ke yang lebih kompleks
- **Analisis response**: Perhatikan perbedaan response untuk identifikasi kerentanan

### Optimasi Payload

- **Customize payload**: Modifikasi payload sesuai konteks aplikasi
- **Encoding**: Gunakan Burp Decoder untuk encoding yang berbeda
- **Grep**: Gunakan Intruder Grep untuk menemukan pola response tertentu

## Disclaimer

⚠️ **PERINGATAN**: Payload ini hanya untuk penggunaan dalam **authorized security testing**. 

- Gunakan hanya pada sistem yang memiliki izin tertulis
- Ikuti Rules of Engagement yang disepakati
- Jangan gunakan untuk aktivitas ilegal
-擅自从 Provider这边获取的 Payload

## Referensi

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)

## Kontribusi

Silakan berkontribusi dengan:
1. Fork repository
2. Tambahkan payload baru
3. Buat Pull Request

## Lisensi

MIT License - lihat file [LICENSE](../../LICENSE) untuk detail.

## Versi

- **Versi Saat Ini**: 1.0.12-20260301-Minggu-1608-WIB
- **Total Payload**: 223+ files
- **Terakhir Diperbarui**: 2026-03-01

---

**Catatan**: Repository ini adalah bagian dari KnowledgeBase Burp Suite. Untuk tutorial dan panduan lengkap, lihat folder `docs/`.
