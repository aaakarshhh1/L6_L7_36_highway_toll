"""Property-based input-validation tests for the Lab 7 toll processor."""

import re

from hypothesis import given, strategies as st

from highway_toll import axle_class, parse_plate, trip_cost


@given(st.text())
def test_parse_plate_rejects_invalid_values_or_returns_valid_data(value):
    try:
        state, district, number = parse_plate(value)
    except ValueError:
        return

    assert re.fullmatch(r"[A-Z]{2}", state)
    assert 1 <= district <= 99
    assert 1 <= number <= 9999


@given(st.text())
def test_trip_cost_rejects_invalid_values_or_returns_positive_cost(value):
    try:
        result = trip_cost(value)
    except ValueError:
        return

    assert isinstance(result, int)
    assert result > 0


@given(st.text())
def test_axle_class_rejects_invalid_values_or_returns_valid_class(value):
    try:
        result = axle_class(value)
    except ValueError:
        return

    assert value.strip().isdigit()
    assert int(value.strip()) >= 2
    assert result in {"car", "truck", "heavy"}


@given(
    st.integers(min_value=1, max_value=99),
    st.integers(min_value=1, max_value=9999),
)
def test_valid_plate_is_parsed_consistently(district, number):
    plate = f"KA-{district:02d}-AB-{number:04d}"
    assert parse_plate(plate) == ("KA", district, number)


@given(st.integers(min_value=1, max_value=1000), st.integers(min_value=1, max_value=10000))
def test_valid_trip_cost_is_multiplication(count, rate):
    assert trip_cost(f"{count}x{rate}") == count * rate


@given(st.integers(min_value=2, max_value=100))
def test_valid_axle_count_has_expected_classification(axles):
    expected = "car" if axles == 2 else "truck" if axles <= 4 else "heavy"
    assert axle_class(str(axles)) == expected
