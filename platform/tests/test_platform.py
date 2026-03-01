"""
Test Suite for Burp Suite KnowledgeBase Platform
================================================

Version: 1.0.0-20260301-Senin-2002-WIB

This test suite covers:
- AI Payload Generator
- Gamification System
- API Endpoints
- Integration Tests
"""

import pytest
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


# ============================================
# TEST: AI Payload Generator
# ============================================

class TestAIPayloadGenerator:
    """Test cases for AI Payload Generator"""
    
    @pytest.fixture
    def generator(self):
        """Create payload generator instance"""
        from ai.payload_generator import AIPayloadGenerator
        return AIPayloadGenerator()
    
    def test_sql_injection_payloads(self, generator):
        """Test SQL injection payload generation"""
        payloads = generator.generate_payloads("sql_injection", count=10)
        
        assert len(payloads) == 10
        assert any("'" in p for p in payloads)
        assert any("UNION" in p.upper() for p in payloads)
    
    def test_xss_payloads(self, generator):
        """Test XSS payload generation"""
        payloads = generator.generate_payloads("xss", count=10)
        
        assert len(payloads) == 10
        assert any("<script>" in p for p in payloads)
    
    def test_command_injection_payloads(self, generator):
        """Test command injection payload generation"""
        payloads = generator.generate_payloads("command_injection", count=10)
        
        assert len(payloads) == 10
        assert any(";" in p or "|" in p for p in payloads)
    
    def test_encoding_support(self, generator):
        """Test encoding support"""
        payload = "'; DROP TABLE users;--"
        encoded = generator.encode_payload(payload, "url")
        
        assert encoded != payload
        assert "%27" in encoded or "%3B" in encoded
    
    def test_waf_bypass_generation(self, generator):
        """Test WAF bypass payloads"""
        bypass_payloads = generator.generate_waf_bypass("sql_injection")
        
        assert len(bypass_payloads) > 0
        # Check for common WAF bypass techniques
        assert any(
            technique in bypass_payloads 
            for technique in ["comment", "encoding", "case"]
        )
    
    def test_framework_specific(self, generator):
        """Test framework-specific payloads"""
        payloads = generator.generate_framework_payloads("django")
        
        assert len(payloads) > 0
        assert any("django" in p.lower() or "{{" in p for p in payloads)


# ============================================
# TEST: Gamification System
# ============================================

class TestGamificationSystem:
    """Test cases for Gamification System"""
    
    @pytest.fixture
    def gamification(self):
        """Create gamification instance"""
        from gamification.challenge_system import GamificationEngine
        return GamificationEngine()
    
    def test_user_xp_award(self, gamification):
        """Test XP award system"""
        user_id = "test_user_1"
        initial_xp = gamification.get_user_xp(user_id)
        
        gamification.award_xp(user_id, 100)
        new_xp = gamification.get_user_xp(user_id)
        
        assert new_xp == initial_xp + 100
    
    def test_level_up(self, gamification):
        """Test level up system"""
        user_id = "test_user_2"
        
        # Award enough XP to level up
        gamification.award_xp(user_id, 500)
        new_level = gamification.get_user_level(user_id)
        
        assert new_level >= 2
    
    def test_badge_award(self, gamification):
        """Test badge awarding"""
        user_id = "test_user_3"
        
        gamification.award_badge(user_id, "first_payload")
        badges = gamification.get_user_badges(user_id)
        
        assert "first_payload" in badges
    
    def test_points_system(self, gamification):
        """Test points system"""
        user_id = "test_user_4"
        
        initial_points = gamification.get_user_points(user_id)
        gamification.award_points(user_id, 50)
        
        assert gamification.get_user_points(user_id) == initial_points + 50
    
    def test_challenge_completion(self, gamification):
        """Test challenge completion"""
        user_id = "test_user_5"
        challenge_id = "challenge_1"
        
        result = gamification.complete_challenge(user_id, challenge_id)
        
        assert result["completed"] == True
        assert result["points_earned"] > 0
    
    def test_leaderboard(self, gamification):
        """Test leaderboard generation"""
        # Add multiple users
        gamification.award_points("user_a", 1000)
        gamification.award_points("user_b", 500)
        gamification.award_points("user_c", 750)
        
        leaderboard = gamification.get_leaderboard()
        
        assert len(leaderboard) >= 3
        assert leaderboard[0]["points"] >= leaderboard[1]["points"]
    
    def test_streak_tracking(self, gamification):
        """Test streak tracking"""
        user_id = "test_user_6"
        
        gamification.update_streak(user_id)
        streak = gamification.get_streak(user_id)
        
        assert streak >= 1


