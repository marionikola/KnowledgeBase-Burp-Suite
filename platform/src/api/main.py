"""
FastAPI Backend for Burp Suite KnowledgeBase Platform
==================================================

REST API for payload access, challenge system, and user management.

Version: 1.0.0-20260301-Senin-2002-WIB
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict
from datetime import datetime
from enum import Enum
import uuid


# ============================================
# MODELS
# ============================================

class VulnerabilityType(str, Enum):
    SQL_INJECTION = "sql_injection"
    XSS = "xss"
    COMMAND_INJECTION = "command_injection"
    SSRF = "ssrf"
    XXE = "xxe"
    LFI = "lfi"
    SSTI = "ssti"
    NOSQL = "nosql"
    LDAP = "ldap"


class UserRole(str, Enum):
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: str
    role: UserRole = UserRole.USER
    xp: int = 0
    level: int = 1
    points: int = 0
    badges: List[str] = []
    created_at: datetime
    
    class Config:
        from_attributes = True


class PayloadBase(BaseModel):
    payload: str
    vulnerability_type: VulnerabilityType
    description: Optional[str] = None
    severity: str = "medium"
    encoding: Optional[str] = None


class PayloadResponse(PayloadBase):
    id: str
    author_id: str
    likes: int = 0
    uses: int = 0
    tested: bool = False
    created_at: datetime
    
    class Config:
        from_attributes = True


class ChallengeBase(BaseModel):
    title: str
    description: str
    vulnerability_type: VulnerabilityType
    difficulty: str = "beginner"
    points: int = 100


class ChallengeResponse(ChallengeBase):
    id: str
    flags: List[str]
    hints: List[str] = []
    completion_count: int = 0
    
    class Config:
        from_attributes = True


class ChallengeSubmission(BaseModel):
    challenge_id: str
    flag: str
    time_taken: int


# ============================================
# DATABASE (In-Memory for Demo)
# ============================================

class InMemoryDB:
    """Simple in-memory database for demo"""
    
    def __init__(self):
        self.users: Dict[str, UserResponse] = {}
        self.payloads: Dict[str, PayloadResponse] = {}
        self.challenges: Dict[str, ChallengeResponse] = {}
        self.sessions: Dict[str, str] = {}  # session_token -> user_id
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        """Create new user"""
        user = UserResponse(
            id=str(uuid.uuid4()),
            username=user_data.username,
            email=user_data.email,
            created_at=datetime.now()
        )
        self.users[user.id] = user
        return user
    
    def get_user(self, user_id: str) -> Optional[UserResponse]:
        """Get user by ID"""
        return self.users.get(user_id)
    
    def get_user_by_username(self, username: str) -> Optional[UserResponse]:
        """Get user by username"""
        for user in self.users.values():
            if user.username == username:
                return user
        return None
    
    def create_payload(self, payload_data: PayloadBase, author_id: str) -> PayloadResponse:
        """Create new payload"""
        payload = PayloadResponse(
            id=str(uuid.uuid4()),
            author_id=author_id,
            created_at=datetime.now(),
            **payload_data.model_dump()
        )
        self.payloads[payload.id] = payload
        return payload
    
    def get_payloads(
        self, 
        vulnerability_type: Optional[VulnerabilityType] = None,
        limit: int = 50
    ) -> List[PayloadResponse]:
        """Get payloads with optional filter"""
        payloads = list(self.payloads.values())
        
        if vulnerability_type:
            payloads = [
                p for p in payloads 
                if p.vulnerability_type == vulnerability_type
            ]
        
        return payloads[:limit]
    
    def get_payload(self, payload_id: str) -> Optional[PayloadResponse]:
        """Get single payload"""
        return self.payloads.get(payload_id)
    
    def create_challenge(self, challenge_data: ChallengeBase) -> ChallengeResponse:
        """Create new challenge"""
        challenge = ChallengeResponse(
            id=str(uuid.uuid4()),
            created_at=datetime.now(),
            **challenge_data.model_dump()
        )
        self.challenges[challenge.id] = challenge
        return challenge
    
    def get_challenges(
        self,
        difficulty: Optional[str] = None,
        vulnerability_type: Optional[VulnerabilityType] = None
    ) -> List[ChallengeResponse]:
        """Get challenges"""
        challenges = list(self.challenges.values())
        
        if difficulty:
            challenges = [
                c for c in challenges 
                if c.difficulty == difficulty
            ]
        
        if vulnerability_type:
            challenges = [
                c for c in challenges 
                if c.vulnerability_type == vulnerability_type
            ]
        
        return challenges
    
    def get_challenge(self, challenge_id: str) -> Optional[ChallengeResponse]:
        """Get single challenge"""
        return self.challenges.get(challenge_id)


# Initialize database
db = InMemoryDB()


# ============================================
# AUTH DEPENDENCIES
# ============================================

async def get_current_user(
    authorization: Optional[str] = None
) -> UserResponse:
    """Get current authenticated user"""
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
    # Extract token from "Bearer <token>"
    parts = authorization.split()
    if len(parts) != 2 or parts[0] != "Bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme"
        )
    
    token = parts[1]
    user_id = db.sessions.get(token)
    
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    user = db.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user


# ============================================
# API ROUTES
# ============================================

app = FastAPI(
    title="Burp Suite KnowledgeBase API",
    description="API for security testing payloads and challenges",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "Burp Suite KnowledgeBase API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


# ============================================
# USER ROUTES
# ============================================

@app.post("/api/users/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    """Register new user"""
    # Check if username exists
    if db.get_user_by_username(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    return db.create_user(user)


@app.get("/api/users/me", response_model=UserResponse)
async def get_current_user_info(current_user: UserResponse = Depends(get_current_user)):
    """Get current user info"""
    return current_user


@app.get("/api/users/leaderboard", response_model=List[UserResponse])
async def get_leaderboard(limit: int = 10):
    """Get top users"""
    users = sorted(
        db.users.values(),
        key=lambda u: u.points,
        reverse=True
    )
    return users[:limit]


# ============================================
# PAYLOAD ROUTES
# ============================================

@app.get("/api/payloads", response_model=List[PayloadResponse])
async def get_payloads(
    vulnerability_type: Optional[VulnerabilityType] = None,
    limit: int = 50,
    current_user: UserResponse = Depends(get_current_user)
):
    """Get payloads with optional filter"""
    return db.get_payloads(vulnerability_type, limit)


@app.get("/api/payloads/{payload_id}", response_model=PayloadResponse)
async def get_payload(payload_id: str):
    """Get single payload"""
    payload = db.get_payload(payload_id)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payload not found"
        )
    return payload


@app.post("/api/payloads", response_model=PayloadResponse)
async def create_payload(
    payload: PayloadBase,
    current_user: UserResponse = Depends(get_current_user)
):
    """Create new payload"""
    return db.create_payload(payload, current_user.id)


@app.post("/api/payloads/{payload_id}/like")
async def like_payload(
    payload_id: str,
    current_user: UserResponse = Depends(get_current_user)
):
    """Like a payload"""
    payload = db.get_payload(payload_id)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payload not found"
        )
    
    payload.likes += 1
    return {"likes": payload.likes}


# ============================================
# CHALLENGE ROUTES
# ============================================

@app.get("/api/challenges", response_model=List[ChallengeResponse])
async def get_challenges(
    difficulty: Optional[str] = None,
    vulnerability_type: Optional[VulnerabilityType] = None
):
    """Get challenges"""
    return db.get_challenges(difficulty, vulnerability_type)


@app.get("/api/challenges/{challenge_id}", response_model=ChallengeResponse)
async def get_challenge(challenge_id: str):
    """Get single challenge"""
    challenge = db.get_challenge(challenge_id)
    if not challenge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Challenge not found"
        )
    return challenge


@app.post("/api/challenges/submit")
async def submit_challenge(
    submission: ChallengeSubmission,
    current_user: UserResponse = Depends(get_current_user)
):
    """Submit challenge flag"""
    challenge = db.get_challenge(submission.challenge_id)
    if not challenge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Challenge not found"
        )
    
    # Check flag
    if submission.flag not in challenge.flags:
        return {
            "correct": False,
            "message": "Incorrect flag"
        }
    
    # Award points
    current_user.points += challenge.points
    current_user.xp += challenge.points
    current_user.level = (current_user.xp // 500) + 1
    
    challenge.completion_count += 1
    
    return {
        "correct": True,
        "message": f"Correct! You earned {challenge.points} points!",
        "points": challenge.points
    }


# ============================================
# SEARCH ROUTES
# ============================================

@app.get("/api/search")
async def search(
    q: str,
    type: str = "payloads",
    current_user: UserResponse = Depends(get_current_user)
):
    """Search payloads or challenges"""
    results = []
    
    if type == "payloads":
        results = [
            p for p in db.payloads.values()
            if q.lower() in p.payload.lower() or 
               q.lower() in (p.description or "").lower()
        ]
    elif type == "challenges":
        results = [
            c for c in db.challenges.values()
            if q.lower() in c.title.lower() or
               q.lower() in c.description.lower()
        ]
    
    return {"results": results, "count": len(results)}


# ============================================
# STATS ROUTES
# ============================================

@app.get("/api/stats")
async def get_stats(current_user: UserResponse = Depends(get_current_user)):
    """Get platform statistics"""
    return {
        "total_users": len(db.users),
        "total_payloads": len(db.payloads),
        "total_challenges": len(db.challenges),
        "payloads_tested": sum(1 for p in db.payloads.values() if p.tested),
        "challenges_completed": sum(
            c.completion_count for c in db.challenges.values()
        )
    }


# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
