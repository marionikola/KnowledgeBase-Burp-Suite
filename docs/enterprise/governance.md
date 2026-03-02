# Enterprise Governance Suite

The Enterprise Governance Suite provides comprehensive security governance, risk management, and compliance tools for large organizations.

## Features

### 1. Multi-Organization Support

Manage multiple security teams and organizations from a single dashboard:

```python
from burp_kb.enterprise import OrganizationManager

manager = OrganizationManager(api_key="ENTERPRISE_API_KEY")

# Create new organization
org = manager.organizations.create(
    name="Acme Corp",
    settings={
        "sso_enabled": True,
        "sso_provider": "okta",
        "data_residency": "us-east-1",
        "max_users": 1000
    }
)

# Add sub-organizations
sub_org = org.sub_organizations.create(
    name="Acme Financial",
    division="finance"
)
```

### 2. Compliance Reporting

Generate compliance reports for various standards:

| Standard | Report Types |
|----------|-------------|
| SOC 2 | Type I, Type II |
| ISO 27001 | Gap Analysis, Compliance |
| PCI-DSS | Quarterly, Annual |
| HIPAA | Security Assessment |
| GDPR | Data Protection |

```python
# Generate compliance report
report = client.compliance.generate(
    standard="soc_2",
    report_type="type_2",
    period="2025-Q4",
    scope=["production", "staging"]
)

# Download report
report.download(format="pdf", output="soc2-report.pdf")
```

### 3. Audit Logging

Comprehensive activity tracking:

```python
# Query audit logs
logs = client.audit.query(
    start_date="2026-01-01",
    end_date="2026-03-01",
    user_id="user_123",
    action="scan.*"
)

# Export for compliance
client.audit.export(
    format="csv",
    start_date="2026-01-01",
    output="audit-log.csv"
)
```

### 4. Data Residency

| Region | Location | Status |
|--------|----------|--------|
| US East | Virginia | ✅ Available |
| US West | Oregon | ✅ Available |
| EU | Frankfurt | ✅ Available |
| EU | Dublin | ✅ Available |
| APAC | Singapore | ✅ Available |
| APAC | Tokyo | Coming Soon |

---

## Dashboard Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│  Enterprise Security Dashboard                    [Organization ▼] │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Risk Overview                    Compliance Status                 │
│  ┌──────────────────┐            ┌──────────────────┐              │
│  │ Risk Score: 72  │            │ SOC 2: ████░░ 65%│              │
│  │ (Medium-High)   │            │ ISO:   █████░ 80%│              │
│  └──────────────────┘            └──────────────────┘              │
│                                                                     │
│  Vulnerabilities by Severity     Scan Activity (30 days)            │
│  ┌──────────────────┐            ┌──────────────────┐              │
│  │ Critical:  5    │            │ Total:  234     │              │
│  │ High:     23    │            │ Completed: 198  │              │
│  │ Medium:   67    │            │ Running:   12   │              │
│  │ Low:     112    │            │ Failed:    24   │              │
│  └──────────────────┘            └──────────────────┘              │
│                                                                     │
│  Recent Scans                   Top Vulnerabilities                 │
│  ┌──────────────────┐            ┌──────────────────┐              │
│  │ web-01    Done  │            │ SQL Injection    │              │
│  │ api-01    Done  │            │ XSS (Reflected) │              │
│  │ api-02    Run   │            │ Auth Bypass      │              │
│  └──────────────────┘            └──────────────────┘              │
│                                                                     │
│  [Reports] [Users] [Settings] [Audit Logs]                         │
└─────────────────────────────────────────────────────────────────────┘
```

---

## User Management

### Role-Based Access Control (RBAC)

```json
{
  "roles": [
    {
      "name": "Security Admin",
      "permissions": [
        "scan:create",
        "scan:read",
        "scan:delete",
        "report:create",
        "report:read",
        "user:manage",
        "org:manage",
        "settings:manage"
      ]
    },
    {
      "name": "Security Analyst",
      "permissions": [
        "scan:create",
        "scan:read",
        "report:create",
        "report:read",
        "vulnerability:manage"
      ]
    },
    {
      "name": "Developer",
      "permissions": [
        "scan:read",
        "report:read",
        "vulnerability:read"
      ]
    },
    {
      "name": "Viewer",
      "permissions": [
        "scan:read",
        "report:read"
      ]
    }
  ]
}
```

### SSO Integration

Supported SSO Providers:

| Provider | SAML | OAuth | OIDC |
|----------|------|-------|------|
| Okta | ✅ | ✅ | ✅ |
| Azure AD | ✅ | ✅ | ✅ |
| Google | ❌ | ✅ | ✅ |
| OneLogin | ✅ | ✅ | ✅ |
| Ping Identity | ✅ | ✅ | ✅ |

```python
# Configure SSO
client.sso.configure(
    provider="okta",
    metadata_url="https://your-org.okta.com/app/abc/sso/saml/metadata",
    attributes={
        "email": "user.email",
        "name": "user.name",
        "role": "user.groups"
    }
)
```

---

## Governance Features

### Policy Engine

```python
# Create security policy
policy = client.policies.create(
    name="Critical Data Protection",
    rules=[
        {
            "condition": "vulnerability.severity == 'critical'",
            "action": "notify",
            "notify": ["security-team", "ciso"]
        },
        {
            "condition": "scan.target matches '.*\\.acme\\.com'",
            "action": "require_approval"
        },
        {
            "condition": "vulnerability.cvss >= 9.0",
            "action": "block_deployment"
        }
    ]
)
```

### Risk Scoring

Automated risk assessment:

```python
# Get risk score
risk = client.risk.calculate(
    target="https://api.acme.com",
    factors=[
        "vulnerability_severity",
        "asset_criticality",
        "exploitability",
        "business_impact"
    ]
)

