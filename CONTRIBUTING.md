# Kintsugi

This project is a small, symbolic interpolation library built on SymPy.

## Project structure

```text
kintsugi/
  __init__.py
  __main__.py
  cli.py
  interpolation.py
```

## Public API

```python
from kintsugi import lagrange_interpolation
```

The main entry point is `lagrange_interpolation(points)`, which returns a SymPy expression.

## Contributing

- keep API behavior predictable
- add tests for new behavior
- document changes in `README.md` when user-facing behavior changes
