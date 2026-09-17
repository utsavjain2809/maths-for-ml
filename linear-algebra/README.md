# Vector Maths Toolkit

> Note: This README was written by AI.

A small, interactive learning tool for common vector operations in Python without using NumPy.

The project intentionally uses plain Python lists and basic arithmetic so the calculations are easy to follow and understand.

## Features

- Add two vectors with the same number of components.
- Subtract one vector from another.
- Multiply every element of a vector by a scalar.
- Check whether two vectors are linearly dependent.
- Compute a linear combination of multiple vectors using corresponding scalars.
- Transform a 2D vector using a 2x2 matrix built from two transformed basis vectors.

## Requirements

- Python 3.10 or newer. The script uses Python's `match`/`case` statement.
- No third-party libraries are required.

## Run the tool

From this directory, run:

```bash
python vector_tool.py
```

You will see this menu:

```text
======== VECTOR MATHS TOOLKIT BUILT FOR LEARNING PURPOSE ========
Please select an option from below:
1. Vector Addition
2. Vector Subtraction
3. Scalar Multiplication
4. Linear Dependence Check
5. Linear Combinations
6. Transform Vector
```

When entering a vector, type its components separated by spaces. For example:

```text
1 5 8
```

Press Enter without entering any value to exit while entering a vector.

## Examples

### Vector addition

```text
Input first vector to add: 1 5
Input second vector to add: 4 3
Vector Addition Result:  [5.0, 8.0]
```

This calculates:

$$
[1, 5] + [4, 3] = [1 + 4, 5 + 3] = [5, 8]
$$

### Vector subtraction

```text
Input vector to subtract from: 3 6
Input second vector to subtract: 2 4
Vector Subtraction Result:  [1.0, 2.0]
```

### Scalar multiplication

```text
Input the vector to scale: 4 9
Input the scalar value: 5
Result:  [20.0, 45.0]
```

### Linear dependence

Two vectors are linearly dependent when one is a scalar multiple of the other. For example, `[1, 2]` and `[2, 4]` are linearly dependent because the second vector is $2$ times the first.

```text
Input first vector: 1 2
Input second vector: 2 4
Is Linear Dependent:  True
```

### Linear combination

The script can combine several vectors with scalar coefficients. For instance, if you enter:

```text
Input Vector 1: 1 2
Input the scalar value: 3
Input Vector 2: 4 5
Input the scalar value: -1
```

it computes:

$$
3[1, 2] + (-1)[4, 5] = [-1, 1]
$$

### Transform vector with a 2x2 matrix

This option expects the original vector and the transformed basis vectors for the x- and y-axes:

```text
Input the original vector: 3 4
Input the transformed î basis vector: 2 0
Input the transformed ĵ basis vector: 1 3
Transformed Vector: [10.0, 12.0]
```

This computes:

$$
\begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}
\begin{bmatrix} 3 \\ 4 \end{bmatrix}
=
\begin{bmatrix} 10 \\ 12 \end{bmatrix}
$$

## Notes and limitations

- Vectors must have matching dimensions for addition, subtraction, and linear-dependence checks.
- A linear combination requires one scalar for each vector, and all vectors must have the same length.
- The program reads values as `float`, so output is displayed as floating-point numbers.
- The linear dependence check compares values directly after computing a scalar ratio from the first non-zero component, so tiny floating-point rounding differences may affect the result.
- This is a learning project and not a replacement for a numerical computing library such as NumPy.

## Project structure

```text
linear-algebra/
├── README.md
└── vector_tool.py
```
