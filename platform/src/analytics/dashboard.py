"""
Analytics Dashboard Module for Burp Suite KnowledgeBase Platform
===============================================================

Version: 1.0.0-20260301-Senin-2013-WIB

Features:
- Usage analytics
- Vulnerability statistics
- User engagement metrics
- Payload performance tracking
- Challenge analytics
- Team performance metrics
- Export functionality
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
from collections import defaultdict
import uuid


# ============================================
# MODELS
# ============================================

class AnalyticsEvent:
    """Analytics event model"""
    
    def __init__(
        self,
        id: str,
        event_type: str,
        user_id: Optional[str],
        metadata: Optional[Dict] = None,
        timestamp: Optional[datetime] = None
    ):
        self.id = id
        self.event_type = event_type
        self.user_id = user_id
        self.metadata = metadata or {}
        self.timestamp = timestamp or datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "event_type": self.event_type,
            "user_id": self.user_id,
            "metadata": self.metadata,
            "timestamp": self.timestamp.isoformat()
        }


class Report:
    """Analytics report model"""
    
    def __init__(
        self,
        id: str,
        name: str,
        report_type: str,
        data: Dict,
        created_by: str,
        created_at: Optional[datetime] = None
    ):
        self.id = id
        self.name = name
        self.report_type = report_type
        self.data = data
        self.created_by = created_by
        self.created_at = created_at or datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "report_type": self.report_type,
            "data": self.data,
            "created_by": self.created_by,
            "created_at": self.created_at.isoformat()
        }


# ============================================
# ANALYTICS DATABASE
# ============================================

class AnalyticsDatabase:
    """In-memory analytics database"""
    
    def __init__(self):
        self.events: List[AnalyticsEvent] = []
        self.reports: Dict[str, Report] = {}
    
    def track_event(
        self,
        event_type: str,
        user_id: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> AnalyticsEvent:
        """Track an analytics event"""
        event = AnalyticsEvent(
            id=str(uuid.uuid4()),
            event_type=event_type,
            user_id=user_id,
            metadata=metadata
        )
        self.events.append(event)
        return event
    
    def get_events(
        self,
        event_type: Optional[str] = None,
        user_id: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        limit: int = 1000
    ) -> List[AnalyticsEvent]:
        """Get filtered events"""
        events = self.events
        
        if event_type:
            events = [e for e in events if e.event_type == event_type]
        
        if user_id:
            events = [e for e in events if e.user_id == user_id]
        
        if start_date:
            events = [e for e in events if e.timestamp >= start_date]
        
        if end_date:
            events = [e for e in events if e.timestamp <= end_date]
        
        # Sort by timestamp descending
        events.sort(key=lambda e: e.timestamp, reverse=True)
        
        return events[:limit]
    
    def get_event_counts(
        self,
        event_type: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> Dict[str, int]:
        """Get event counts by type"""
        events = self.get_events(event_type, None, start_date, end_date, 10000)
        
        counts = defaultdict(int)
        for event in events:
            counts[event.event_type] += 1
        
        return dict(counts)
    
    def get_user_stats(
        self,
        user_id: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> dict:
        """Get user statistics"""
        events = self.get_events(None, user_id, start_date, end_date, 10000)
        
        event_counts = defaultdict(int)
        for event in events:
            event_counts[event.event_type] += 1
        
        # Calculate engagement score
        engagement_score = sum(event_counts.values())
        
        return {
            "user_id": user_id,
            "total_events": len(events),
            "event_breakdown": dict(event_counts),
            "engagement_score": engagement_score,
            "first_seen": events[-1].timestamp.isoformat() if events else None,
            "last_seen": events[0].timestamp.isoformat() if events else None
        }
    
    def get_daily_stats(
        self,
        days: int = 30,
        event_type: Optional[str] = None
    ) -> List[dict]:
        """Get daily statistics"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        events = self.get_events(event_type, None, start_date, end_date, 10000)
        
        # Group by date
        daily_stats = defaultdict(lambda: {"date": "", "count": 0, "users": set()})
        
        for event in events:
            date_key = event.timestamp.date().isoformat()
            daily_stats[date_key]["date"] = date_key
            daily_stats[date_key]["count"] += 1
            if event.user_id:
                daily_stats[date_key]["users"].add(event.user_id)
        
        # Convert to list
        result = []
        for date_key in sorted(daily_stats.keys()):
            stats = daily_stats[date_key]
            result.append({
                "date": stats["date"],
                "count": stats["count"],
                "unique_users": len(stats["users"])
            })
        
        return result
    
    def get_vulnerability_stats(
        self,
        days: int = 30
    ) -> dict:
        """Get vulnerability testing statistics"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Get payload usage events
        events = self.get_events("payload_used", None, start_date, end_date, 10000)
        
        vuln_counts = defaultdict(int)
        for event in events:
            vuln_type = event.metadata.get("vulnerability_type", "unknown")
            vuln_counts[vuln_type] += 1
        
        return {
            "period_days": days,
            "total_payload_uses": len(events),
            "by_vulnerability_type": dict(vuln_counts),
            "most_tested": sorted(
                vuln_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]
        }
    
    def get_challenge_stats(
        self,
        days: int = 30
    ) -> dict:
        """Get challenge statistics"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Get challenge events
        completed = self.get_events("challenge_completed", None, start_date, end_date, 10000)
        started = self.get_events("challenge_started", None, start_date, end_date, 10000)
        
        # Get unique completions by user
        user_completions = defaultdict(int)
        for event in completed:
            user_completions[event.user_id] += 1
        
        return {
            "period_days": days,
            "challenges_started": len(started),
            "challenges_completed": len(completed),
            "completion_rate": len(completed) / len(started) if started else 0,
            "avg_completions_per_user": sum(user_completions.values()) / len(user_completions) if user_completions else 0,
            "top_completers": sorted(
                user_completions.items(),
                key=lambda x: x[1],
                reverse=True
            )[:10]
        }
    
    def get_platform_overview(self) -> dict:
        """Get platform overview statistics"""
        all_events = self.events
        
        # Get unique users
        users = set()
        for event in all_events:
            if event.user_id:
                users.add(event.user_id)
        
        # Get event counts
        event_counts = self.get_event_counts()
        
        # Get last 30 days
        daily = self.get_daily_stats(30)
        
        return {
            "total_events": len(all_events),
            "total_users": len(users),
            "event_types": len(event_counts),
            "events_by_type": event_counts,
            "last_30_days": {
                "total_events": sum(d["count"] for d in daily),
                "avg_daily_events": sum(d["count"] for d in daily) / len(daily) if daily else 0
            }
        }
    
    def create_report(
        self,
        name: str,
        report_type: str,
        data: Dict,
        created_by: str
    ) -> Report:
        """Create a saved report"""
        report = Report(
            id=str(uuid.uuid4()),
            name=name,
            report_type=report_type,
            data=data,
            created_by=created_by
        )
        self.reports[report.id] = report
        return report
    
    def get_report(self, report_id: str) -> Optional[Report]:
        """Get report by ID"""
        return self.reports.get(report_id)
    
    def get_user_reports(self, user_id: str) -> List[Report]:
        """Get reports created by user"""
        return [r for r in self.reports.values() if r.created_by == user_id]


