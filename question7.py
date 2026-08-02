"""
Question 7: Newton and Lagrange Interpolation (with libraries)
Data: X = [1, 2, 4, 7], Y = [3, 6, 5, 10]
Uses NumPy, SciPy, SymPy, Matplotlib.
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange  # for comparison

def divided_diff_table(x, y):
    """Construct divided difference table and return coefficients."""
    n = len(x)
    table = [y[:]]  # first column is y
    for j in range(1, n):
        col = []
        for i in range(n - j):
            num = table[j-1][i+1] - table[j-1][i]
            den = x[i+j] - x[i]
            col.append(num / den)
        table.append(col)
    coeffs = [table[i][0] for i in range(n)]
    return table, coeffs

def newton_poly(coeffs, x_points, x_val):
    """Evaluate Newton polynomial at x_val."""
    n = len(coeffs)
    result = coeffs[-1]
    for i in range(n-2, -1, -1):
        result = result * (x_val - x_points[i]) + coeffs[i]
    return result

def lagrange_poly(x_points, y_points, x_val):
    """Evaluate Lagrange polynomial at x_val."""
    n = len(x_points)
    result = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x_val - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

def main():
    # Data
    x = np.array([1, 2, 4, 7], dtype=float)
    y = np.array([3, 6, 5, 10], dtype=float)

    # 1. Divided difference table and coefficients
    table, coeffs = divided_diff_table(x, y)
    print("Divided Difference Table")
    print("------------------------")
    header = "x_i\tf[ ]"
    for i in range(1, len(x)):
        header += f"\tf[...,{i}]"
    print(header)
    for i in range(len(x)):
        row = f"{x[i]:.0f}\t"
        for j in range(len(x) - i):
            row += f"{table[j][i]:.4f}\t"
        print(row)
    print()

    # 2. Newton polynomial (symbolic)
    X = sp.Symbol('x')
    newton_expr = coeffs[0]
    prod = 1
    for i in range(1, len(coeffs)):
        prod *= (X - x[i-1])
        newton_expr += coeffs[i] * prod
    print("Newton General Interpolation Polynomial (symbolic):")
    sp.pprint(newton_expr, use_unicode=True)
    print()

    # 3. Evaluate at x=5 using Newton
    x_eval = 5
    newton_val = newton_poly(coeffs, x, x_eval)
    print(f"Newton evaluation at x = {x_eval}: {newton_val:.6f}")

    # 4. Lagrange evaluation at x=5
    lagrange_val = lagrange_poly(x, y, x_eval)
    print(f"Lagrange evaluation at x = {x_eval}: {lagrange_val:.6f}")

    # 5. Verify
    print("\nVerification:")
    if np.isclose(newton_val, lagrange_val, rtol=1e-9):
        print("✓ Both methods give the same value at x = 5.")
    else:
        print("✗ Values differ!")

    # 6. Display Lagrange polynomial (symbolic)
    # Build Lagrange basis symbolically
    lagrange_expr = 0
    for i in range(len(x)):
        basis = 1
        for j in range(len(x)):
            if i != j:
                basis *= (X - x[j]) / (x[i] - x[j])
        lagrange_expr += y[i] * basis
    print("\nLagrange Interpolation Polynomial (symbolic):")
    sp.pprint(sp.expand(lagrange_expr), use_unicode=True)  # expand for clarity

    # (Optional) Compare with SciPy's built-in Lagrange
    scipy_poly = lagrange(x, y)
    scipy_val = scipy_poly(x_eval)
    print(f"\nSciPy Lagrange evaluation at x = {x_eval}: {scipy_val:.6f}")
    print("(Should match our Lagrange value)")

    # Plotting
    x_plot = np.linspace(0, 8, 200)
    # Newton function (vectorized)
    def newton_func(xx):
        return newton_poly(coeffs, x, xx)
    y_newton = np.array([newton_func(xx) for xx in x_plot])
    y_lagrange = lagrange_poly(x, y, x_plot)  # our function works with arrays

    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_newton, 'b-', label='Newton polynomial')
    plt.plot(x_plot, y_lagrange, 'r--', label='Lagrange polynomial')
    plt.plot(x, y, 'ko', markersize=8, label='Data points')
    plt.plot(x_eval, newton_val, 'g*', markersize=12, label=f'x={x_eval}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Newton and Lagrange Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()