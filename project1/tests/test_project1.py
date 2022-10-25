from project1.script import hello


def test_hello():
    assert hello() == "Hello Stranger"
    assert hello("Salih") == "Hello Salih"
