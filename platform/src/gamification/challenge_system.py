"""
Gamification System
==================

Security Challenge Arena, Points, Badges, and Leaderboard System

Version: 1.0.0-20260301-Senin-2002-WIB
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict
from datetime import datetime, timedelta
from enum import Enum
import uuid


class BadgeType(Enum):
    """Available badge types"""
    # Skill badges
    SQLI_EXPERT = "sqli_expert"
    XSS_HUNTER = "xss_hunter"
    COMMAND_MASTER = "command_master"
    SSRF_SPECIALIST = "ssrf_specialist"
    XXE_NINJA = "xxe_ninja"
    
    # Achievement badges
    FIRST_BLOOD = "first_blood"
    PERFECT_RUN = "perfect_run"
    STREAK_MASTER = "streak_master"
    SPEED_DEMON = "speed_demon"
    CONSISTENCY_KING = "consistency_king"
    
    # Special badges
    COMMUNITY_HELPER = "community_helper"
    PAYLOAD_CONTRIBUTOR = "payload_contributor"
    MENTOR = "mentor"


class ChallengeDifficulty(Enum):
    """Challenge difficulty levels"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"
    MASTER = "master"


class ChallengeCategory(Enum):
    """Challenge categories"""
    SQL_INJECTION = "sql_injection"
    XSS = "xss"
    COMMAND_INJECTION = "command_injection"
    SSRF = "ssrf"
    XXE = "xxe"
    AUTH_BYPASS = "auth_bypass"
    IDOR = "idor"
    CSRF = "csrf"
    BUSINESS_LOGIC = "business_logic"


@dataclass
class Badge:
    """Badge definition"""
    id: str
    name: str
    description: str
    badge_type: BadgeType
    icon: str
    points: int
    rarity: str  # common, rare, epic, legendary
    requirements: Dict = field(default_factory=dict)


@dataclass
class Challenge:
    """Security challenge"""
    id: str
    title: str
    description: str
    category: ChallengeCategory
    difficulty: ChallengeDifficulty
    points: int
    time_limit: int  # minutes
    hints: List[str] = field(default_factory=list)
    solution: Optional[str] = None
    flags: List[str] = field(default_factory=list)
    environment_url: Optional[str] = None


@dataclass
class User:
    """User profile"""
    id: str
    username: str
    email: str
    xp: int = 0
    level: int = 1
    badges: List[str] = field(default_factory=list)
    challenges_completed: List[str] = field(default_factory=list)
    points: int = 0
    streak: int = 0
    longest_streak: int = 0
    rank: str = "Bronze"
    created_at: datetime = field(default_factory=datetime.now)
    last_active: datetime = field(default_factory=datetime.now)


@dataclass
class ChallengeResult:
    """Challenge completion result"""
    user_id: str
    challenge_id: str
    completed: bool
    points_earned: int
    time_taken: int  # seconds
    hints_used: int = 0
    attempts: int = 1


class PointsSystem:
    """Points calculation system"""
    
    BASE_POINTS = {
        ChallengeDifficulty.BEGINNER: 50,
        ChallengeDifficulty.INTERMEDIATE: 100,
        ChallengeDifficulty.ADVANCED: 200,
        ChallengeDifficulty.EXPERT: 350,
        ChallengeDifficulty.MASTER: 500,
    }
    
    MULTIPLIERS = {
        "first_attempt": 1.5,
        "no_hints": 1.25,
        "speed_bonus": 1.1,
        "streak_bonus": 0.1,  # per streak day
    }
    
    @classmethod
    def calculate_points(
        cls,
        difficulty: ChallengeDifficulty,
        hints_used: int,
        time_taken: int,
        time_limit: int,
        streak_days: int
    ) -> int:
        """Calculate points for a challenge"""
        
        base = cls.BASE_POINTS[difficulty]
        
        # Hint penalty
        hint_penalty = 0.9 ** hints_used
        
        # Speed bonus (if completed in less than 50% of time)
        if time_taken < time_limit * 0.5:
            speed_multiplier = cls.MULTIPLIERS["speed_bonus"]
        else:
            speed_multiplier = 1.0
        
        # Streak bonus
        streak_multiplier = 1 + (streak_days * cls.MULTIPLIERS["streak_bonus"])
        
        # Calculate final
        points = int(
            base 
            * hint_penalty 
            * speed_multiplier 
            * streak_multiplier
        )
        
        return max(points, 10)  # Minimum 10 points


