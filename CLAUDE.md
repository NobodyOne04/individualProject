# individualProject

A 2020 university project: Django 2.2 web app for Russian morphology with pymorphy2.

## Commands
```sh
pip install -r requiraments.txt        # note the file name's spelling
python3 manage.py runserver 127.0.0.1:8000
```
No tests (`rest` has none).

## Layout
- `vendor/`: Django project settings/urls/wsgi; `rest/`: the app (controllers, forms, templates).
- `operations/`: `morph` (pymorphy2 wrapper), `config` (`config/project.conf` reader), `json` helper.
- `sources/morph/`: case/number options; `docs/`: class diagram, Singleton rationale (Russian).
- `docs/adr/`: decision records (`.adr`), index in `docs/adr/README.md`.

## Conventions
- Read the ADR before changing a recorded decision; commit subjects carry its number.
- Dev-only settings (`DEBUG`, committed `SECRET_KEY`, `ALLOWED_HOSTS = ['*']`): never deploy as is.
- Old pins (Django 2.2, Python 3.7-3.8 era); upgrading is a separate, deliberate change.
- Archived project: docs or small fixes only unless asked.
