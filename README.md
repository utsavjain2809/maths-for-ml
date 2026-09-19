# Maths for Machine Learning

A hands-on learning repository for implementing the mathematics behind machine learning in Python.

The current project is a dependency-free linear algebra toolkit. It uses Python lists and basic arithmetic instead of NumPy so that each operation remains visible and easy to connect to the underlying mathematics. Calculus, probability, statistics, and machine learning applications are planned as the repository grows.

## Current project: linear algebra

The interactive toolkit in `linear-algebra/` supports:

1. Vector addition
2. Vector subtraction
3. Scalar multiplication
4. Linear-dependence checks for two vectors
5. Linear combinations of vectors
6. Applying a 2x2 matrix transformation to a 2D vector
7. Applying multiple 2x2 transformations in sequence
8. Determinants of 2x2 matrices
9. Determinants of 3x3 matrices

The implementation also includes 2x2 matrix multiplication as a reusable operation, although it is not currently exposed as a menu option.

## Requirements

- Python 3.10 or newer
- No third-party Python packages

Python 3.10 is required because the command-line tool uses the `match`/`case` statement.

## Run the toolkit

From the repository root:

```bash
cd linear-algebra
python3 vector_tool.py
```

Choose an operation from the menu and enter vector components separated by spaces. For example:

```text
1 5 8
```

Press Enter without entering a value when the tool offers a vector prompt to exit that input flow. The program parses all vector and matrix components as floating-point values.

## Examples

### Vector operations

```text
Input first vector to add: 1 5
Input second vector to add: 4 3
Vector Addition Result:  [5.0, 8.0]
```

The calculation is:

$$
[1, 5] + [4, 3] = [5, 8]
$$

Scalar multiplication works the same way for every component:

$$
5[4, 9] = [20, 45]
$$

### Matrix transformation

For a 2D vector, enter the transformed basis vectors for the x- and y-axes. For example, entering `[2, 0]` and `[1, 3]` creates the matrix whose columns are those basis vectors:

$$
\begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}
\begin{bmatrix} 3 \\ 4 \end{bmatrix}
=
\begin{bmatrix} 10 \\ 12 \end{bmatrix}
$$

The multiple-transformation option applies this process repeatedly and prints both intermediate and final vectors.

### Linear combinations

The toolkit computes expressions such as:

$$
3[1, 2] + (-1)[4, 5] = [-1, 1]
$$

Enter one vector and its scalar at a time. Press Enter at the next vector prompt when all terms have been entered.

## Project structure

```text
.
├── README.md
└── linear-algebra/
	├── README.md
	├── vector_maths_interface.py
	├── vector_maths_no_numpy.py
	└── vector_tool.py
```

- `vector_maths_interface.py` defines the abstract operation interface.
- `vector_maths_no_numpy.py` implements the operations using plain Python.
- `vector_tool.py` provides the interactive command-line menu.
- `linear-algebra/README.md` contains more detailed notes and examples for the toolkit.

## Known limitations

- Operations that combine vectors require compatible dimensions; invalid dimensions print an error and return `None`.
- Matrix operations are limited to the 2x2 and 3x3 cases currently implemented.
- The linear-dependence check uses direct floating-point comparisons, so very small rounding differences can affect its result.
- The command-line input flow handles invalid vector components, but numeric prompts such as scalar values and transformation counts do not yet provide the same recovery behavior.
- There are currently no automated tests.

## Learning roadmap

Future additions will build on this foundation with more linear algebra, then move into:

- Calculus, derivatives, gradients, and optimization
- Probability and distributions
- Statistics and inference
- Machine learning algorithms that use these concepts

The goal is to understand the mathematics first, implement it directly, and introduce specialized libraries when they add value rather than hide the fundamentals.
