"""
Subscription & Payment Module for Burp Suite KnowledgeBase Platform
====================================================================

Version: 1.0.0-20260301-Senin-2014-WIB

Features:
- Subscription tiers (Free, Pro, Enterprise)
- Payment processing
- Usage tracking
- Feature access control
- Invoice management
- Webhook handling
"""

from datetime import datetime, timedelta
from typing import List, Optional, Dict
from enum import Enum
import uuid


# ============================================
# MODELS
# ============================================

class SubscriptionTier(str, Enum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class BillingPeriod(str, Enum):
    MONTHLY = "monthly"
    YEARLY = "yearly"


class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    PAST_DUE = "past_due"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    TRIALING = "trialing"


class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    CRYPTO = "crypto"


class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"


# ============================================
# PRICING
# ============================================

PRICING = {
    SubscriptionTier.PRO: {
        BillingPeriod.MONTHLY: {
            "price": 29.99,
            "currency": "USD",
            "features": [
                "unlimited_payloads",
                "ai_payload_generator",
                "advanced_challenges",
                "priority_support",
                "no_ads"
            ]
        },
        BillingPeriod.YEARLY: {
            "price": 299.99,
            "currency": "USD",
            "features": [
                "unlimited_payloads",
                "ai_payload_generator", 
                "advanced_challenges",
                "priority_support",
                "no_ads",
                "2_months_free"
            ]
        }
    },
    SubscriptionTier.ENTERPRISE: {
        BillingPeriod.MONTHLY: {
            "price": 99.99,
            "currency": "USD",
            "features": [
                "everything_in_pro",
                "team_features",
                "analytics_dashboard",
                "api_access",
                "custom_integrations",
                "dedicated_support",
                "sla_guarantee"
            ]
        },
        BillingPeriod.YEARLY: {
            "price": 999.99,
            "currency": "USD",
            "features": [
                "everything_in_pro",
                "team_features",
                "analytics_dashboard",
                "api_access",
                "custom_integrations",
                "dedicated_support",
                "sla_guarantee",
                "3_months_free"
            ]
        }
    }
}


# ============================================
# SUBSCRIPTION
# ============================================

class Subscription:
    """Subscription model"""
    
    def __init__(
        self,
        id: str,
        user_id: str,
        tier: SubscriptionTier,
        billing_period: BillingPeriod,
        status: SubscriptionStatus = SubscriptionStatus.TRIALING,
        current_period_start: Optional[datetime] = None,
        current_period_end: Optional[datetime] = None,
        cancel_at_period_end: bool = False,
        trial_end: Optional[datetime] = None
    ):
        self.id = id
        self.user_id = user_id
        self.tier = tier
        self.billing_period = billing_period
        self.status = status
        self.current_period_start = current_period_start or datetime.now()
        self.current_period_end = current_period_end or (
            datetime.now() + timedelta(days=30 if billing_period == BillingPeriod.MONTHLY else 365)
        )
        self.cancel_at_period_end = cancel_at_period_end
        self.trial_end = trial_end
    
    def has_feature(self, feature: str) -> bool:
        """Check if subscription has a feature"""
        if self.tier == SubscriptionTier.FREE:
            return feature in ["basic_payloads", "basic_challenges", "community_forum"]
        
        pricing = PRICING.get(self.tier, {}).get(self.billing_period, {})
        features = pricing.get("features", [])
        
        if feature in features:
            return True
        
        if feature.startswith("everything_in_"):
            return True
        
        return False
    
    def is_active(self) -> bool:
        """Check if subscription is active"""
        return self.status in [SubscriptionStatus.ACTIVE, SubscriptionStatus.TRIALING]
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "tier": self.tier.value,
            "billing_period": self.billing_period.value,
            "status": self.status.value,
            "current_period_start": self.current_period_start.isoformat(),
            "current_period_end": self.current_period_end.isoformat(),
            "cancel_at_period_end": self.cancel_at_period_end,
            "trial_end": self.trial_end.isoformat() if self.trial_end else None
        }


