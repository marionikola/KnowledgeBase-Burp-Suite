# Installation Guide - Burp Suite

## Daftar Isi

1. [Persyaratan Sistem](#persyaratan-sistem)
2. [Instalasi Java](#instalasi-java)
3. [Download Burp Suite](#download-burp-suite)
4. [Instalasi pada Windows](#instalasi-pada-windows)
5. [Instalasi pada Linux](#instalasi-pada-linux)
6. [Instalasi pada macOS](#instalasi-pada-macos)
7. [Verifikasi Instalasi](#verifikasi-instalasi)
8. [Troubleshooting](#troubleshooting)

---

## Persyaratan Sistem

### Minimum Requirements
- **Processor**: Intel Core i3 atau setara
- **RAM**: 4 GB
- **Disk Space**: 500 MB
- **Java**: Java 8 atau lebih tinggi

### Recommended Requirements
- **Processor**: Intel Core i5/i7 atau setara
- **RAM**: 8 GB atau lebih
- **Disk Space**: 1 GB
- **Java**: Java 11 atau lebih tinggi

---

## Instalasi Java

### Windows

#### Menggunakan Installer
1. Download Java JDK dari [Oracle](https://www.oracle.com/java/technologies/downloads/) atau [Adoptium](https://adoptium.net/)
2. Jalankan installer
3. Ikuti instruksi di layar
4. Set environment variable jika diperlukan

#### Menggunakan Chocolatey
```powershell
# Install Chocolatey (jika belum ada)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Java
choco install openjdk11
```

### Linux

#### Ubuntu/Debian
```bash
# Update package list
sudo apt update

# Install OpenJDK 11
sudo apt install openjdk-11-jdk

# Verify installation
java -version
```

#### Fedora/RHEL
```bash
# Install Java
sudo dnf install java-11-openjdk-devel

# Verify installation
java -version
```

### macOS

#### Menggunakan Homebrew
```bash
# Install Homebrew (jika belum ada)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install OpenJDK
brew install openjdk@11

# Link Java
sudo ln -sfn $(brew --prefix)/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk
```

---

## Download Burp Suite

### Community Edition (Gratis)
1. Kunjungi [PortSwigger Download Page](https://portswigger.net/burp/releases)
2. Pilih "Burp Suite Community Edition"
3. Download file JAR

### Professional Edition (Berbayar)
1. Kunjungi [PortSwigger](https://portswigger.net/)
2. Beli lisensi atau gunakan trial
3. Download Professional Edition

### Enterprise Edition
1. Untuk penggunaan enterprise, hubungi PortSwigger
2. Atau coba trial Enterprise

---

## Instalasi pada Windows

### Metode 1: JAR File
```powershell
# Create Burp Suite directory
mkdir C:\BurpSuite
cd C:\BurpSuite

# Download burpsuite_community.jar
# (download dari https://portswigger.net/burp/releases)

# Run Burp Suite
java -jar burpsuite_community.jar
```

### Metode 2: Executable
```powershell
# Download installer (.exe)
# Run installer sebagai Administrator
# Ikuti instruksi wizard
```

---

## Instalasi pada Linux

### Metode 1: JAR File
```bash
# Create directory
mkdir -p ~/burp-suite
cd ~/burp-suite

# Download Burp Suite
wget https://portswigger.net/burp/releases/burpsuite-community-latest.jar

# Make executable (optional)
chmod +x burpsuite_community.jar

# Run Burp Suite
java -jar burpsuite_community.jar
```

### Metode 2: Desktop Launcher
```bash
# Create desktop entry
cat > ~/Desktop/BurpSuite.desktop << EOF
[Desktop Entry]
Type=Application
Name=Burp Suite Community
Comment=Web Application Security Testing
Exec=java -jar /path/to/burpsuite_community.jar
Icon=/path/to/icon.png
Terminal=false
Categories=Development;Security;
EOF

# Make executable
chmod +x ~/Desktop/BurpSuite.desktop
```

---

## Instalasi pada macOS

### Metode 1: JAR File
```bash
# Create directory
mkdir -p ~/Applications/BurpSuite
cd ~/Applications/BurpSuite

# Download Burp Suite
curl -O https://portswigger.net/burp/releases/burpsuite-community-latest.jar

# Run Burp Suite
java -jar burpsuite_community.jar
```

### Metode 2: Application Bundle
```bash
# Download dan install seperti aplikasi biasa
# Atau buat .app wrapper menggunakan Platypus
```

---

## Verifikasi Instalasi

### Check Java Version
```bash
java -version
# Output harus menampilkan Java 8 atau lebih tinggi
```

### Test Burp Suite Launch
```bash
# Run dengan minimal memory
java -jar -Xmx512m burpsuite_community.jar

# Run dengan recommended memory
java -jar -Xmx2048m burpsuite_community.jar
```

### Success Indicators
- [ ] Burp Suite window appears
- [ ] No error messages in console
- [ ] Proxy listener starts on localhost:8080

---

## Troubleshooting

### Problem: "Java Not Found"
**Solution:**
1. Verify Java installation: `java -version`
2. Check PATH environment variable
3. Reinstall Java

### Problem: "Port 8080 Already in Use"
**Solution:**
1. Find process using port 8080: `netstat -ano | findstr :8080`
2. Kill the process or change Burp Proxy port

### Problem: "Out of Memory Error"
**Solution:**
```bash
# Increase memory allocation
java -jar -Xmx4096m burpsuite_community.jar
```

### Problem: "SSL/TLS Errors"
**Solution:**
1. Install Burp Suite CA certificate
2. Go to Proxy > Options > Import/Export CA certificate
3. Install in browser/system trust store

### Problem: "Application Doesn't Start"
**Solution:**
1. Check Java version compatibility
2. Try running as Administrator
3. Check for conflicting software
4. Review log files

---

## Next Steps

Setelah instalasi berhasil, lanjutkan ke:
- [Quick Start Guide](quick-start.md)

---

**Version**: 1.0.0-20260301-Minggu-0939-WIB  
**Last Updated**: 2026-03-01 - Minggu - 09:39 GMT+7 (WIB)  
**Author**: waktuberhenti
