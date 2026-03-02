# On-Premise Deployment

The Burp Suite KnowledgeBase On-Premise solution provides full platform capabilities within your own infrastructure.

## Why On-Premise?

| Benefit | Description |
|---------|-------------|
| Data Sovereignty | Keep all data in your environment |
| Compliance | Meet regulatory requirements |
| Customization | Full control over configuration |
| Integration | Connect with internal systems |
| Latency | Optimize for your network |

---

## System Requirements

### Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| CPU | 8 cores (Intel/AMD 64-bit) |
| RAM | 32 GB |
| Storage | 500 GB SSD |
| Network | 1 Gbps |
| OS | Ubuntu 20.04+ / RHEL 8+ / CentOS 8+ |

### Recommended Requirements

| Component | Requirement |
|-----------|-------------|
| CPU | 16+ cores |
| RAM | 64+ GB |
| Storage | 1 TB+ SSD |
| Network | 10 Gbps |
| High Availability | 3 nodes minimum |

### Production Requirements

| Component | Requirement |
|-----------|-------------|
| CPU | 32+ cores |
| RAM | 128+ GB |
| Storage | 2 TB+ NVMe |
| Network | 10 Gbps redundant |
| HA Setup | 5+ nodes |

---

## Deployment Options

### 1. Docker Deployment

```yaml
# docker-compose.yml
version: '3.8'

services:
  # API Server
  api:
    image: burpkb/enterprise-api:latest
    ports:
      - "443:8443"
    volumes:
      - ./data:/data
      - ./logs:/var/log
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/burpkb
      - REDIS_URL=redis://redis:6379
      - ENCRYPTION_KEY=${ENCRYPTION_KEY}
    depends_on:
      - db
      - redis

  # Worker for scans
  worker:
    image: burpkb/enterprise-worker:latest
    environment:
      - API_URL=http://api
      - WORKER_CONCURRENCY=4
    depends_on:
      - api

  # PostgreSQL
  db:
    image: postgres:14
    environment:
      - POSTGRES_DB=burpkb
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - ./postgres-data:/var/lib/postgresql/data

  # Redis for caching
  redis:
    image: redis:7-alpine
    volumes:
      - ./redis-data:/data

  # Nginx reverse proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api
```

### 2. Kubernetes Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: burpkb-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: burpkb-api
  template:
    metadata:
      labels:
        app: burpkb-api
    spec:
      containers:
      - name: api
        image: burpkb/enterprise-api:latest
        ports:
        - containerPort: 8443
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: burpkb-secrets
              key: database-url
---
apiVersion: v1
kind: Service
metadata:
  name: burpkb-api
spec:
  selector:
    app: burpkb-api
  ports:
  - port: 443
    targetPort: 8443
```

---

## Configuration

### Environment Variables

```bash
# Required
export DATABASE_URL="postgresql://user:pass@host:5432/burpkb"
export REDIS_URL="redis://host:6379"
export ENCRYPTION_KEY="your-256-bit-encryption-key"

# Optional
export SMTP_HOST="smtp.example.com"
export SMTP_PORT="587"
export SMTP_USER="notifications@example.com"
export SMTP_PASSWORD="smtp-password"

export S3_ENDPOINT="http://minio:9000"
export S3_BUCKET="burpkb-uploads"
export S3_ACCESS_KEY="minio-access"
export S3_SECRET_KEY="minio-secret"

