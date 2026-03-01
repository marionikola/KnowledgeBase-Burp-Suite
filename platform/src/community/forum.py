"""
Community Forum Module for Burp Suite KnowledgeBase Platform
=======================================================

Version: 1.0.0-20260301-Senin-2011-WIB

Features:
- Discussion threads
- Post comments
- Upvote/Downvote system
- Category-based organization
- User reputation
"""

from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum
import uuid


# ============================================
# MODELS
# ============================================

class PostCategory(str, Enum):
    GENERAL = "general"
    TUTORIAL = "tutorial"
    PAYLOAD = "payload"
    QUESTION = "question"
    SHOWCASE = "showcase"
    ANNOUNCEMENT = "announcement"


class PostStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"
    DELETED = "deleted"


class Comment:
    """Forum comment model"""
    
    def __init__(
        self,
        id: str,
        post_id: str,
        author_id: str,
        content: str,
        parent_id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        upvotes: int = 0,
        downvotes: int = 0
    ):
        self.id = id
        self.post_id = post_id
        self.author_id = author_id
        self.content = content
        self.parent_id = parent_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.upvotes = upvotes
        self.downvotes = downvotes
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "post_id": self.post_id,
            "author_id": self.author_id,
            "content": self.content,
            "parent_id": self.parent_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "upvotes": self.upvotes,
            "downvotes": self.downvotes
        }


class Post:
    """Forum post model"""
    
    def __init__(
        self,
        id: str,
        author_id: str,
        title: str,
        content: str,
        category: PostCategory,
        tags: List[str] = None,
        status: PostStatus = PostStatus.PUBLISHED,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        upvotes: int = 0,
        downvotes: int = 0,
        views: int = 0,
        comment_count: int = 0
    ):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.content = content
        self.category = category
        self.tags = tags or []
        self.status = status
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.views = views
        self.comment_count = comment_count
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "author_id": self.author_id,
            "title": self.title,
            "content": self.content,
            "category": self.category.value,
            "tags": self.tags,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "upvotes": self.upvotes,
            "downvotes": self.downvotes,
            "views": self.views,
            "comment_count": self.comment_count
        }


# ============================================
# FORUM DATABASE
# ============================================

