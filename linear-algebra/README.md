# Vector Maths Toolkit

An interactive, dependency-free learning tool for vector and small-matrix operations in Python. The implementation uses plain lists and arithmetic instead of NumPy so the calculations remain easy to inspect.

## Features

- Add and subtract vectors.
- Multiply a vector by a scalar.
- Check whether two vectors are linearly dependent.
- Compute a linear combination of vectors.
- Apply one or more 2x2 transformations to a 2D vector.
- Multiply two 2x2 matrices through the reusable implementation API.
- Calculate 2x2 and 3x3 determinants.

## Requirements

- Python 3.10 or newer. The command-line tool uses `match`/`case`.
- No third-party libraries.

## Run the tool

From this directory, run:

```bash
python3 vector_tool.py
```

The menu provides these options:

```text
1. Vector Addition
2. Vector Subtraction
3. Scalar Multiplication
4. Linear Dependence Check
5. Linear Combinations
6. Transform Vector
7. Multiple Transformation
8. Find Determinant 2x2 Matrix
9. Find Determinant 3x3 Matrix
```

Enter vector components separated by spaces, for example `1 5 8`. Press Enter without a value at a vector prompt to exit that input flow. Values are parsed as floating-point numbers.

## Examples

### Vector addition

```text
Input first vector to add: 1 5
Input second vector to add: 4 3
Vector Addition Result:  [5.0, 8.0]
```

$$
[1, 5] + [4, 3] = [5, 8]
$$

### Linear dependence

Two vectors are linearly dependent when one is a scalar multiple of the other. For example, `[1, 2]` and `[2, 4]` are dependent because the second vector is $2$ times the first.

```text
Input first vector: 1 2
Input second vector: 2 4
Is Linear Dependent:  True
```

### Matrix transformation

The transformation option builds a matrix from the transformed x- and y-basis vectors. For example, `[2, 0]` and `[1, 3]` produce:

$$
\begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}
\begin{bmatrix} 3 \\ 4 \end{bmatrix}
=
\begin{bmatrix} 10 \\ 12 \end{bmatrix}
$$

The multiple-transformation option repeats this process and prints each intermediate result.

### Determinants

For a 2x2 matrix:

$$
\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc
$$

The 3x3 operation expands the determinant using its 2x2 minors.

## Source files

- `vector_maths_interface.py` defines the abstract operation interface.
- `vector_maths_no_numpy.py` contains the plain-Python implementation.
- `vector_tool.py` provides the interactive command-line interface.

## Notes and limitations

- Vector operations that combine values require compatible dimensions.
- Matrix operations currently support only 2x2 and 3x3 matrices.
- Linear-dependence checks use direct floating-point comparisons, so tiny rounding differences may affect the result.
- Invalid vector components are reprompted, but scalar and transformation-count prompts do not yet have equivalent recovery behavior.
- There are currently no automated tests.