class LevelSystem:
    """Level progression system"""
    
    XP_PER_LEVEL = 500
    LEVEL_MULTIPLIER = 1.2
    
    @classmethod
    def calculate_level(cls, xp: int) -> int:
        """Calculate level from XP"""
        level = 1
        required_xp = cls.XP_PER_LEVEL
        
        while xp >= required_xp:
            xp -= required_xp
            level += 1
            required_xp = int(required_xp * cls.LEVEL_MULTIPLIER)
        
        return level
    
    @classmethod
    def get_rank(cls, level: int) -> str:
        """Get rank title from level"""
        if level < 5:
            return "Bronze"
        elif level < 10:
            return "Silver"
        elif level < 20:
            return "Gold"
        elif level < 30:
            return "Platinum"
        elif level < 50:
            return "Diamond"
        else:
            return "Master"


class BadgeSystem:
    """Badge management system"""
    
    BADGES = {
        BadgeType.SQLI_EXPERT: Badge(
            id="sqli_expert",
            name="SQL Injection Expert",
            description="Complete 50 SQL injection challenges",
            badge_type=BadgeType.SQLI_EXPERT,
            icon="🗄️",
            points=500,
            rarity="epic",
            requirements={"category": "sql_injection", "count": 50}
        ),
        BadgeType.XSS_HUNTER: Badge(
            id="xss_hunter",
            name="XSS Hunter",
            description="Complete 50 XSS challenges",
            badge_type=BadgeType.XSS_HUNTER,
            icon="🔴",
            points=500,
            rarity="epic",
            requirements={"category": "xss", "count": 50}
        ),
        BadgeType.FIRST_BLOOD: Badge(
            id="first_blood",
            name="First Blood",
            description="Complete your first challenge",
            badge_type=BadgeType.FIRST_BLOOD,
            icon="🩸",
            points=100,
            rarity="rare",
            requirements={"count": 1}
        ),
        BadgeType.PERFECT_RUN: Badge(
            id="perfect_run",
            name="Perfect Run",
            description="Complete 10 challenges without hints",
            badge_type=BadgeType.PERFECT_RUN,
            icon="💎",
            points=300,
            rarity="epic",
            requirements={"hints": 0, "count": 10}
        ),
        BadgeType.STREAK_MASTER: Badge(
            id="streak_master",
            name="Streak Master",
            description="Maintain a 30-day streak",
            badge_type=BadgeType.STREAK_MASTER,
            icon="🔥",
            points=1000,
            rarity="legendary",
            requirements={"streak": 30}
        ),
        BadgeType.COMMUNITY_HELPER: Badge(
            id="community_helper",
            name="Community Helper",
            description="Help 50 other users in the forum",
            badge_type=BadgeType.COMMUNITY_HELPER,
            icon="🤝",
            points=750,
            rarity="legendary",
            requirements={"helped_users": 50}
        ),
    }
    
    @classmethod
    def check_badges(cls, user: User, stats: Dict) -> List[Badge]:
        """Check and award badges based on user stats"""
        awarded = []
        
        for badge in cls.BADGES.values():
            if badge.id in user.badges:
                continue
            
            # Check requirements
            requirements = badge.requirements
            
            if "count" in requirements:
                if stats.get("total_completed", 0) >= requirements["count"]:
                    awarded.append(badge)
            
            if "category" in requirements:
                category = requirements["category"]
                if stats.get(f"{category}_completed", 0) >= requirements["count"]:
                    awarded.append(badge)
            
            if "streak" in requirements:
                if user.streak >= requirements["streak"]:
                    awarded.append(badge)
            
            if "hints" in requirements:
                if stats.get("hints_used", 0) == 0 and stats.get("total_completed", 0) >= requirements["count"]:
                    awarded.append(badge)
        
        return awarded


