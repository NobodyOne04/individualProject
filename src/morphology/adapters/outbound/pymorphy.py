import pymorphy3


class PymorphyAnalyzer:
    """MorphAnalyzer over pymorphy3. Loading it reads 50-100 MB of dictionaries: build it once."""

    def __init__(self) -> None:
        self._morph = pymorphy3.MorphAnalyzer()

    def normal_form(self, word: str) -> str | None:
        return self._best(word).normal_form

    def tags(self, word: str) -> str | None:
        return self._best(word).tag.cyr_repr

    def inflect(self, word: str, grammemes: frozenset[str]) -> str | None:
        form = self._best(word).inflect(set(grammemes))
        return form.word if form else None

    def _best(self, word: str):
        return self._morph.parse(word)[0]  # pymorphy always returns at least one guess
