import pytest
from cb03.cb03 import reverse_string

def test_reverse_string_basic():
    assert reverse_string("hello") == "olleh", "Basic string reversal did not work"

def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh", "Spaces in string not handled correctly"

def test_reverse_string_empty():
    assert reverse_string("") == "", "Empty string should return empty"

def test_reverse_string_non_string():
    with pytest.raises(ValueError):
        reverse_string(123)  # 非字符串输入应该抛出 ValueError
