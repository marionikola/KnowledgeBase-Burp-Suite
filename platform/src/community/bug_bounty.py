"""
Bug Bounty Integration Module for Burp Suite KnowledgeBase Platform
=============================================================

Version: 1.0.0-20260301-Senin-2011-WIB

Features:
- Bug bounty program integration
- Program management
- Vulnerability reporting
- Reward tracking
- Hall of fame
"""

from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum
import uuid


# ============================================
# MODELS
# ============================================

class BugStatus(str, Enum):
    SUBMITTED = "submitted"
    TRIAGED = "triaged"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    REJECTED = "rejected"
    CLOSED = "closed"


class BugSeverity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class Bug:
    """Bug report model"""
    
    def __init__(
        self,
        id: str,
        program_id: str,
        reporter_id: str,
        title: str,
        description: str,
        severity: BugSeverity,
        status: BugStatus = BugStatus.SUBMITTED,
        reward: Optional[float] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        resolved_at: Optional[datetime] = None
    ):
        self.id = id
        self.program_id = program_id
        self.reporter_id = reporter_id
        self.title = title
        self.description = description
        self.severity = severity
        self.status = status
        self.reward = reward
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.resolved_at = resolved_at
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "program_id": self.program_id,
            "reporter_id": self.reporter_id,
            "title": self.title,
            "description": self.description,
            "severity": self.severity.value,
            "status": self.status.value,
            "reward": self.reward,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "resolved_at": self.resolved_at.isoformat() if self.resolved_at else None
        }


class Program:
    """Bug bounty program model"""
    
    def __init__(
        self,
        id: str,
        name: str,
        organization: str,
        description: str,
        scope: List[str],
        rewards: Dict[str, float],
        is_active: bool = True,
        created_at: Optional[datetime] = None
    ):
        self.id = id
        self.name = name
        self.organization = organization
        self.description = description
        self.scope = scope
        self.rewards = rewards
        self.is_active = is_active
        self.created_at = created_at or datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "organization": self.organization,
            "description": self.description,
            "scope": self.scope,
            "rewards": self.rewards,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat()
        }


class BountyClaim:
    """Bounty claim model"""
    
    def __init__(
        self,
        id: str,
        bug_id: str,
        user_id: str,
        amount: float,
        status: str = "pending",
        created_at: Optional[datetime] = None
    ):
        self.id = id
        self.bug_id = bug_id
        self.user_id = user_id
        self.amount = amount
        self.status = status
        self.created_at = created_at or datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "bug_id": self.bug_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }


# ============================================
# BUG BOUNTY DATABASE
# ============================================

