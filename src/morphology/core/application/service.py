from collections.abc import Callable

from morphology.core.domain import CASES, NUMBERS, WordResult, words
from morphology.core.ports import MorphAnalyzer


class UnknownGrammeme(ValueError):
    """A case or number code the service doesn't offer."""


class MorphologyService:
    """The three operations, word by word; words the analyzer can't handle are left out."""

    def __init__(self, analyzer: MorphAnalyzer) -> None:
        self._analyzer = analyzer

    def normal_forms(self, text: str) -> list[WordResult]:
        return self._each(text, self._analyzer.normal_form)

    def grammar(self, text: str) -> list[WordResult]:
        return self._each(text, self._analyzer.tags)

    def inflect(self, text: str, case: str, number: str) -> list[WordResult]:
        if case not in CASES:
            raise UnknownGrammeme(f"unknown case: {case!r}")
        if number not in NUMBERS:
            raise UnknownGrammeme(f"unknown number: {number!r}")
        grammemes = frozenset({case, number})
        return self._each(text, lambda word: self._analyzer.inflect(word, grammemes))

    @staticmethod
    def _each(text: str, op: Callable[[str], str | None]) -> list[WordResult]:
        results = []
        for word in words(text):
            value = op(word)
            if value is not None:
                results.append(WordResult(word, value))
        return results
