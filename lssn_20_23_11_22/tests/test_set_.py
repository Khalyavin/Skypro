from lssn_20_23_11_22.set_ import set_

def test_set_():
    coll = {"a": {"b": {"c": 3}}}

    assert(set_(coll, ["a", "b", "c"], 4)) == 4
    assert(set_(coll, ["x", "y", "z"], 5)) == 5
    assert(coll["a"]["b"]["c"]) == 4
    assert (coll["x"]["y"]["z"]) == 5
