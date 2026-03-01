"""
Team Features Module for Burp Suite KnowledgeBase Platform
==========================================================

Version: 1.0.0-20260301-Senin-2013-WIB

Features:
- Team management
- Role-based access control
- Shared workspaces
- Team collaboration
- Activity tracking
- Resource sharing
"""

from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum
import uuid


# ============================================
# MODELS
# ============================================

class TeamRole(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"
    VIEWER = "viewer"


class InviteStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "rejected"
    EXPIRED = "expired"


class Team:
    """Team model"""
    
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        owner_id: str,
        is_public: bool = False,
        created_at: Optional[datetime] = None,
        settings: Optional[Dict] = None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.is_public = is_public
        self.created_at = created_at or datetime.now()
        self.settings = settings or {
            "allow_public_sharing": True,
            "require_approval": False,
            "max_members": 10
        }
        self.members: Dict[str, TeamRole] = {}
        self.invites: Dict[str, Dict] = {}
    
    def add_member(self, user_id: str, role: TeamRole):
        """Add member to team"""
        self.members[user_id] = role
    
    def remove_member(self, user_id: str):
        """Remove member from team"""
        if user_id in self.members:
            del self.members[user_id]
    
    def get_members(self) -> List[str]:
        """Get all member IDs"""
        return list(self.members.keys())
    
    def has_permission(self, user_id: str, required_role: TeamRole) -> bool:
        """Check if user has required role"""
        user_role = self.members.get(user_id)
        if not user_role:
            return False
        
        role_hierarchy = {
            TeamRole.OWNER: 4,
            TeamRole.ADMIN: 3,
            TeamRole.MEMBER: 2,
            TeamRole.VIEWER: 1
        }
        
        return role_hierarchy.get(user_role, 0) >= role_hierarchy.get(required_role, 0)
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "owner_id": self.owner_id,
            "is_public": self.is_public,
            "created_at": self.created_at.isoformat(),
            "settings": self.settings,
            "member_count": len(self.members)
        }


class Workspace:
    """Shared workspace model"""
    
    def __init__(
        self,
        id: str,
        team_id: str,
        name: str,
        description: str,
        created_by: str,
        created_at: Optional[datetime] = None,
        is_shared: bool = True
    ):
        self.id = id
        self.team_id = team_id
        self.name = name
        self.description = description
        self.created_by = created_by
        self.created_at = created_at or datetime.now()
        self.is_shared = is_shared
        self.payloads: List[str] = []
        self.configs: List[str] = []
        self.notes: List[Dict] = []
    
    def add_payload(self, payload_id: str):
        """Add payload to workspace"""
        if payload_id not in self.payloads:
            self.payloads.append(payload_id)
    
    def remove_payload(self, payload_id: str):
        """Remove payload from workspace"""
        if payload_id in self.payloads:
            self.payloads.remove(payload_id)
    
    def add_config(self, config_id: str):
        """Add config to workspace"""
        if config_id not in self.configs:
            self.configs.append(config_id)
    
    def add_note(self, content: str, author_id: str) -> Dict:
        """Add note to workspace"""
        note = {
            "id": str(uuid.uuid4()),
            "content": content,
            "author_id": author_id,
            "created_at": datetime.now().isoformat()
        }
        self.notes.append(note)
        return note
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "team_id": self.team_id,
            "name": self.name,
            "description": self.description,
            "created_by": self.created_by,
            "created_at": self.created_at.isoformat(),
            "is_shared": self.is_shared,
            "payload_count": len(self.payloads),
            "config_count": len(self.configs),
            "note_count": len(self.notes)
        }


class TeamActivity:
    """Team activity model"""
    
    def __init__(
        self,
        id: str,
        team_id: str,
        user_id: str,
        action: str,
        resource_type: str,
        resource_id: Optional[str] = None,
        details: Optional[Dict] = None,
        created_at: Optional[datetime] = None
    ):
        self.id = id
        self.team_id = team_id
        self.user_id = user_id
        self.action = action
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.details = details or {}
        self.created_at = created_at or datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "team_id": self.team_id,
            "user_id": self.user_id,
            "action": self.action,
            "resource_type": self.resource_type,
            "resource_id": self.resource_id,
            "details": self.details,
            "created_at": self.created_at.isoformat()
        }


