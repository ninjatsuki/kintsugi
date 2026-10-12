# Kintsugi

Lagrange interpolation in Python with SymPy.

Kintsugi fits a smooth symbolic polynomial through scattered `(x_i, y_i)` points using the classic Lagrange basis construction. It is intentionally small, readable, and reusable enough to be useful both as a library and as a quick command-line tool.

## Why this project exists

The original project was a minimal script that printed a polynomial for a fixed dataset. The goal of this version is to make that idea durable and credible as an open-source project:

- reusable library API
- clear installation and usage instructions
- tests for correctness and failure modes
- packaging metadata for Python tooling
- a basic CI loop for regression checks

## Features

- Symbolic Lagrange interpolation using SymPy
- Validation of malformed or duplicate-point input
- Library functions suitable for scripts or notebooks
- CLI usage for quick polynomial generation

## Installation

From a checkout of this repository:

```bash
python -m pip install -e .
```

If you want development tooling as well:

```bash
python -m pip install -e '.[dev]'
```

## Quick start

```python
from kintsugi import lagrange_interpolation

points = [(0, 1), (1, 3), (2, 9)]
polynomial = lagrange_interpolation(points)
print(polynomial)
# x**2 + x + 1
```

## CLI usage

```bash
python -m kintsugi --point 0,1 --point 1,3 --point 2,9
```

This prints the interpolated polynomial for the supplied points.

## Mathematical behavior

Given points `(x_1, y_1), ..., (x_n, y_n)`, the interpolating polynomial is built as:

```text
P(x) = sum_i y_i * L_i(x)
```

where each basis polynomial is:

```text
L_i(x) = product_{j != i} (x - x_j) / (x_i - x_j)
```

This is the standard Lagrange interpolation formula.

## Input validation

The library rejects invalid inputs such as:

- empty point lists
- points that are not `(x, y)` pairs
- duplicate `x` values (which would make interpolation ambiguous)

## Running tests

```bash
python -m pytest
```

## Contributing

Contributions are welcome. Please keep changes focused, add or update tests when behavior changes, and prefer small, readable improvements over broad refactors.

## License

This project is licensed under the MIT License.
