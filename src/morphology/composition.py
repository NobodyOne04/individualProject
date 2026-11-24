"""Composition root: the only place that picks adapters."""

from functools import cache

from morphology.adapters.outbound.pymorphy import PymorphyAnalyzer
from morphology.core.application import MorphologyService


@cache
def morphology_service() -> MorphologyService:
    """The app's one service; the analyzer and its dictionaries are loaded on first use."""
    return MorphologyService(PymorphyAnalyzer())