# ============================================
# TEAM DATABASE
# ============================================

class TeamDatabase:
    """In-memory team database"""
    
    def __init__(self):
        self.teams: Dict[str, Team] = {}
        self.workspaces: Dict[str, Workspace] = {}
        self.activities: Dict[str, TeamActivity] = {}
        self.user_teams: Dict[str, List[str]] = {}  # user_id -> [team_ids]
    
    def create_team(
        self,
        name: str,
        description: str,
        owner_id: str,
        is_public: bool = False
    ) -> Team:
        """Create a new team"""
        team = Team(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            owner_id=owner_id,
            is_public=is_public
        )
        team.add_member(owner_id, TeamRole.OWNER)
        
        self.teams[team.id] = team
        
        # Track user-team relationship
        if owner_id not in self.user_teams:
            self.user_teams[owner_id] = []
        self.user_teams[owner_id].append(team.id)
        
        # Log activity
        self._log_activity(team.id, owner_id, "created", "team")
        
        return team
    
    def get_team(self, team_id: str) -> Optional[Team]:
        """Get team by ID"""
        return self.teams.get(team_id)
    
    def get_user_teams(self, user_id: str) -> List[Team]:
        """Get all teams for a user"""
        team_ids = self.user_teams.get(user_id, [])
        return [self.teams[tid] for tid in team_ids if tid in self.teams]
    
    def add_member(
        self,
        team_id: str,
        user_id: str,
        role: TeamRole
    ) -> Optional[Team]:
        """Add member to team"""
        team = self.teams.get(team_id)
        if not team:
            return None
        
        team.add_member(user_id, role)
        
        if user_id not in self.user_teams:
            self.user_teams[user_id] = []
        if team_id not in self.user_teams[user_id]:
            self.user_teams[user_id].append(team_id)
        
        self._log_activity(team_id, user_id, "joined", "team")
        
        return team
    
    def remove_member(self, team_id: str, user_id: str) -> bool:
        """Remove member from team"""
        team = self.teams.get(team_id)
        if not team:
            return False
        
        team.remove_member(user_id)
        
        if user_id in self.user_teams:
            self.user_teams[user_id] = [
                tid for tid in self.user_teams[user_id]
                if tid != team_id
            ]
        
        return True
    
    def create_workspace(
        self,
        team_id: str,
        name: str,
        description: str,
        created_by: str
    ) -> Optional[Workspace]:
        """Create a workspace"""
        team = self.teams.get(team_id)
        if not team:
            return None
        
        workspace = Workspace(
            id=str(uuid.uuid4()),
            team_id=team_id,
            name=name,
            description=description,
            created_by=created_by
        )
        
        self.workspaces[workspace.id] = workspace
        self._log_activity(team_id, created_by, "created", "workspace", workspace.id)
        
        return workspace
    
    def get_workspace(self, workspace_id: str) -> Optional[Workspace]:
        """Get workspace by ID"""
        return self.workspaces.get(workspace_id)
    
    def get_team_workspaces(self, team_id: str) -> List[Workspace]:
        """Get all workspaces for a team"""
        return [w for w in self.workspaces.values() if w.team_id == team_id]
    
    def _log_activity(
        self,
        team_id: str,
        user_id: str,
        action: str,
        resource_type: str,
        resource_id: Optional[str] = None
    ):
        """Log team activity"""
        activity = TeamActivity(
            id=str(uuid.uuid4()),
            team_id=team_id,
            user_id=user_id,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id
        )
        self.activities[activity.id] = activity
    
    def get_team_activity(
        self,
        team_id: str,
        limit: int = 50
    ) -> List[TeamActivity]:
        """Get team activity"""
        activities = [
            a for a in self.activities.values()
            if a.team_id == team_id
        ]
        activities.sort(key=lambda a: a.created_at, reverse=True)
        return activities[:limit]


# ============================================
# TEAM SERVICE
# ============================================

