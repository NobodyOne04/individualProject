# individualProject

A Django web app for **Russian morphological analysis** with
[pymorphy2](https://pymorphy2.readthedocs.io) (university individual project, 2020).

- **Normal form**: words to their dictionary form (singular, nominative).
- **Inflect**: put words into a chosen form, e.g. plural accusative.
- **Grammar**: show each word's morphological tags.

## Run

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -r requiraments.txt          # Django 2.2, DRF 3.10, pymorphy2 0.8 + Russian dictionaries
python3 manage.py runserver 127.0.0.1:8000
```

Pages: `/` (index), `/normal`, `/inflect`, `/grammar`. Each has a form; the text is split
into Cyrillic words and analysed word by word.

## Layout

| Path | What |
|---|---|
| `vendor/` | Django project (settings, root urls, wsgi) |
| `rest/` | the app: `urls.py`, `controllers/` (one class-based view per page), `forms.py`, `views/` (templates, CSS) |
| `operations/morph/morph.py` | `MorphAnalyzer`: wraps pymorphy2 (normal form, tags, inflect) |
| `operations/config/config.py` | `Config`: reads `config/project.conf` |
| `sources/morph/*.json` | case and number options for the inflect form |
| `docs/` | class diagram and the reasoning for Singleton (Russian) |

Development settings only (`DEBUG = True`, a committed `SECRET_KEY`): don't deploy as is.

Decisions: [docs/adr](docs/adr/README.md).
