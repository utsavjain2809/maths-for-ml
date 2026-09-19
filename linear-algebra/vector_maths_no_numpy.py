import sys
from vector_maths_interface import VectorMaths
class VectorMathsNoNumPy(VectorMaths):
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

    def multiply_2x2_matrix(matrix_1, matrix_2):
        """
            Multiply 2x2 matrix with 2x2 matrix. 
            For example:
            [2  4]      .    [3  2]
            [3  7]      .    [2  1]

            So, [2x3 + 4x2      2x2 + 4x1]     =   [14  8]
                [3x3 + 7x2      3x2 + 7x1]         [23  13]
        """

        if len(matrix_1) != 2 or len(matrix_2) != 2:
            print('Matrix must be 2x2.')
            return

        if any(len(matrix_arr) != 2 for matrix_arr in matrix_1) or any(len(matrix_arr) != 2 for matrix_arr in matrix_2):
            print('Matrix must be 2x2.')
            return

        result = [[0, 0], [0, 0]]
        result[0][0] = matrix_1[0][0] * matrix_2[0][0] + matrix_1[0][1] * matrix_2[1][0]
        result[0][1] = matrix_1[0][0] * matrix_2[0][1] + matrix_1[0][1] * matrix_2[1][1]

        result[1][0] = matrix_1[1][0] * matrix_2[0][0] + matrix_1[1][1] * matrix_2[1][0]
        result[1][1] = matrix_1[1][0] * matrix_2[0][1] + matrix_1[1][1] * matrix_2[1][1]
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