import re

_WORD = re.compile(r"[а-я]+")


def words(text: str) -> list[str]:
    """The Cyrillic words of text, lower-cased, with ё read as е (the dictionaries use е)."""
    return _WORD.findall(text.lower().replace("ё", "е"))