class Payment:
    """Payment model"""
    
    def __init__(
        self,
        id: str,
        subscription_id: str,
        user_id: str,
        amount: float,
        currency: str,
        status: PaymentStatus = PaymentStatus.PENDING,
        payment_method: PaymentMethod = PaymentMethod.CREDIT_CARD,
        transaction_id: Optional[str] = None,
        created_at: Optional[datetime] = None
    ):
        self.id = id
        self.subscription_id = subscription_id
        self.user_id = user_id
        self.amount = amount
        self.currency = currency
        self.status = status
        self.payment_method = payment_method
        self.transaction_id = transaction_id
        self.created_at = created_at or datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "subscription_id": self.subscription_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "currency": self.currency,
            "status": self.status.value,
            "payment_method": self.payment_method.value,
            "transaction_id": self.transaction_id,
            "created_at": self.created_at.isoformat()
        }


class Invoice:
    """Invoice model"""
    
    def __init__(
        self,
        id: str,
        user_id: str,
        subscription_id: str,
        amount: float,
        currency: str,
        status: str = "draft",
        items: Optional[List[Dict]] = None,
        paid_at: Optional[datetime] = None,
        created_at: Optional[datetime] = None
    ):
        self.id = id
        self.user_id = user_id
        self.subscription_id = subscription_id
        self.amount = amount
        self.currency = currency
        self.status = status
        self.items = items or []
        self.paid_at = paid_at
        self.created_at = created_at or datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "subscription_id": self.subscription_id,
            "amount": self.amount,
            "currency": self.currency,
            "status": self.status,
            "items": self.items,
            "paid_at": self.paid_at.isoformat() if self.paid_at else None,
            "created_at": self.created_at.isoformat()
        }


# ============================================
# BILLING DATABASE
# ============================================

class BillingDatabase:
    """In-memory billing database"""
    
    def __init__(self):
        self.subscriptions: Dict[str, Subscription] = {}
        self.payments: Dict[str, Payment] = {}
        self.invoices: Dict[str, Invoice] = {}
        self.user_subscriptions: Dict[str, str] = {}  # user_id -> subscription_id
        
        # Initialize free tier for all users
        self._init_free_tier()
    
    def _init_free_tier(self):
        """Initialize free tier subscription"""
        # This would typically be called for new users
        pass
    
    def create_subscription(
        self,
        user_id: str,
        tier: SubscriptionTier,
        billing_period: BillingPeriod
    ) -> Subscription:
        """Create a new subscription"""
        subscription = Subscription(
            id=str(uuid.uuid4()),
            user_id=user_id,
            tier=tier,
            billing_period=billing_period,
            status=SubscriptionStatus.TRIALING
        )
        
        self.subscriptions[subscription.id] = subscription
        self.user_subscriptions[user_id] = subscription.id
        
        return subscription
    
    def get_subscription(self, subscription_id: str) -> Optional[Subscription]:
        """Get subscription by ID"""
        return self.subscriptions.get(subscription_id)
    
    def get_user_subscription(self, user_id: str) -> Optional[Subscription]:
        """Get user's subscription"""
        subscription_id = self.user_subscriptions.get(user_id)
        if subscription_id:
            return self.subscriptions.get(subscription_id)
        return None
    
    def update_subscription(
        self,
        subscription_id: str,
        tier: Optional[SubscriptionTier] = None,
        billing_period: Optional[BillingPeriod] = None,
        status: Optional[SubscriptionStatus] = None
    ) -> Optional[Subscription]:
        """Update subscription"""
        subscription = self.subscriptions.get(subscription_id)
        if not subscription:
            return None
        
        if tier:
            subscription.tier = tier
        if billing_period:
            subscription.billing_period = billing_period
        if status:
            subscription.status = status
        
        return subscription
    
    def cancel_subscription(
        self,
        subscription_id: str,
        immediate: bool = False
    ) -> Optional[Subscription]:
        """Cancel subscription"""
        subscription = self.subscriptions.get(subscription_id)
        if not subscription:
            return None
        
        if immediate:
            subscription.status = SubscriptionStatus.CANCELLED
        else:
            subscription.cancel_at_period_end = True
        
        return subscription
    
    def create_payment(
        self,
        subscription_id: str,
        user_id: str,
        amount: float,
        currency: str,
        payment_method: PaymentMethod
    ) -> Payment:
        """Create a payment"""
        payment = Payment(
            id=str(uuid.uuid4()),
            subscription_id=subscription_id,
            user_id=user_id,
            amount=amount,
            currency=currency,
            payment_method=payment_method
        )
        
        self.payments[payment.id] = payment
        return payment
    
    def complete_payment(
        self,
        payment_id: str,
        transaction_id: str
    ) -> Optional[Payment]:
        """Mark payment as completed"""
        payment = self.payments.get(payment_id)
        if not payment:
            return None
        
        payment.status = PaymentStatus.COMPLETED
        payment.transaction_id = transaction_id
        
        # Update subscription status
        subscription = self.subscriptions.get(payment.subscription_id)
        if subscription:
            subscription.status = SubscriptionStatus.ACTIVE
            subscription.current_period_start = datetime.now()
            period_days = 30 if subscription.billing_period == BillingPeriod.MONTHLY else 365
            subscription.current_period_end = datetime.now() + timedelta(days=period_days)
        
        return payment
    
    def get_user_payments(self, user_id: str) -> List[Payment]:
        """Get user's payment history"""
        return [p for p in self.payments.values() if p.user_id == user_id]
    
    def create_invoice(
        self,
        user_id: str,
        subscription_id: str,
        amount: float,
        currency: str,
        items: List[Dict]
    ) -> Invoice:
        """Create an invoice"""
        invoice = Invoice(
            id=str(uuid.uuid4()),
            user_id=user_id,
            subscription_id=subscription_id,
            amount=amount,
            currency=currency,
            items=items
        )
        
        self.invoices[invoice.id] = invoice
        return invoice
    
    def get_user_invoices(self, user_id: str) -> List[Invoice]:
        """Get user's invoices"""
        return [i for i in self.invoices.values() if i.user_id == user_id]


