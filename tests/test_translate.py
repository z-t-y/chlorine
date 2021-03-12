from chlorine import RESERVED_KEYWORDS, Translate


def test_reserved_keywords():
    assert "bilibili" in RESERVED_KEYWORDS
    assert RESERVED_KEYWORDS == Translate.reserved_keywords()


def test_translate():
    t = Translate("bilibili")
    assert t.translate() == "bilibili"
