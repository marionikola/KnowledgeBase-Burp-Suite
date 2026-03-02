# Burp Suite KnowledgeBase API

The Burp Suite KnowledgeBase API provides programmatic access to payloads, scans, reports, and team management features.

## Base URL

```
Production: https://api.burpkb.com/v1
Sandbox:    https://sandbox.api.burpkb.com/v1
```

## Authentication

### API Keys

```bash
# Using API Key
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.burpkb.com/v1/payloads

# Using API Key in request
curl -H "X-API-Key: YOUR_API_KEY" \
     https://api.burpkb.com/v1/payloads
```

### OAuth 2.0

```python
import requests
from requests_oauthlib import OAuth2Session

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

oauth = OAuth2Session(client_id, redirect_uri="https://yourapp.com/callback")
token = oauth.fetch_token(
    "https://api.burpkb.com/oauth/token",
    client_id=client_id,
    client_secret=client_secret
)

# Make authenticated requests
response = oauth.get("https://api.burpkb.com/v1/payloads")
```

## Rate Limits

| Plan | Requests/minute | Daily Limit |
|------|-----------------|-------------|
| Free | 60 | 1,000 |
| Pro | 300 | 50,000 |
| Enterprise | 1,000 | Unlimited |

## Response Format

All responses are in JSON format:

```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "total": 100,
    "page": 1,
    "per_page": 20,
    "total_pages": 5
  }
}
```

## Error Handling

```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests",
    "details": "Rate limit exceeded. Upgrade your plan."
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| UNAUTHORIZED | 401 | Invalid or missing API key |
| FORBIDDEN | 403 | Insufficient permissions |
| NOT_FOUND | 404 | Resource not found |
| RATE_LIMITED | 429 | Rate limit exceeded |
| SERVER_ERROR | 500 | Internal server error |

---

## Endpoints

### Payloads

#### List Payloads

```
GET /payloads
```

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| category | string | Filter by category (sqli, xss, etc.) |
| severity | string | Filter by severity |
| search | string | Search in payload content |
| page | int | Page number (default: 1) |
| per_page | int | Items per page (default: 20, max: 100) |

**Example:**

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "https://api.burpkb.com/v1/payloads?category=sqli&per_page=50"
```

**Response:**

```json
{
  "success": true,
  "data": [
    {
      "id": "pld_abc123",
      "name": "SQL Injection Basic",
      "category": "sqli",
      "payload": "' OR '1'='1",
      "severity": "high",
      "tags": ["injection", "authentication"],
      "created_at": "2026-01-15T10:30:00Z"
    }
  ],
  "meta": {
    "total": 500,
    "page": 1,
    "per_page": 50,
    "total_pages": 10
  }
}
```

#### Create Payload

```
POST /payloads
```

**Request Body:**

```json
{
  "name": "Custom SQL Injection",
  "category": "sqli",
  "payload": "'; DROP TABLE users--",
  "severity": "critical",
  "tags": ["custom", "destructive"],
  "description": "Custom payload for SQL injection testing"
}
```

**Example:**

```bash
curl -X POST -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"name":"Custom SQLi","category":"sqli","payload":"test","severity":"high"}' \
     https://api.burpkb.com/v1/payloads
```

#### Get Payload

```
GET /payloads/{id}
```

#### Update Payload

```
PUT /payloads/{id}
```

#### Delete Payload

```
DELETE /payloads/{id}
```

---

### Scans

#### Start Scan

```
POST /scans
```

**Request Body:**

```json
{
  "target": "https://example.com",
  "scan_type": "full",
  "options": {
    "sql_injection": true,
    "xss": true,
    "authentication": true,
    "api_testing": true,
    "concurrent_requests": 10
  },
  "exclude_paths": ["/admin", "/health"],
  "auth_credentials": {
    "username": "testuser",
    "password": "testpass"
  }
}
```

**Response:**

```json
{
  "success": true,
  "data": {
    "scan_id": "scan_xyz789",
    "status": "running",
    "target": "https://example.com",
    "started_at": "2026-03-01T10:00:00Z",
    "progress": 0
  }
}
```

#### Get Scan Status

```
GET /scans/{scan_id}
```

#### List Scan Results

```
GET /scans/{scan_id}/results
```

#### Stop Scan

```
POST /scans/{scan_id}/stop
```

---

### Reports

#### Generate Report

```
POST /reports
```

**Request Body:**

```json
{
  "scan_id": "scan_xyz789",
  "format": "pdf",
  "template": "executive",
  "include_screenshots": true,
  "include_raw_requests": false
}
```

**Available Formats:** `pdf`, `html`, `json`, `csv`

**Available Templates:** `executive`, `technical`, `compliance`, `custom`

#### Download Report

```
GET /reports/{report_id}/download
```

---

### Teams

#### List Team Members

```
GET /teams/{team_id}/members
```

#### Invite Member

```
POST /teams/{team_id}/members
```

**Request Body:**

```json
{
  "email": "user@example.com",
  "role": "member",
  "permissions": ["scan", "view_reports"]
}
```

#### Remove Member

```
DELETE /teams/{team_id}/members/{user_id}
```

---

### Webhooks

#### Create Webhook

```
POST /webhooks
```

**Request Body:**

```json
{
  "url": "https://yourapp.com/webhook",
  "events": ["scan.completed", "vulnerability.found"],
  "secret": "your_webhook_secret"
}
```

#### Available Events

| Event | Description |
|-------|-------------|
| scan.started | Scan has started |
| scan.completed | Scan has completed |
| scan.failed | Scan has failed |
| vulnerability.found | New vulnerability discovered |
| vulnerability.resolved | Vulnerability marked as resolved |
| team.member.added | New team member added |

---

## SDK Examples

### Python SDK

```python
from burp_kb import BurpKBClient

client = BurpKBClient(api_key="YOUR_API_KEY")

# Get payloads
payloads = client.payloads.list(category="sqli", per_page=50)

# Start scan
scan = client.scans.create(
    target="https://example.com",
    scan_type="full"
)

# Get results
results = client.scans.get_results(scan["scan_id"])

# Generate report
report = client.reports.create(
    scan_id=scan["scan_id"],
    format="pdf"
)
```

### JavaScript SDK

```javascript
import { BurpKB } from '@burpkb/sdk';

const client = new BurpKB({ apiKey: 'YOUR_API_KEY' });

// Get payloads
const payloads = await client.payloads.list({ category: 'xss' });

// Start scan
const scan = await client.scans.create({
  target: 'https://example.com',
  scanType: 'quick'
});

// Download report
await client.reports.download(reportId, './report.pdf');
```

---

## SDK Installation

```bash
# Python
pip install burp-kb

# JavaScript
npm install @burpkb/sdk

# Go
go get github.com/burpkb/sdk-go
```

---

## Support

- Email: api-support@burpkb.com
- Documentation: https://docs.burpkb.com
- Status Page: https://status.burpkb.com
