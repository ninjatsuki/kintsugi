from __future__ import annotations

import argparse

from .interpolation import lagrange_interpolation


def _parse_point(raw_point: str) -> tuple[float, float]:
    try:
        x_value, y_value = (part.strip() for part in raw_point.split(","))
    except ValueError as exc:  # pragma: no cover - argparse handles path
        raise argparse.ArgumentTypeError(
            "Each point must be specified as x,y, for example 0,1"
        ) from exc

    try:
        return float(x_value), float(y_value)
    except ValueError as exc:  # pragma: no cover - argparse handles path
        raise argparse.ArgumentTypeError(
            "Point coordinates must be numeric values."
        ) from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compute a symbolic Lagrange interpolation polynomial.",
    )
    parser.add_argument(
        "--point",
        dest="points",
        action="append",
        default=[],
        help="Supply one point as x,y; repeat the flag for additional points.",
    )
    args = parser.parse_args(argv)

    if not args.points:
        points = [(1.0, 1.0), (2.0, 2.0), (3.0, 4.0), (4.0, 8.0)]
    else:
        points = [_parse_point(raw_point) for raw_point in args.points]

    polynomial = lagrange_interpolation(points)
    print(polynomial)
    return 0
