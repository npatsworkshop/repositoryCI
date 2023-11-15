def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # do not change this line until prompted to do so.

def test_add():
    assert add(5, 5) == 10
    assert add(5, -5) == 0

def test_subtract():
    assert subtract(5, 5) == 0
