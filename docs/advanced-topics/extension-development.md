# Extension Development - Burp Suite

## Daftar Isi

1. [Apa itu Burp Extensions?](#apa-itu-burp-extensions)
2. [Persiapan Development](#persiapan-development)
3. [Python Extension Contoh](#python-extension-contoh)
4. [Java Extension Contoh](#java-extension-contoh)
5. [API Reference](#api-reference)
6. [Best Practices](#best-practices)

---

## Apa itu Burp Extensions?

Burp Extensions adalah custom plugins untuk menambah fungsionalitas Burp Suite:

### Jenis Extension
| Type | Language | Use Case |
|------|----------|----------|
| Passive | Python/Java | Analyze traffic |
| Active | Python/Java | Modify requests |
| Scanner | Python/Java | Custom checks |
| Intruder | Python/Java | Custom payloads |

### Keuntungan
- Otomasi tugas repetitive
- Custom vulnerability detection
- Integrasi dengan tools lain
- Custom reporting

---

## Persiapan Development

### Install Jython (for Python)
```bash
# Download Jython:
# https://www.jython.org/download

# Atau via pip:
pip install jython

# Configure di Burp:
# Extender > Options > Python Environment > Select Jython JAR
```

### IDE Recommendations
```
# VS Code:
- Extension: Burp extension support
- Python IntelliSense

# IntelliJ/Eclipse:
- Project setup untuk Java extensions
```

---

## Python Extension Contoh

### Basic Extension Structure
```python
from burp import IBurpExtender
from burp import IProxyListener
from java.io import PrintWriter

class BurpExtender(IBurpExtender, IProxyListener):
    
    def registerExtenderCallbacks(self, callbacks):
        # Setup
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        # Set extension name
        callbacks.setExtensionName("My Custom Extension")
        
        # Register proxy listener
        callbacks.registerProxyListener(self)
        
        # Get stdout
        self.stdout = PrintWriter(System.out, True)
        
        self.stdout.println("Extension loaded!")
    
    def processProxyMessage(self, messageIsRequest, message):
        if messageIsRequest:
            # Process request
            request = message.getMessageInfo()
            self.stdout.println("Request: " + str(request))
```

### Passive Scanner Extension
```python
from burp import IBurpExtender, IScannerCheck

class CustomScanner(IBurpExtender, IScannerCheck):
    
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("Custom Vulnerability Scanner")
        callbacks.registerScannerCheck(self)
    
    def doPassiveScan(self, baseRequestResponse):
        # Analyze request/response
        # Return issue if found
        return None  # or custom issue
```

---

## Java Extension Contoh

### Basic Maven Dependency
```xml
<dependencies>
    <dependency>
        <groupId>net.portswigger.burp</groupId>
        <artifactId>burp-extender</artifactId>
        <version>2.1</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

### Basic Java Class
```java
package mypackage;

import burp.IBurpExtender;
import burp.IBurpExtenderCallbacks;
import burp.IHttpRequestResponse;
import java.io.PrintWriter;

public class BurpExtender implements IBurpExtender {
    
    private PrintWriter stdout;
    private IBurpExtenderCallbacks callbacks;
    
    @Override
    public void registerExtenderCallbacks(IBurpExtenderCallbacks callbacks) {
        this.callbacks = callbacks;
        this.stdout = new PrintWriter(callbacks.getStdout(), true);
        
        callbacks.setExtensionName("My Java Extension");
        stdout.println("Java Extension loaded!");
    }
}
```

---

## API Reference

### Interface Utama
| Interface | Fungsi |
|-----------|--------|
| IBurpExtender | Main extension point |
| IHttpListener | HTTP traffic analysis |
| IProxyListener | Proxy event handling |
| IScannerListener | Scanner events |
| ITab | Custom UI tabs |
| IMessageEditor | Custom message editors |

### Commonly Used Methods
```python
# Helpers
helpers = callbacks.getHelpers()
requestInfo = helpers.analyzeRequest(request)
responseInfo = helpers.analyzeResponse(response)

# Build responses
newRequest = helpers.buildRequest(params)
newResponse = helpers.buildResponse(body)

# Utilities
callbacks.addScanIssue(issue)
callbacks.printOutput(message)
callbacks.saveToFile(name, data)
```

---

## Best Practices

### Development Tips
```
✅ Start simple - Basic first
✅ Use logging - Debug lebih mudah
✅ Handle errors - Don't crash Burp
✅ Test incrementally - Build pelan-pelan
✅ Document code - Untuk maintainability

❌ Don't block main thread
❌ Don't use too much memory
❌ Don't create infinite loops
❌ Don't crash Burp
```

### Performance
```
# Optimization:
- Process asynchronously
- Use threading carefully
- Cache frequently used data
- Limit memory usage
- Clean up resources
```

### Testing
```
# Test on:
- Simple requests
- Edge cases
- Large responses
- Binary data
- Malformed input
```

---

## Useful Extensions (Examples)

### Opensource to Learn From
1. **BurpFuzz** - Fuzzing framework
2. **JSON Beautifier** - Format JSON
3. **Request Highlighter** - Color coding
4. **Active Scan++** - Enhanced scanning
5. **Logger++** - Enhanced logging

---

## Distribution

### Loading Extension
```
# Extender > Add
# Extension type: Python / Java
# Select file
# Click Next
```

### Exporting
```
# Save as .jar (Java)
# Save as .py (Python)
```

---

**Version**: 1.0.4-20260301-Minggu-1003-WIB  
**Catatan**: Extension development memerlukan Burp Suite Professional  
**Author**: waktuberhenti
