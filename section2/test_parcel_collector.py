#!/usr/bin/env python

from ex6 import *
import pytest

def test_parse_dim_string_works_with_correct_input():
    assert parse_dim_string("40 20 15") == [40, 20, 15]

def test_parse_dim_string_raises_value_error_wrong_number_of_items():
    with pytest.raises(ValueError):
        parse_dim_string("1")

def test_parse_dim_string_raises_value_error_not_int():
    with pytest.raises(ValueError):
        parse_dim_string("one two three")
