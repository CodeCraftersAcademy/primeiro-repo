import funcs


def test_15_add_15_equal_30():
    assert funcs.calc(15, 15, 'add') == 30

def test_15_add_15_equal_28():
    assert funcs.calc(15, 13, 'add') == 30