# ============================================
# BILLING SERVICE
# ============================================

class BillingService:
    """Main billing service"""
    
    def __init__(self):
        self.db = BillingDatabase()
    
    def create_subscription(
        self,
        user_id: str,
        tier: SubscriptionTier,
        billing_period: BillingPeriod
    ) -> Subscription:
        """Create a new subscription"""
        return self.db.create_subscription(user_id, tier, billing_period)
    
    def get_subscription(self, subscription_id: str) -> Optional[Subscription]:
        """Get subscription"""
        return self.db.get_subscription(subscription_id)
    
    def get_user_subscription(self, user_id: str) -> Subscription:
        """Get user's current subscription"""
        subscription = self.db.get_user_subscription(user_id)
        
        if not subscription:
            # Create free tier
            subscription = self.db.create_subscription(
                user_id,
                SubscriptionTier.FREE,
                BillingPeriod.MONTHLY
            )
            subscription.status = SubscriptionStatus.ACTIVE
        
        return subscription
    
    def upgrade_subscription(
        self,
        user_id: str,
        new_tier: SubscriptionTier,
        billing_period: BillingPeriod
    ) -> Optional[Subscription]:
        """Upgrade subscription"""
        current = self.db.get_user_subscription(user_id)
        
        if current:
            return self.db.update_subscription(
                current.id,
                tier=new_tier,
                billing_period=billing_period,
                status=SubscriptionStatus.ACTIVE
            )
        
        return self.create_subscription(user_id, new_tier, billing_period)
    
    def cancel_subscription(
        self,
        user_id: str,
        immediate: bool = False
    ) -> bool:
        """Cancel subscription"""
        subscription = self.db.get_user_subscription(user_id)
        if not subscription:
            return False
        
        self.db.cancel_subscription(subscription.id, immediate)
        return True
    
    def get_pricing(self, tier: SubscriptionTier, period: BillingPeriod) -> Dict:
        """Get pricing for tier and period"""
        return PRICING.get(tier, {}).get(period, {})
    
    def get_all_pricing(self) -> Dict:
        """Get all pricing plans"""
        return PRICING
    
    def check_feature_access(self, user_id: str, feature: str) -> bool:
        """Check if user has access to feature"""
        subscription = self.get_user_subscription(user_id)
        return subscription.has_feature(feature)
    
    def initiate_payment(
        self,
        user_id: str,
        tier: SubscriptionTier,
        billing_period: BillingPeriod,
        payment_method: PaymentMethod
    ) -> Payment:
        """Initiate payment"""
        # Get or create subscription
        subscription = self.db.get_user_subscription(user_id)
        
        if not subscription:
            subscription = self.create_subscription(user_id, tier, billing_period)
        
        # Get price
        pricing = self.get_pricing(tier, billing_period)
        
        # Create payment
        payment = self.db.create_payment(
            subscription.id,
            user_id,
            pricing["price"],
            pricing["currency"],
            payment_method
        )
        
        return payment
    
    def confirm_payment(
        self,
        payment_id: str,
        transaction_id: str
    ) -> bool:
        """Confirm payment"""
        payment = self.db.complete_payment(payment_id, transaction_id)
        return payment is not None
    
    def get_payment_history(self, user_id: str) -> List[Payment]:
        """Get payment history"""
        return self.db.get_user_payments(user_id)
    
    def get_invoices(self, user_id: str) -> List[Invoice]:
        """Get user invoices"""
        return self.db.get_user_invoices(user_id)
    
    def create_checkout_session(
        self,
        user_id: str,
        tier: SubscriptionTier,
        billing_period: BillingPeriod
    ) -> Dict:
        """Create Stripe checkout session (mock)"""
        pricing = self.get_pricing(tier, billing_period)
        
        return {
            "session_id": str(uuid.uuid4()),
            "url": f"https://checkout.stripe.com/pay/{uuid.uuid4()}",
            "amount": pricing["price"],
            "currency": pricing["currency"],
            "tier": tier.value,
            "billing_period": billing_period.value
        }
    
    def get_usage_stats(self, user_id: str) -> Dict:
        """Get usage statistics for user"""
        subscription = self.get_user_subscription(user_id)
        
        # Mock usage data
        return {
            "user_id": user_id,
            "tier": subscription.tier.value,
            "api_calls_used": 1500,
            "api_calls_limit": 10000 if subscription.tier != SubscriptionTier.FREE else 100,
            "storage_used_mb": 250,
            "storage_limit_mb": 10000 if subscription.tier != SubscriptionTier.FREE else 100,
            "team_members": 3,
            "team_limit": 100 if subscription.tier == SubscriptionTier.ENTERPRISE else 1
        }