class BugBountyDatabase:
    """In-memory bug bounty database"""
    
    def __init__(self):
        self.programs: Dict[str, Program] = {}
        self.bugs: Dict[str, Bug] = {}
        self.claims: Dict[str, BountyClaim] = {}
        self.hall_of_fame: Dict[str, List[str]] = {}  # program_id -> [user_ids]
        
        # Add sample programs
        self._init_sample_data()
    
    def _init_sample_data(self):
        """Initialize sample data"""
        # Sample program
        program = Program(
            id="prog_1",
            name="Web Security Test",
            organization="Example Corp",
            description="Bug bounty program for Example Corp web applications",
            scope=["*.example.com", "api.example.com"],
            rewards={
                "critical": 5000.0,
                "high": 2000.0,
                "medium": 500.0,
                "low": 100.0,
                "info": 50.0
            }
        )
        self.programs[program.id] = program
    
    def create_program(
        self,
        name: str,
        organization: str,
        description: str,
        scope: List[str],
        rewards: Dict[str, float]
    ) -> Program:
        """Create a bug bounty program"""
        program = Program(
            id=str(uuid.uuid4()),
            name=name,
            organization=organization,
            description=description,
            scope=scope,
            rewards=rewards
        )
        self.programs[program.id] = program
        return program
    
    def get_program(self, program_id: str) -> Optional[Program]:
        """Get program by ID"""
        return self.programs.get(program_id)
    
    def get_active_programs(self) -> List[Program]:
        """Get all active programs"""
        return [p for p in self.programs.values() if p.is_active]
    
    def create_bug_report(
        self,
        program_id: str,
        reporter_id: str,
        title: str,
        description: str,
        severity: BugSeverity
    ) -> Optional[Bug]:
        """Create a bug report"""
        program = self.programs.get(program_id)
        if not program:
            return None
        
        bug = Bug(
            id=str(uuid.uuid4()),
            program_id=program_id,
            reporter_id=reporter_id,
            title=title,
            description=description,
            severity=severity
        )
        self.bugs[bug.id] = bug
        return bug
    
    def get_bug(self, bug_id: str) -> Optional[Bug]:
        """Get bug by ID"""
        return self.bugs.get(bug_id)
    
    def get_bugs_by_program(self, program_id: str) -> List[Bug]:
        """Get all bugs for a program"""
        return [b for b in self.bugs.values() if b.program_id == program_id]
    
    def get_bugs_by_reporter(self, reporter_id: str) -> List[Bug]:
        """Get all bugs reported by a user"""
        return [b for b in self.bugs.values() if b.reporter_id == reporter_id]
    
    def update_bug_status(
        self,
        bug_id: str,
        status: BugStatus,
        reward: Optional[float] = None
    ) -> Optional[Bug]:
        """Update bug status"""
        bug = self.bugs.get(bug_id)
        if not bug:
            return None
        
        bug.status = status
        bug.updated_at = datetime.now()
        
        if reward:
            bug.reward = reward
        
        if status == BugStatus.RESOLVED:
            bug.resolved_at = datetime.now()
            self._add_to_hall_of_fame(bug.program_id, bug.reporter_id)
        
        return bug
    
    def get_program_stats(self, program_id: str) -> dict:
        """Get program statistics"""
        bugs = self.get_bugs_by_program(program_id)
        
        stats = {
            "total_bugs": len(bugs),
            "by_severity": {
                "critical": len([b for b in bugs if b.severity == BugSeverity.CRITICAL]),
                "high": len([b for b in bugs if b.severity == BugSeverity.HIGH]),
                "medium": len([b for b in bugs if b.severity == BugSeverity.MEDIUM]),
                "low": len([b for b in bugs if b.severity == BugSeverity.LOW]),
                "info": len([b for b in bugs if b.severity == BugSeverity.INFO])
            },
            "by_status": {
                "submitted": len([b for b in bugs if b.status == BugStatus.SUBMITTED]),
                "triaged": len([b for b in bugs if b.status == BugStatus.TRIAGED]),
                "in_progress": len([b for b in bugs if b.status == BugStatus.IN_PROGRESS]),
                "resolved": len([b for b in bugs if b.status == BugStatus.RESOLVED]),
                "rejected": len([b for b in bugs if b.status == BugStatus.REJECTED])
            },
            "total_rewards": sum(b.reward or 0 for b in bugs)
        }
        
        return stats
    
    def get_hall_of_fame(self, program_id: str) -> List[dict]:
        """Get hall of fame for a program"""
        bugs = self.get_bugs_by_program(program_id)
        
        # Calculate user stats
        user_stats = {}
        for bug in bugs:
            if bug.status == BugStatus.RESOLVED:
                if bug.reporter_id not in user_stats:
                    user_stats[bug.reporter_id] = {
                        "bugs_found": 0,
                        "total_reward": 0,
                        "severities": []
                    }
                user_stats[bug.reporter_id]["bugs_found"] += 1
                user_stats[bug.reporter_id]["total_reward"] += bug.reward or 0
                user_stats[bug.reporter_id]["severities"].append(bug.severity.value)
        
        # Convert to list and sort
        hall_of_fame = [
            {
                "user_id": user_id,
                "bugs_found": stats["bugs_found"],
                "total_reward": stats["total_reward"],
                "severities": stats["severities"]
            }
            for user_id, stats in user_stats.items()
        ]
        
        hall_of_fame.sort(
            key=lambda x: (x["total_reward"], x["bugs_found"]),
            reverse=True
        )
        
        return hall_of_fame
    
    def _add_to_hall_of_fame(self, program_id: str, user_id: str):
        """Add user to hall of fame"""
        if program_id not in self.hall_of_fame:
            self.hall_of_fame[program_id] = []
        if user_id not in self.hall_of_fame[program_id]:
            self.hall_of_fame[program_id].append(user_id)
    
    def claim_reward(self, bug_id: str, user_id: str) -> Optional[BountyClaim]:
        """Claim bug bounty reward"""
        bug = self.bugs.get(bug_id)
        if not bug or bug.reward is None:
            return None
        
        claim = BountyClaim(
            id=str(uuid.uuid4()),
            bug_id=bug_id,
            user_id=user_id,
            amount=bug.reward
        )
        self.claims[claim.id] = claim
        return claim
    
    def get_user_claims(self, user_id: str) -> List[BountyClaim]:
        """Get all claims for a user"""
        return [c for c in self.claims.values() if c.user_id == user_id]


