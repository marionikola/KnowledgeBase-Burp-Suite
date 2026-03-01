# Reporting Guide - Burp Suite

## Daftar Isi

1. [Report Types](#report-types)
2. [Report Structure](#report-structure)
3. [Finding Details](#finding-details)
4. [Evidence Collection](#evidence-collection)
5. [Remediation](#remediation)
6. [Tools Integration](#tools-integration)

---

## Report Types

### Executive Summary
- High-level overview
- Risk rating summary
- Key findings
- Recommendations
- Non-technical language

### Technical Report
- Detailed findings
- Technical evidence
- Reproduction steps
- Remediation guidance
- References

### Compliance Report
- Specific framework mapping
- Audit compliance
- Regulatory requirements
- Compliance gaps

---

## Report Structure

### 1. Cover Page
```
# Include:
- Report title
- Client name
- Tester name
- Date
- Version
- Classification
```

### 2. Executive Summary
```
# Include:
- Overview
- Scope
- Key findings (top 5)
- Overall risk rating
- Recommendations summary
```

### 3. Methodology
```
# Include:
- Testing approach
- Tools used
- Standards followed (OWASP, NIST)
- Timeline
```

### 4. Scope
```
# Include:
- In-scope URLs
- Exclusions
- Constraints
- Assumptions
```

### 5. Findings
```
# For each finding:
- ID
- Title
- Severity
- Description
- Impact
- Steps to reproduce
- Evidence
- Remediation
- References
```

---

## Finding Details

### Severity Matrix
| Rating | Color | Description |
|--------|-------|-------------|
| Critical | 🔴 | Immediate exploitation possible |
| High | 🟠 | Significant impact |
| Medium | 🟡 | Moderate impact |
| Low | 🔵 | Minor impact |
| Info | ⚪ | Informational |

### Finding Template
```markdown
## [ID-001] SQL Injection in Login Form

### Severity: Critical

### Description
The login form at /login is vulnerable to SQL injection...

### Impact
- Complete database compromise
- Data exfiltration possible
- Potential system access

### Steps to Reproduce
1. Navigate to /login
2. Enter payload: admin'--
3. Submit form
4. Access granted without password

### Evidence
[Insert screenshots, logs, request/response]

### Remediation
- Use parameterized queries
- Implement input validation
- Apply least privilege to DB user

### References
- OWASP SQL Injection
- CWE-89
```

---

## Evidence Collection

### What to Capture
```
# Always capture:
- Request that triggered vulnerability
- Response showing exploitation
- URL and parameters
- Timestamp
- Screenshot if applicable
```

### Burp Evidence Export
```
# Export methods:
1. Right-click > Copy to file
2. Scanner > Report > Save
3. Proxy > HTTP history > Export
```

### Evidence Format
```
# Organize:
/evidence/
  /finding-id/
    /request.txt
    /response.txt
    /screenshot.png
    /notes.txt
```

---

## Remediation

### Writing Recommendations
```
# Be specific:
❌ "Fix the input validation"
✅ "Implement input validation using whitelist approach for username field"

# Be actionable:
❌ "Improve security"
✅ "Add CSRF token to all state-changing forms"

# Prioritize:
- Fix critical first
- Provide timeline recommendations
```

### Remediation Templates
```
# For each vulnerability type:
- SQL Injection: Use parameterized queries
- XSS: Output encoding, CSP headers
- IDOR: Implement proper authorization checks
- Auth issues: Implement MFA, session controls
```

---

## Tools Integration

### Burp Report Features
```
# Generate report:
1. Scanner > Report
2. Select issues
3. Choose format (HTML, PDF, XML)
4. Customize template
```

### Export Formats
| Format | Use Case |
|--------|----------|
| HTML | Web-based reports |
| PDF | Client presentations |
| XML | Integration with other tools |
| JSON | API integration |

### Integration with Other Tools
```
# Export to:
- JIRA
- ServiceNow
- DefectDojo
- Generic CSV/JSON
```

---

## Quality Checklist

```
# Before submitting report:
✅ All findings verified
✅ Evidence captured
✅ Steps reproducible
✅ Recommendations specific
✅ No false positives
✅ Proper severity
✅ Proofread
✅ Format consistent
✅ Client-appropriate language
```

---

**Version**: 1.0.5-20260301-Minggu-1007-WIB  
**Author**: waktuberhenti
