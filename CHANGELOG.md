# Changelog - Burp Suite Documentation

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.19] - 2026-03-01 - Senin - 18:27 GMT+7 (WIB)

### Added
- GitHub Actions CI/CD workflow
- MkDocs configuration for documentation site
- Markdown linting configuration
- Maintenance guide documentation
- GitHub issue and PR templates

### Completed Phases
- Fase 5: Payload Enrichment
- Fase 6: Automation & Integration
- Fase 7: Advanced Feature Development
- Fase 8: Community Contribution
- Fase 9: Platform & Deployment
- Fase 10: Maintenance & Updates

---

## [1.0.18] - 2026-03-01 - Senin - 18:12 GMT+7 (WIB)

### Added
- SMTP injection comprehensive payloads
- LDAP injection comprehensive payloads
- Deserialization payloads (Java/PHP/Python)
- Race condition/TOCTOU payloads
- Docker configuration for Burp Suite
- CI/CD integration configs
- Python extension examples
- Enhanced CONTRIBUTING.md

---

## [1.0.17] - 2026-03-01 - Minggu - 17:38 GMT+7 (WIB)

### Added
- 14 comprehensive payload files added with detailed content:
  - command-injection-comprehensive.txt (229+ payloads)
  - csrf-cors-comprehensive.txt (398+ payloads)
  - idor-comprehensive.txt (328+ payloads)
  - jwt-comprehensive.txt (351+ payloads)
  - lfi-rfi-comprehensive.txt (264+ payloads)
  - mssql-comprehensive.txt (286+ payloads)
  - mysql-comprehensive.txt (247+ payloads)
  - nosql-comprehensive.txt (336+ payloads)
  - oracle-comprehensive.txt (293+ payloads)
  - postgresql-comprehensive.txt (323+ payloads)
  - ssrf-comprehensive.txt (288+ payloads)
  - ssti-comprehensive.txt (323+ payloads)
  - xss-comprehensive.txt (266+ payloads)
  - xxe-comprehensive.txt (348+ payloads)
- Total: 4,280+ new payload entries

### Changed
- Payload files reorganized into comprehensive single files with extensive content

---

## [1.0.16] - 2026-03-01 - Minggu - 16:50 GMT+7 (WIB)

### Added
- All payload files now contain valid security testing payloads
- Updated payload content to ensure validity

---

## [1.0.15] - 2026-03-01 - Minggu - 16:21 GMT+7 (WIB)

### Added
- 2000+ organized payload files by category
- Enhanced payload structure and organization

---

## [1.0.14] - 2026-03-01 - Minggu - 16:12 GMT+7 (WIB)

### Added
- 500+ organized payload files by category

---

## [1.0.13] - 2026-03-01 - Minggu - 16:10 GMT+7 (WIB)

### Added
- README.md for payloads directory

---

## [1.0.0] - 2026-03-01 - Minggu - 09:39 GMT+7 (WIB)

### Added
- Initial repository creation
- Complete project structure with documentation folders
- README.md with comprehensive documentation
- LICENSE file (MIT License)
- .gitignore file with proper configurations
- PLAN.md with development roadmap
- CHANGELOG.md for version tracking
- Getting started guides (installation, quick start)
- Resources and references documentation

### Documentation Features
- Project overview and objectives
- Technology stack information
- Installation instructions
- Usage guidelines
- Folder structure explanation
- Development phases and timeline
- Contribution guidelines
- References and resources

### Project Structure
```
burp-suite-documentation/
├── .gitignore
├── LICENSE
├── README.md
├── CHANGELOG.md
├── PLAN.md
├── docs/
│   ├── getting-started/
│   │   ├── installation.md
│   │   └── quick-start.md
│   ├── tutorials/
│   ├── tips-and-tricks/
│   ├── advanced-topics/
│   └── best-practices/
├── examples/
│   ├── payloads/
│   └── configs/
└── resources/
    └── references.md
```

### Infrastructure
- Git repository initialized
- Main branch configured
- Version control workflow established
- Commit conventions defined

### Author
- waktuberhenti

---

## Version Format

Format: `[VERSION]-[TAHUNBULANTANGGAL]-[HARI]-[JAM]-[WIB]`

Example: `1.0.17-20260301-Minggu-1738-WIB`

### Version Numbering
- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in a backward-compatible manner
- **PATCH**: Backward-compatible bug fixes

---

## How to Update This Changelog

1. Add new entries under the `[Unreleased]` section
2. When releasing a new version:
   - Move `[Unreleased]` content to a new version section
   - Update the version number and date
   - Create a new `[Unreleased]` section

---

## Authors

- **waktuberhenti** - Initial work - [waktuberhenti](https://github.com/waktuberhenti)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Version**: 1.0.19
**Last Updated**: 2026-03-01 - Senin - 18:27 GMT+7 (WIB)
**Author**: waktuberhenti
