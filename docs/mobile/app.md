# Mobile Companion App

The Burp Suite KnowledgeBase Mobile App allows security professionals to monitor scans, access payloads, and collaborate with teams on the go.

## Features

### Core Features

- **Scan Dashboard** - Monitor active scans in real-time
- **Payload Library** - Browse and search 10,000+ payloads
- **Team Collaboration** - Chat and share findings with team
- **Vulnerability Tracker** - Track and manage vulnerabilities
- **Quick Actions** - Execute common tasks from mobile

### Platform Support

| Platform | Version | Status |
|----------|---------|--------|
| iOS | 14.0+ | ✅ Available |
| Android | 8.0+ | ✅ Available |
| iPadOS | 14.0+ | ✅ Available |
| Android Tablet | 8.0+ | ✅ Available |

---

## Installation

### iOS (App Store)

```
1. Open App Store
2. Search "Burp KB"
3. Tap Install
4. Open and sign in
```

### Android (Google Play)

```
1. Open Google Play Store
2. Search "Burp KB"
3. Tap Install
4. Open and sign in
```

### Direct APK Download

For enterprise customers without Google Play access:

```
https://downloads.burpkb.com/mobile/latest/burpkb.apk
```

---

## Screens

### 1. Dashboard

The main dashboard provides an overview of your security posture:

```
┌─────────────────────────────────┐
│  🔒 Burp KB            👤      │
├─────────────────────────────────┤
│                                 │
│  Active Scans          3       │
│  ┌─────────────────────────┐   │
│  │ 🔄 example.com          │   │
│  │   Progress: 45%         │   │
│  └─────────────────────────┘   │
│  ┌─────────────────────────┐   │
│  │ 🔄 api.example.com       │   │
│  │   Progress: 12%         │   │
│  └─────────────────────────┘   │
│                                 │
│  Recent Vulnerabilities         │
│  ┌─────────────────────────┐   │
│  │ 🔴 SQL Injection        │   │
│  │    example.com/login    │   │
│  └─────────────────────────┘   │
│                                 │
│  [Scan] [Payloads] [Team]      │
└─────────────────────────────────┘
```

### 2. Scan Control

Start, monitor, and control scans from your mobile:

```python
# Mobile scan API
POST /api/v1/mobile/scans

{
    "target": "https://example.com",
    "scan_type": "quick",
    "notifications": {
        "on_complete": true,
        "on_critical": true
    }
}
```

**Scan Types:**

| Type | Duration | Coverage |
|------|----------|----------|
| Quick | 5-10 min | Basic vulnerabilities |
| Standard | 30-60 min | Common vulnerabilities |
| Full | 2-4 hours | Comprehensive scan |
| Custom | Variable | User-defined |

### 3. Payload Library

Browse and search payloads:

```
┌─────────────────────────────────┐
│  🔍 Search payloads...          │
├─────────────────────────────────┤
│  Categories                     │
│  ├─ SQL Injection      (523)    │
│  ├─ XSS               (412)     │
│  ├─ Command Injection (298)     │
│  ├─ SSRF              (156)     │
│  ├─ XXE                (89)     │
│  └─ Authentication    (234)    │
│                                 │
│  Recent                         │
│  ├─ ' OR '1'='1                │
│  ├─ <script>alert(1)</script>  │
│  └─ ; cat /etc/passwd          │
│                                 │
│  [Favorites] [History] [Share] │
└─────────────────────────────────┘
```

**Features:**

- Search by category, keyword, severity
- Save favorites for quick access
- Copy payload to clipboard
- Share with team members
- Generate variations with AI

### 4. Vulnerability Details

View and manage vulnerabilities:

```
┌─────────────────────────────────┐
│  ← Vulnerability Details        │
├─────────────────────────────────┤
│                                 │
│  SQL Injection in Login        │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│                                 │
│  Severity: 🔴 Critical          │
│  Confidence: 95%                │
│  Status: 🟡 Open                │
│                                 │
│  Target: example.com/login    │
│  Method: POST                  │
│  Found: 2026-03-01 10:30      │
│                                 │
│  Description                   │
│  The login form is vulnerable  │
│  to SQL injection via the      │
│  username parameter.           │
│                                 │
│  [📋 Copy] [📤 Share] [✅ Fix] │
│                                 │
│  Evidence                       │
│  POST /login                   │
│  username=' OR '1'='1--       │
│                                 │
│  Actions                        │
│  [Create Ticket] [Add to Report]│
│  [Request Review] [Dismiss]    │
│                                 │
└─────────────────────────────────┘
```

