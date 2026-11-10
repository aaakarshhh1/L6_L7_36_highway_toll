"""Intentional pre-fix Hypothesis demonstrations.

Run explicitly with:
    python -m pytest -v hypothesis_bug_demo.py

These tests are expected to fail against highway_toll_buggy.py. They are
kept outside pytest's default test_*.py discovery so the fixed test suite
remains green.
"""

import pytest
from hypothesis import given, strategies as st

from highway_toll_buggy import axle_class, parse_plate, trip_cost


@given(st.integers(max_value=0), st.integers(min_value=1))
def test_trip_count_must_be_positive(count, rate):
    with pytest.raises(ValueError):
        trip_cost(f"{count}x{rate}")


@given(st.integers(max_value=1))
def test_axles_must_be_at_least_two(axles):
    with pytest.raises(ValueError):
        axle_class(str(axles))


@given(st.sampled_from([
    "XX-00-AA-0000",
    "K-05-A-1234",
    "KA-00-AB-0000",
]))
def test_invalid_plates_must_be_rejected(plate):
    with pytest.raises(ValueError):
        parse_plate(plate)
