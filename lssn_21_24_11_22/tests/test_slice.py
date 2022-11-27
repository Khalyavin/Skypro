from lssn_21_24_11_22.slice import my_slice

def test_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]
    
    # added tests
    assert my_slice([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert my_slice([1, 2, 3, 4, 5, 6], 1, -1) == [2, 3, 4, 5]
    assert my_slice([1, 2, 3, 4, 5, 6], -5, -1) == [2, 3, 4, 5]
    assert my_slice([1, 2, 3, 4, 5, 6], -11, -1) == [1, 2, 3, 4, 5]
    assert my_slice([], 1, -1) == []
    assert my_slice([1, 2, 3, 4, 5, 6], 11, -1) == []
    assert my_slice([1, 2, 3, 4, 5, 6], 1, -31) == []
