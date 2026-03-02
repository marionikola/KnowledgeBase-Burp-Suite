# Integration Hub

The Integration Hub connects Burp Suite KnowledgeBase with your favorite security and DevOps tools.

## Supported Integrations

### CI/CD Platforms

#### GitHub Actions

```yaml
# .github/workflows/security-scan.yml
name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Burp Suite Security Scan
        uses: burpkb/scan-action@v1
        with:
          api_key: ${{ secrets.BURPKB_API_KEY }}
          target: ${{ secrets.TARGET_URL }}
          scan_type: quick
          severity_threshold: medium
          
      - name: Upload Results
        uses: actions/upload-artifact@v3
        with:
          name: scan-results
          path: results/
```

#### GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - security

burp_scan:
  stage: security
  image: burpkb/scan:latest
  script:
    - burpkb-scan --target $TARGET_URL --output results.json
  artifacts:
    paths:
      - results.json
    expire_in: 30 days
  only:
    - main
    - merge_requests
```

#### Jenkins

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    stages {
        stage('Security Scan') {
            steps {
                script {
                    def scanResult = burpKBScan(
                        target: 'https://example.com',
                        scanType: 'full',
                        apiKey: credentials('burpkb-api-key')
                    )
                    
                    if (scanResult.severity == 'critical') {
                        error('Critical vulnerabilities found!')
                    }
                }
            }
        }
    }
}
```

---

### Security Tools

#### OWASP ZAP Integration

```python
from burp_kb import BurpKBClient
from zapv2 import ZAPv2

# Start ZAP scan
zap = ZAPv2(proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})
zap.urlopen('http://target.com')

# Spider
zap.spider.scan(url='http://target.com')

# Get results and import to Burp KB
client = BurpKBClient(api_key="YOUR_API_KEY")
for alert in zap.core.alerts():
    client.vulnerabilities.create(
        title=alert.get('name'),
        severity=alert.get('risk'),
        url=alert.get('url'),
        description=alert.get('description')
    )
```

#### Nessus Integration

```python
import nessusbeat
from burp_kb import BurpKBClient

# Connect to Nessus
nessus = nessusbeat.Client(
    url='https://nessus.example.com',
    access_key='YOUR_ACCESS_KEY',
    secret_key='YOUR_SECRET_KEY'
)

# Get scan results
scan = nessus.scans.get(scan_id=123)

# Import to Burp KB
client = BurpKBClient(api_key="YOUR_API_KEY")
for finding in scan['vulnerabilities']:
    client.vulnerabilities.create(
        title=finding['name'],
        severity=finding['severity'],
        cvss=finding['cvss'],
        description=finding['description']
    )
```

---

### Communication Tools

#### Slack Integration

1. Go to Slack App Directory
2. Search for "Burp KB"
3. Install and authorize
4. Configure channels and notifications

```json
{
  "webhook_url": "https://hooks.slack.com/services/xxx",
  "channel": "#security-alerts",
  "notifications": {
    "scan_completed": true,
    "critical_findings": true,
    "team_activity": false
  },
  "format": {
    "include_screenshots": true,
    "include_details": true
  }
}
```

#### Microsoft Teams Integration

```json
{
  "webhook_url": "https://outlook.office.com/webhook/xxx",
  "team": "Security Team",
  "channel": "Alerts",
  "notifications": {
    "critical_findings": true,
    "daily_summary": true
  }
}
```

#### Discord Integration

```json
{
  "webhook_url": "https://discord.com/api/webhooks/xxx",
  "server": "Security Community",
  "channel": "#vulnerability-alerts",
  "notifications": {
    "new_findings": true,
    "scan_status": true
  }
}
```

---

### Issue Trackers

#### Jira Integration

```python
from burp_kb import BurpKBClient
from jira import JIRA

# Get latest vulnerabilities
client = BurpKBClient(api_key="YOUR_API_KEY")
vulns = client.vulnerabilities.list(severity="critical")

# Create Jira tickets
jira = JIRA(
    server='https://yourcompany.atlassian.net',
    basic_auth=('user', 'api_token')
)

for vuln in vulns:
    issue = jira.create_issue(
        project='SEC',
        summary=f"[{vuln.severity.upper()}] {vuln.title}",
        description=vuln.description,
        issuetype={'name': 'Bug'}
    )
    
    # Add security label
    jira.add_issues_to_sprint(issue.id, sprint_id=123)
```

#### GitHub Issues Integration

