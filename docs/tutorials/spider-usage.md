# Tutorial Spider Usage - Burp Suite

## Daftar Isi

1. [Apa itu Spider?](#apa-itu-spider)
2. [Menjalankan Spider](#menjalankan-spider)
3. [Configuration](#configuration)
4. [Scope Management](#scope-management)
5. [Monitoring Progress](#monitoring-progress)
6. [Results Analysis](#results-analysis)
7. [Tips dan Best Practices](#tips-dan-best-practices)

---

## Apa itu Spider?

Burp Spider adalah web crawler untuk menemukan dan mape semua halaman pada aplikasi web:

### Fungsi Utama
- **Automatic Discovery** - Temukan semua pages
- **Form Detection** - Temukan forms untuk fuzzing
- **Link Parsing** - Parse semua links
- **Crawl Authentication** - Crawl behind login

### Apa yang Ditemukan
- Pages dan endpoints
- Parameters
- Forms (login, search, dll)
- File uploads
- JavaScript files
- API endpoints
- Hidden directories

---

## Menjalankan Spider

### Cara 1: From Target Tab
```
Target > Site Map
Klik kanan URL > Spider this host
```

### Cara 2: From Spider Tab
```
Spider > New scan
Masukkan URL
Klik OK
```

### Cara 3: From Proxy
```
Spider > Options > Spider Integration
- Spider running from Proxy
```

---

## Configuration

### Scope Settings
```
Spider > Scope
- Use scope limit
- Exclude from scope (regex)
- Boring domains
```

### Crawling Options
```
Spider > Options > Crawling
- Maximum link depth: 10
- Maximum drill depth: 5
- Maximum requests: No limit
- Follow redirects: ✓
- Check sitemaps: ✓
- Check robots.txt: ✓
```

### Form Submission
```
Spider > Options > Forms
- Don't submit forms
- Prompt for guidance
- Automatically submit
- Ask for confirmation
```

### Passive Scanning
```
Spider > Options > Passive
- Link parsing: ✓
- Parse HTML: ✓
- Parse JavaScript: ✓
```

---

## Scope Management

### Add to Scope
```
Target > Scope
Add: https://target.com/*
```

### Exclude from Scope
```
Target > Scope > Exclude
- logout
- admin
- *.jpg
- *.css
```

### Check Scope
```
Target > Site Map
Filter: Show only in-scope items
```

---

## Monitoring Progress

### Spider Dashboard
```
Dashboard > Spider tasks
- URLs queued
- URLs discovered
- Forms found
- Errors
```

### Status Indicators
| Status | Arti |
|--------|------|
| 🟢 Running | Active crawling |
| ⏸️ Paused | Paused |
| 🔴 Stopped | Completed/Error |
| ⚪ Pending | In queue |

### Statistics
```
- Requests made
- Data received
- Forms discovered
- Errors encountered
- Time elapsed
```

---

## Results Analysis

### Site Map
```
Target > Site Map
- Tree view of discovered URLs
- Folder structure
- Request/response data
```

### Information Gathered
| Type | Description |
|------|-------------|
| URL | Discovered paths |
| Parameters | Input points |
| Forms | Form fields |
| Comments | HTML comments |
| Meta | Meta tags |
| Errors | Crawl errors |

### Filter Options
```
- Show: JavaScript, CSS, Images
- Filter by: Method, Status
- Hide: Static files
```

---

## Tips dan Best Practices

### ✅ Best Practices
1. **Set scope first** - Jangan crawl di luar target
2. **Configure forms** - Handle form submission dengan benar
3. **Monitor resources** - Don't overload server
4. **Use with Scanner** - Combined approach

### ❌ Hindari
1. Crawl without scope
2. Too aggressive crawling
3. Ignore form submission
4. Missing authentication

### Configuration Example
```
# Untuk aplikasi besar
Thread: 5
Delay: 100ms
Depth: 10
Forms: Ask first

# Untuk aplikasi sensitive
Thread: 1-2
Delay: 500ms
Depth: 5
Forms: Don't submit
```

---

## Common Issues

### Forms Not Being Submitted
- Enable form submission options
- Provide credentials jika perlu
- Check authentication handling

### Missing Pages
- Check JavaScript parsing
- Verify link extraction
- Check redirect handling

### Performance Issues
- Kurangi threads
- Tambah delay
- Set crawl limits

---

## Workflow: Complete Testing

### Step 1: Spider
```
1. Set scope
2. Run spider
3. Wait for completion
4. Review site map
```

### Step 2: Manual Explore
```
1. Browse manually
2. Fill forms
3. Test features
4. Spider adds more URLs
```

### Step 3: Scanner
```
1. Active scan (Professional)
2. Passive scan
3. Review findings
```

### Step 4: Manual Testing
```
1. Use Repeater
2. Use Intruder
3. Test manually
```

---

## Example Output

### Discovered Structure
```
target.com/
├── / (root)
├── /login
├── /register
├── /dashboard
├── /profile
├── /api/
│   ├── /users
│   ├── /data
│   └── /admin
├── /admin/
│   ├── /users
│   └── /settings
└── /static/
    ├── /css/
    └── /js/
```

---

## Next Steps

Lanjutkan ke:
- [Scanner Usage](scanner-usage.md) - Automated vulnerability scanning
- [Intruder Usage](intruder-usage.md) - Automated attacks
- [Proxy Configuration](proxy-configuration.md) - Traffic interception

---

**Version**: 1.0.2-20260301-Minggu-0956-WIB  
**Last Updated**: 2026-03-01 - Minggu - 09:56 GMT+7 (WIB)  
**Author**: waktuberhenti
