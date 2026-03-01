# Automation - Burp Suite

## Daftar Isi

1. [CLI Usage](#cli-usage)
2. [API Integration](#api-integration)
3. [CI/CD Integration](#cicd-integration)
4. [Macros](#macros)
5. [Scheduled Tasks](#scheduled-tasks)
6. [Scripting](#scripting)

---

## CLI Usage

### Command Line Options
```bash
# Basic startup
java -jar burpsuite_pro.jar

# With project file
java -jar burpsuite_pro.jar --project-file=myproject.burp

# Headless mode (Professional)
java -jar burpsuite_pro.jar --headless

# With config
java -jar burpsuite_pro.jar --user-config=config.json
```

### Exit Codes
| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Error |
| 2 | Startup failed |

---

## API Integration

### REST API (Professional)
```bash
# Start API:
java -jar burpsuite_pro.jar --api

# Default port: 8090
# API documentation: http://localhost:8090/
```

### API Endpoints
```python
import requests

# Get issues
GET http://localhost:8090/v0/issues

# Scan URL
POST http://localhost:8090/v0/scan
{
  "urls": ["https://target.com"]
}

# Get scan status
GET http://localhost:8090/v0/scan/{id}
```

### Python API Example
```python
import requests

BASE_URL = "http://localhost:8090"

# Login
session = requests.Session()
session.auth = ("burp", "api_key")

# Start scan
response = session.post(
    f"{BASE_URL}/v0/scan",
    json={"urls": ["https://example.com"]}
)
print(response.json())

# Get results
issues = session.get(f"{BASE_URL}/v0/issues")
print(issues.json())
```

---

## CI/CD Integration

### Jenkins Pipeline
```groovy
pipeline {
    agent any
    
    stages {
        stage('Burp Scan') {
            steps {
                sh '''
                    java -jar burpsuite_pro.jar \
                        --project-file=scan.burp \
                        --api \
                        --scan-urls=https://target.com
                '''
            }
        }
        
        stage('Results') {
            steps {
                archiveArtifacts 'report.html'
            }
        }
    }
}
```

### GitLab CI
```yaml
burp_scan:
  stage: security
  script:
    - java -jar burpsuite_pro.jar --project-file=scan.burp --api
  artifacts:
    reports:
      sarif: results.sarif
```

### GitHub Actions
```yaml
name: Burp Scan
on: [push]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Burp
        run: |
          java -jar burpsuite_pro.jar \
            --project-file=scan.burp
```

---

## Macros

### Creating Macros
```
1. Project options > Macros > Add
2. Record macro:
   - Capture login request
   - Test response
3. Configure session handling:
   - Rules > Add
   - Scope > Define
4. Test and save
```

### Use Cases
```
- Auto-login untuk authenticated scans
- Handle CSRF tokens
- Dynamic parameter handling
- Session refresh
```

### Configuration
```
# Macros can:
- Execute multiple requests
- Extract and store cookies
- Update anti-CSRF tokens
- Handle redirects
```

---

## Scheduled Tasks

### Burp Enterprise
```
# Scheduled scans:
- Daily full scan
- Weekly differential
- Monthly comprehensive
```

### External Scheduling
```bash
# Cron job example:
0 2 * * * /path/to/burp.sh

# burp.sh:
#!/bin/bash
java -jar burpsuite_pro.jar \
  --project-file=/projects/client.burp \
  --scan-urls=https://client.com
```

---

## Scripting

### Python Automation
```python
from burp import IBurpExtender

class Automation(IBurpExtender):
    def registerExtenderCallbacks(self, callbacks):
        # Automated tasks
        print("Running automated scan...")
        
        # Scan targets
        callbacks.addSiteMap("https://target.com")
        
        # Generate report
        callbacks.generateScanReport()
```

### Batch Processing
```bash
# Multiple targets:
for target in $(cat targets.txt); do
    java -jar burpsuite_pro.jar \
        --project-file=${target}.burp \
        --scan-urls=${target}
done
```

---

## Best Practices

### Automation Tips
```
✅ Start small - Test on one URL
✅ Use logging - Track progress
✅ Handle errors - Graceful failures
✅ Clean up - Delete temp files
✅ Monitor resources - Don't overload

❌ Don't scan too aggressive
❌ Don't ignore warnings
❌ Don't leave credentials in scripts
```

### Security Considerations
```
# Protect credentials:
- Use environment variables
- Don't commit secrets
- Rotate API keys
- Use vault services
```

---

**Version**: 1.0.4-20260301-Minggu-1003-WIB  
**Catatan**: Beberapa fitur memerlukan Burp Suite Professional  
**Author**: waktuberhenti
