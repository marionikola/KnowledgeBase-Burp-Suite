# Tutorial Scanner Usage - Burp Suite

## Daftar Isi

1. [Apa itu Burp Scanner?](#apa-itu-burp-scanner)
2. [Persiapan Scanning](#persiapan-scanning)
3. [Jenis Scanning](#jenis-scanning)
4. [Menjalankan Scan](#menjalankan-scan)
5. [Analisis Hasil](#analisis-hasil)
6. [Scan Configuration](#scan-configuration)
7. [Schedule Scan](#schedule-scan)
8. [Tips dan Best Practices](#tips-dan-best-practices)

---

## Apa itu Burp Scanner?

Burp Scanner adalah fitur otomatis untuk menemukan vulnerability pada aplikasi web:

### Fitur Utama
- **Automated Crawling** - Menemukan semua halaman
- **Vulnerability Detection** - Mendeteksi 100+ jenis vulnerability
- **False Positive Reduction** - Filter noise
- **Detailed Reporting** - Laporan lengkap

### Vulnerability yang Dideteksi
| Kategori | Contoh |
|----------|--------|
| **Injection** | SQL Injection, Command Injection, LDAP Injection |
| **XSS** | Reflected, Stored, DOM-based |
| **Auth** | Broken Authentication, Session Management |
| **Sensitive Data** | Information Disclosure |
| **Access Control** | IDOR, Privilege Escalation |
| **Configuration** | Security Misconfiguration |

---

## Persiapan Scanning

### Step 1: Tentukan Scope
```
Target > Scope
- Add URL to scope
- Exclude from scope (logout, dll)
```

### Step 2: Add to Site Map
```
Target > Site Map
- Right-click URL > Add to scope
```

### Step 3: Configure Proxy (jika belum)
Lihat [Proxy Configuration](proxy-configuration.md)

---

## Jenis Scanning

### 1. Active Scanning
- Mengirim request ke server
- Menguji semua parameter
- Lebih akurat tapi lebih lambat
- Bisa merusak aplikasi

### 2. Passive Scanning
- Hanya menganalisis traffic yang melalui proxy
- Tidak mengirim request tambahan
- Aman tapi kurang komprehensif

### 3. Insertion Points
```
Scanner > Options > Insertion Points
- URL parameter values
- Body parameters (POST, JSON, XML)
- Headers (User-Agent, Cookie)
- Cookies
```

---

## Menjalankan Scan

### Cara 1: Quick Scan
```
1. Target > Site Map
2. Klik kanan pada URL
3. Scan
4. Pilih: Crawl only / Crawl and audit
```

### Cara 2: Custom Scan
```
1. Scanner > New Scan
2. Pilih type:
   - Crawl and audit (recommended)
   - Crawl only
   - Audit only
3. Select URLs
4. Configure options
5. Click OK
```

### Cara 3: From Proxy History
```
1. Proxy > HTTP History
2. Filter: Select items
3. Klik kanan > Scan selected items
```

---

## Analisis Hasil

### Dashboard View
```
Scanner > Dashboard
- Running scans
- Completed scans
- Issues by severity
```

### Issues Tab
```
Scanner > Issues
- Severity: Critical, High, Medium, Low, Info
- Confidence: Certain, Firm, Tentative
- Types: Vulnerability name
- Locations: Where found
```

### Issue Details
```
- Summary: Deskripsi vulnerability
- Path: URL yang terpengaruh
- Request: Request yang memicu
- Response: Response yang menunjukkan vuln
- Remediation: Cara fix
- References: Link referensi
```

### Severity Levels
| Level | Warna | Arti |
|-------|-------|------|
| Critical | 🔴 | Immediate exploitation |
| High | 🟠 | Serious impact |
| Medium | 🟡 | Moderate impact |
| Low | 🔵 | Minor impact |
| Info | ⚪ | Informational |

---

## Scan Configuration

### Scan Speed
```
Scanner > Options > Speed
- Normal (default)
- Thorough
- Slow
- Quick
```

### Resource Usage
```
Scanner > Options > Resource Limits
- Concurrent requests: 5-10
- Retries for failed requests: 3
```

### Passive Scanning Options
```
Scanner > Options > Passive Scanning
- Scan passively
- Scan Alexa top 100
- Scan JS files
```

### Audit Optimization
```
Scanner > Options > Audit Coverage
- Coverage: Medium (default) / Thorough / Minimum
- Insertion points: Standard / All
```

---

## Schedule Scan

### Membuat Schedule
```
Scanner > New Scan > Schedule
- Set start time
- Set recurrence (daily, weekly)
- Email notifications (Professional)
```

### Monitoring
```
Dashboard > Task details
- Progress bar
- Issues found
- Time remaining
```

---

## Tips dan Best Practices

### ✅ Best Practices
1. **Always get permission** - Hanya scan sistem yang diizinkan
2. **Set proper scope** - Jangan scan semua
3. **Use during off-peak** - Scan saat traffic rendah
4. **Save project** - Rutin simpan progress
5. **Review false positives** - Validasi findings

### ❌ Hindari
1. Scanning tanpa scope yang jelas
2. Terlalu banyak concurrent requests
3. Scanning production selama jam kerja
4. Mengabaikan informasi sensitif di report

### Automation Tips
```bash
# Command line scanning (Professional)
java -jar burpsuite_pro.jar \
  --project-file=scan.burp \
  --scan URL_TO_SCAN
```

---

## Troubleshooting

### Scan Stuck
- Periksa network connectivity
- Kurangi concurrent requests
- Periksa server timeout

### Too Many False Positives
- Tingkatkan audit thoroughness
- Tambah exclusion patterns
- Review insertion points

### Performance Issues
- Kurangi resource usage
- Batasi crawl depth
- Exclude large files

---

## Next Steps

Lanjutkan ke:
- [Repeater Usage](repeater-usage.md) - Manual testing
- [Intruder Usage](intruder-usage.md) - Automated attacks

---

**Catatan**: Scanner hanya tersedia di **Burp Suite Professional** dan **Enterprise**. Versi Community hanya bisa passive scanning.

---

**Version**: 1.0.1-20260301-Minggu-0954-WIB  
**Last Updated**: 2026-03-01 - Minggu - 09:54 GMT+7 (WIB)  
**Author**: waktuberhenti
