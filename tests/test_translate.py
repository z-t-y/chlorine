from chlorine import Translate

def test_to_translate():
    assert Translate("bilibili").to_translate == "bilibili"

def test_reserved_keywords():
    assert "bilibili" in Translate.keywords()

def test_translate():
    assert Translate("抄饭咋做，轮胎波萝咋冲气").translate() == "炒饭怎么做，轮胎菠萝怎么充气"
    assert Translate('鸽视频是啥').translate() == "鸽视频是什么"
