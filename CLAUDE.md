# individualProject (morphology)

Russian morphology web app: hexagonal core, pymorphy3 and Django 5 adapters (ADR 0004).

## Commands
```sh
make install    # uv sync
make run        # dev server, 127.0.0.1:8000
make check      # ruff check + ruff format --check + pytest (run before every PR)
make fmt        # ruff format + fixes
```

## Layout
- `src/morphology/core/`: `domain/` (tokenizer, grammemes, `WordResult`), `ports/`
  (`MorphAnalyzer` protocol), `application/` (`MorphologyService`). No Django, no pymorphy3.
- `src/morphology/adapters/outbound/pymorphy.py`: the pymorphy3 analyzer.
- `src/morphology/adapters/inbound/web/`: Django app (forms, views, urls, `templates/morphology/`, `static/morphology/`).
- `src/morphology/composition.py`: the composition root, `morphology_service()`.
- `project/`: Django settings/urls/wsgi; `manage.py` at the root.
- `tests/`: `test_core.py` (fake analyzer), `test_pymorphy_adapter.py`, `test_web.py`.
- `docs/adr/`: decision records (`.adr`), index in `docs/adr/README.md`.

## Conventions
- Read the ADR before changing a recorded decision; commit subjects carry its number.
- The core imports nothing from `adapters/`, Django or pymorphy3; new I/O goes behind a port.
- Views take the service from `composition.morphology_service()`; never build analyzers in
  views (pymorphy3 loads 50-100 MB of dictionaries).
- Settings only from the environment (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`).
- New logic gets a core test with a fake analyzer.
