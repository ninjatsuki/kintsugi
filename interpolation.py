# interpolation.py
"""
Lagrange Interpolation using SymPy

This program computes the Lagrange interpolation polynomial
for a set of given points (x, y) using symbolic computation.
"""

from sympy import symbols, expand

# Input points
x_values = [1, 2, 3, 4]
y_values = [1, 2, 4, 8]

# Placeholder for Lagrange basis polynomials
basis_polys = []

def lagrange_interpolation():
    x = symbols('x')
    
    for i, x_i in enumerate(x_values):
        L_i = 1
        for j, x_j in enumerate(x_values):
            if i != j:
                L_i *= (x - x_j) / (x_i - x_j)
        L_i = expand(L_i)
        basis_polys.append(L_i)
        print(f"L_{i}(x) = {L_i}")
    
    # Construct final interpolation polynomial
    polynomial = sum(y * L for y, L in zip(y_values, basis_polys))
    polynomial = expand(polynomial)
    
    print("\nFinal interpolation polynomial:")
    print(polynomial)
    return polynomial

if __name__ == "__main__":
    lagrange_interpolation()
