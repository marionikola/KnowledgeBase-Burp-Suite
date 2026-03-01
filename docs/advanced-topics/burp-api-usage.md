# Burp Suite API Usage

## Daftar Isi

1. [API Overview](#api-overview)
2. [Getting Started](#getting-started)
3. [Core Endpoints](#core-endpoints)
4. [Scan Operations](#scan-operations)
5. [Issue Management](#issue-management)
6. [Advanced Usage](#advanced-usage)

---

## API Overview

### What is Burp API?
REST API untuk automate Burp Suite Professional:
- Start/comonitor scans
- Retrieve findings
- Manage targets
- Generate reports

### Requirements
- Burp Suite Professional
- API key configuration
- Port 8090 (default)

---

## Getting Started

### Enable API
```bash
# Command line:
java -jar burpsuite_pro.jar --api

# Or in GUI:
Proxy > Options > Allow API access
```

### Authentication
```python
# Generate API key:
# Settings > API Key > Generate

# Use in requests:
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
```

### Base URL
```
http://localhost:8090/v0/
```

---

## Core Endpoints

### Information
```python
# Get Burp version
GET /v0/info

# Get license status
GET /v0/license
```

### Sites Management
```python
# Get all sites
GET /v0/sites

# Add target site
POST /v0/sites
{
    "url": "https://target.com",
    "scope": ["https://target.com/*"]
}
```

---

## Scan Operations

### Start Scan
```python
POST /v0/scan
{
    "urls": [
        "https://target.com/page1",
        "https://target.com/page2"
    ],
    "scan_config": "Default",
    "application_logos": True,
    "exclude_from_scope": []
}
```

### Scan Status
```python
# Get scan status
GET /v0/scan/{scan_id}

# Response:
{
    "id": "abc123",
    "status": "running",
    "progress": 45,
    "issues_count": 12
}
```

### Stop Scan
```python
DELETE /v0/scan/{scan_id}
```

---

## Issue Management

### Get Issues
```python
# All issues
GET /v0/issues

# Filter by severity
GET /v0/issues?severity=critical

# Filter by type
GET /v0/issues?type=sql_injection
```

### Issue Details
```python
GET /v0/issues/{issue_id}

# Response:
{
    "name": "SQL injection",
    "severity": "critical",
    "confidence": "certain",
    "host": "https://target.com",
    "path": "/search",
    "description": "...",
    "remediation": "..."
}
```

---

## Advanced Usage

### Web Scanner API
```python
# Configure scan settings
POST /v0/scan/options
{
    "crawl_strategy": "depth_first",
    "max_crawl_depth": 5,
    "max_concurrent_requests": 10
}
```

### Crawl and Audit
```python
# Combined crawl + audit
POST /v0/scan
{
    "urls": ["https://target.com"],
    "crawl_and_audit": True,
    "audit_links": True,
    "audit_forms": True
}
```

---

## Python Examples

### Complete Scan Workflow
```python
import requests
import time

BASE = "http://localhost:8090/v0"
API_KEY = "your-api-key"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# 1. Add target
requests.post(f"{BASE}/sites", 
    json={"url": "https://example.com"},
    headers=HEADERS)

# 2. Start scan
scan = requests.post(f"{BASE}/scan",
    json={"urls": ["https://example.com"]},
    headers=HEADERS).json()

scan_id = scan["id"]

# 3. Monitor progress
while True:
    status = requests.get(f"{BASE}/scan/{scan_id}", headers=HEADERS).json()
    print(f"Progress: {status['progress']}%")
    if status["status"] == "completed":
        break
    time.sleep(10)

# 4. Get results
issues = requests.get(f"{BASE}/issues", headers=HEADERS).json()
print(f"Found {len(issues)} issues")
```

---

## Error Handling

### Common Errors
| Code | Meaning |
|------|---------|
| 401 | Invalid API key |
| 403 | No license |
| 404 | Endpoint not found |
| 429 | Rate limited |

---

**Version**: 1.0.10-20260301-Minggu-1042-WIB  
**Catatan**: Requires Burp Suite Professional  
**Author**: waktuberhenti
