from chlorine import keyword

def test_keyword():
    keywords = keyword()
    assert "bilibili" in keywords