# ============================================
# DEMO
# ============================================

if __name__ == "__main__":
    billing = BillingService()
    
    # Get all pricing
    print("=== Pricing Plans ===")
    for tier in [SubscriptionTier.PRO, SubscriptionTier.ENTERPRISE]:
        for period in [BillingPeriod.MONTHLY, BillingPeriod.YEARLY]:
            price = billing.get_pricing(tier, period)
            print(f"{tier.value} - {period.value}: ${price['price']}")
    
    # Create subscription
    print("\n=== Create Subscription ===")
    sub = billing.create_subscription(
        user_id="user_new",
        tier=SubscriptionTier.PRO,
        billing_period=BillingPeriod.MONTHLY
    )
    print(f"Created subscription: {sub.id}")
    
    # Check feature access
    print("\n=== Feature Access ===")
    print(f"AI Generator: {billing.check_feature_access('user_new', 'ai_payload_generator')}")
    print(f"Basic Payloads: {billing.check_feature_access('user_new', 'basic_payloads')}")
    
    # Create checkout session
    print("\n=== Checkout Session ===")
    session = billing.create_checkout_session(
        "user_new",
        SubscriptionTier.ENTERPRISE,
        BillingPeriod.YEARLY
    )
    print(f"Checkout URL: {session['url']}")
    
    # Get usage
    print("\n=== Usage Stats ===")
    usage = billing.get_usage_stats("user_new")
    print(f"API Calls: {usage['api_calls_used']}/{usage['api_calls_limit']}")
    print(f"Storage: {usage['storage_used_mb']}MB/{usage['storage_limit_mb']}MB")
