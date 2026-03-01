# Testing Methodology - Burp Suite

## Daftar Isi

1. [Pre-Engagement](#pre-engagement)
2. [Information Gathering](#information-gathering)
3. [Mapping](#mapping)
4. [Vulnerability Discovery](#vulnerability-discovery)
5. [Exploitation](#exploitation)
6. [Reporting](#reporting)

---

## Pre-Engagement

### Scope Definition
```
# Questions to ask client:
1. What's the target?
2. What's out of scope?
3. Are there subdomains?
4. Are APIs in scope?
5. Is mobile apps included?
6. What's the timeline?
7. Are there third-party integrations?
```

### Rules of Engagement
```
✅ Only test authorized systems
✅ Don't attack DoS
✅ Don't exfiltrate data
✅ Respect data privacy
✅ Report immediately if critical found
```

### Documentation
```
# Pre-engagement checklist:
- Scope document signed
- NDA signed
- Contact information
- Emergency contacts
- Timeline agreed
- Testing window defined
```

---

## Information Gathering

### Passive Reconnaissance
```
# Use:
- DNS lookups
- WHOIS information
- Public documents
- Job postings
- Wayback Machine
```

### Active Reconnaissance
```
# Port scanning:
- nmap for network mapping
- WhatWeb for technology detection
- Wappalyzer for CMS detection
```

### Burp Tools for Recon
```
- Spider: Crawl website
- Target tab: Map structure
- Proxy: Capture all traffic
- Engagement tools: Find hidden content
```

---

## Mapping

### Application Mapping
```
1. Spider untuk crawl semua pages
2. Manual exploration untuk dynamic content
3. Identify:
   - Entry points
   - Parameters
   - Authentication mechanisms
   - Session management
   - Data flows
```

### Understanding Architecture
```
# Identify:
- Frontend technology
- Backend technology
- Database
- APIs
- Third-party services
- Load balancers
- WAF
```

---

## Vulnerability Discovery

### Testing Approach
```
# OWASP Testing Guide v4:
1. Information Gathering
2. Configuration and Deploy Management
3. Identity Management
4. Authentication
5. Authorization
6. Session Management
7. Input Validation
8. Error Handling
9. Cryptography
10. Business Logic
11. Client-side
```

### Burp Scanner Usage
```
# Workflow:
1. Set scope
2. Run spider
3. Passive scan (ongoing)
4. Active scan (targeted)
5. Manual verification
6. False positive removal
```

### Manual Testing
```
# Test manually:
- Repeater untuk verify
- Intruder untuk fuzzing
- Encoder/Decoder untuk manipulation
- Comparer untuk differences
```

---

## Exploitation

### Exploitation Principles
```
✅ Only exploit with permission
✅ Document everything
✅ Don't pivot without approval
✅ Stop if requested
❌ Don't cause damage
❌ Don't access beyond scope
```

### Proof of Concept
```
# Document:
- Steps to reproduce
- Impact assessment
- Evidence (screenshots, logs)
- Remediation suggestions
```

---

## Reporting

### Report Structure
```
1. Executive Summary
2. Methodology
3. Scope
4. Findings
   - Severity
   - Description
   - Impact
   - Steps to reproduce
   - Evidence
   - Remediation
5. Conclusion
6. Appendices
```

### Severity Ratings
| Level | Criteria |
|-------|----------|
| Critical | Immediate threat, data breach |
| High | Serious impact, requires fix |
| Medium | Moderate impact |
| Low | Minor impact |
| Info | Informational |

---

## Best Practices Summary

```
✅ Always get authorization
✅ Document everything
✅ Test systematically
✅ Verify findings manually
✅ Prioritize by risk
✅ Provide actionable recommendations
✅ Follow up on remediation
```

---

**Version**: 1.0.5-20260301-Minggu-1007-WIB  
**Author**: waktuberhenti
