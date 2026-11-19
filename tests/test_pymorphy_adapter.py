"""The outbound adapter against real pymorphy3 dictionaries."""

import pytest

from morphology.adapters.outbound.pymorphy import PymorphyAnalyzer


@pytest.fixture(scope="module")
def analyzer():
    return PymorphyAnalyzer()


def test_normal_form(analyzer):
    assert analyzer.normal_form("стали") in {"стать", "сталь"}
    assert analyzer.normal_form("котами") == "кот"


def test_tags_are_cyrillic(analyzer):
    assert "СУЩ" in analyzer.tags("кот")


def test_inflect(analyzer):
    assert analyzer.inflect("кот", frozenset({"gent", "plur"})) == "котов"


def test_inflect_returns_none_when_impossible(analyzer):
    assert analyzer.inflect("и", frozenset({"gent", "plur"})) is None
