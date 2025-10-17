def test_add():
    from calculator import add
    assert add(3, 3) == 6
    assert add(2, -1) == 1
    assert add(10, 12) == 22
    assert add(88, 22) == 110

def test_division():
    from calculator import division
    assert division(80, 4) == 20
    assert division(30, 3) == 10
    assert division(20, -2) == -10
