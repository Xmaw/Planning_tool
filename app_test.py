import app


def test_index():
    assert app.index() == 'Hello World!'
