# Plugin Marketplace

Custom extensions and plugins for Burp Suite KnowledgeBase.

## Submit Plugin

### Requirements

- Python/Java/JS extension
- Unit tests included
- Documentation
- Open source license

### Submission Process

```bash
# Package your plugin
zip -r my-plugin.zip plugin/

# Submit via API
curl -X POST https://api.burpkb.com/plugins \
  -H "Authorization: Bearer TOKEN" \
  -F "plugin=@my-plugin.zip" \
  -F "metadata.json"
```

## Featured Plugins

### Authentication Tester

```python
# Auth Tester Plugin
from burp_kb.plugins import BurpExtension

class AuthTester(BurpExtension):
    name = "Authentication Tester"
    
    def register(self, callbacks):
        callbacks.registerHttpListener(self)
        
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if toolFlag == TOOL_PROXY:
            # Test authentication
            self.test_auth(messageInfo)
```

### Param Miner

```python
# Auto-discover hidden parameters
from burp_kb.plugins import IntruderPayloadProcessor

class ParamMiner(IntruderPayloadProcessor):
    payloads = [
        "id", "page", "debug", "test",
        "admin", "user", "view", "edit"
    ]
```

### JSON Web Token Attacker

```python
# JWT Attack Toolkit
class JWTAttacker:
    algorithms = ["none", "HS256", "RS256"]
    weak_keys = ["secret", "key", "password"]
    
    def attack(self, token):
        for alg in self.algorithms:
            for key in self.weak_keys:
                if self.verify(token, alg, key):
                    return f"Exploited with {alg}/{key}"
```

---

## Categories

| Category | Plugins | Popular |
|----------|---------|---------|
| Vulnerability Detection | 45 | AuthBuster, ParamMiner |
| Authentication | 32 | JWT Decoder, SAML Raider |
| API Testing | 28 | OpenAPI Scanner, GraphQL Volley |
| Passive Scanning | 55 | Backslash Powered, HTTP Mock |
| Reporting | 18 | Markdown Report, PDF Export |

---

## Installation

```bash
# From marketplace
burpkb plugin install jwt-attacker

# From file
burpkb plugin install ./my-plugin.jar

# List installed
burpkb plugin list
```
