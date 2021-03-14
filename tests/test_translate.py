from chlorine import Translate


def test_reserved_keywords():
    assert "bilibili" in Translate.keywords()


def test_translate():
    t = Translate("抄饭咋做，轮胎波萝咋冲气")
    assert t.translate() == "炒饭怎么做，轮胎菠萝怎么充气"
