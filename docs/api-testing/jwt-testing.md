# JWT Testing - Burp Suite

## Apa itu JWT?

JSON Web Token (JWT) adalah standar untuk membuat access tokens yang signed secara digital.

## JWT Structure
```
xxxxx.yyyyy.zzzzz
header.payload.signature
```

### Header
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### Payload
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "role": "user"
}
```

## Vulnerabilities

### 1. None Algorithm
```json
{"alg": "none"}
```
→ Remove signature, send as is

### 2. Algorithm Confusion
```json
{"alg": "HS256"}
```
→ Change to RS256, use public key

### 3. Weak Secret
```json
{"alg": "HS256"}
```
→ Brute force secret key

### 4. Key Injection
```
- Fetch public key
- Create token with public key as secret
```

## Testing dengan Burp

### Manual Testing
```
1. Capture JWT token
2. Send to Decoder
3. Analyze header and payload
4. Modify claims
5. Resign with known key
```

### Intruder for Brute Force
```
1. Use wordlist for secrets
2. Attempt to verify signature
3. Find weak keys
```

### Extension: JSON Web Token
```
# Burp extension for JWT:
- Attack none algorithm
- Key confusion
- View decoded
```

## Tools

### Decoder
```
- Decode JWT
- View header/payload
- Analyze claims
```

### Intruder
```
- Brute force secret
- Payload fuzzing
```

### Extensions
```
- JSON Web Token
- JWT Editor
```

---

**Version**: 1.0.7-20260301-Minggu-1011-WIB  
**Author**: waktuberhenti
