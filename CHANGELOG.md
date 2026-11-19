# Changelog

## Unreleased

### Changed
- Redesigned hexagonally (ADR 0004): framework-free core, pymorphy3 and Django 5.2 adapters, one analyzer built in a composition root; Python 3.12+ with uv, ruff and pytest

### Removed
- Django REST framework, pymorphy2, the INI config and JSON choice files, the hand-written singletons

### Added
- README in English, CLAUDE.md, changelog and ADRs
- Tests for the singletons

### Fixed
- `MorphAnalyzer` rebuilt pymorphy2 (50-100 MB) on every request and `Config` never cached: both singletons work now
- `SECRET_KEY` was committed; it now comes from `DJANGO_SECRET_KEY` (random per start without it)

### Changed
- Default branch renamed from `master` to `main`
