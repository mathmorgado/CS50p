from hello import hello


def test_default():
    assert hello() == "Hello World!"


def test_title_argument():
    assert hello("David Fincher") == "Hello David Fincher!"


def test_lower_argument():
    assert hello("david fincher") == "Hello David Fincher!"


def test_space_around_argument():
    assert hello("    David Fincher  ") == "Hello David Fincher!"


def test_number_argument():
    assert hello("123") == "Hello 123!"