### 5. Team Collaboration

```
┌─────────────────────────────────┐
│  👥 Team                        │
├─────────────────────────────────┤
│  Security Team                 │
│  ┌─────────────────────────┐   │
│  │ 👤 john    Online       │   │
│  │ 👤 jane    Online       │   │
│  │ 👤 bob     Away         │   │
│  │ 👤 alice   Offline      │   │
│  └─────────────────────────┘   │
│                                 │
│  Recent Activity                │
│  ┌─────────────────────────┐   │
│  │ john started scan...    │   │
│  │ jane found SQLi!        │   │
│  │ bob commented on vuln   │   │
│  └─────────────────────────┘   │
│                                 │
│  [💬 Chat] [📞 Call] [📹 Meet] │
└─────────────────────────────────┘
```

---

## Configuration

### Scan Profiles

Create custom scan profiles for different targets:

```json
{
  "profile_name": "E-commerce Quick Scan",
  "target_type": "web",
  "scan_options": {
    "sql_injection": true,
    "xss": true,
    "auth_bypass": true,
    "api_testing": true,
    "concurrent_requests": 5
  },
  "exclude_paths": [
    "/admin",
    "/api/health",
    "/static"
  ],
  "notifications": {
    "email": true,
    "push": true,
    "slack": false
  }
}
```

### Notification Settings

| Setting | Description | Default |
|---------|-------------|---------|
| Scan Complete | Notify when scan finishes | On |
| Critical Finding | Alert for critical vulns | On |
| Medium Finding | Alert for medium+ vulns | Off |
| Team Activity | Team member updates | On |
| Daily Summary | Daily digest | On |

### Offline Mode

The app supports offline access to:

- Saved payloads (up to 1,000)
- Recent vulnerability data
- Scan history
- Team contacts

Sync automatically when online.

---

## Security

### Authentication

- **Biometric Login** - Face ID / Fingerprint
- **PIN Code** - 6-digit fallback
- **Session Timeout** - Auto-lock after 5 minutes

### Data Protection

- **Encryption at Rest** - AES-256
- **Certificate Pinning** - Prevent MITM
- **No Sensitive Data** - Credentials stored in keychain

---

## API Integration

### REST API

```python
# Python example
import requests

BASE_URL = "https://api.burpkb.com/v1/mobile"

# Get active scans
scans = requests.get(
    f"{BASE_URL}/scans",
    headers={"Authorization": f"Bearer {API_TOKEN}"}
).json()

# Get payloads
payloads = requests.get(
    f"{BASE_URL}/payloads",
    params={"category": "sqli", "limit": 50},
    headers={"Authorization": f"Bearer {API_TOKEN}"}
).json()
```

### WebSocket

For real-time updates:

```javascript
// Connect to real-time events
const ws = new WebSocket('wss://api.burpkb.com/v1/ws');

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    
    if (data.type === 'scan.progress') {
        updateProgress(data.progress);
    } else if (data.type === 'vulnerability.found') {
        showNotification(data.vulnerability);
    }
};
```

---

## Enterprise Features

### MDM Deployment

- **iOS**: Apple Configurator, Jamf, Microsoft Intune
- **Android**: Google Play EMM, Microsoft Intune

### Configuration

```xml
<!-- iOS MobileConfig -->
<dict>
    <key>APIEndpoint</key>
    <string>https://api.burpkb.com</string>
    <key>SSOEnabled</key>
    <true/>
    <key>AllowBackup</key>
    <false/>
</dict>
```

### Custom Branding

Enterprise customers can customize:

- App icon and splash screen
- Color scheme
- Company logo
- Custom domains

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Can't connect | Check internet, verify API key |
| Slow performance | Clear cache, restart app |
| Missing payloads | Sync from cloud |
| Notifications | Check notification permissions |

### Support

- Email: mobile-support@burpkb.com
- In-app support chat
- Documentation: https://docs.burpkb.com/mobile

---

## Pricing

| Feature | Free | Pro | Enterprise |
|---------|------|-----|------------|
| Scan Monitoring | ✅ | ✅ | ✅ |
| Payload Access | 100 | Unlimited | Unlimited |
| Team Collaboration | ❌ | ✅ | ✅ |
| Offline Mode | 50 | 1000 | Unlimited |
| MDM Deployment | ❌ | ❌ | ✅ |
| Custom Branding | ❌ | ❌ | ✅ |
| Priority Support | ❌ | Email | 24/7 |

**Pro**: $9.99/month
**Enterprise**: Contact sales
