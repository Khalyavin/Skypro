from lssn_21_24_11_22.get import get

def test_get():
    assert get([1, 2, 3], 1, "a") == 2
    assert get([4, 5, 6], 7, "val") == "val"
    # added tests
    assert get([1, 2, 3], -3, "a") == "a"
    assert get([1, 2, 3], -8,) == None
    assert get([], 1, -12) == -12
    assert get([], 11) == None