class TeamService:
    """Main team service"""
    
    def __init__(self):
        self.db = TeamDatabase()
    
    def create_team(
        self,
        name: str,
        description: str,
        owner_id: str,
        is_public: bool = False
    ) -> Team:
        """Create a new team"""
        return self.db.create_team(name, description, owner_id, is_public)
    
    def get_team(self, team_id: str) -> Optional[Team]:
        """Get team by ID"""
        return self.db.get_team(team_id)
    
    def get_user_teams(self, user_id: str) -> List[Team]:
        """Get user's teams"""
        return self.db.get_user_teams(user_id)
    
    def add_member(
        self,
        team_id: str,
        user_id: str,
        role: TeamRole
    ) -> Optional[Team]:
        """Add member to team"""
        return self.db.add_member(team_id, user_id, role)
    
    def remove_member(self, team_id: str, user_id: str) -> bool:
        """Remove member from team"""
        return self.db.remove_member(team_id, user_id)
    
    def create_workspace(
        self,
        team_id: str,
        name: str,
        description: str,
        created_by: str
    ) -> Optional[Workspace]:
        """Create a workspace"""
        return self.db.create_workspace(team_id, name, description, created_by)
    
    def get_workspace(self, workspace_id: str) -> Optional[Workspace]:
        """Get workspace"""
        return self.db.get_workspace(workspace_id)
    
    def get_team_workspaces(self, team_id: str) -> List[Workspace]:
        """Get team workspaces"""
        return self.db.get_team_workspaces(team_id)
    
    def add_to_workspace(
        self,
        workspace_id: str,
        payload_id: Optional[str] = None,
        config_id: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Optional[Workspace]:
        """Add resource to workspace"""
        workspace = self.db.get_workspace(workspace_id)
        if not workspace:
            return None
        
        if payload_id:
            workspace.add_payload(payload_id)
        if config_id:
            workspace.add_config(config_id)
        
        if user_id:
            self._log_activity(
                workspace.team_id,
                user_id,
                "added resource to",
                "workspace",
                workspace_id
            )
        
        return workspace
    
    def add_note_to_workspace(
        self,
        workspace_id: str,
        content: str,
        author_id: str
    ) -> Optional[Dict]:
        """Add note to workspace"""
        workspace = self.db.get_workspace(workspace_id)
        if not workspace:
            return None
        
        note = workspace.add_note(content, author_id)
        
        self._log_activity(
            workspace.team_id,
            author_id,
            "added note to",
            "workspace",
            workspace_id
        )
        
        return note
    
    def get_team_activity(self, team_id: str) -> List[TeamActivity]:
        """Get team activity"""
        return self.db.get_team_activity(team_id)
    
    def get_team_stats(self, team_id: str) -> dict:
        """Get team statistics"""
        team = self.db.get_team(team_id)
        if not team:
            return {}
        
        workspaces = self.db.get_team_workspaces(team_id)
        activities = self.db.get_team_activity(team_id)
        
        return {
            "team_id": team_id,
            "team_name": team.name,
            "member_count": len(team.members),
            "workspace_count": len(workspaces),
            "activity_count": len(activities),
            "is_public": team.is_public
        }


# ============================================
# DEMO
# ============================================

if __name__ == "__main__":
    service = TeamService()
    
    # Create team
    team = service.create_team(
        name="Security Team",
        description="Our internal security testing team",
        owner_id="user_1"
    )
    print(f"Created team: {team.name} ({team.id})")
    
    # Add members
    service.add_member(team.id, "user_2", TeamRole.MEMBER)
    service.add_member(team.id, "user_3", TeamRole.VIEWER)
    print(f"Members: {team.get_members()}")
    
    # Create workspace
    workspace = service.create_workspace(
        team_id=team.id,
        name="Project Alpha",
        description="Security testing for Project Alpha",
        created_by="user_1"
    )
    print(f"Created workspace: {workspace.name}")
    
    # Add to workspace
    workspace = service.add_to_workspace(
        workspace_id=workspace.id,
        payload_id="payload_1",
        user_id="user_1"
    )
    print(f"Workspace payloads: {workspace.payloads}")
    
    # Add note
    note = service.add_note_to_workspace(
        workspace_id=workspace.id,
        content="Remember to test for SQL injection in login form",
        author_id="user_2"
    )
    print(f"Added note: {note['id']}")
    
    # Get activity
    activity = service.get_team_activity(team.id)
    print(f"Team activity: {len(activity)} actions")
    
    # Get stats
    stats = service.get_team_stats(team.id)
    print(f"Team stats: {stats}")
