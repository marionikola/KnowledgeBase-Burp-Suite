# API Testing - Burp Suite

## Apa itu API Testing?

API (Application Programming Interface) testing involves testing REST and GraphQL APIs for security vulnerabilities.

## REST API Testing

### Common Endpoints
```
GET    /api/users      # List users
GET    /api/users/{id} # Get user
POST   /api/users      # Create user
PUT    /api/users/{id} # Update user
DELETE /api/users/{id} # Delete user
```

### Testing Areas

### 1. Authorization
```http
GET /api/admin/users
# Test: Can user access admin endpoints?

GET /api/users/123
# Test: Can user access other user's data?
```

### 2. HTTP Methods
```http
# Test all methods:
GET /api/resource
POST /api/resource
PUT /api/resource
DELETE /api/resource
PATCH /api/resource
```

### 3. Content Types
```http
Content-Type: application/json
Content-Type: application/xml
Content-Type: application/x-www-form-urlencoded
```

### 4. Parameter Pollution
```json
{"id": 1, "id": 2}
{"id": "1", "id": 1}
```

## Tools di Burp

### Repeater
```
- Test API endpoints
- Modify JSON
- Check authorization
```

### Intruder
```
- Fuzz parameters
- Enumerate endpoints
- Test rate limiting
```

### Decoder
```
- Encode/decode payloads
- Base64 handling
- URL encoding
```

## Testing Checklist

```
✅ Authentication bypass
✅ Authorization issues (IDOR)
✅ Input validation
✅ HTTP method override
✅ Content-type handling
✅ Rate limiting
✅ SQL injection
✅ XXE (XML)
✅ Mass assignment
```

---

**Version**: 1.0.7-20260301-Minggu-1011-WIB  
**Author**: waktuberhenti
