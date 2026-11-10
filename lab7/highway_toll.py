"""Validated highway toll input-processing functions."""

import re


_PLATE_PATTERN = re.compile(r"^([A-Z]{2})-(\d{2})-([A-Z]{2})-(\d{4})$", re.IGNORECASE)


def parse_plate(plate):
    """Return (state, district, registration_number) for a valid plate."""
    if not isinstance(plate, str):
        raise ValueError("Plate must be a string")

    match = _PLATE_PATTERN.fullmatch(plate.strip())
    if match is None:
        raise ValueError("Plate must follow the format KA-05-AB-1234")

    state, district_text, _series, number_text = match.groups()
    district = int(district_text)
    number = int(number_text)

    if not 1 <= district <= 99:
        raise ValueError("District must be between 01 and 99")
    if not 1 <= number <= 9999:
        raise ValueError("Registration number must be between 0001 and 9999")

    return state.upper(), district, number


def trip_cost(text):
    """Calculate total cost from a positive 'count x rate' expression."""
    if not isinstance(text, str):
        raise ValueError("Trip expression must be a string")

    match = re.fullmatch(r"\s*(\d+)\s*[xX]\s*(\d+)\s*", text)
    if match is None:
        raise ValueError("Trip expression must follow the format 3x150")

    count, rate = map(int, match.groups())
    if count <= 0 or rate <= 0:
        raise ValueError("Trip count and rate must be positive")

    return count * rate


def axle_class(axles):
    """Classify a vehicle using its positive integer axle count."""
    if isinstance(axles, bool):
        raise ValueError("Axle count must be an integer")

    try:
        value = str(axles).strip()
        if not re.fullmatch(r"\d+", value):
            raise ValueError("Axle count must be a positive integer")
        n = int(value)
    except (TypeError, ValueError):
        raise ValueError("Axle count must be a positive integer") from None

    if n < 2:
        raise ValueError("Axle count must be at least 2")
    if n == 2:
        return "car"
    if n <= 4:
        return "truck"
    return "heavy"


def main():
    print("==== Running parse_plate ====")
    try:
        print("State, District and Number:", parse_plate(input("Enter a plate (e.g. KA-05-AB-1234): ")))
        print("\n==== Running trip_cost ====")
        print("Trip Cost:", trip_cost(input("Enter trips x rate (e.g. 3x150): ")))
        print("\n==== Running axle_class ====")
        print("Vehicle Class:", axle_class(input("Enter an axle count (e.g. 3): ")))
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
