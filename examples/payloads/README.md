# Burp Suite Payload Collection

> Koleksi payload komprehensif untuk security testing menggunakan Burp Suite - 2,540+ files

## Overview

Direktori ini berisi kumpulan payload yang digunakan untuk menguji berbagai jenis kerentanan keamanan (vulnerability) pada aplikasi web. Payload dikelompokkan berdasarkan kategori untuk memudahkan penetration tester dalam melakukan security assessment.

## Struktur Folder

```
examples/payloads/
├── api/                    # API Testing Payloads
├── authentication/         # Authentication Testing
├── cloud/                 # Cloud Security Testing
├── cms/                   # CMS Vulnerabilities
├── cookies/               # Cookie Fuzzing
├── encoding/              # Encoding Bypass
├── files/                 # File-Related Testing
├── fuzzing/               # General Fuzzing
├── graphql/               # GraphQL Testing
├── headers/               # HTTP Header Injection
├── idor/                  # Insecure Direct Object Reference
├── injection/             # Injection Payloads
├── javascript/            # JavaScript Injection
├── javascript/            # JavaScript/Node.js Testing
├── jwt/                   # JWT Vulnerabilities
├── ldap/                  # LDAP Injection
├── linux/                 # Linux Exploitation
├── log4j/                 # Log4j Vulnerabilities
├── memcached/             # Memcached Injection
├── mobile/                # Mobile API Testing
├── mongodb/               # MongoDB Injection
├── mysql/                 # MySQL Injection
├── network/               # Network Attacks
├── oracle/                # Oracle Injection
├── oauth/                 # OAuth Vulnerabilities
├── parameters/            # Parameter Fuzzing
├── path/                  # Path Traversal
├── postgresql/            # PostgreSQL Injection
├── privilege-escalation/  # Privilege Escalation
├── rails/                 # Ruby on Rails
├── rce/                   # Remote Code Execution
├── react/                 # React.js Testing
├── redis/                 # Redis Injection
├── rest/                  # REST API Testing
├── saml/                  # SAML Injection
├── serialization/         # Deserialization
├── soap/                  # SOAP API Testing
├── spring/                # Spring Framework
├── ssti/                  # Server-Side Template Injection
├── sql-injection/         # SQL Injection
├── struts/                # Apache Struts
├── svn/                   # SVN Information Disclosure
├── upload/                # File Upload Bypass
├── vue/                   # Vue.js Testing
├── websockets/            # WebSocket Testing
├── windows/               # Windows Exploitation
├── xss/                   # Cross-Site Scripting
├── xxe/                   # XML External Entity
└── django/                # Django Testing
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

### 5. API Testing (`api/`, `rest/`, `graphql/`)

| File | Deskripsi |
|------|-----------|
| `rest-*.txt` | REST API testing |
| `graphql-*.txt` | GraphQL testing |
| `jwt-*.txt` | JWT API testing |
| `oauth-*.txt` | OAuth/API security |

### 6. Cloud Security (`cloud/`)

| File | Deskripsi |
|------|-----------|
| `cloud-aws-*.txt` | AWS metadata endpoint testing |
| `cloud-azure-*.txt` | Azure metadata testing |
| `cloud-gcp-*.txt` | GCP metadata testing |

### 7. Framework-Specific

| Direktori | Framework |
|-----------|-----------|
| `log4j/` | Log4j vulnerabilities |
| `struts/` | Apache Struts |
| `spring/` | Spring Framework |
| `rails/` | Ruby on Rails |
| `django/` | Django |
| `laravel/` | Laravel |
| `express/` | Express.js |
| `angular/` | Angular |
| `react/` | React.js |
| `vue/` | Vue.js |

### 8. Database Injection

| Direktori | Database |
|-----------|----------|
| `mysql/` | MySQL |
| `postgresql/` | PostgreSQL |
| `oracle/` | Oracle |
| `mongodb/` | MongoDB |
| `redis/` | Redis |
| `memcached/` | Memcached |

### 9. CI/CD & DevOps

| Direktori | Tools |
|-----------|-------|
| `jenkins/` | Jenkins |
| `docker/` | Docker |
| `kubernetes/` | Kubernetes |
| `git/` | Git |
| `svn/` | SVN |
| `ci-cd/` | CI/CD Pipelines |

### 10. Platform-Specific

| Direktori | Platform |
|-----------|----------|
| `windows/` | Windows |
| `linux/` | Linux |

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

## Statistics

- **Total Files**: 2,540+
- **Categories**: 40+
- **Version**: 1.0.15-20260301-Minggu-1621-WIB

## Disclaimer

⚠️ **PERINGATAN**: Payload ini hanya untuk penggunaan dalam **authorized security testing**. 

- Gunakan hanya pada sistem yang memiliki izin tertulis
- Ikuti Rules of Engagement yang disepakati
- Jangan gunakan untuk aktivitas ilegal
- 所有Payload仅供安全研究使用

## Referensi

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [Burp Suite Official Documentation](https://portswigger.net/burp/documentation)

## Kontribusi

Silakan berkontribusi dengan:
1. Fork repository
2. Tambahkan payload baru
3. Buat Pull Request

## Lisensi

MIT License - lihat file [LICENSE](../../LICENSE) untuk detail.

## Versi

- **Versi Saat Ini**: 1.0.15-20260301-Minggu-1621-WIB
- **Total Payload**: 2,540+ files
- **Terakhir Diperbarui**: 2026-03-01

---

**Catatan**: Repository ini adalah bagian dari KnowledgeBase Burp Suite. Untuk tutorial dan panduan lengkap, lihat folder `docs/`.
