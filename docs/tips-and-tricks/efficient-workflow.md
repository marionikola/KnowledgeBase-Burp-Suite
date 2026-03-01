# Efficient Workflow - Burp Suite

## Daftar Isi

1. [Project Setup](#project-setup)
2. [Scope Management](#scope-management)
3. [Session Handling](#session-handling)
4. [Automation Tips](#automation-tips)
5. [Organization Tips](#organization-tips)
6. [Time-Saving Techniques](#time-saving-techniques)

---

## Project Setup

### Best Practices
```
# Selalu mulai dengan:
1. ✅ Scope yang jelas
2. ✅ Project di-save regularly  
3. ✅ Proxy listener dikonfigurasi
4. ✅ CA certificate di-install
```

### Project Structure
```
# Naming convention
[CLIENT]-[DATE]-[TYPE]
contoh: AcmeCorp_20260301_Pentest.burp
```

### Environment Profiles
```
# Multiple environments
- Dev environment
- Staging environment
- Production (hati-hati!)
```

---

## Scope Management

### Effective Scope Definition
```
# Scope yang baik:
✅ https://app.target.com/*
✅ https://api.target.com/*

# Exclude:
❌ https://app.target.com/logout
❌ https://app.target.com/static/*
❌ https://app.target.com/healthcheck
```

### Scope Workflow
```
1. Define scope SEBELUM mulai
2. Use "Show only in-scope items"
3. Regular scope review
4. Document scope changes
```

---

## Session Handling

### Maintaining Sessions
```python
# Tips:
1. Save session reguler
2. Use "Restore session" jika crash
3. Export cookies untuk reuse
4. Test session timeout
```

### Cookie Handling
```
# Best practices:
- Store cookies properly
- Test session regeneration
- Check for session fixation
- Test concurrent sessions
```

---

## Automation Tips

### Using Macros
```
# Macros untuk:
- Auto login
- Anti-CSRF token handling
- Dynamic parameter handling
```

### Search Patterns
```
# Regex patterns useful:
- \b\d{3}-\d{2}-\d{4}\b (SSN)
- [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,} (Email)
- password|passwd|pwd (Password fields)
```

---

## Organization Tips

### Tab Management
```
# Organize dengan:
- Rename tabs clearly
- Group related requests
- Use color coding
- Close unused tabs
```

### Notes and Comments
```
# Selalu add comments untuk:
- Interesting findings
- False positives
- Follow-up needed
- Client-specific notes
```

### Filtering
```
# Use filters untuk:
- Hide static content
- Show only POST/GET
- Filter by status code
- Show only parameterized
```

---

## Time-Saving Techniques

### Quick Access
1. **Use keyboard shortcuts** - Wajib hukumnya!
2. **Create custom tools** - Untuk repetitive tasks
3. **Use search** - Ctrl+F everywhere
4. **Bookmarks** - Save important URLs

### Templates
```
# Request templates:
- Blank GET request
- Blank POST JSON
- Common headers
- Authentication templates
```

### Common Workflows
```
# Standard pentest workflow:
1. Spider (crawl)
2. Passive scan (monitor)
3. Active scan (audit)
4. Manual testing (Repeater/Intruder)
5. Document findings
```

---

## Performance Tips

### Speed Optimization
```
# Kurangi load:
- Filter HTTP history
- Exclude static files
- Limit concurrent requests
- Use compression
```

### Memory Management
```
# Save memory:
- Close unused tabs
- Clear history periodically
- Export then delete
- Split large projects
```

---

## Collaboration Tips

### Team Workflow
```
# If working in team:
- Share scope documents
- Use consistent naming
- Regular sync meetings
- Centralized reporting
```

### Reporting
```
# Quick reporting:
- Use Burp's report feature
- Export to multiple formats
- Keep evidence organized
- Document immediately
```

---

**Version**: 1.0.3-20260301-Minggu-1001-WIB  
**Author**: waktuberhenti
