#!/usr/bin/env python3
"""
Burp Suite KnowledgeBase Python SDK
Official client library for programmatic access
"""

import requests
import json
from typing import List, Dict, Optional
from dataclasses import dataclass

BASE_URL = "https://api.burpkb.com/v1"

@dataclass
class Vulnerability:
    id: str
    title: str
    severity: str
    url: str
    description: str
    status: str

@dataclass  
class Scan:
    id: str
    target: str
    status: str
    progress: int

class BurpKBClient:
    """Main client for Burp KB API"""
    
    def __init__(self, api_key: str, base_url: str = BASE_URL):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    # ========== Payloads ==========
    
    def list_payloads(self, category: str = None, limit: int = 20) -> List[Dict]:
        """List available payloads"""
        params = {"per_page": limit}
        if category:
            params["category"] = category
        return self._get("/payloads", params)
    
    def create_payload(self, name: str, category: str, 
                      payload: str, severity: str) -> Dict:
        """Create new payload"""
        data = {
            "name": name,
            "category": category,
            "payload": payload,
            "severity": severity
        }
        return self._post("/payloads", data)
    
    def search_payloads(self, query: str) -> List[Dict]:
        """Search payloads"""
        return self._get("/payloads/search", {"q": query})
    
    # ========== Scans ==========
    
    def create_scan(self, target: str, scan_type: str = "quick") -> Scan:
        """Start a new scan"""
        data = {"target": target, "scan_type": scan_type}
        result = self._post("/scans", data)
        return Scan(**result)
    
    def get_scan(self, scan_id: str) -> Scan:
        """Get scan status"""
        result = self._get(f"/scans/{scan_id}")
        return Scan(**result)
    
    def list_findings(self, scan_id: str) -> List[Vulnerability]:
        """List scan findings"""
        results = self._get(f"/scans/{scan_id}/results")
        return [Vulnerability(**r) for r in results]
    
    # ========== Reports ==========
    
    def create_report(self, scan_id: str, format: str = "pdf") -> Dict:
        """Generate report"""
        data = {"scan_id": scan_id, "format": format}
        return self._post("/reports", data)
    
    def download_report(self, report_id: str, filename: str) -> bytes:
        """Download report"""
        url = f"{self.base_url}/reports/{report_id}/download"
        response = self.session.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename
    
    # ========== Teams ==========
    
    def list_team_members(self, team_id: str) -> List[Dict]:
        """List team members"""
        return self._get(f"/teams/{team_id}/members")
    
    def invite_member(self, team_id: str, email: str, role: str) -> Dict:
        """Invite team member"""
        data = {"email": email, "role": role}
        return self._post(f"/teams/{team_id}/members", data)
    
    # ========== Webhooks ==========
    
    def create_webhook(self, url: str, events: List[str], 
                       secret: str = None) -> Dict:
        """Create webhook"""
        data = {"url": url, "events": events}
        if secret:
            data["secret"] = secret
        return self._post("/webhooks", data)
    
    # ========== Helper Methods ==========
    
    def _get(self, endpoint: str, params: Dict = None) -> any:
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json().get("data", response.json())
    
    def _post(self, endpoint: str, data: Dict) -> any:
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json().get("data", response.json())
    
    def _put(self, endpoint: str, data: Dict) -> any:
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=data)
        response.raise_for_status()
        return response.json().get("data", response.json())
    
    def _delete(self, endpoint: str) -> bool:
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url)
        response.raise_for_status()
        return response.status_code == 204


# ========== Example Usage ==========

def main():
    # Initialize client
    client = BurpKBClient(api_key="YOUR_API_KEY")
    
    # List payloads
    payloads = client.list_payloads(category="sqli", limit=10)
    print(f"Found {len(payloads)} SQLi payloads")
    
    # Start scan
    scan = client.create_scan("https://example.com", "full")
    print(f"Scan started: {scan.id}")
    
    # Wait for completion
    import time
    while scan.status != "completed":
        time.sleep(30)
        scan = client.get_scan(scan.id)
        print(f"Progress: {scan.progress}%")
    
    # Get findings
    findings = client.list_findings(scan.id)
    print(f"Found {len(findings)} vulnerabilities")
    
    # Generate report
    report = client.create_report(scan.id, "pdf")
    client.download_report(report["id"], "report.pdf")
    print("Report saved!")


if __name__ == "__main__":
    main()
