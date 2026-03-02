# Cloud Security Scanner

The Cloud Security Scanner identifies misconfigurations and vulnerabilities in cloud infrastructure across AWS, Azure, and GCP.

## Supported Cloud Platforms

| Platform | Services Scanned | Status |
|----------|-----------------|--------|
| AWS | 80+ | ✅ Available |
| Azure | 60+ | ✅ Available |
| GCP | 50+ | ✅ Available |
| Kubernetes | Full | ✅ Available |
| Terraform | All | ✅ Available |

---

## Features

### 1. AWS Security Scanner

```python
from burp_kb.cloud import AWSScanner

scanner = AWSScanner(
    profile="production",
    region="us-east-1"
)

# Scan all services
results = scanner.scan()

# Scan specific services
results = scanner.scan(services=['ec2', 's3', 'rds', 'lambda'])

# Get findings by severity
critical = results.filter(severity="critical")
high = results.filter(severity="high")
```

### 2. Azure Security Scanner

```python
from burp_kb.cloud import AzureScanner

scanner = AzureScanner(
    subscription_id="xxx",
    tenant_id="xxx",
    client_id="xxx",
    client_secret="xxx"
)

results = scanner.scan(
    resource_groups=["production", "staging"],
    services=["storage", "vm", "sql"]
)
```

### 3. GCP Security Scanner

```python
from burp_kb.cloud import GCPScanner

scanner = GCPScanner(
    project_id="my-project",
    credentials_path="/path/to/credentials.json"
)

results = scanner.scan(
    services=["compute", "storage", "iam"],
    include_organizations=True
)
```

---

## Scan Categories

### Identity & Access Management

| Check | Description | Severity |
|-------|-------------|----------|
| IAM-001 | Overly permissive IAM roles | Critical |
| IAM-002 | Root account usage without MFA | Critical |
| IAM-003 | Service accounts with admin access | High |
| IAM-004 | Users with excessive permissions | High |
| IAM-005 | Password policy not enforced | Medium |

### Storage Security

| Check | Description | Severity |
|-------|-------------|----------|
| STORAGE-001 | Public S3 bucket | Critical |
| STORAGE-002 | Bucket encryption disabled | High |
| STORAGE-003 | Versioning not enabled | Medium |
| STORAGE-004 | Access logging disabled | Medium |

### Network Security

| Check | Description | Severity |
|-------|-------------|----------|
| NET-001 | Security group with 0.0.0.0/0 | Critical |
| NET-002 | Unrestricted SSH/RDP access | High |
| NET-003 | VPC endpoints exposed | High |
| NET-004 | Default VPC in use | Medium |

### Compute Security

| Check | Description | Severity |
|-------|-------------|----------|
| COMP-001 | Instance with public IP | High |
| COMP-002 | Root volume unencrypted | Critical |
| COMP-003 | IMDSv2 not enforced | Medium |
| COMP-004 | Instance role with excessive permissions | High |

### Database Security

| Check | Description | Severity |
|-------|-------------|----------|
| DB-001 | Database publicly accessible | Critical |
| DB-002 | Encryption at rest disabled | Critical |
| DB-003 | SSL not enforced | High |
| DB-004 | Audit logging disabled | Medium |

---

## Integration with Burp Suite

### Cloud Proxy Configuration

```yaml
# burp-cloud-proxy.yaml
proxy:
  listen: 127.0.0.1:8080
  cloud_metadata:
    enabled: true
    headers:
      - X-aws-ec2-instance-id
      - X-aws-ec2-ami-id
    token_url: "http://169.254.169.254/latest/meta-data/"
    
scanner:
  auto_scan: true
  severity_threshold: medium
  scan_on_detection: true
```

### Scan Results Import

```python
# Import cloud findings to Burp KB
from burp_kb import BurpKBClient

client = BurpKBClient(api_key="YOUR_API_KEY")

# Import AWS findings
aws_results = scanner.scan()
for finding in aws_results:
    client.vulnerabilities.create(
        title=finding.title,
        severity=finding.severity,
        category="cloud-misconfiguration",
        cloud_provider=finding.provider,
        resource=finding.resource_id,
        description=finding.description,
        remediation=finding.remediation
    )
```

