# Threat Intelligence Module

The Threat Intelligence Module provides real-time threat data, CVE tracking, and vulnerability intelligence.

## Features

### CVE Database Integration

```python
from burp_kb.threat_intel import CVETracker

tracker = CVETracker()

# Track specific CVEs
cve = tracker.get_cve("CVE-2024-1234")
print(f"CVSS: {cve.cvss_score}")
print(f"Severity: {cve.severity}")
print(f"Description: {cve.description}")
```

### Real-time Alerts

```python
# Set up alerts for new CVEs
tracker.alert(
    keywords=["SQL injection", "XSS"],
    severity="high",
    callback=send_notification
)
```

### Vulnerability Intelligence

| Source | Updates | Coverage |
|--------|---------|----------|
| NVD | Real-time | 100K+ CVEs |
| Vendor Advisories | Daily | 500+ vendors |
| Exploit DB | Real-time | 50K+ exploits |
| Threat Feeds | Real-time | APT campaigns |

## Integration

### SIEM Integration

```python
# Send to Splunk
tracker.to_splunk(
    host="splunk.example.com",
    token="your-token"
)

# Send to ELK
tracker.to_elk(
    hosts=["elk1:9200", "elk2:9200"]
)
```

### Custom Feeds

```python
# Add custom threat feed
tracker.add_feed(
    name="Company Intel",
    format="stix",
    url="https://intel.company.com/feed",
    api_key="xxx"
)
```

---

## Dashboard

```
┌─────────────────────────────────────────────┐
│  Threat Intelligence Dashboard              │
├─────────────────────────────────────────────┤
│                                             │
│  Active CVEs: 1,234                        │
│  Critical: 45  |  High: 123  |  Medium: 456│
│                                             │
│  Recent Advisories                          │
│  ├─ CVE-2024-001 (Critical) - PHP         │
│  ├─ CVE-2024-002 (High)    - Apache      │
│  └─ CVE-2024-003 (Medium)  - WordPress    │
│                                             │
│  Exploit Availability                      │
│  ├─ 12 CVEs with public exploits           │
│  └─ 3 APT campaigns targeting our stack    │
│                                             │
└─────────────────────────────────────────────┘
```

## Pricing

| Plan | Price | Features |
|------|-------|----------|
| Free | $0 | Basic CVE tracking |
| Pro | $49/mo | Real-time alerts, SIEM |
| Enterprise | Custom | Custom feeds, API |
