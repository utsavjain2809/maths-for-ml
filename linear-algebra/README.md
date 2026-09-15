# Vector Maths Toolkit

A very basic, interactive tool for learning common vector operations in Python without using NumPy.

The project is intentionally small and uses Python lists and built-in operations so that the underlying calculations are easy to read and understand.

## Features

- Add two vectors with the same number of components.
- Subtract one vector from another.
- Multiply every component of a vector by a scalar.
- Check whether two vectors are linearly dependent.

## Requirements

- Python 3.10 or newer. The program uses Python's `match`/`case` statement.
- No third-party packages are required.

## Run the tool

From this directory, run:

```bash
python vector_tool.py
```

You will be shown a menu:

```text
1. Vector Addition
2. Vector Subtraction
3. Scalar Multiplication
4. Linear Dependence Check
```

Enter the number for the operation you want to try. When entering a vector, type its components separated by spaces. For example:

```text
1 5 8
```

Press Enter without entering a value to exit while entering a vector.

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

## Notes and limitations

- Vectors must have matching dimensions for addition, subtraction, and linear-dependence checks.
- Values are read as `float`, so results are displayed as floating-point numbers.
- This is a learning project, not a replacement for a numerical computing library.
- The linear-dependence check is designed for two vectors and compares calculated values directly, so very small floating-point rounding differences may affect the result.

## Project structure

```text
linear-algebra/
├── README.md
└── vector_tool.py
```
