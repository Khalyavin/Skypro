from lssn_21_24_11_22.index_of import index_of

def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    
    # added tests
    assert index_of([2, 7, 3, 2, 4], 2, 2) == 3
    assert index_of([2, 7, 3, 2, 4], 2, 4) == -1
    assert index_of([2, 7, 3, 2, 4], 5) == -1
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([], 2, 2) == -1
    assert index_of([2, 7, 3, 2, 4], 2, -3) == 3
    assert index_of([2, 7, 3, 2, 4], 2, -5) == 0
    assert index_of([2, 7, 3, 2, 4], 2, -15) == 0
