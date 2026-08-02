"""
Question 12: Numerical Integration with libraries
Evaluate ∫₀² (x³ + 2x + 1) dx
Uses NumPy, SymPy, Matplotlib.
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 2*x + 1

def exact_integral_sym():
    x = sp.Symbol('x')
    expr = x**3 + 2*x + 1
    integral = sp.integrate(expr, (x, 0, 2))
    return float(integral), integral

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = 0.5 * (y[0] + y[-1]) + np.sum(y[1:-1])
    return integral * h

def simpson_rule(a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = y[0] + y[-1]
    integral += 4 * np.sum(y[1:-1:2])
    integral += 2 * np.sum(y[2:-1:2])
    return integral * h / 3

def main():
    # Input
    while True:
        try:
            n = int(input("Enter number of subintervals (even for Simpson): "))
            if n <= 0:
                print("n must be positive.")
                continue
            break
        except ValueError:
            print("Enter an integer.")

    a, b = 0, 2

    # Exact value using SymPy (also analytical)
    exact_val, exact_sym = exact_integral_sym()
    print(f"\nExact integral (symbolic): {exact_sym}")
    print(f"Exact numeric value: {exact_val:.10f}")

    # Numerical methods
    trap_val = trapezoidal_rule(a, b, n)
    trap_err = abs(exact_val - trap_val)

    try:
        simp_val = simpson_rule(a, b, n)
        simp_err = abs(exact_val - simp_val)
    except ValueError as e:
        simp_val = None
        simp_err = None
        print(e)

    # Results table
    print("\n" + "="*60)
    print("Numerical Integration Results")
    print("="*60)
    print(f"{'Method':<20} {'Approximation':<20} {'Absolute Error':<20}")
    print("-"*60)
    print(f"{'Trapezoidal Rule':<20} {trap_val:<20.10f} {trap_err:<20.10f}")
    if simp_val is not None:
        print(f"{'Simpson 1/3 Rule':<20} {simp_val:<20.10f} {simp_err:<20.10f}")
    else:
        print(f"{'Simpson 1/3 Rule':<20} {'Not applicable':<20} {'---':<20}")
    print("="*60)

    # Plot the function and the approximations
    x_plot = np.linspace(a-0.5, b+0.5, 200)
    y_plot = f(x_plot)

    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_plot, 'k-', linewidth=2, label='f(x) = x³ + 2x + 1')
    plt.fill_between(x_plot, 0, y_plot, where=(x_plot>=a)&(x_plot<=b), alpha=0.2, color='gray', label='Exact area')

    # Show trapezoids (if n not too large for visibility)
    if n <= 20:
        x_trap = np.linspace(a, b, n+1)
        y_trap = f(x_trap)
        plt.step(x_trap, y_trap, where='post', color='blue', linestyle='--', linewidth=1, label='Trapezoid steps')
        # Simpson not easy to show via step, but we can show points
        if simp_val is not None:
            x_simp = np.linspace(a, b, n+1)
            y_simp = f(x_simp)
            plt.plot(x_simp, y_simp, 'ro', markersize=4, label='Simpson points')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Numerical Integration Visualization')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()