# Contributing Guide

## Cara Berkontribusi

Kami menyambut baik kontribusi dari komunitas! Berikut panduan untuk berkontribusi.

## Langkah-langkah

### 1. Fork Repository
Klik tombol "Fork" di GitHub untuk membuat salinan repository.

### 2. Clone Repository
```bash
git clone https://github.com/waktuberhenti/burp-suite-documentation.git
cd burp-suite-documentation
```

### 3. Buat Branch Baru
```bash
git checkout -b feature/nama-fitur
# atau
git checkout -b fix/nama-perbaikan
```

### 4. Buat Perubahan
- Edit file yang ingin diperbaiki
- Tambah konten baru
- Perbaiki typo

### 5. Commit Perubahan
```bash
git add .
git commit -m "ADD: Deskripsi perubahan - vVERSION-DATE"
```

### 6. Push ke GitHub
```bash
git push origin feature/nama-fitur
```

### 7. Buat Pull Request
Buka GitHub dan buat Pull Request dari branch baru.

## Format Commit Message

Gunakan format berikut:
```
[TYPE]: Deskripsi - VERSION-DATE
```

Types:
- `INIT`: Commit pertama
- `ADD`: Tambah konten
- `UPDATE`: Update konten
- `FIX`: Perbaikan bug
- `DOCS`: Perubahan dokumentasi
- `DELETE`: Hapus konten

Contoh:
```
ADD: SQL Injection Testing Guide - v1.0.5-20260301-Minggu-1009-WIB
```

## Standar Konten

### Struktur File
- Gunakan Markdown (.md)
- Ikuti format yang ada
- Sertakan versi di akhir file

### Quality Guidelines
- ✅ Gunakan bahasa yang jelas
- ✅ Sertakan contoh kode
- ✅ Sertakan screenshot jika perlu
- ✅ Review sebelum commit

### Jenis Konten yang Diterima
- Tutorial baru
- Tips dan tricks
- Vulnerability guides
- Best practices
- Payload lists

## Lisensi

Dengan berkontribusi, Anda setuju bahwa kontribusi Anda akan dilisensikan di bawah MIT License.

---

**Version**: 1.0.9-20260301-Minggu-1013-WIB  
**Author**: waktuberhenti
