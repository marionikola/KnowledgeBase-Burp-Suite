# Security Testing Training Curriculum

## Beginner Path (4 weeks)

### Week 1: Fundamentals

| Day | Topic | Duration |
|-----|-------|----------|
| 1 | Introduction to Web Security | 2 hours |
| 2 | Burp Suite Installation & Setup | 2 hours |
| 3 | Proxy Configuration | 2 hours |
| 4 | Understanding HTTP/HTTPS | 2 hours |
| 5 | Spider & Crawling | 2 hours |
| 6 | Practice: Basic Reconnaissance | 3 hours |
| 7 | **Quiz & Review** | 1 hour |

### Week 2: Basic Vulnerabilities

| Day | Topic | Duration |
|-----|-------|----------|
| 1 | SQL Injection Theory | 2 hours |
| 2 | SQL Injection - Hands-on | 2 hours |
| 3 | Cross-Site Scripting (XSS) | 2 hours |
| 4 | XSS - Hands-on Lab | 2 hours |
| 5 | CSRF Fundamentals | 2 hours |
| 6 | Practice: Find Vulnerabilities | 3 hours |
| 7 | **Quiz & Review** | 1 hour |

### Week 3: Intermediate Topics

| Day | Topic | Duration |
|-----|-------|----------|
| 1 | Authentication Testing | 2 hours |
| 2 | Session Management | 2 hours |
| 3 | IDOR Vulnerabilities | 2 hours |
| 4 | File Inclusion | 2 hours |
| 5 | SSRF Attacks | 2 hours |
| 6 | Practice: Full Assessment | 3 hours |
| 7 | **Quiz & Review** | 1 hour |

### Week 4: Tools & Automation

| Day | Topic | Duration |
|-----|-------|----------|
| 1 | Burp Scanner Basics | 2 hours |
| 2 | Intruder & Repeater | 2 hours |
| 3 | Extension Ecosystem | 2 hours |
| 4 | Reporting Fundamentals | 2 hours |
| 5 | Professional Workflow | 2 hours |
| 6 | Practice: Complete Assessment | 3 hours |
| 7 | **Final Exam** | 2 hours |

---

## Intermediate Path (6 weeks)

### Week 1-2: Advanced SQL Injection

- Time-based blind injection
- Boolean-based injection
- Error-based injection
- UNION-based injection
- Second-order injection
- WAF bypass techniques

### Week 3-4: Advanced XSS

- DOM-based XSS
- Stored XSS
- Reflected XSS
- CSP bypass
- Mutation XSS
- Advanced payloads

### Week 5-6: API Security

- REST API testing
- GraphQL security
- WebSocket testing
- gRPC security
- OAuth/OIDC testing

---

## Advanced Path (8 weeks)

### Week 1-2: Business Logic

- Race conditions
- Workflow bypasses
- Logic flaws
- Payment vulnerabilities

### Week 3-4: Advanced Attacks

- Deserialization attacks
- XXE exploitation
- SSRF deep dive
- LDAP injection

### Week 5-6: Cloud Security

- AWS security testing
- Azure security testing
- GCP security testing
- Cloud metadata attacks

### Week 7-8: Red Team Ops

- Attack chain development
- Persistence techniques
- Privilege escalation
- Lateral movement

---

## Certification Prep

### Burp Suite Associate (BSA)

| Topic | Weight |
|-------|--------|
| Basic Concepts | 20% |
| Proxy & Spider | 25% |
| Scanner | 20% |
| Basic Vulnerabilities | 25% |
| Reporting | 10% |

### Burp Suite Professional (BSP)

| Topic | Weight |
|-------|--------|
| Advanced Tools | 20% |
| Complex Vulnerabilities | 30% |
| Automation | 20% |
| Extensions | 15% |
| Methodology | 15% |

---

## Hands-on Labs

### Lab Environment Setup

```bash
# Using Docker
docker run -d -p 80:80 -p 443:443 \
  --name vuln-app \
  vulnerable/webapp:latest

# Access DVWA
http://localhost
```

### Practice Platforms

| Platform | URL | Focus |
|----------|-----|-------|
| DVWA | http://dvwa.co.uk | Basic vulnerabilities |
| OWASP WebGoat | webgoat.org | Structured learning |
| PortSwigger Lab | portsweiger.com/web-security | Professional |
| HackTheBox | hackthebox.eu | CTF style |

---

## Assessment Criteria

### Beginner

- [ ] Understand HTTP protocol
- [ ] Configure Burp Suite proxy
- [ ] Identify basic XSS
- [ ] Identify basic SQLi
- [ ] Create basic report

### Intermediate

- [ ] Test REST APIs
- [ ] Bypass simple WAFs
- [ ] Exploit blind vulnerabilities
- [ ] Use extensions effectively
- [ ] Full penetration test

### Advanced

- [ ] Complex attack chains
- [ ] Cloud security assessment
- [ ] Custom tool development
- [ ] Team collaboration
- [ ] Executive reporting
