# WebSocket Testing - Burp Suite

## Apa itu WebSocket?

WebSocket adalah protocol untuk komunikasi bidirectional antara client dan server melalui single TCP connection.

## WebSocket Basics

### Connection
```javascript
// Client initiates:
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
```

### Messages
```json
// Client -> Server
{"type": "message", "content": "Hello"}

{"type": "message", "content": "<script>alert(1)</script>"}
```

## Vulnerabilities

### 1. Lack of Authorization
```
# Test:
1. Connect to WebSocket
2. Send messages
3. Check if you should be authorized
```

### 2. XSS via WebSocket
```
# Test:
{"message": "<script>alert(1)</script>"}
```

### 3. Injection
```
# SQL Injection via WebSocket:
{"query": "SELECT * FROM users"}
```

### 4. Origin-based Bypass
```
# Test:
Origin: https://evil.com
# Check if server validates origin
```

## Testing dengan Burp

### Enable WebSocket
```
# Proxy > Options > WebSocket
# Enable: Intercept messages from and to client
```

### Monitor Traffic
```
# Proxy > WebSocket history
# View all messages
```

### Send Messages
```
# Right-click > Send to Repeater
# Modify and send
```

## Tools

### Proxy History
```
- Monitor all messages
- Filter by direction
- Search content
```

### Repeater
```
- Manual message testing
- Injection testing
- Authentication testing
```

### Intruder
```
- Fuzzing messages
- Brute force
- Automation
```

---

**Version**: 1.0.7-20260301-Minggu-1011-WIB  
**Author**: waktuberhenti