# ============================================
# BUG BOUNTY SERVICE
# ============================================

class BugBountyService:
    """Main bug bounty service"""
    
    def __init__(self):
        self.db = BugBountyDatabase()
    
    def create_program(
        self,
        name: str,
        organization: str,
        description: str,
        scope: List[str],
        rewards: Dict[str, float]
    ) -> Program:
        """Create a program"""
        return self.db.create_program(name, organization, description, scope, rewards)
    
    def get_programs(self) -> List[Program]:
        """Get all active programs"""
        return self.db.get_active_programs()
    
    def get_program(self, program_id: str) -> Optional[Program]:
        """Get program by ID"""
        return self.db.get_program(program_id)
    
    def submit_bug(
        self,
        program_id: str,
        reporter_id: str,
        title: str,
        description: str,
        severity: BugSeverity
    ) -> Optional[Bug]:
        """Submit a bug report"""
        return self.db.create_bug_report(
            program_id, reporter_id, title, description, severity
        )
    
    def get_bug(self, bug_id: str) -> Optional[Bug]:
        """Get bug by ID"""
        return self.db.get_bug(bug_id)
    
    def update_bug(
        self,
        bug_id: str,
        status: BugStatus,
        reward: Optional[float] = None
    ) -> Optional[Bug]:
        """Update bug status"""
        return self.db.update_bug_status(bug_id, status, reward)
    
    def get_program_bugs(self, program_id: str) -> List[Bug]:
        """Get all bugs for a program"""
        return self.db.get_bugs_by_program(program_id)
    
    def get_program_stats(self, program_id: str) -> dict:
        """Get program statistics"""
        return self.db.get_program_stats(program_id)
    
    def get_hall_of_fame(self, program_id: str) -> List[dict]:
        """Get hall of fame"""
        return self.db.get_hall_of_fame(program_id)
    
    def claim_reward(self, bug_id: str, user_id: str) -> Optional[BountyClaim]:
        """Claim reward"""
        return self.db.claim_reward(bug_id, user_id)
    
    def get_user_stats(self, user_id: str) -> dict:
        """Get user bug bounty stats"""
        bugs = self.db.get_bugs_by_reporter(user_id)
        claims = self.db.get_user_claims(user_id)
        
        resolved = [b for b in bugs if b.status == BugStatus.RESOLVED]
        
        return {
            "total_bugs_reported": len(bugs),
            "bugs_resolved": len(resolved),
            "total_rewards_earned": sum(b.reward or 0 for b in resolved),
            "pending_claims": len([c for c in claims if c.status == "pending"]),
            "severity_breakdown": {
                "critical": len([b for b in bugs if b.severity == BugSeverity.CRITICAL]),
                "high": len([b for b in bugs if b.severity == BugSeverity.HIGH]),
                "medium": len([b for b in bugs if b.severity == BugSeverity.MEDIUM]),
                "low": len([b for b in bugs if b.severity == BugSeverity.LOW])
            }
        }


# ============================================
# DEMO
# ============================================

if __name__ == "__main__":
    service = BugBountyService()
    
    # Get programs
    programs = service.get_programs()
    print(f"Active programs: {len(programs)}")
    
    if programs:
        program = programs[0]
        
        # Submit a bug
        bug = service.submit_bug(
            program_id=program.id,
            reporter_id="hacker_1",
            title="SQL Injection in Login",
            description="Found SQL injection in login form",
            severity=BugSeverity.CRITICAL
        )
        print(f"Submitted bug: {bug.id}")
        
        # Update bug status
        updated = service.update_bug_status(
            bug.id,
            BugStatus.RESOLVED,
            reward=5000.0
        )
        print(f"Bug status: {updated.status.value}, Reward: ${updated.reward}")
        
        # Get stats
        stats = service.get_program_stats(program.id)
        print(f"Program stats: {stats}")
        
        # Hall of fame
        hof = service.get_hall_of_fame(program.id)
        print(f"Hall of Fame: {len(hof)} hunters")
        
        # User stats
        user_stats = service.get_user_stats("hacker_1")
        print(f"User stats: {user_stats}")
