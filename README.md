# Computor v2

## Project Overview
Computor v2 is a mathematical interpreter designed to manage and compute complex numbers, rational numbers, matrices, and polynomial equations. It allows for variable assignments, equation solving, and advanced mathematical operations using a command-line interface. This project builds upon concepts introduced in Computor v1, with enhanced capabilities for resolving expressions and managing mathematical types.

## Features

- **Supported Mathematical Types:**
  - Rational numbers (e.g., `2`, `4.242`)
  - Complex numbers (e.g., `3 + 2i`, `-4 - 4i`)
  - Matrices (e.g., `[[2, 3]; [4, 3]]`)
  - Polynomial equations (up to degree 2)

- **Key Operations:**
  - Assign and reassign variables to any supported mathematical type
  - Perform arithmetic operations on these types
  - Solve mathematical expressions or equations (up to degree 2)
  - Use function definitions for single-variable functions
  - Command evaluation using `?` to return computed values

## Example Usage

- Assign variables:
  ```sh
  > varA = 2
  2
  > varB = 4.242
  4.242
  ```

- Work with complex numbers:
  ```sh
  > varA = 2*i + 3
  3 + 2i
  > varB = -4i - 4
  -4 - 4i
  ```

- Perform matrix operations:
  ```sh
  > matA = [[1, 2]; [3, 2]]
  [1, 2]
  [3, 2]
  ```

- Define and evaluate functions:
  ```sh
  > funA(x) = 2*x^5 + 4*x^2 - 5*x + 4
  2 * x^5 + 4 * x^2 - 5 * x + 4
  ```

- Solve equations:
  ```sh
  > funA(2) + funB(4) = ?
  41
  ```
