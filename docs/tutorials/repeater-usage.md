# Tutorial Repeater Usage - Burp Suite

## Daftar Isi

1. [Apa itu Repeater?](#apa-itu-repeater)
2. [Mengirim Request ke Repeater](#mengirim-request-ke-repeater)
3. [Interface Overview](#interface-overview)
4. [Manipulasi Request](#manipulasi-request)
5. [Response Analysis](#response-analysis)
6. [Use Cases](#use-cases)
7. [Tips dan Tricks](#tips-dan-tricks)

---

## Apa itu Repeater?

Burp Repeater adalah tools untuk **manual testing** dan **request manipulation**. 
Tidak seperti Proxy yang mengintercept, Repeater digunakan untuk:

- **Repetitive Testing** - Uji payload yang sama berkali-kali
- **Manual Exploitation** - Exploitasi manual vulnerability
- **Request Crafting** - Buat request dari nol
- **Response Analysis** - Analisis detail response

---

## Mengirim Request ke Repeater

### Cara 1: Dari Proxy
```
1. Proxy > HTTP History
2. Klik kanan pada request
3. Send to Repeater
```

### Cara 2: Dari Target
```
1. Target > Site Map
2. Klik kanan pada URL
3. Request in Repeater
```

### Cara 3: Manual Input
```
1. Repeater > New tab
2. Masukkan request manual
```

---

## Interface Overview

```
┌─────────────────────────────────────────────────────┐
│ Repeater                                            │
├─────────────────────────────────────────────────────┤
│ [Target] [Headers] [Body] [Auth]     [Send] [Go]   │
├─────────────────────────────────────────────────────┤
│ Request:                                            │
│ GET /api/user?id=1 HTTP/1.1                        │
│ Host: target.com                                    │
│ ...                                                 │
├─────────────────────────────────────────────────────┤
│ Response:                                           │
│ HTTP/1.1 200 OK                                    │
│ Content-Type: application/json                      │
│ ...                                                 │
└─────────────────────────────────────────────────────┘
```

### Tab Definitions
| Tab | Fungsi |
|-----|--------|
| Target | URL dan port |
| Headers | Edit headers |
| Body | Edit request body |
| Auth | Authentication settings |

---

## Manipulasi Request

### URL Parameters
```http
GET /search?q=test&page=1 HTTP/1.1
```
- Ubah nilai parameter
- Tambah/hapus parameter
- Encode/decode otomatis

### POST Data
```http
POST /login HTTP/1.1
Content-Type: application/x-www-form-urlencoded

username=admin&password=test123
```

### JSON Body
```http
POST /api/user HTTP/1.1
Content-Type: application/json

{"username": "admin", "role": "user"}
```

### Headers
```http
GET /admin HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0
Cookie: session=abc123
X-Custom-Header: test
```

---

## Response Analysis

### Response Panel
```
- Pretty: Format JSON/XML
- Raw: Asli response
- Render: Render HTML
```

### Informasi Penting
| Element | Arti |
|---------|------|
| Status Code | 200=OK, 404=Not Found, 500=Error |
| Content-Length | Ukuran response |
| Content-Type | Tipe data |
| Set-Cookie | Cookie yang di-set |
| Location | Redirect target |

### Colors
| Color | Status |
|-------|--------|
| 🟢 Green | 2xx Success |
| 🔵 Blue | 3xx Redirect |
| 🟠 Orange | 4xx Client Error |
| 🔴 Red | 5xx Server Error |

---

## Use Cases

### 1. SQL Injection Testing
```
# Original
GET /user?id=1 HTTP/1.1

# Test
GET /user?id=1' OR '1'='1 HTTP/1.1
GET /user?id=1' UNION SELECT * FROM users-- HTTP/1.1
```

### 2. XSS Testing
```
# Original
GET /search?q=test HTTP/1.1

# Test XSS
GET /search?q=<script>alert(1)</script> HTTP/1.1
GET /search?q=<img src=x onerror=alert(1)> HTTP/1.1
```

### 3. IDOR Testing
```
# User 1
GET /api/user/1 HTTP/1.1

# Test User 2
GET /api/user/2 HTTP/1.1
```

### 4. Authentication Bypass
```
# Login request
POST /login HTTP/1.1
username=admin&password=wrong

# Bypass attempts
username=admin'--&password=anything
username=admin&password[]=anything
```

### 5. Header Injection
```
GET / HTTP/1.1
Host: target.com
X-Forwarded-For: 127.0.0.1
```

---

## Tips dan Tricks

### Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| Ctrl+Enter | Send request |
| Alt+Left/Right | Switch history |
| Ctrl+Shift+E | Encode selection |
| Ctrl+Shift+D | Decode selection |

### Request Tabs
```
- Rename tabs untuk organisasi
- Simpan request penting
- Multiple tabs untuk testing parallel
```

### History Navigation
```
- Gunakan < > untuk navigasi
- Lihat request sebelumnya
- Compare responses
```

### AutoEncode
```
- Enable Auto URL-encode
- Handle special characters
- Automatic encoding
```

### Follow Redirects
```
- Options > Follow redirects
- Never / On-site only / Always
```

---

## Example Workflow

### SQL Injection Manual
```bash
1. Proxy: Capture login request
2. Send to Repeater
3. Test each parameter:
   - '
   - '
   - ' OR '1'='1
   - ' UNION SELECT...
4. Note interesting responses
5. Document findings
```

### API Testing
```bash
1. Capture API call
2. Modify JSON body
3. Test:
   - Parameter pollution
   - Type confusion
   - Missing fields
   - Extra fields
4. Check authorization
```

---

## Troubleshooting

### Response Not Loading
- Periksa network connectivity
- Cek timeout settings
- Verify SSL certificates

### Large Response
- Disable auto-render
- Use Raw view
- Check Content-Length

### Encoding Issues
- Manual encode special chars
- Use Decoder tool
- Check Content-Type

---

## Next Steps

Lanjutkan ke:
- [Intruder Usage](intruder-usage.md) - Automated payload testing
- [Scanner Usage](scanner-usage.md) - Automated scanning
- [Proxy Configuration](proxy-configuration.md) - Basic proxy

---

**Version**: 1.0.2-20260301-Minggu-0956-WIB  
**Last Updated**: 2026-03-01 - Minggu - 09:56 GMT+7 (WIB)  
**Author**: waktuberhenti