class ForumDatabase:
    """In-memory forum database"""
    
    def __init__(self):
        self.posts: Dict[str, Post] = {}
        self.comments: Dict[str, Comment] = {}
        self.user_reputation: Dict[str, int] = {}  # user_id -> reputation
    
    def create_post(
        self,
        author_id: str,
        title: str,
        content: str,
        category: PostCategory,
        tags: List[str] = None
    ) -> Post:
        """Create a new forum post"""
        post = Post(
            id=str(uuid.uuid4()),
            author_id=author_id,
            title=title,
            content=content,
            category=category,
            tags=tags
        )
        self.posts[post.id] = post
        
        # Award reputation for creating post
        self._award_reputation(author_id, 5)
        
        return post
    
    def get_post(self, post_id: str) -> Optional[Post]:
        """Get post by ID"""
        return self.posts.get(post_id)
    
    def get_posts(
        self,
        category: Optional[PostCategory] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[Post]:
        """Get posts with optional filter"""
        posts = [p for p in self.posts.values() if p.status == PostStatus.PUBLISHED]
        
        if category:
            posts = [p for p in posts if p.category == category]
        
        # Sort by created_at descending
        posts.sort(key=lambda p: p.created_at, reverse=True)
        
        return posts[offset:offset + limit]
    
    def update_post(
        self,
        post_id: str,
        title: Optional[str] = None,
        content: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> Optional[Post]:
        """Update a post"""
        post = self.posts.get(post_id)
        if not post:
            return None
        
        if title:
            post.title = title
        if content:
            post.content = content
        if tags:
            post.tags = tags
        
        post.updated_at = datetime.now()
        return post
    
    def delete_post(self, post_id: str) -> bool:
        """Delete a post"""
        post = self.posts.get(post_id)
        if not post:
            return False
        
        post.status = PostStatus.DELETED
        return True
    
    def view_post(self, post_id: str) -> Optional[Post]:
        """Increment view count"""
        post = self.posts.get(post_id)
        if post:
            post.views += 1
        return post
    
    def create_comment(
        self,
        post_id: str,
        author_id: str,
        content: str,
        parent_id: Optional[str] = None
    ) -> Optional[Comment]:
        """Create a comment on a post"""
        post = self.posts.get(post_id)
        if not post:
            return None
        
        comment = Comment(
            id=str(uuid.uuid4()),
            post_id=post_id,
            author_id=author_id,
            content=content,
            parent_id=parent_id
        )
        self.comments[comment.id] = comment
        
        # Update comment count
        post.comment_count += 1
        
        # Award reputation
        self._award_reputation(author_id, 2)
        
        return comment
    
    def get_comments(self, post_id: str) -> List[Comment]:
        """Get comments for a post"""
        return [
            c for c in self.comments.values()
            if c.post_id == post_id
        ]
    
    def upvote_post(self, post_id: str, user_id: str) -> bool:
        """Upvote a post"""
        post = self.posts.get(post_id)
        if not post:
            return False
        
        post.upvotes += 1
        self._award_reputation(post.author_id, 10)
        return True
    
    def downvote_post(self, post_id: str, user_id: str) -> bool:
        """Downvote a post"""
        post = self.posts.get(post_id)
        if not post:
            return False
        
        post.downvotes += 1
        return True
    
    def upvote_comment(self, comment_id: str, user_id: str) -> bool:
        """Upvote a comment"""
        comment = self.comments.get(comment_id)
        if not comment:
            return False
        
        comment.upvotes += 1
        self._award_reputation(comment.author_id, 5)
        return True
    
    def downvote_comment(self, comment_id: str, user_id: str) -> bool:
        """Downvote a comment"""
        comment = self.comments.get(comment_id)
        if not comment:
            return False
        
        comment.downvotes += 1
        return True
    
    def _award_reputation(self, user_id: str, points: int):
        """Award reputation points to user"""
        if user_id not in self.user_reputation:
            self.user_reputation[user_id] = 0
        self.user_reputation[user_id] += points
    
    def get_user_reputation(self, user_id: str) -> int:
        """Get user reputation"""
        return self.user_reputation.get(user_id, 0)
    
    def search_posts(self, query: str) -> List[Post]:
        """Search posts by title or content"""
        query_lower = query.lower()
        return [
            p for p in self.posts.values()
            if p.status == PostStatus.PUBLISHED and (
                query_lower in p.title.lower() or
                query_lower in p.content.lower() or
                any(query_lower in tag.lower() for tag in p.tags)
            )
        ]
    
    def get_popular_posts(self, limit: int = 10) -> List[Post]:
        """Get popular posts by votes"""
        posts = [
            p for p in self.posts.values()
            if p.status == PostStatus.PUBLISHED
        ]
        posts.sort(
            key=lambda p: (p.upvotes - p.downvotes),
            reverse=True
        )
        return posts[:limit]
    
    def get_user_posts(self, user_id: str) -> List[Post]:
        """Get posts by user"""
        return [
            p for p in self.posts.values()
            if p.author_id == user_id and p.status != PostStatus.DELETED
        ]


# ============================================
# FORUM SERVICE
# ============================================

class ForumService:
    """Main forum service"""
    
    def __init__(self):
        self.db = ForumDatabase()
    
    def create_post(
        self,
        author_id: str,
        title: str,
        content: str,
        category: PostCategory,
        tags: List[str] = None
    ) -> Post:
        """Create a new post"""
        return self.db.create_post(author_id, title, content, category, tags)
    
    def get_post(self, post_id: str) -> Optional[Post]:
        """Get post and increment view"""
        post = self.db.get_post(post_id)
        if post:
            self.db.view_post(post_id)
        return post
    
    def get_feed(
        self,
        category: Optional[PostCategory] = None,
        limit: int = 20
    ) -> List[Post]:
        """Get post feed"""
        return self.db.get_posts(category, limit)
    
    def create_comment(
        self,
        post_id: str,
        author_id: str,
        content: str,
        parent_id: Optional[str] = None
    ) -> Optional[Comment]:
        """Create a comment"""
        return self.db.create_comment(post_id, author_id, content, parent_id)
    
    def vote_post(
        self,
        post_id: str,
        user_id: str,
        is_upvote: bool
    ) -> bool:
        """Vote on a post"""
        if is_upvote:
            return self.db.upvote_post(post_id, user_id)
        else:
            return self.db.downvote_post(post_id, user_id)
    
    def vote_comment(
        self,
        comment_id: str,
        user_id: str,
        is_upvote: bool
    ) -> bool:
        """Vote on a comment"""
        if is_upvote:
            return self.db.upvote_comment(comment_id, user_id)
        else:
            return self.db.downvote_comment(comment_id, user_id)
    
    def search(self, query: str) -> List[Post]:
        """Search posts"""
        return self.db.search_posts(query)
    
    def get_popular(self, limit: int = 10) -> List[Post]:
        """Get popular posts"""
        return self.db.get_popular_posts(limit)
    
    def get_user_profile(self, user_id: str) -> dict:
        """Get user forum profile"""
        posts = self.db.get_user_posts(user_id)
        reputation = self.db.get_user_reputation(user_id)
        
        total_upvotes = sum(p.upvotes for p in posts)
        total_downvotes = sum(p.downvotes for p in posts)
        
        return {
            "user_id": user_id,
            "post_count": len(posts),
            "reputation": reputation,
            "total_upvotes": total_upvotes,
            "total_downvotes": total_downvotes,
            "net_votes": total_upvotes - total_downvotes
        }


# ============================================
# DEMO
# ============================================

if __name__ == "__main__":
    # Demo usage
    forum = ForumService()
    
    # Create a post
    post = forum.create_post(
        author_id="user_1",
        title="Best SQL Injection Payloads for 2026",
        content="Here's a comprehensive list of SQL injection payloads...",
        category=PostCategory.PAYLOAD,
        tags=["sql-injection", "payloads", "security"]
    )
    print(f"Created post: {post.id}")
    
    # Get feed
    feed = forum.get_feed()
    print(f"Feed has {len(feed)} posts")
    
    # Create comment
    comment = forum.create_comment(
        post_id=post.id,
        author_id="user_2",
        content="Great list! Very useful."
    )
    print(f"Created comment: {comment.id}")
    
    # Upvote post
    forum.vote_post(post.id, "user_3", True)
    print(f"Post upvotes: {post.upvotes}")
    
    # Search
    results = forum.search("SQL")
    print(f"Found {len(results)} posts")
    
    # Get user profile
    profile = forum.get_user_profile("user_1")
    print(f"User profile: {profile}")
