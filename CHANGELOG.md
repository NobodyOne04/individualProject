# Changelog

## Unreleased

### Added
- README in English, CLAUDE.md, changelog and ADRs
- Tests for the singletons

### Fixed
- `MorphAnalyzer` rebuilt pymorphy2 (50-100 MB) on every request and `Config` never cached: both singletons work now
- `SECRET_KEY` was committed; it now comes from `DJANGO_SECRET_KEY` (random per start without it)

### Changed
- Default branch renamed from `master` to `main`