# ============================================
# ANALYTICS SERVICE
# ============================================

class AnalyticsService:
    """Main analytics service"""
    
    def __init__(self):
        self.db = AnalyticsDatabase()
    
    def track(
        self,
        event_type: str,
        user_id: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> AnalyticsEvent:
        """Track an event"""
        return self.db.track_event(event_type, user_id, metadata)
    
    def get_dashboard_data(self) -> dict:
        """Get dashboard data"""
        overview = self.db.get_platform_overview()
        vuln_stats = self.db.get_vulnerability_stats()
        challenge_stats = self.db.get_challenge_stats()
        daily = self.db.get_daily_stats(30)
        
        return {
            "overview": overview,
            "vulnerabilities": vuln_stats,
            "challenges": challenge_stats,
            "daily_trends": daily
        }
    
    def get_user_dashboard(self, user_id: str) -> dict:
        """Get user-specific dashboard"""
        user_stats = self.db.get_user_stats(user_id)
        user_events = self.db.get_events(None, user_id, limit=100)
        
        return {
            "user_stats": user_stats,
            "recent_activity": [e.to_dict() for e in user_events[:10]]
        }
    
    def get_vulnerability_analytics(self) -> dict:
        """Get vulnerability analytics"""
        return self.db.get_vulnerability_stats()
    
    def get_challenge_analytics(self) -> dict:
        """Get challenge analytics"""
        return self.db.get_challenge_stats()
    
    def export_report(
        self,
        report_type: str,
        user_id: str,
        format: str = "json"
    ) -> Report:
        """Export a report"""
        data = {}
        
        if report_type == "overview":
            data = self.db.get_platform_overview()
        elif report_type == "vulnerabilities":
            data = self.db.get_vulnerability_stats()
        elif report_type == "challenges":
            data = self.db.get_challenge_stats()
        elif report_type == "daily":
            data = {"daily": self.db.get_daily_stats(30)}
        
        return self.db.create_report(
            name=f"{report_type} - {datetime.now().date()}",
            report_type=report_type,
            data=data,
            created_by=user_id
        )
    
    def get_saved_reports(self, user_id: str) -> List[Report]:
        """Get user's saved reports"""
        return self.db.get_user_reports(user_id)
    
    # ============================================
    # CONVENIENCE TRACKING METHODS
    # ============================================
    
    def track_payload_use(
        self,
        user_id: str,
        payload_id: str,
        vulnerability_type: str,
        success: bool
    ):
        """Track payload usage"""
        self.db.track_event(
            "payload_used",
            user_id,
            {
                "payload_id": payload_id,
                "vulnerability_type": vulnerability_type,
                "success": success
            }
        )
    
    def track_challenge_start(
        self,
        user_id: str,
        challenge_id: str,
        difficulty: str
    ):
        """Track challenge start"""
        self.db.track_event(
            "challenge_started",
            user_id,
            {
                "challenge_id": challenge_id,
                "difficulty": difficulty
            }
        )
    
    def track_challenge_complete(
        self,
        user_id: str,
        challenge_id: str,
        time_taken: int,
        points_earned: int
    ):
        """Track challenge completion"""
        self.db.track_event(
            "challenge_completed",
            user_id,
            {
                "challenge_id": challenge_id,
                "time_taken": time_taken,
                "points_earned": points_earned
            }
        )
    
    def track_search(
        self,
        user_id: str,
        query: str,
        results_count: int
    ):
        """Track search activity"""
        self.db.track_event(
            "search",
            user_id,
            {
                "query": query,
                "results_count": results_count
            }
        )
    
    def track_forum_post(
        self,
        user_id: str,
        post_id: str,
        category: str
    ):
        """Track forum activity"""
        self.db.track_event(
            "forum_post_created",
            user_id,
            {
                "post_id": post_id,
                "category": category
            }
        )


# ============================================
# DEMO
# ============================================

if __name__ == "__main__":
    analytics = AnalyticsService()
    
    # Track some events
    analytics.track_payload_use("user_1", "payload_1", "sql_injection", True)
    analytics.track_payload_use("user_1", "payload_2", "xss", False)
    analytics.track_payload_use("user_2", "payload_1", "sql_injection", True)
    analytics.track_challenge_start("user_1", "challenge_1", "beginner")
    analytics.track_challenge_complete("user_1", "challenge_1", 300, 100)
    analytics.track_search("user_1", "sql injection", 50)
    analytics.track_forum_post("user_2", "post_1", "tutorial")
    
    # Get dashboard
    dashboard = analytics.get_dashboard_data()
    print("Dashboard:")
    print(f"  Total events: {dashboard['overview']['total_events']}")
    print(f"  Total users: {dashboard['overview']['total_users']}")
    print(f"  Vulnerabilities tested: {dashboard['vulnerabilities']['total_payload_uses']}")
    print(f"  Challenges completed: {dashboard['challenges']['challenges_completed']}")
    
    # Get user dashboard
    user_dash = analytics.get_user_dashboard("user_1")
    print(f"\nUser 1 Dashboard:")
    print(f"  Total events: {user_dash['user_stats']['total_events']}")
    print(f"  Engagement score: {user_dash['user_stats']['engagement_score']}")
    
    # Export report
    report = analytics.export_report("overview", "user_1")
    print(f"\nExported report: {report.name}")