class Leaderboard:
    """Leaderboard management"""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
    
    def add_user(self, user: User):
        """Add user to leaderboard"""
        self.users[user.id] = user
    
    def get_top(self, limit: int = 10) -> List[User]:
        """Get top users by points"""
        sorted_users = sorted(
            self.users.values(),
            key=lambda u: u.points,
            reverse=True
        )
        return sorted_users[:limit]
    
    def get_rank(self, user_id: str) -> int:
        """Get user rank"""
        sorted_users = sorted(
            self.users.values(),
            key=lambda u: u.points,
            reverse=True
        )
        
        for i, user in enumerate(sorted_users):
            if user.id == user_id:
                return i + 1
        
        return -1
    
    def update_user(self, result: ChallengeResult):
        """Update user stats after challenge"""
        if result.user_id not in self.users:
            return
        
        user = self.users[result.user_id]
        
        # Add points
        user.points += result.points_earned
        user.xp += result.points_earned
        
        # Update level
        new_level = LevelSystem.calculate_level(user.xp)
        if new_level > user.level:
            user.level = new_level
            user.rank = LevelSystem.get_rank(new_level)
        
        # Update streak
        if result.completed:
            user.streak += 1
            if user.streak > user.longest_streak:
                user.longest_streak = user.streak
        
        user.last_active = datetime.now()


# Pre-defined challenges
DEFAULT_CHALLENGES = [
    Challenge(
        id="sqli-001",
        title="Basic SQL Injection",
        description="Find the vulnerability in the login form",
        category=ChallengeCategory.SQL_INJECTION,
        difficulty=ChallengeDifficulty.BEGINNER,
        points=50,
        time_limit=30,
        hints=["Try using OR in the username field"],
        flags=["FLAG{sql1_b4s1c}"]
    ),
    Challenge(
        id="xss-001",
        title="Reflected XSS",
        description="Execute JavaScript in the search parameter",
        category=ChallengeCategory.XSS,
        difficulty=ChallengeDifficulty.BEGINNER,
        points=50,
        time_limit=30,
        hints=["Try <script> tag"],
        flags=["FLAG{xss_r3fl3ct3d}"]
    ),
    Challenge(
        id="sqli-002",
        title="Union-based SQL Injection",
        description="Extract admin password using UNION",
        category=ChallengeCategory.SQL_INJECTION,
        difficulty=ChallengeDifficulty.INTERMEDIATE,
        points=100,
        time_limit=45,
        hints=["Use ORDER BY to find column count"],
        flags=["FLAG{sql1_un10n}"]
    ),
    Challenge(
        id="auth-001",
        title="Authentication Bypass",
        description="Bypass the admin login",
        category=ChallengeCategory.AUTH_BYPASS,
        difficulty=ChallengeDifficulty.INTERMEDIATE,
        points=100,
        time_limit=45,
        hints=["Check for default credentials"],
        flags=["FLAG{4uth_byp4ss}"]
    ),
    Challenge(
        id="idor-001",
        title="IDOR Vulnerability",
        description="Access another user's profile",
        category=ChallengeCategory.IDOR,
        difficulty=ChallengeDifficulty.ADVANCED,
        points=200,
        time_limit=60,
        hints=["Try changing the ID parameter"],
        flags=["FLAG{1d0r_4cc3ss}"]
    ),
]


# Example usage
if __name__ == "__main__":
    # Create leaderboard
    lb = Leaderboard()
    
    # Create users
    user1 = User(
        id=str(uuid.uuid4()),
        username="hacker_pro",
        email="hacker@example.com"
    )
    
    user2 = User(
        id=str(uuid.uuid4()),
        username="security_expert",
        email="expert@example.com"
    )
    
    # Add users
    lb.add_user(user1)
    lb.add_user(user2)
    
    # Simulate challenge completion
    result = ChallengeResult(
        user_id=user1.id,
        challenge_id="sqli-001",
        completed=True,
        points_earned=50,
        time_taken=120,
        hints_used=0
    )
    
    lb.update_user(result)
    
    # Get leaderboard
    top = lb.get_top()
    print("🏆 Leaderboard:")
    for i, user in enumerate(top, 1):
        print(f"  {i}. {user.username} - {user.points} pts")
    
    # Check badges
    stats = {"total_completed": 50, "sql_injection": 50}
    badges = BadgeSystem.check_badges(user1, stats)
    print(f"\n🎖️ New badges earned: {len(badges)}")
