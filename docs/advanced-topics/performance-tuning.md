# Performance Tuning - Burp Suite

## Daftar Isi

1. [Memory Optimization](#memory-optimization)
2. [Network Settings](#network-settings)
3. [Scanner Performance](#scanner-performance)
4. [Intruder Optimization](#intruder-optimization)
5. [Proxy Performance](#proxy-performance)

---

## Memory Optimization

### JVM Settings
```bash
# Recommended settings for 8GB RAM
-Xmx4g                # Max heap size
-XX:MaxMetaspaceSize=512m  # Metaspace
-XX:+UseG1GC         # Garbage collector
-XX:ParallelGCThreads=4     # GC threads
```

### Startup Configuration
```bash
# Create startup script
java -Xmx4g -XX:MaxMetaspaceSize=512m \
     -XX:+UseG1GC \
     -jar burpsuite_pro.jar
```

### Memory Tips
```
✅ Allocate 50-75% of available RAM
✅ Close unused tabs
✅ Split large projects
✅ Export and delete old data
✅ Restart Burp regularly
```

---

## Network Settings

### Connection Settings
```
# Settings > Network
- Timeout: 30 seconds
- Follow redirects: On-site only
- Enable HTTP/1.1: ✓
- Enable HTTP/2: ✓
```

### Proxy Settings
```
- Threads: 10-20
- SOCKS proxy: If needed
- Upstream proxy: For routing
```

---

## Scanner Performance

### Speed Options
| Setting | Speed | Accuracy |
|---------|-------|----------|
| Quick | Fastest | Lower |
| Normal | Balanced | Good |
| Thorough | Slow | Highest |

### Optimization Tips
```
# Scanner > Options:
- Concurrent requests: 5-10
- Retries: 2-3
- Delay between requests: 0-100ms

# Exclude:
- Static files (images, CSS)
- Large files
- APIs returning large data
```

### Crawl Optimization
```
# Spider settings:
- Max depth: 10
- Max drill depth: 5
- Max requests: Unlimited
- Parse HTML: ✓
- Parse JavaScript: ✓
```

---

## Intruder Optimization

### Thread Management
```
# Don't overload:
- Web apps: 5-10 threads
- APIs: 10-20 threads
- Heavy servers: 1-3 threads
```

### Throttling
```python
# Add delays:
- Network: 10-50ms
- Authentication: 100-500ms
- Rate limited: 1000ms+
```

### Resource Usage
```
# Reduce memory:
- Clear results regularly
- Export and delete
- Use simple payloads
```

---

## Proxy Performance

### History Management
```
# Settings:
- Store up to: 10,000 items
- Maximum size: 50MB
- Auto-cleanup: Enabled

# Tips:
- Filter aggressively
- Clear old items
- Export periodically
```

### SSL Performance
```
# For HTTPS:
- Enable HTTP/2
- Keep-alive: ✓
- Compression: ✓
```

---

## Best Practices

### Daily Optimization
```
✅ Clear proxy history weekly
✅ Save and restart daily
✅ Split large projects
✅ Use filters always
✅ Monitor memory usage
```

### Troubleshooting Slow Performance
```
❌ High memory: Increase -Xmx
❌ Slow scans: Reduce threads
❌ Timeouts: Check network
❌ Freezes: Restart Burp
❌ Crashes: Check Java version
```

---

**Version**: 1.0.10-20260301-Minggu-1042-WIB  
**Author**: waktuberhenti