# Risk score: 0-100
# 0-25: Low
# 26-50: Medium
# 51-75: High
# 76-100: Critical
```

---

## SLA & Support

| Feature | Business | Enterprise |
|---------|----------|------------|
| Uptime SLA | 99.9% | 99.99% |
| Support Hours | Business Hours | 24/7 |
| Response Time | 24 hours | 1 hour |
| Dedicated CSM | ❌ | ✅ |
| Training | Self-serve | On-site |
| Custom Integration | Limited | Full |

---

## On-Premise Deployment

For organizations requiring on-premise solutions:

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 8 cores | 16+ cores |
| RAM | 32 GB | 64+ GB |
| Storage | 500 GB SSD | 1 TB SSD |
| Network | 1 Gbps | 10 Gbps |

### Deployment Options

```yaml
# docker-compose.yml
version: '3.8'

services:
  burpkb-api:
    image: burpkb/enterprise-api:v1
    ports:
      - "443:443"
    volumes:
      - data:/data
      - logs:/var/log
    environment:
      - DATABASE_URL=postgresql://...
      - REDIS_URL=redis://...
      - ENCRYPTION_KEY=...

  burpkb-worker:
    image: burpkb/enterprise-worker:v1
    depends_on:
      - burpkb-api
    environment:
      - API_URL=http://burpkb-api
```

### Features

- Full feature parity with cloud
- Air-gapped deployment option
- Custom SSL certificates
- LDAP/Active Directory integration
- Hardware security module support
- Annual licensing

---

## Pricing

### Enterprise Plans

| Feature | Standard | Advanced | Premium |
|---------|----------|----------|---------|
| Users | 25 | 100 | Unlimited |
| Scans/month | 500 | 2,000 | Unlimited |
| Storage | 50 GB | 200 GB | Unlimited |
| API Rate Limit | 500/min | 2,000/min | Unlimited |
| SSO | ✅ | ✅ | ✅ |
| Audit Logs | 90 days | 1 year | 2 years |
| SLA | 99.9% | 99.99% | 99.99% |
| Support | Email | Priority | Dedicated |

**Contact sales for custom enterprise solutions**

---

## Success Metrics

Track your security program:

```python
# Get security metrics
metrics = client.metrics.get(
    period="quarterly",
    dimensions=[
        "vulnerability_trend",
        "scan_coverage",
        "remediation_rate",
        "team_velocity"
    ]
)

# Metrics include:
# - Mean Time to Detect (MTTD)
# - Mean Time to Remediate (MTTR)
# - Vulnerability Discovery Rate
# - False Positive Rate
# - Scan Coverage
# - Team Productivity
```

---

## Support

- **Email**: enterprise@burpkb.com
- **Phone**: +1-888-BURP-KB
- **Portal**: https://enterprise.burpkb.com/support
- **Documentation**: https://docs.burpkb.com/enterprise
