# Numerical Methods Project

A Python project demonstrating classical numerical methods — polynomial interpolation and numerical integration — using NumPy, SciPy, SymPy, and Matplotlib.

## 📋 Overview

This project contains two main components:

- **Question 7 — Interpolation**: Implements and compares Newton's Divided Difference method and Lagrange interpolation for a given dataset.
- **Question 12 — Numerical Integration**: Implements and compares the Trapezoidal Rule and Simpson's 1/3 Rule for evaluating a definite integral, verified against the exact symbolic result.

## 📁 Project Structure

.
├── main.py # Driver script that runs both questions
├── question7.py # Newton & Lagrange interpolation
├── question12.py # Numerical integration (Trapezoidal & Simpson's rule)
└── README.md


## ⚙️ Requirements

- Python 3.8+
- NumPy
- SciPy
- SymPy
- Matplotlib

### Installation

```bash
pip install numpy scipy sympy matplotlib
```

## 🚀 Usage

### Run the full project (both questions)

```bash
python main.py
```

This will run Question 7 first, then pause and wait for you to press Enter before running Question 12.

### Run a single question

```bash
python question7.py
python question12.py
```

## 📊 Question 7: Newton and Lagrange Interpolation

**Data:**

| x | 1 | 2 | 4 | 7 |
|---|---|---|---|---|
| y | 3 | 6 | 5 | 10 |

**What it does:**
- Builds the divided difference table
- Constructs the Newton interpolation polynomial (symbolic form via SymPy)
- Constructs the Lagrange interpolation polynomial (symbolic form via SymPy)
- Evaluates both polynomials at `x = 5` and verifies they match
- Cross-checks against SciPy's built-in `lagrange` function
- Plots both polynomials along with the original data points

## 📐 Question 12: Numerical Integration

**Function:** f(x) = x³ + 2x + 1, integrated over [0, 2]

**What it does:**
- Computes the exact integral symbolically using SymPy
- Approximates the integral using the Trapezoidal Rule
- Approximates the integral using Simpson's 1/3 Rule (requires an even number of subintervals)
- Displays a results table comparing approximations and absolute errors
- Plots the function, the exact area under the curve, and a visualization of the numerical method(s) used

**Note:** You will be prompted to enter the number of subintervals (`n`). Use an even number if you want Simpson's Rule results as well.

## 📈 Sample Output
============================================================
NUMERICAL METHODS PROJECT

Running Question 7: Interpolation <

Divided Difference Table

...
Newton evaluation at x = 5: ...
Lagrange evaluation at x = 5: ...
✓ Both methods give the same value at x = 5.

Press Enter to continue to Question 12...

Running Question 12: Numerical Integration <

Enter number of subintervals (even for Simpson): 4

Exact integral (symbolic): 14
Exact numeric value: 14.0000000000

============================================================
Numerical Integration Results
Method Approximation Absolute Error
Trapezoidal Rule ... ...
Simpson 1/3 Rule ... ...

## 📝 Notes

- Plots will open in a separate window (via `plt.show()`), so run this in an environment with GUI/display support, or modify the scripts to save figures instead (`plt.savefig(...)`) if running headlessly.
- `main.py` imports `question7` and `question12` as modules, so all three files must be in the same directory.

## 👤 Author
-Sangam Paudel
-Asmit panthi

Numerical Methods Coursework Project