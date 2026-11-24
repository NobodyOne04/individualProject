# individualProject (morphology)

A web app for **Russian morphological analysis** (university individual project, 2020;
redesigned 2026): turn words into their dictionary form, show their grammatical tags, or
inflect them into a chosen case and number. Built on [pymorphy3](https://github.com/no-plagiarism/pymorphy3).

## Run

```sh
make install        # uv sync: Python 3.12+, Django 5.2, pymorphy3 + Russian dictionaries
make run            # http://127.0.0.1:8000
make check          # ruff lint + format check, pytest
```

Pages: `/` (pick an operation), `/normal`, `/grammar`, `/inflect`.

## Design

Hexagonal, like [personal-ai](https://github.com/NobodyOne04/personal-ai): the logic knows nothing
about Django or pymorphy3.

```
src/morphology/
  core/
    domain/          words() tokenizer, CASES / NUMBERS, WordResult
    ports/           MorphAnalyzer (normal_form, tags, inflect)
    application/     MorphologyService: the three operations
  adapters/
    outbound/        PymorphyAnalyzer (pymorphy3)
    inbound/web/     Django app: forms, views, urls, templates, CSS
  composition.py     morphology_service(): builds the analyzer once
project/             Django settings, urls, wsgi
tests/               core (fake analyzer), pymorphy3 adapter, web (test client)
```

Settings come from the environment: `DJANGO_SECRET_KEY` (random per start without it),
`DJANGO_DEBUG=1`, `DJANGO_ALLOWED_HOSTS` (default `localhost,127.0.0.1`).

Decisions: [docs/adr](docs/adr/README.md).
