# Tutorial Intruder Usage - Burp Suite

## Daftar Isi

1. [Apa itu Intruder?](#apa-itu-intruder)
2. [Attack Types](#attack-types)
3. [Payload Types](#payload-types)
4. [Menjalankan Attack](#menjalankan-attack)
5. [Options Configuration](#options-configuration)
6. [Results Analysis](#results-analysis)
7. [Use Cases](#use-cases)

---

## Apa itu Intruder?

Burp Intruder adalah tools untuk **automated attacks** dan **fuzzing**:
- **Brute Force** - Crack passwords
- **Fuzzing** - Test berbagai input
- **Enumeration** - Find hidden resources
- **Parameter Testing** - Test semua input

---

## Attack Types

### 1. Sniper
- Satu payload set
- Satu position per request
- **Use case**: Single parameter testing

### 2. Battering Ram
- Satu payload set  
- Semua positions sama
- **Use case**: Same input to all positions

### 3. Pitchfork
- Multiple payload sets
- Each position gets own payload
- **Use case**: Username + Password testing

### 4. Cluster Bomb
- Multiple payload sets
- All combinations
- **Use case**: Full combinatorial testing

---

## Payload Types

### Simple List
```bash
admin
root
test
user
```

### Runtime File
```bash
# Load from file
file:/path/to/wordlist.txt
```

### Numbers
```
Range: 1-1000
Step: 1
Format: Decimal/Hex
```

### Dates
```
Format: yyyy-MM-dd
Range: 2020-01-01 to 2024-12-31
```

### Character Blocks
```
Length: 10-100
Min chars: 10
```

### Custom Generator
```
Grep - Extract from response
```

### Brute Forcer
```
Character set: a-z, A-Z, 0-9
Length: 4-8
```

---

## Menjalankan Attack

### Step 1: Send Request to Intruder
```
Proxy > HTTP History
Klik kanan > Send to Intruder
```

### Step 2: Set Positions
```
Intruder > Positions
- § marker untuk posisi payload
- Clear all / Auto
- Add §manual§
```

### Step 3: Set Payloads
```
Intruder > Payloads
- Payload Set: 1
- Payload type: Simple list
- Load file atau add manually
```

### Step 4: Start Attack
```
Intruder > Start attack
- Attack type: Sniper/Battering/etc
- Results akan muncul
```

---

## Options Configuration

### Request Engine
```
Number of threads: 5-10
Throttle: 0 (no delay)
Retry after: 3 seconds
```

### Attack Results
```
Store requests: ✓
Make unmodified baseline request: ✓
```

### Grep - Match
```
Extract from response
Pattern untuk find
```

### Grep - Extract
```
Display
- Status
- Length
- Response time
```

### Redirections
```
Follow redirects: Always
Process cookies: ✓
```

---

## Results Analysis

### Results Table
| Column | Description |
|--------|-------------|
| # | Request number |
| Status | HTTP status |
| Length | Response length |
| Timeout | Timeout indicator |
| Grep | Custom matches |

### Response View
```
- Request tab
- Response tab
- Payload tab
- Error tab
```

### Filtering
```
- Show only: 2xx, 3xx, 4xx, 5xx
- Grep: Match specific
- Sort by: Length, Status
```

---

## Use Cases

### 1. Password Brute Force
```
POST /login
username=admin§password§

Payload: wordlist.txt
Attack: Sniper

Extract: "Invalid password" vs "Login successful"
```

### 2. Parameter Fuzzing
```
GET /search?q=§test§

Payloads:
- SQLi: ', OR 1=1, UNION SELECT...
- XSS: <script>alert(1)</script>
- Path traversal: ../../../etc/passwd
```

### 3. ID Enumeration
```
GET /user/§id§

Payloads: Numbers 1-1000

Look for:
- Different response length
- 200 vs 404
- User data in response
```

### 4. Directory Fuzzing
```
GET /§path§

Payloads:
- admin
- api
- backup
- config
- phpmyadmin
```

### 5. Session Token Testing
```
GET /page
Cookie: session=§token§

Payloads: captured tokens
Test: session fixation, token reuse
```

---

## Example: Login Brute Force

### Setup
```
Request:
POST /login HTTP/1.1
Host: target.com

username=admin&password=§pwd§

Attack Type: Sniper
```

### Payloads
```
Set 1: password-wordlist.txt
admin
123456
password
admin123
letmein
```

### Analysis
```
Status 302 = Redirect (success)
Status 200 = Error
Look for: "Welcome" / "Invalid" / Location header
```

---

## Tips dan Tricks

### Performance
```
- Thread: 5-10 untuk webapps
- Throttle: 10-50ms untuk sensitive targets
- Concurrent: Jangan terlalu agresif
```

### Accuracy
```
- Use grep untuk extract interesting
- Compare responses carefully
- Test manually jika ada doubt
```

### Automation
```
- Save attack results
- Export to file
- Resume attack
```

### Common Wordlists
```bash
/root/.burpsuite/proxylists
/usr/share/wordlists/
SecLists/
```

---

## Troubleshooting

### Too Many Timeouts
- Kurangi threads
- Tambah throttle
- Check network

### False Positives
- Increase grep precision
- Manual verify interesting
- Check baseline response

### Rate Limiting
```
- Increase throttle
- Use proxies (Professional)
- Slow down attack
```

---

## Next Steps

Lanjutkan ke:
- [Spider Usage](spider-usage.md) - Web crawling
- [Repeater Usage](repeater-usage.md) - Manual testing

---

**Version**: 1.0.2-20260301-Minggu-0956-WIB  
**Last Updated**: 2026-03-01 - Minggu - 09:56 GMT+7 (WIB)  
**Author**: waktuberhenti