# ============================================
# TEST: API Endpoints (Mock)
# ============================================

class TestAPIEndpoints:
    """Test cases for API endpoints"""
    
    @pytest.fixture
    def client(self):
        """Create test client"""
        from fastapi.testclient import TestClient
        from main import app
        return TestClient(app)
    
    def test_root_endpoint(self, client):
        """Test root endpoint"""
        response = client.get("/")
        
        assert response.status_code == 200
        assert "name" in response.json()
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get("/health")
        
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
    
    def test_get_payloads(self, client):
        """Test get payloads endpoint"""
        # Note: This will fail without authentication
        response = client.get("/api/payloads")
        
        # Should return 401 without auth
        assert response.status_code in [200, 401]
    
    def test_search_endpoint(self, client):
        """Test search endpoint"""
        response = client.get("/api/search?q=sql")
        
        # Should return 401 without auth
        assert response.status_code in [200, 401]


# ============================================
# TEST: Integration
# ============================================

class TestIntegration:
    """Integration test cases"""
    
    def test_payload_to_gamification(self):
        """Test integration between payload and gamification"""
        from ai.payload_generator import AIPayloadGenerator
        from gamification.challenge_system import GamificationEngine
        
        generator = AIPayloadGenerator()
        gamification = GamificationEngine()
        
        # Generate payloads
        payloads = generator.generate_payloads("sql_injection", count=5)
        
        # Award XP for generating payloads
        user_id = "integration_test_user"
        gamification.award_xp(user_id, len(payloads) * 10)
        
        # Check XP was awarded
        xp = gamification.get_user_xp(user_id)
        
        assert xp >= len(payloads) * 10
    
    def test_challenge_to_payload(self):
        """Test integration between challenge and payload"""
        from ai.payload_generator import AIPayloadGenerator
        from gamification.challenge_system import ChallengeArena
        
        generator = AIPayloadGenerator()
        arena = ChallengeArena()
        
        # Create a challenge
        challenge = arena.create_challenge(
            title="SQL Injection Challenge",
            vulnerability_type="sql_injection",
            difficulty="beginner"
        )
        
        # Get hints (should contain relevant payloads)
        hints = arena.get_challenge_hints(challenge["id"])
        
        assert len(hints) > 0


# ============================================
# PERFORMANCE TESTS
# ============================================

class TestPerformance:
    """Performance test cases"""
    
    def test_payload_generation_performance(self):
        """Test payload generation speed"""
        import time
        from ai.payload_generator import AIPayloadGenerator
        
        generator = AIPayloadGenerator()
        
        start = time.time()
        payloads = generator.generate_payloads("sql_injection", count=100)
        elapsed = time.time() - start
        
        assert len(payloads) == 100
        assert elapsed < 5.0  # Should complete within 5 seconds
    
    def test_concurrent_payload_generation(self):
        """Test concurrent payload generation"""
        import concurrent.futures
        from ai.payload_generator import AIPayloadGenerator
        
        generator = AIPayloadGenerator()
        
        def generate():
            return generator.generate_payloads("xss", count=10)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(generate) for _ in range(5)]
            results = [f.result() for f in concurrent.futures.as_completed(futures)]
        
        assert len(results) == 5
        assert all(len(r) == 10 for r in results)


# ============================================
# RUN TESTS
# ============================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=src"])
