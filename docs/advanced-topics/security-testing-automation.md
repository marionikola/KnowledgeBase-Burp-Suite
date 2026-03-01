# Security Testing Automation

## Daftar Isi

1. [Automation Overview](#automation-overview)
2. [CI/CD Integration](#cicd-integration)
3. [Scheduled Scanning](#scheduled-scanning)
4. [Automated Reporting](#automated-reporting)
5. [DevSecOps Pipeline](#devsecops-pipeline)

---

## Automation Overview

### Why Automate?
- Consistent testing
- Faster feedback
- Regular scans
- Integration with workflows

### What to Automate
```
# Automate:
✅ Regular vulnerability scans
✅ Regression testing
✅ CI/CD pipeline security
✅ API security testing
✅ Configuration audits
```

---

## CI/CD Integration

### GitHub Actions
```yaml
name: Security Scan

on:
  push:
    branches: [main]
  schedule:
    - cron: '0 2 * * *'  # Daily at 2AM

jobs:
  burp-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Burp Scan
        run: |
          docker run -v ${{ github.workspace }}:/data \
            burpsuite:latest \
            --project-file=/data/scan.burp \
            --scan-urls=${{ secrets.TARGET_URL }}
            
      - name: Upload Results
        uses: actions/upload-artifact@v3
        with:
          name: burp-report
          path: report.html
```

### GitLab CI
```yaml
burp_scan:
  stage: security
  image: burpsuite:latest
  script:
    - java -jar burp.jar --project-file=scan.burp --scan-urls=$TARGET_URL
  artifacts:
    paths:
      - report.html
    expire_in: 30 days
```

### Jenkins
```groovy
pipeline {
    stages {
        stage('Security Scan') {
            steps {
                sh '''
                    docker run -v $WORKSPACE:/data \
                        burpsuite:latest \
                        --project-file=/data/scan.burp
                '''
            }
        }
        
        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportDir: '.',
                    reportFiles: 'report.html'
                ])
            }
        }
    }
}
```

---

## Scheduled Scanning

### Cron Schedule Examples
```bash
# Daily scan
0 2 * * *

# Weekly on Sunday
0 3 * * 0

# Monthly first day
0 4 1 * *
```

### Burp Enterprise Scheduling
```
# Configure in Burp Enterprise:
- Schedule > Create Scan
- Frequency: Daily/Weekly/Monthly
- Scope: Define URLs
- Actions: Email results
```

---

## Automated Reporting

### Report Generation
```bash
# Command line report:
java -jar burp.jar \
    --project-file=scan.burp \
    --report-format=HTML \
    --report-file=report.html
```

### Report Automation
```python
# Python script:
import requests
from datetime import datetime

BASE = "http://localhost:8090/v0"

def generate_report(scan_id):
    report = {
        "format": "HTML",
        "include_issues": True,
        "severities": ["critical", "high", "medium"]
    }
    
    response = requests.post(
        f"{BASE}/scan/{scan_id}/report",
        json=report
    )
    
    with open(f"scan_{datetime.now()}.html", "wb") as f:
        f.write(response.content)
```

---

## DevSecOps Pipeline

### Pipeline Design
```
# DevSecOps Flow:
Code Commit → SAST → DAST → Burp Scan → Deploy
                ↓
           Fix Issues → Re-scan → Approve
```

### Integration Points
```
# Pre-commit:
- Pre-commit hooks
- IDE security scanning

# Build stage:
- Dependency scanning
- SAST tools

# Test stage:
- Burp scanning
- API security tests

# Deploy stage:
- Configuration review
- Compliance checks
```

### Best Practices
```
✅ Scan early and often
✅ Fix critical issues first
✅ Automate where possible
✅ Maintain audit trail
✅ Regular pipeline review
```

---

**Version**: 1.0.10-20260301-Minggu-1042-WIB  
**Author**: waktuberhenti
