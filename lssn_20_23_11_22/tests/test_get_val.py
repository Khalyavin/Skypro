from lssn_20_23_11_22.get_val import get_val

def test_get_val():
    assert(get_val({"hello": "world"}, "hello")) == "world"
    assert(get_val({"hello": "world"}, "hello", "python")) == "python"
    assert(get_val({"hello": "world"}, "", "python")) == "python"
    assert(get_val({"hello": "world"}, "")) == None
    assert(get_val({}, "hello", "python", "SkyPro")) == "python"
