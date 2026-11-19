# Architecture Decision Records

Decisions behind this project. Format and statuses: [0001](0001-record-decisions-as-adr-files.adr).

| # | Decision | Status |
|---|---|---|
| [0001](0001-record-decisions-as-adr-files.adr) | Record architecture decisions as .adr files | Accepted |
| [0002](0002-django-app-over-pymorphy2.adr) | A Django app with one class-based view per operation, over pymorphy2 | Superseded by [0004](0004-hexagonal-core-with-django-and-pymorphy3-adapters.adr) |
| [0003](0003-singletons-for-analyzer-and-config.adr) | Singletons for the analyzer and the config | Superseded by [0004](0004-hexagonal-core-with-django-and-pymorphy3-adapters.adr) |
| [0004](0004-hexagonal-core-with-django-and-pymorphy3-adapters.adr) | Hexagonal core; Django 5 and pymorphy3 as adapters | Accepted |
