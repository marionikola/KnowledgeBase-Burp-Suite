# Certification Program

The Burp Suite KnowledgeBase Certification Program validates your web application security testing skills.

## Certification Tracks

### 1. Burp Suite Associate (BSA)

**Entry-level certification for beginners**

| Aspect | Details |
|--------|---------|
| Duration | 90 minutes |
| Questions | 60 multiple choice |
| Passing Score | 70% |
| Prerequisites | None |
| Price | $199 |

**Topics Covered:**

- Burp Suite fundamentals
- Proxy configuration
- Spider and scanner basics
- Basic vulnerability identification
- Report generation

### 2. Burp Suite Professional (BSP)

**Intermediate certification for practitioners**

| Aspect | Details |
|--------|---------|
| Duration | 3 hours |
| Questions | 80 (multiple choice + practical) |
| Passing Score | 75% |
| Prerequisites | BSA recommended |
| Price | $349 |

**Topics Covered:**

- Advanced proxy usage
- Intruder techniques
- Extension development
- Session handling
- Advanced vulnerability testing
- Automation and scripting

### 3. Burp Suite Expert (BSX)

**Advanced certification for experienced testers**

| Aspect | Details |
|--------|---------|
| Duration | 4 hours |
| Format | Practical hands-on exam |
| Passing Score | 80% |
| Prerequisites | BSP required |
| Price | $599 |

**Topics Covered:**

- Complex attack scenarios
- Custom tool development
- Enterprise security architecture
- Cloud security testing
- Advanced automation
- Team collaboration

### 4. Burp Suite Master (BSM)

**Expert-level certification for security leaders**

| Aspect | Details |
|--------|---------|
| Duration | 2 days |
| Format | Practical + Interview |
| Passing Score | 85% |
| Prerequisites | BSX + 5 years experience |
| Price | $1,299 |

**Topics Covered:**

- Security program development
- Team leadership
- Advanced threat modeling
- Custom security frameworks
- Enterprise integration

---

## Exam Format

### Practical Exam Environment

```
┌─────────────────────────────────────────────┐
│  Exam Environment                           │
├─────────────────────────────────────────────┤
│                                              │
│  🎯 Targets: 3 vulnerable applications      │
│                                              │
│  Target 1: E-commerce platform              │
│  - SQL Injection                            │
│  - XSS vulnerabilities                      │
│  - IDOR issues                              │
│                                              │
│  Target 2: REST API                         │
│  - Authentication bypass                     │
│  - Authorization flaws                       │
│  - Business logic vulnerabilities           │
│                                              │
│  Target 3: Legacy application               │
│  - Multiple critical vulnerabilities         │
│  - Complex attack chains                    │
│                                              │
│  Deliverables:                              │
│  - Vulnerability report                     │
│  - Proof of exploitation                    │
│  - Remediation recommendations              │
│                                              │
└─────────────────────────────────────────────┘
```

### Exam Requirements

1. **Technical Requirements**
   - Stable internet connection
   - Modern browser
   - Burp Suite Professional license

2. **Environment**
   - Private workspace
   - No external resources (except Burp Suite)
   - Screen recording required

---

## Preparation Resources

### Official Training

| Course | Duration | Price | Included |
|--------|----------|-------|----------|
| BSA Prep Course | 20 hours | $299 | ✅ |
| BSP Prep Course | 40 hours | $499 | ✅ |
| BSX Prep Course | 60 hours | $799 | ✅ |
| Bundle (All) | 120 hours | $1,299 | ✅ |

### Study Materials

```python
# Official practice questions
from burp_kb.certification import PracticeExam

exam = PracticeExam(
    certification="BSP",
    question_count=80
)

# Take practice exam
results = exam.take()
print(f"Score: {results.score}%")
print(f"Time: {results.time_taken}")
print(f"Areas to improve: {results.weak_areas}")
```

### Recommended Resources

- Web Security Academy (free)
- OWASP Testing Guide
- PortSwigger Burp Suite Documentation
- SecurityTube courses

---

## Benefits

### Career Advancement

| Benefit | Description |
|---------|-------------|
| Industry Recognition | Globally recognized certification |
| Higher Salary | 15-25% salary increase |
| Job Priority | Featured in job listings |
| Freelance Rates | Higher hourly rates |

### Perks

| Level | Digital Badge | Logo Usage | Directory Listing |
|-------|--------------|------------|-------------------|
| BSA | ✅ | ❌ | ❌ |
| BSP | ✅ | ✅ | ✅ |
| BSX | ✅ | ✅ | ✅ + Featured |
| BSM | ✅ | ✅ | ✅ + VIP |

---

## Exam Scheduling

### Book Your Exam

```python
# Schedule exam via API
from burp_kb.certification import ExamScheduler

scheduler = ExamScheduler(api_key="YOUR_API_KEY")

# Get available slots
slots = scheduler.get_slots(
    certification="BSP",
    timezone="UTC"
)

# Book slot
booking = scheduler.book(
    slot_id="slot_abc123",
    candidate_id="candidate_xyz"
)
```

### Cancellation Policy

| Time Before Exam | Refund |
|------------------|--------|
| 7+ days | 100% |
| 3-7 days | 50% |
| < 3 days | 0% |

---

## Renewal

### Continuing Education

| Certification | Validity | CEU Required |
|---------------|----------|--------------|
| BSA | 3 years | 30 CEUs |
| BSP | 3 years | 45 CEUs |
| BSX | 3 years | 60 CEUs |
| BSM | 3 years | 90 CEUs |

### Earn CEUs

| Activity | CEUs |
|----------|------|
| Complete training course | 10-20 |
| Pass practice exam | 5 |
| Present at conference | 15 |
| Publish article | 10 |
| Mentor candidate | 10 |
| Bug bounty (critical) | 5 |

---

## Success Stories

> "The BSP certification helped me land my dream job as a senior penetration tester. The practical exam really tested my real-world skills." - **Sarah K., Security Analyst**

> "As a team lead, requiring BSX certification for our security team has significantly improved our testing quality." - **Mike T., CISO**

---

## FAQ

### Common Questions

**Q: Can I retake the exam?**
A: Yes, you can retake after 30 days. Maximum 3 attempts per year.

**Q: Is the exam proctored?**
A: Yes, all exams are proctored via webcam and screen recording.

**Q: What if I need accommodations?**
A: Contact our support team for accommodation requests.

**Q: How long does it take to get results?**
A: Results are typically available within 5 business days.

---

## Contact

- Email: certification@burpkb.com
- Support: https://support.burpkb.com/certification
- Directory: https://directory.burpkb.com
