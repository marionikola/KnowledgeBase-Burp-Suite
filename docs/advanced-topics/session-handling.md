# Session Handling - Burp Suite

## Daftar Isi

1. [Understanding Session Management](#understanding-session-management)
2. [Session Handling Rules](#session-handling-rules)
3. [Macro Configuration](#macro-configuration)
4. [Cookie Handling](#cookie-handling)
5. [Advanced Techniques](#advanced-techniques)

---

## Understanding Session Management

### Why Session Handling Matters
Session handling adalah critical untuk:
- Maintaining authentication state
- Testing authenticated features
- Handling session timeouts
- Dealing with anti-CSRF tokens

### Session Types
| Type | Description |
|------|-------------|
| Cookie-based | Session ID in cookies |
| Token-based | Bearer tokens, JWT |
| Header-based | Custom headers |
| URL-based | Session in URL |

---

## Session Handling Rules

### Creating Rules
```
Project Options > Session Handling Rules > Add
```

### Rule Actions
```
1. Check session is valid
2. Run macro
3. Update cookie
4. Prompt for confirmation
```

### Example Rules
```
# Rule: Auto-login when session expires
- Scope: All URLs in scope
- Action: Run login macro
- Update cookies from macro response

# Rule: Check session validity
- Action: Request test URL
- Check for "session expired" message
- If expired, run macro
```

---

## Macro Configuration

### What are Macros?
Macros adalah sequences of requests yang dijalankan secara otomatis untuk:
- Handle authentication
- Refresh tokens
- Maintain session state

### Creating a Macro
```
1. Project Options > Macros > Record new macro
2. Select requests to include
3. Configure parameter extraction
4. Test macro
5. Save
```

### Macro Editor
```
# Parameters:
- Parameter name: session_token
- Response location: Set-Cookie header
- Regular expression: SESSION=(.*?)
```

---

## Cookie Handling

### Cookie Propagation
```
# Options:
- Use cookies from Burp's cookie jar
- Update cookies from macro responses
- Apply scope filters
```

### Cookie Jar
```
# View:
- Project Options > Session > Cookie Jar
- Shows all captured cookies
- Can manually add/edit
```

### Cookie Scope
```
# Filter options:
- Apply to specific domains
- Exclude certain paths
- Session vs persistent cookies
```

---

## Advanced Techniques

### Anti-CSRF Token Handling
```python
# Macro extracts CSRF token:
1. Request: GET /form
2. Response contains: <input name="csrf" value="abc123">
3. Extract using regex: name="csrf" value="(.*?)"
4. Apply to subsequent requests
```

### Dynamic Parameter Handling
```
# Handle:
- Timestamps
- Nonces
- Sequence numbers
- HMAC signatures
```

### Multi-Step Authentication
```python
# Login flow:
1. GET /login - extract form token
2. POST /login - submit credentials
3. GET /mfa - if 2FA enabled
4. POST /mfa - submit 2FA code
5. Extract final session cookies
```

---

## Troubleshooting

### Common Issues
```
❌ Session not being updated
❌ Macro fails intermittently  
❌ Anti-CSRF tokens not captured
❌ Cookies not applied to requests

# Solutions:
✅ Check macro order
✅ Verify regex patterns
✅ Test scope settings
✅ Check timing issues
```

---

**Version**: 1.0.10-20260301-Minggu-1042-WIB  
**Author**: waktuberhenti