---

## Compliance Mapping

### AWS Foundational Security

| Control | Checks | Standard |
|---------|--------|----------|
| SEC-1 | IAM policies | AWS Foundational |
| SEC-2 | Logging enabled | AWS Foundational |
| SEC-3 | Protect RCMS data | AWS Foundational |
| SEC-4 | Enforce IMDSv2 | AWS Foundational |

### CIS Benchmarks

| Benchmark | Provider | Coverage |
|-----------|----------|----------|
| CIS AWS | AWS | 80/80 |
| CIS Azure | Azure | 55/55 |
| CIS GCP | GCP | 45/45 |

---

## Example Report

```json
{
  "scan_id": "cloud_abc123",
  "timestamp": "2026-03-01T10:00:00Z",
  "provider": "aws",
  "region": "us-east-1",
  "resources_scanned": 156,
  "findings": {
    "critical": 3,
    "high": 12,
    "medium": 28,
    "low": 45
  },
  "top_issues": [
    {
      "id": "IAM-001",
      "title": "Overly permissive IAM role",
      "severity": "critical",
      "resource": "arn:aws:iam::123456789:role/AdminRole",
      "remediation": "Review and restrict permissions to least privilege"
    },
    {
      "id": "S3-001",
      "title": "Public S3 bucket",
      "severity": "critical",
      "resource": "arn:aws:s3:::company-sensitive-data",
      "remediation": "Block public access and review bucket policy"
    }
  ]
}
```

---

## Remediation

### Automated Remediation

```python
# Enable remediation for specific checks
scanner = AWSScanner(profile="production")

scanner.remediate(
    checks=["IAM-001", "S3-001"],
    dry_run=True  # Preview changes
)
```

### Integration with AWS Config

```python
# Enable AWS Config rules
scanner.enable_config_rules(
    rules=[
        "s3-bucket-public-read-prohibited",
        "s3-bucket-server-side-encryption-enabled",
        "iam-root-account-mfa-enabled"
    ]
)
```

---

## Kubernetes Security

```python
from burp_kb.cloud import K8sScanner

scanner = K8sScanner(
    kubeconfig_path="/path/to/kubeconfig",
    context="production"
)

results = scanner.scan(
    namespaces=["default", "production"],
    include_images=True
)
```

### K8s Checks

| Check | Description | Severity |
|-------|-------------|----------|
| K8S-001 | Privileged container | Critical |
| K8S-002 | Root user in container | High |
| K8S-003 | HostPath volume mounted | High |
| K8S-004 | Namespace resource limits not set | Medium |
| K8S-005 | NetworkPolicy missing | Medium |

---

## Terraform Scanning

```python
from burp_kb.cloud import TerraformScanner

scanner = TerraformScanner()

# Scan Terraform files
results = scanner.scan_directory(
    path="./infrastructure",
    var_files=["prod.tfvars"]
)

# Scan plan output
results = scanner.scan_plan(
    plan_file="terraform plan -out=tfplan"
)
```

---

## Pricing

| Plan | Price | Scans/month | Resources |
|------|-------|-------------|-----------|
| Starter | $99/mo | 50 | 100 |
| Professional | $299/mo | 200 | 500 |
| Enterprise | Custom | Unlimited | Unlimited |

---

## Getting Started

### Quick Start

```bash
# Install CLI
pip install burpkb-cloud

# Configure AWS
burpkb-cloud config aws --profile production

# Run scan
burpkb-cloud scan aws --output report.json

# View results
burpkb-cloud report report.json
```

---

## Best Practices

1. **Regular Scanning** - Run cloud scans weekly
2. **Baseline** - Create a baseline after initial scan
3. **Remediation Tracking** - Track and verify fixes
4. **Integration** - Integrate into CI/CD pipeline
5. **Alerting** - Set up real-time alerts for critical findings
