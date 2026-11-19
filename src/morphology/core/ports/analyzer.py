from typing import Protocol


class MorphAnalyzer(Protocol):
    """Morphology of single Russian words; each method returns None if it can't handle the word."""

    def normal_form(self, word: str) -> str | None: ...

    def tags(self, word: str) -> str | None: ...

    def inflect(self, word: str, grammemes: frozenset[str]) -> str | None: ...
