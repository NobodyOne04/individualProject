"""The core alone: a fake analyzer, no Django, no dictionaries."""

import pytest

from morphology.core.application import MorphologyService, UnknownGrammeme
from morphology.core.domain import WordResult, words


class FakeAnalyzer:
    def __init__(self):
        self.inflect_calls = []

    def normal_form(self, word):
        return {"коты": "кот", "ежики": "ежик"}.get(word)

    def tags(self, word):
        return "СУЩ,од,мр мн,им" if word == "коты" else None

    def inflect(self, word, grammemes):
        self.inflect_calls.append((word, grammemes))
        return word + "ов" if word == "кот" else None


def test_words_keeps_cyrillic_lowercases_and_reads_yo_as_e():
    assert words("Коты, ЁЖИКИ и cats 42!") == ["коты", "ежики", "и"]


def test_normal_forms_skip_words_the_analyzer_cannot_handle():
    service = MorphologyService(FakeAnalyzer())
    assert service.normal_forms("коты и ёжики") == [
        WordResult("коты", "кот"),
        WordResult("ежики", "ежик"),
    ]


def test_grammar():
    assert MorphologyService(FakeAnalyzer()).grammar("коты") == [
        WordResult("коты", "СУЩ,од,мр мн,им")
    ]


def test_inflect_passes_both_grammemes():
    analyzer = FakeAnalyzer()
    assert MorphologyService(analyzer).inflect("кот", "gent", "plur") == [
        WordResult("кот", "котов")
    ]
    assert analyzer.inflect_calls == [("кот", frozenset({"gent", "plur"}))]


@pytest.mark.parametrize("case, number", [("bogus", "plur"), ("gent", "dual")])
def test_inflect_rejects_unknown_grammemes(case, number):
    with pytest.raises(UnknownGrammeme):
        MorphologyService(FakeAnalyzer()).inflect("кот", case, number)


def test_result_reads_as_word_colon_value():
    assert str(WordResult("коты", "кот")) == "коты: кот"
