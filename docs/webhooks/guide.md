# Webhook Configuration Guide

Configure webhooks to integrate Burp KB with your workflow.

## Supported Events

### Scan Events

| Event | Description | Payload |
|-------|-------------|---------|
| `scan.started` | Scan initiated | scan_id, target |
| `scan.progress` | Progress update | scan_id, progress |
| `scan.completed` | Scan finished | scan_id, findings_count |
| `scan.failed` | Scan error | scan_id, error |

### Vulnerability Events

| Event | Description |
|-------|-------------|
| `vulnerability.found` | New vulnerability discovered |
| `vulnerability.updated` | Vulnerability status changed |
| `vulnerability.resolved` | Marked as fixed |

### Team Events

| Event | Description |
|-------|-------------|
| `team.member.added` | New member joined |
| `team.member.removed` | Member removed |
| `team.scan.shared` | Scan shared with team |

## Webhook Payload Format

```json
{
  "event": "scan.completed",
  "timestamp": "2026-03-01T22:00:00Z",
  "data": {
    "scan_id": "scan_abc123",
    "target": "https://example.com",
    "findings": {
      "critical": 2,
      "high": 5,
      "medium": 12,
      "low": 8
    }
  }
}
```

## Configuration

### Create Webhook

```bash
curl -X POST https://api.burpkb.com/v1/webhooks \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://your-server.com/webhook",
    "events": ["scan.completed", "vulnerability.found"],
    "secret": "your-secret-key"
  }'
```

### Verify Signature

```python
import hmac
import hashlib

def verify_signature(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)
```

## Retry Policy

- First retry: 1 minute
- Second retry: 5 minutes  
- Third retry: 30 minutes
- Fourth retry: 2 hours
- Then abandon

## Testing

```bash
# Send test webhook
curl -X POST https://api.burpkb.com/v1/webhooks/test \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"webhook_id": "wh_123"}'
```
