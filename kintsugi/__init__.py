from __future__ import annotations

from collections.abc import Sequence
from typing import TypeAlias

from sympy import Expr, expand, symbols

Point: TypeAlias = tuple[float, float]


def _normalise_points(points: Sequence[Point]) -> list[Point]:
    """Validate and normalise the input point collection."""
    if not points:
        raise ValueError("At least one point is required for interpolation.")

    normalised: list[Point] = []
    for item in points:
        if len(item) != 2:  # pragma: no cover - defensive programming
            raise ValueError(f"Each point must contain exactly two values: {item!r}")
        x_value, y_value = item
        normalised.append((float(x_value), float(y_value)))

    x_values = [x for x, _ in normalised]
    if len(set(x_values)) != len(x_values):
        raise ValueError("Duplicate x values are not allowed in interpolation input.")

    return normalised


def lagrange_basis_polynomials(
    points: Sequence[Point],
    x_symbol: str | Expr = "x",
) -> list[Expr]:
    """Return the Lagrange basis polynomials for the supplied points."""
    validated = _normalise_points(points)
    x = symbols(x_symbol) if isinstance(x_symbol, str) else x_symbol

    basis_polynomials: list[Expr] = []
    for i, (x_i, _) in enumerate(validated):
        basis = 1
        for j, (x_j, _) in enumerate(validated):
            if i != j:
                basis *= (x - x_j) / (x_i - x_j)
        basis_polynomials.append(expand(basis))

    return basis_polynomials


def lagrange_interpolation(
    points: Sequence[Point],
    x_symbol: str | Expr = "x",
) -> Expr:
    """Construct the interpolating polynomial for a set of `(x, y)` points."""
    validated = _normalise_points(points)
    basis_polynomials = lagrange_basis_polynomials(validated, x_symbol)

    polynomial = sum(y * basis for (_, y), basis in zip(validated, basis_polynomials))
    return expand(polynomial)


def evaluate_polynomial(polynomial: Expr, x_value: float) -> float:
    """Evaluate a polynomial expression at a given x value."""
    x = symbols("x")
    return float(polynomial.subs(x, x_value).evalf())
