# Tools Integration - Burp Suite

## Integrasi dengan Security Tools

### 1. Nmap Integration
```bash
# Scan ports
nmap -p 443 target.com

# Export to Burp
# Import Nmap XML di Target > Analysis
```

### 2. SQLMap Integration
```bash
# Use with Burp proxy
sqlmap -r request.txt --proxy=http://127.0.0.1:8080
```

### 3. Nikto Integration
```bash
# Scan via Burp
nikto -h target.com -proxy http://127.0.0.1:8080
```

## CI/CD Integration

### Jenkins Pipeline
```groovy
pipeline {
    stages {
        stage('Burp Scan') {
            steps {
                sh '''
                    java -jar burpsuite_pro.jar \
                        --project-file=scan.burp \
                        --scan-urls=${TARGET_URL}
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts '*.html'
        }
    }
}
```

### GitLab CI
```yaml
burp_scan:
  script:
    - java -jar burpsuite_pro.jar --project-file=scan.burp
  artifacts:
    paths:
      - report.html
```

## Reporting Tools

### DefectDojo Integration
```bash
# Export Burp scan to DefectDojo
import-scan \
    --engagement 1 \
    --product 1 \
    --scan_type "Burp Scan" \
    --file burp_scan.xml
```

### JIRA Integration
```
# Export findings ke JIRA:
1. Generate XML report
2. Use JIRA import
3. Map fields
```

## API Integration

### REST API Usage
```python
import requests

BURP_API = "http://localhost:8090"

# Start scan
response = requests.post(
    f"{BURP_API}/v0/scan",
    json={"urls": ["https://target.com"]}
)

# Get results
issues = requests.get(f"{BURP_API}/v0/issues")
```

---

**Version**: 1.0.8-20260301-Minggu-1012-WIB  
**Author**: waktuberhenti
