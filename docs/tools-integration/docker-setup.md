# Docker Setup - Burp Suite

## Mengapa Docker?

Docker memungkinkan menjalankan Burp Suite di container untuk konsistensi dan portabilitas.

## Docker Installation

### Dockerfile
```dockerfile
FROM openjdk:11-jdk-slim

# Install wget and ca-certificates
RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Download Burp Suite
RUN wget -O /opt/burpsuite.jar \
    https://portswigger.net/burp/releases/download?product=pro&version=2024.1 \
    && chmod 666 /opt/burpsuite.jar

# Create user
RUN useradd -m -s /bin/bash burp

# Set working directory
WORKDIR /home/burp

# Run Burp
ENTRYPOINT ["java", "-jar", "/opt/burpsuite.jar"]
```

### Build Image
```bash
docker build -t burp-suite-pro .
```

### Run Container
```bash
# Run with X11 forwarding (for GUI)
docker run -it \
    --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    burp-suite-pro

# Run headless (Professional only)
docker run -d \
    --name burp-scan \
    -v $(pwd)/reports:/home/burp/reports \
    burp-suite-pro \
    --project-file=/home/burp/scan.burp \
    --scan-urls=https://target.com
```

## Docker Compose

### docker-compose.yml
```yaml
version: '3.8'

services:
  burp:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./projects:/home/burp/projects
      - ./reports:/home/burp/reports
    environment:
      - JVM_OPTS=-Xmx4g

  api:
    build: ./api-service
    ports:
      - "8090:8090"
    depends_on:
      - burp
```

## Headless Usage

### API Mode
```bash
docker run -d \
    burp-suite-pro \
    --api \
    --port=8090
```

### CLI Mode
```bash
docker run -v $(pwd):/results \
    burp-suite-pro \
    --project-file=/results/scan.burp \
    --scan-urls=https://target.com
```

## Best Practices

### Resource Limits
```yaml
services:
  burp:
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: '2'
```

### Data Persistence
```yaml
volumes:
  - ./projects:/home/burp/projects
  - ./configs:/home/burp/configs
```

---

**Version**: 1.0.8-20260301-Minggu-1012-WIB  
**Catatan**: Membutuhkan Burp Suite Professional  
**Author**: waktuberhenti