export LDAP_URL="ldap://ldap.example.com:389"
export LDAP_BASE_DN="dc=example,dc=com"
```

### SSL/TLS Configuration

```nginx
# nginx.conf
server {
    listen 443 ssl http2;
    server_name burpkb.example.com;

    ssl_certificate /etc/ssl/certs/burpkb.crt;
    ssl_certificate_key /etc/ssl/private/burpkb.key;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    location / {
        proxy_pass http://burpkb-api:8443;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## Authentication

### LDAP/Active Directory

```yaml
# config.yaml
authentication:
  type: ldap
  ldap:
    url: ldap://ldap.example.com:389
    base_dn: dc=example,dc=com
    user_dn_template: uid={username},ou=users,dc=example,dc=com
    group_search:
      base_dn: ou=groups,dc=example,dc=com
      filter: (member={user_dn})
    attributes:
      name: cn
      email: mail
```

### SAML 2.0

```yaml
authentication:
  type: saml
  saml:
    idp_entity_id: https://idp.example.com/metadata
    idp_sso_url: https://idp.example.com/sso
    idp_cert: /etc/ssl/idp-cert.pem
    sp_entity_id: https://burpkb.example.com
    sp_acs_url: https://burpkb.example.com/auth/saml/callback
```

---

## Backup & Recovery

### Automated Backups

```bash
# Backup script
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/burpkb"

# Database backup
pg_dump -h db -U postgres burpkb > $BACKUP_DIR/db_$DATE.sql

# Upload to S3
aws s3 cp $BACKUP_DIR/db_$DATE.sql s3://company-backups/burpkb/

# Retention (30 days)
find $BACKUP_DIR -type f -mtime +30 -delete
```

### Restore Procedure

```bash
# Stop services
docker-compose down

# Restore database
pg_restore -h db -U postgres -d burpkb backup/db_latest.sql

# Start services
docker-compose up -d
```

---

## High Availability

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Load Balancer                           │
│                    (HAProxy / NGINX)                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │  API 1  │   │  API 2  │   │  API 3  │
   └────┬────┘   └────┬────┘   └────┬────┘
        │             │             │
        └─────────────┼─────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │PostgreSQL│  │PostgreSQL│  │PostgreSQL│
   │Primary  │◄─│ Standby  │◄─│ Standby  │
   └─────────┘   └─────────┘   └─────────┘
```

### Health Checks

```yaml
# docker-compose.yml
services:
  api:
    healthcheck:
      test: ["CMD", "curl", "-f", "https://localhost:8443/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
```

---

## Monitoring

### Prometheus Metrics

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'burpkb'
    static_configs:
      - targets: ['burpkb-api:8443']
```

### Available Metrics

| Metric | Description |
|--------|-------------|
| burpkb_scans_total | Total scans run |
| burpkb_scans_duration | Scan duration |
| burpkb_payloads_total | Payloads in database |
| burpkb_users_active | Active users |
| burpkb_api_requests | API request count |
| burpkb_errors_total | Error count |

---

## Upgrades

### Standard Upgrade

```bash
# Pull latest images
docker-compose pull

# Stop services
docker-compose down

# Start with new images
docker-compose up -d
```

### Rolling Upgrade

```bash
# Upgrade one node at a time
kubectl rollout restart deployment/burpkb-api
```

---

## Support

### Enterprise Support

| Level | Response Time | Hours |
|-------|--------------|-------|
| Standard | 24 hours | Business |
| Professional | 4 hours | 12x5 |
| Premium | 1 hour | 24x7 |

### Support Channels

- Email: enterprise-support@burpkb.com
- Phone: +1-888-BURP-KB
- Portal: https://enterprise.burpkb.com/support
- On-site: Available for Premium

---

## Pricing

### On-Premise Licensing

| Users | Annual License | Support |
|-------|---------------|---------|
| 25 | $25,000/year | Standard |
| 50 | $45,000/year | Professional |
| 100 | $80,000/year | Professional |
| Unlimited | Custom | Premium |

### Includes

- All Enterprise features
- Docker/Kubernetes deployment
- LDAP/AD integration
- Custom SSL certificates
- 1-year support
- Quarterly updates

---

## Migration from Cloud

```python
# Export from cloud
export_data = cloud_client.export(
    format="json",
    include=["payloads", "scans", "reports", "users"]
)

# Import to on-premise
onpremise_client.import_data(
    source=export_data,
    conflict_resolution="merge"
)
```

---

## Contact

- Sales: sales@burpkb.com
- Support: enterprise-support@burpkb.com
- Documentation: https://docs.burpkb.com/on-premise
