import sys
def add_vectors(vector1, vector2):
    """
        Add two vectors with same dimensions. 
        Let the first vector A have componenets [a1, a2, a3.....]; Let the second vector B have components [b1, b2, b3......]
        The sum of two vectors A and B be C;
        C = A + B; C = [a1+b1, a2+b2, a3+b3......]

        Example: 
        Let Vector A be [1, 5] and Vector B be [4, 3]
        Vector C is A + B; So C = [1+4, 5+3] = [5, 8]
    """

    if len(vector1) != len(vector2):
        print('Dimensions of the vector must be equal.')
        return
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

def subtract_vectors(vector1, vector2):
    """
        Subtract two vectors with same dimensions. 
        Let the first vector A have componenets [a1, a2, a3.....]; Let the second vector B have components [b1, b2, b3......]
        The difference of two vectors A and B be C;
        C = A - B; C = [a1-b1, a2-b2, a3-b3......]

        Example: 
        Let Vector A be [3, 6] and Vector B be [2, 4]
        Vector C is A - B; So C = [3-2, 6-4] = [1, 2]
    """

    if len(vector1) != len(vector2):
        print('Dimensions of the vector must be equal.')
        return
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

def scalar_multiply(vector, scalar):
    """
        Scales the given vector by a scalar. 
        Let the scalar value be c; and let the vector v components be [v1, v2, v3......]
        So cv = c(v1, v2, v3.......) = [c*v1, c*v2, c*v3......]
        Example,
        Let the vector v be [4, 9] and scalar value c be 5:
        So cv = [5*4, 5*9]; cv = [20, 45]
    """
    return [v1 * scalar for v1 in vector]

def is_linear_dependent(vector1, vector2):
    """
        To check is the two vectors collapses into 1D single line. 
        In this case, one vector is a scaled version of another. 
        Let the Vector A and Vector B;
        B = c(A) where c is a scalar
        Here first, we'll calculate the scalar value c using one corresponding non-zero components of vectors.
        Then we'll scale the Vector A by the scalar c and if it is equal to Vector B, it means Vector B is scaled version of Vector A hence linear dependent. 
    """
    if len(vector1) != len(vector2):
        print('Dimensions of the vector must be equal.')
        return
    scalar = 1
    for i in range(len(vector1)):
        if vector1[i] != 0:
            scalar = vector2[i] / vector1[i]
            break
    return all(v2 == v1 * scalar for v1, v2 in zip(vector1, vector2))

def linear_combination(vectors, scalars):
    """
        Calculate Linear Combinations (w): Scale the vectors and then add them
        Let Vector A be x and Vector B be y;
        Let the scalar of Vector A be a and scalar of Vector B be b;
        w = ax + by
    """
    if len(scalars) != len(vectors):
        print('There must be exactly one scalar for every vector.')
        return

    if not vectors:
        return []

    dimensions = len(vectors[0])

    if any(len(vector) != dimensions for vector in vectors):
        print('Dimensions must be same for all vectors.')
        return

    linear_comb = [0] * dimensions
    for i in range(len(vectors)):
        scaled_vector = scalar_multiply(vectors[i], scalars[i])
        linear_comb = add_vectors(linear_comb, scaled_vector)

    return linear_comb

def multiply_vector_2x2_matrix(matrix_2x2, vector):
    """
        Multiply 2x2 matrix with 2x1 column vector. 
        For example:
        [2  4]      .    [4]
        [3  7]      .    [7]

        So, [2x4 + 4x7]     =   [36]
            [3x4 + 7x7]         [61]
    """

    if len(matrix_2x2) != 2:
        print('Matrix must be 2x2.')
        return

    if any(len(matrix_arr) != 2 for matrix_arr in matrix_2x2):
        print('Matrix must be 2x2.')
        return

    if len(vector) != 2:
        print('Please input valid vector.')
        return

    result = [0, 0]
    result[0] = matrix_2x2[0][0] * vector[0] + matrix_2x2[0][1] * vector[1]
    result[1] = matrix_2x2[1][0] * vector[0] + matrix_2x2[1][1] * vector[1]
    return result

def input_vector(input_text, kill_program = True):
    while True:
        try:
            userInput = input(input_text)
            if userInput == '':
                if kill_program:
                    sys.exit()
                else:
                    return None
            return list(map(float, userInput.split()))
        except ValueError:
            print('Please enter vector components seperated by space.')

def main():
    print('======== VECTOR MATHS TOOLKIT BUILT FOR LEARNING PURPOSE ========')
    print('Please select an option from below: ')
    print('1. Vector Addition')
    print('2. Vector Subtraction')
    print('3. Scalar Multiplication')
    print('4. Linear Dependence Check')
    print('5. Linear Combinations')
    print('6. Transform Vector')
    choice = input('Please enter your choice: ')
    match choice:
        case "1":
            vector1 = input_vector("Input first vector to add: ")
            vector2 = input_vector("Input second vector to add: ")
            print('Vector Addition Result: ', add_vectors(vector1, vector2))
        case "2":
            vector1 = input_vector("Input vector to subtract from: ")
            vector2 = input_vector("Input second vector to subtract: ")
            print('Vector Subtraction Result: ', subtract_vectors(vector1, vector2))
        case "3":
            vector = input_vector("Input the vector to scale: ")
            scalar = float(input('Input the scalar value: '))
            print('Result: ', scalar_multiply(vector, scalar))
        case "4":
            vector1 = input_vector("Input first vector: ")
            vector2 = input_vector("Input second vector: ")
            print('Is Linear Dependent: ', is_linear_dependent(vector1, vector2))
        case "5":
            vectors = list()
            scalars = list()
            vector = input_vector('Input Vector ' + str(len(vectors) + 1) + ': ')

            while vector is not None:
                scalar = float(input('Input the scalar value: '))
                vectors.append(vector)
                scalars.append(scalar)
                vector = input_vector('Input Vector ' + str(len(vectors) + 1) + ': ', False)
            print('Result: ', linear_combination(vectors, scalars))
        case "6":
            original_vector = input_vector('Input the original vector: ')
            i_hat = input_vector('Input the transformed î basis vector: ')
            j_hat = input_vector('Input the transformed ĵ basis vector: ')
            print('Transformed Vector:', multiply_vector_2x2_matrix([i_hat, j_hat], original_vector))

if __name__ == '__main__':
    main()