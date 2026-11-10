# L6_L7_36 — Highway Toll Calculator

## Lab 7: Fuzz Testing with Hypothesis

This folder contains the Lab 7 input-validation exercise. The original starter implementation is preserved as
`highway_toll_buggy.py`; the validated implementation is `highway_toll.py`.

### Files

| File | Description |
|---|---|
| `highway_toll_buggy.py` | Original starter implementation, retained for baseline comparison |
| `highway_toll.py` | Corrected input-processing functions |
| `test_highway_toll.py` | Hypothesis property-based tests for all three functions |

### Setup and execution

```bash
python -m pip install pytest hypothesis
pytest -v
```

The tests fuzz arbitrary text inputs and verify that malformed values are rejected with `ValueError`, while accepted values satisfy the expected output constraints. They also test generated valid inputs.

### Input rules applied

- Registration plates follow `AA-00-AA-0000`, with district 01–99 and registration number 0001–9999.
- Trip costs use a positive `count x rate` expression.
- Axle counts are positive integers of at least two: 2 = car, 3–4 = truck, 5+ = heavy.

The original Lab 6 directory is unchanged.
