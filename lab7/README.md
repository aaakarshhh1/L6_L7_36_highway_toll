# L6_L7_36 — Highway Toll Calculator

## Lab 7: Fuzz Testing with Hypothesis

This folder contains the Lab 7 input-validation exercise. The original starter implementation is preserved as
`highway_toll_buggy.py`; the validated implementation is `highway_toll.py`.

### Files

| File | Description |
|---|---|
| `highway_toll_buggy.py` | Original starter implementation, retained for baseline comparison |
| `highway_toll.py` | Corrected input-processing functions |
| `test_highway_toll.py` | Six Hypothesis property-based tests for all three functions |
| `hypothesis_bug_demo.py` | Intentional pre-fix tests; expected to fail against the buggy implementation |

### Setup and execution

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest hypothesis
```

Run the corrected test suite:

```bash
python -m pytest -v test_highway_toll.py
```

The corrected suite should report **6 passed**.

To reproduce the original defects, run the separate demonstration explicitly:

```bash
python -m pytest -v hypothesis_bug_demo.py
```

Those three tests are intentionally expected to fail against `highway_toll_buggy.py`. The file is named
`hypothesis_bug_demo.py` rather than `test_*.py` so it is not collected during the normal test run.

### Input rules applied

- Registration plates follow `AA-00-AA-0000`, with district 01–99 and registration number 0001–9999.
- Trip costs use a positive `count x rate` expression.
- Axle counts must be integers of at least two: 2 = car, 3–4 = truck, 5+ = heavy.

The original Lab 6 directory is unchanged.
