from dataclasses import dataclass


@dataclass(frozen=True)
class WordResult:
    """One analysed word and what the operation produced for it."""

    word: str
    value: str

    def __str__(self) -> str:
        return f"{self.word}: {self.value}"
