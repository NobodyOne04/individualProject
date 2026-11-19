"""The grammemes the inflect operation offers: OpenCorpora codes → Russian labels."""

CASES: dict[str, str] = {
    "nomn": "именительный",
    "gent": "родительный",
    "datv": "дательный",
    "accs": "винительный",
    "ablt": "творительный",
    "loct": "предложный",
    "voct": "звательный",
    "gen2": "второй родительный (частичный)",
    "acc2": "второй винительный",
    "loc2": "второй предложный (местный)",
}

NUMBERS: dict[str, str] = {
    "sing": "единственное число",
    "plur": "множественное число",
}
