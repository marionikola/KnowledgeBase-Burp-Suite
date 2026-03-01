# Common Issues - Burp Suite

## Daftar Isi

1. [Installation Issues](#installation-issues)
2. [Proxy Issues](#proxy-issues)
3. [Certificate Issues](#certificate-issues)
4. [Performance Issues](#performance-issues)
5. [Scanning Issues](#scanning-issues)
6. [Network Issues](#network-issues)

---

## Installation Issues

### Java Not Found
```bash
# Problem: "Java not found" or "No Java runtime"

# Solutions:
1. Install Java JDK 11+
   - Windows: Download dari Oracle/Adoptium
   - Linux: sudo apt install openjdk-11-jdk
   - Mac: brew install openjdk@11

2. Set JAVA_HOME:
   - Windows: System Properties > Environment Variables
   - Linux/Mac: export JAVA_HOME=/path/to/java
```

### Port Already in Use
```bash
# Problem: "Port 8080 already in use"

# Solutions:
1. Find process using port:
   - Linux: sudo lsof -i :8080
   - Windows: netstat -ano | findstr :8080

2. Kill the process ATAU

3. Change Burp proxy port:
   - Proxy > Options > Proxy Listeners
   - Edit > Change port number
```

### Out of Memory
```bash
# Problem: "Out of memory" atau "Java heap space"

# Solution - Increase heap size:
java -jar -Xmx4096m burpsuite_community.jar

# Permanent fix:
# Edit Burp Suite startup script
# Set: -Xmx4g -XX:MaxMetaspaceSize=1g
```

---

## Proxy Issues

### Traffic Not Being Intercepted
```
# Problem: Browser traffic tidak masuk Burp

# Checklist:
1. ✅ Proxy listener aktif?
   - Proxy > Options > Proxy Listeners

2. ✅ Browser proxy settings benar?
   - HTTP Proxy: 127.0.0.1
   - Port: 8080

3. ✅ CA certificate installed?
   - Install Burp CA di browser

4. ✅ Check "Intercept is on"?
   - Proxy > Intercept > Intercept is on
```

### Infinite Loop / Redirect
```
# Problem: Request terus redirect

# Solutions:
1. Proxy > Options > Uncheck "Follow redirects"
2. Check untuk redirect chains
3. Use "Drop" untuk stop
4. Check Scope exclusions
```

### HTTPS Not Working
```
# Problem: HTTPS sites tidak bisa di-browse

# Solutions:
1. Install CA Certificate:
   - Proxy > Options > Import/Export CA
   - Install di browser trust store

2. Restart browser after install

3. Check certificate:
   - Chrome: DevTools > Security
   - Look for "Certificate valid"
```

---

## Certificate Issues

### Certificate Error in Browser
```
# Problem: "Your connection is not private"

# Solution:
1. Open http://burpsuite (tanpa https)
2. Click "CA Certificate"
3. Download certificate
4. Install to browser:
   - Chrome: Settings > Certificates > Import
   - Firefox: Options > Certificates > Import
5. Trust for SSL/TLS websites
```

### Certificate Not Trusted
```
# Problem: Even after install, still getting errors

# Fix:
1. Remove old certificates first
2. Install to "Trusted Root CA"
3. Restart browser completely
4. Clear browser cache
5. Try incognito mode
```

---

## Performance Issues

### Slow Response Times
```
# Problem: Everything berjalan lambat

# Solutions:
1. Kurangi concurrent connections:
   - Intruder > Options > Threads: 1-5

2. Disable image scanning:
   - Scanner > Options > Don't scan images

3. Clear history periodically:
   - Proxy > HTTP history > Delete old items

4. Use filters:
   - Filter out CSS, images, static files
```

### High Memory Usage
```
# Problem: Burp menggunakan banyak RAM

# Solutions:
1. Kurangi buffer sizes
2. Split projects
3. Clear history reguler
4. Disable auto-save
5. Use smaller wordlists for Intruder
```

---

## Scanning Issues

### Scanner Not Finding Anything
```
# Problem: Scan completes with no issues found

# Solutions:
1. Check scanner is active:
   - Scanner > Options > Active Scanning Enabled

2. Scope sudah benar?
   - Add target ke scope

3. Manual explore first:
   - Spider needs to find URLs

4. Check exclusion patterns:
   - Scanner > Options > Exclusions
```

### Scan Stuck / Frozen
```
# Problem: Scan stuck di satu URL

# Solutions:
1. Pause and resume
2. Cancel and restart
3. Check for timeouts:
   - Scanner > Options > Timeout settings
4. Skip problematic URL
5. Check server status
```

---

## Network Issues

### Connection Timeout
```
# Problem: "Connection timeout" errors

# Solutions:
1. Check target server is online
2. Increase timeout:
   - Settings > Network > Timeouts
3. Check firewall/proxy
4. Try different network
5. UseSSL/TLS settings adjustment
```

### SSL/TLS Errors
```
# Problem: SSL handshake failures

# Solutions:
1. Try different TLS version
2. Disable certificate validation (testing only)
3. Check server TLS support
4. Use nmap untuk check:
   nmap --script ssl-enum-ciphers target.com
```

---

## Quick Troubleshooting Checklist

```
# Always check first:
□ Proxy listener running
□ Browser proxy settings correct
□ CA certificate installed
□ Scope defined
□ Java version correct
□ Enough memory allocated
□ Network connectivity
```

---

## Emergency Fixes

### Complete Reset
```bash
# Jika semua gagal:
1. Close Burp
2. Delete config files:
   - ~/.BurpSuite/user.config
   - ~/.BurpSuite/*state*
3. Restart Burp
4. Reconfigure everything
```

### Factory Reset
```
# Backup first:
1. Export project
2. Save settings
3. Then reset:
   - Delete BurpSuite folder
   - Reinstall if needed
```

---

**Version**: 1.0.3-20260301-Minggu-1001-WIB  
**Author**: waktuberhenti