```bash
# Configure GitHub Issues
export GITHUB_ORG=your-org
export GITHUB_REPO=security-issues
export GITHUB_TOKEN=ghp_xxx

# Create issue from vulnerability
burpkb issues create \
  --title "SQL Injection in /api/users" \
  --severity critical \
  --labels security,sql-injection \
  --assignee security-team
```

---

### Cloud Platforms

#### AWS Security Hub

```python
import boto3
from burp_kb import BurpKBClient

# Get findings from Burp KB
client = BurpKBClient(api_key="YOUR_API_KEY")
findings = client.vulnerabilities.list(scan_id="scan_123")

# Send to AWS Security Hub
securityhub = boto3.client('securityhub')

for finding in findings:
    securityhub.import_findings(
        Findings=[{
            'SchemaVersion': '2018-10-08',
            'Id': f"burpkb/{finding.id}",
            'ProductArn': 'arn:aws:securityhub:us-east-1:123456789012:product/burpkb/default',
            'GeneratorId': 'burpkb-scanner',
            'Title': finding.title,
            'Description': finding.description,
            'Severity': {
                'Label': finding.severity.upper()
            },
            'Resources': [{
                'Type': 'Website',
                'Id': finding.url
            }]
        }]
    )
```

#### Azure Sentinel

```python
from azure.sentinel import Sentinel
from burp_kb import BurpKBClient

client = BurpKBClient(api_key="YOUR_API_KEY")
findings = client.vulnerabilities.list(severity="high")

sentinel = Sentinel(
    workspace_id="xxx",
    credential=...
)

for finding in findings:
    sentinel.create_incident(
        title=finding.title,
        severity=finding.severity,
        description=finding.description
    )
```

---

### SIEM Integration

#### Splunk

```python
import splunklib.client
from burp_kb import BurpKBClient

client = BurpKBClient(api_key="YOUR_API_KEY")
findings = client.vulnerabilities.list()

# Connect to Splunk
service = splunklib.client.connect(
    host='splunk.example.com',
    port=8089,
    username='admin',
    password='password'
)

# Index findings
for finding in findings:
    service.indexes['security'].submit(
        f"severity={finding.severity} title={finding.title} url={finding.url}",
        sourcetype='burpkb:findings'
    )
```

#### ELK Stack

```yaml
# Logstash config
input {
  http {
    port => 8080
    codec => json
  }
}

filter {
  mutate {
    add_field => { "index_name" => "burpkb-findings" }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "%{index_name}"
  }
}
```

---

## Custom Integrations

### Building Custom Integrations

```python
from burp_kb import BurpKBClient

class CustomIntegration:
    def __init__(self, api_key, config):
        self.client = BurpKBClient(api_key=api_key)
        self.config = config
    
    def on_vulnerability_found(self, vuln):
        # Custom logic
        pass
    
    def on_scan_completed(self, scan):
        # Custom logic
        pass
    
    def sync_findings(self):
        # Sync all findings
        for vuln in self.client.vulnerabilities.list():
            self.on_vulnerability_found(vuln)

# Usage
integration = CustomIntegration(
    api_key="YOUR_API_KEY",
    config={"key": "value"}
)
integration.sync_findings()
```

### Webhook Events

Subscribe to real-time events:

```json
{
  "webhook_url": "https://yourapp.com/webhook",
  "events": [
    "scan.started",
    "scan.completed",
    "scan.failed",
    "vulnerability.found",
    "vulnerability.updated",
    "team.member.added",
    "report.generated"
  ]
}
```

---

## Integration SDK

### Installation

```bash
pip install burpkb-integration-sdk
```

### Quick Start

```python
from burpkb.integration import IntegrationBuilder

# Create custom integration
integration = (
    IntegrationBuilder("my-integration")
    .trigger("scan.completed")
    .action(lambda scan: print(f"Scan completed: {scan['id']}"))
    .build()
)

integration.start()
```

---

## Marketplace

Visit our [Integration Marketplace](https://marketplace.burpkb.com) to discover community-built integrations.

### Featured Integrations

| Integration | Downloads | Rating |
|-------------|-----------|--------|
| GitHub Actions | 10K+ | ⭐⭐⭐⭐⭐ |
| Jira | 5K+ | ⭐⭐⭐⭐ |
| Slack | 8K+ | ⭐⭐⭐⭐⭐ |
| Splunk | 2K+ | ⭐⭐⭐⭐ |

---

## Support

- Documentation: https://docs.burpkb.com/integrations
- Community Forum: https://forum.burpkb.com/integrations
- Support: support@burpkb.com
