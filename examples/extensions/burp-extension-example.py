# Burp Suite Extension Examples
# Version: 1.0.18-20260301-Senin-1812-WIB

# ============================================
# EXAMPLE 1: Custom Header Injector (Python)
# ============================================

from burp import IBurpExtender
from burp import IHttpListener
import re

class BurpExtender(IBurpExtender, IHttpListener):
    
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        # Set extension name
        callbacks.setExtensionName("Custom Header Injector")
        
        # Register HTTP listener
        callbacks.registerHttpListener(self)
        
        print("Custom Header Injector loaded successfully")
    
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # Only process requests
        if not messageIsRequest:
            return
        
        # Get request
        request = messageInfo.getRequest()
        analyzed_request = self._helpers.analyzeRequest(request)
        
        # Get headers
        headers = analyzed_request.getHeaders()
        
        # Add custom header
        new_headers = list(headers)
        new_headers.add("X-Custom-Header: Burp-Extension")
        new_headers.add("X-Scanner: CustomTool")
        
        # Get body
        body_offset = analyzed_request.getBodyOffset()
        body = request[body_offset:]
        
        # Build new request
        new_request = self._helpers.buildHttpMessage(new_headers, body)
        
        # Update request
        messageInfo.setRequest(new_request)

# ============================================
# EXAMPLE 2: SQL Injection Detector (Python)
# ============================================

from burp import IBurpExtender
from burp import IHttpListener
from burp import IScannerListener
import re

class BurpExtender(IBurpExtender, IHttpListener, IScannerListener):
    
    # SQL injection patterns
    SQLI_PATTERNS = [
        r"('|\")(?=.*(union|select|insert|update|delete|drop|create|alter))",
        r"(union|select|insert|update|delete|drop|create|alter).*(from|into|table|database)",
        r"(--|\#|\/\*|\*\/)",
        r"(or|and)\s+\d+=\d+",
        r"'\s+or\s+'1'='1",
        r"'\s+or\s+1=1",
    ]
    
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName("SQLi Detector")
        self._callbacks.registerHttpListener(self)
        self._callbacks.registerScannerListener(self)
        
        print("SQLi Detector loaded")
    
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if not messageIsRequest:
            return
        
        request = messageInfo.getRequest()
        analyzed = self._helpers.analyzeRequest(request)
        body = request[analyzed.getBodyOffset():].tostring()
        
        # Check for SQLi patterns
        for pattern in self.SQLI_PATTERNS:
            if re.search(pattern, body, re.IGNORECASE):
                print("[!] Potential SQLi detected: " + pattern)
                # Add to scanner
                self._callbacks.addScanIssue(
                    CustomScanIssue(
                        messageInfo.getHttpService(),
                        self._helpers.analyzeRequest(messageInfo).getUrl(),
                        [self._callbacks.applyMarkers(messageInfo, None, None)],
                        "SQL Injection Detected",
                        "Possible SQL injection via body parameter",
                        "High"
                    )
                )
                break

# ============================================
# EXAMPLE 3: Passive Scanner (Python)
# ============================================

from burp import IBurpExtender
from burp import IScannerCheck

class BurpExtender(IBurpExtender, IScannerCheck):
    
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName("Passive Scanner")
        self._callbacks.registerScannerCheck(self)
        
        print("Passive Scanner loaded")
    
    def doPassiveScan(self, messageInfo):
        # Analyze response for information disclosure
        response = messageInfo.getResponse()
        analyzed = self._helpers.analyzeResponse(response)
        
        # Check for sensitive data
        if analyzed.getStatusCode() == 200:
            body = response[analyzed.getBodyOffset():].tostring()
            
            # Look for potential secrets
            secrets = ["api_key", "password", "secret", "token", "private_key"]
            
            for secret in secrets:
                if secret in body.lower():
                    return [
                        self._callbacks.applyMarkers(
                            messageInfo, 
                            None, 
                            [analyzed.getBodyOffset() + body.lower().find(secret)]
                        )
                    ]
        return None

# ============================================
# EXAMPLE 4: Intruder Payload Generator (Python)
# ============================================

from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
    
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._callbacks.setExtensionName("Custom Payload Generator")
        self._callbacks.registerIntruderPayloadGeneratorFactory(self)
        
        print("Payload Generator loaded")
    
    def getGeneratorName(self):
        return "Custom Payload Generator"
    
    def createNewInstance(self, attack):
        return CustomPayloadGenerator()

class CustomPayloadGenerator(IIntruderPayloadGenerator):
    def __init__(self):
        self._payloads = [
            "admin",
            "root",
            "test",
            "guest",
            "user",
            "administrator"
        ]
        self._index = 0
    
    def hasMorePayloads(self):
        return self._index < len(self._payloads)
    
    def getNextPayload(self, baseValue):
        payload = self._payloads[self._index]
        self._index += 1
        return payload
    
    def reset(self):
        self._index = 0

# ============================================
# EXAMPLE 5: Custom Logger (Python)
# ============================================

from burp import IBurpExtender
from burp import IHttpListener
from datetime import datetime
import json

class BurpExtender(IBurpExtender, IHttpListener):
    
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName("Request Logger")
        self._callbacks.registerHttpListener(self)
        
        self.log_file = "burp_requests.log"
        print("Request Logger loaded")
    
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        timestamp = datetime.now().isoformat()
        service = messageInfo.getHttpService()
        
        if messageIsRequest:
            request = messageInfo.getRequest()
            analyzed = self._helpers.analyzeRequest(request)
            
            log_entry = {
                "timestamp": timestamp,
                "tool": self._callbacks.getToolName(toolFlag),
                "method": analyzed.getMethod(),
                "url": str(analyzed.getUrl()),
                "host": service.getHost(),
            }
            
            with open(self.log_file, "a") as f:
                f.write(json.dumps(log_entry) + "\n")

# ============================================
# EXAMPLE 6: BApp Store Style Extension
# ============================================

from burp import IBurpExtender
from burp import IContextMenuFactory

from javax.swing import JMenuItem
from java.util import List

class BurpExtender(IBurpExtender, IContextMenuFactory):
    
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName("Context Menu Tool")
        self._callbacks.registerContextMenuFactory(self)
        
        print("Context Menu Tool loaded")
    
    def createMenuItems(self, contextMenuContext):
        menu = []
        
        item = JMenuItem("Send to Custom Tool")
        item.addActionListener(lambda: self.processMenuClick(contextMenuContext))
        menu.append(item)
        
        return menu
    
    def processMenuClick(self, context):
        # Get selected messages
        messages = context.getSelectedMessages()
        
        for message in messages:
            print("Processing: " + str(message.getUrl()))

