# Contributing Guide

## Cara Berkontribusi

Kami menyambut baik kontribusi dari komunitas! Berikut panduan lengkap untuk berkontribusi pada project ini.

##Daftar Isi

1. [Panduan Memulai](#panduan-memulai)
2. [Proses Pengembangan](#proses-pengembangan)
3. [Standar Kode](#standar-kode)
4. [Format Commit](#format-commit)
5. [Pull Request](#pull-request)
6. [Issue Reporting](#issue-reporting)
7. [Lisensi](#lisensi)

---

## Panduan Memulai

### 1. Fork Repository
Klik tombol "Fork" di GitHub untuk membuat salinan repository.

### 2. Clone Repository
```bash
git clone https://github.com/marionikola/KnowledgeBase-Burp-Suite.git
cd KnowledgeBase-Burp-Suite
```

### 3. Setup Remote
```bash
git remote add upstream https://github.com/marionikola/KnowledgeBase-Burp-Suite.git
```

### 4. Buat Branch Baru
```bash
git checkout -b feature/nama-fitur
# atau
git checkout -b fix/nama-perbaikan
# atau
git checkout -b docs/nama-dokumentasi
```

### 5. Sync dengan upstream
```bash
git fetch upstream
git merge upstream/main
```

---

## Proses Pengembangan

### Workflow
1. **Buat branch** dari `main`
2. **Develop** di branch Anda
3. **Test** perubahan secara lokal
4. **Commit** dengan format yang benar
5. **Push** ke fork Anda
6. **Buat Pull Request** ke `main`

### Jenis Branch
- `feature/*` - Fitur baru
- `fix/*` - Perbaikan bug
- `docs/*` - Dokumentasi
- `payload/*` - Payload baru
- `refactor/*` - Refactoring

---

## Standar Kode

### Untuk Dokumentasi
- Gunakan Markdown (.md)
- Ikuti format yang sudah ada
- Sertakan versi di setiap file
- Gunakan bahasa Indonesia (untuk konten) atau English (untuk kode)
- Review sebelum submit

### Untuk Payload Files
- Ikuti format payload yang ada
- Sertakan kategori dan deskripsi
- Comment setiap section
- Test payload sebelum submit

### Untuk Code/Extension
- Ikuti PEP8 (Python)
- Sertakan comments
- Sertakan error handling
- Test secara thorough

### Quality Checklist
- [ ] Tidak ada typo
- [ ] Format konsisten
- [ ] Link berfungsi
- [ ] Contoh kode sudah diuji
- [ ] Sesuai dengan project guidelines

---

## Format Commit

### Format
```
[TYPE]: Deskripsi - VERSION-DATE
```

### Jenis Commit
| Type | Deskripsi |
|------|-----------|
| `INIT` | Commit pertama repository |
| `ADD` | Menambah konten baru |
| `UPDATE` | Memperbarui konten yang ada |
| `FIX` | Memperbaiki bug/kesalahan |
| `DELETE` | Menghapus konten |
| `DOCS` | Perubahan dokumentasi |
| `REFACTOR` | Refactoring kode |
| `CONFIG` | Perubahan konfigurasi |

### Contoh Commit
```
ADD: New SQL Injection Payloads - v1.0.18-20260301-Senin-1812-WIB
FIX: Typo in XSS Tutorial - v1.0.18-20260301-Senin-1812-WIB
DOCS: Update Installation Guide - v1.0.18-20260301-Senin-1812-WIB
```

### Format Versi
```
VERSION-TAHUNBULANTANGGAL-HARI-JAM-WIB
Contoh: 1.0.18-20260301-Senin-1812-WIB
```

---

## Pull Request

### Checklist PR
- [ ] Branch sudah di-sync dengan main
- [ ] Tidak ada konflik
- [ ] Semua test passed
- [ ] Dokumentasi sudah diupdate
- [ ] Commit message sesuai format

### Langkah Membuat PR
1. Push branch ke GitHub
2. Buka Pull Request
3. Isi template PR
4. Tunggu review
5. Apply feedback jika ada
6. Merge setelah approved

### PR Template
```markdown
## Deskripsi
[Isi deskripsi perubahan]

## Tipe Perubahan
- [ ] Fitur baru
- [ ] Perbaikan bug
- [ ] Dokumentasi
- [ ] Payload baru
- [ ] Lainnya

## Testing
[Describe testing yang dilakukan]

## Screenshot (jika ada)
[Screenshot]
```

---

## Issue Reporting

### Jenis Issue
- **Bug Report**: Error atau masalah
- **Feature Request**: Permintaan fitur baru
- **Documentation**: Koreksi/penambahan docs
- **Payload Request**: Permintaan payload baru
- **Question**: Pertanyaan umum

### Issue Template
```markdown
## Deskripsi
[Deskripsi jelas tentang issue]

## Steps to Reproduce
1. 
2. 
3. 

## Expected Behavior
[Apa yang diharapkan]

## Actual Behavior
[Apa yang terjadi]

## Environment
- OS: 
- Burp Version: 
- Browser: 

## Additional Context
[Informasi tambahan]
```

---

## Lisensi

Dengan berkontribusi, Anda setuju bahwa:
1. Kontribusi Anda akan dilisensikan di bawah MIT License
2. Anda memiliki hak untuk mengkontribusikan konten tersebut
3. Anda mengizinkan penggunaan konten Anda dalam project ini

---

## Pertanyaan?

Jika ada pertanyaan:
1. Buka **Issue** di GitHub
2. Diskusikan di **Discussions**
3. Contact langsung via email

---

**Version**: 1.0.18-20260301-Senin-1812-WIB  
**Author**: waktuberhenti
