from vector_maths_no_numpy import VectorMathsNoNumPy
from vector_maths_interface import VectorMaths

def main():
    print('======== VECTOR MATHS TOOLKIT BUILT FOR LEARNING PURPOSE ========')
    print('Please select an option from below: ')
    print('1. Vector Addition')
    print('2. Vector Subtraction')
    print('3. Scalar Multiplication')
    print('4. Linear Dependence Check')
    print('5. Linear Combinations')
    print('6. Transform Vector')
    print('7. Multiple Transformation')
    print('8. Find Determinant 2x2 Matrix')
    print('9. Find Determinant 3x3 Matrix')
    choice = input('Please enter your choice: ')
    match choice:
        case "1":
            vector1 = VectorMathsNoNumPy.input_vector("Input first vector to add: ")
            vector2 = VectorMathsNoNumPy.input_vector("Input second vector to add: ")
            print('Vector Addition Result: ', VectorMathsNoNumPy.add_vectors(vector1, vector2))
        case "2":
            vector1 = VectorMathsNoNumPy.input_vector("Input vector to subtract from: ")
            vector2 = VectorMathsNoNumPy.input_vector("Input second vector to subtract: ")
            print('Vector Subtraction Result: ', VectorMathsNoNumPy.subtract_vectors(vector1, vector2))
        case "3":
            vector = VectorMathsNoNumPy.input_vector("Input the vector to scale: ")
            scalar = float(input('Input the scalar value: '))
            print('Result: ', VectorMathsNoNumPy.scalar_multiply(vector, scalar))
        case "4":
            vector1 = VectorMathsNoNumPy.input_vector("Input first vector: ")
            vector2 = VectorMathsNoNumPy.input_vector("Input second vector: ")
            print('Is Linear Dependent: ', VectorMathsNoNumPy.is_linear_dependent(vector1, vector2))
        case "5":
            vectors = list()
            scalars = list()
            vector = VectorMathsNoNumPy.input_vector('Input Vector ' + str(len(vectors) + 1) + ': ')

            while vector is not None:
                scalar = float(input('Input the scalar value: '))
                vectors.append(vector)
                scalars.append(scalar)
                vector = VectorMathsNoNumPy.input_vector('Input Vector ' + str(len(vectors) + 1) + ': ', False)
            print('Result: ', VectorMathsNoNumPy.linear_combination(vectors, scalars))
        case "6":
            original_vector = VectorMathsNoNumPy.input_vector('Input the original vector: ')
            i_hat = VectorMathsNoNumPy.input_vector('Input the transformed î basis vector: ')
            j_hat = VectorMathsNoNumPy.input_vector('Input the transformed ĵ basis vector: ')
            print('Transformed Vector:', VectorMathsNoNumPy.multiply_vector_2x2_matrix([[i_hat[0], j_hat[0]], [i_hat[1], j_hat[1]]], original_vector))
        case "7":
            original_vector = VectorMathsNoNumPy.input_vector('Input the original vector: ')
            no_of_transformations = int(input('Input the No of Transformations: '))
            transformed_vector = original_vector
            for i in range(no_of_transformations):
                i_hat = VectorMathsNoNumPy.input_vector('Input the transformed î basis vector for ' + str(i + 1) + 'th transformation: ')
                j_hat = VectorMathsNoNumPy.input_vector('Input the transformed ĵ basis vector for ' + str(i + 1) + 'th transformation: ')
                matrix_1 = [[i_hat[0], j_hat[0]], [i_hat[1], j_hat[1]]]
                transformed_vector = VectorMathsNoNumPy.multiply_vector_2x2_matrix(matrix_1, transformed_vector)
                print('Transformed Vector:', transformed_vector)

            print('Final Transformed Vector:', transformed_vector)
        case "8":
            i_hat = VectorMathsNoNumPy.input_vector('Input the î basis vector for the matrix: ')
            j_hat = VectorMathsNoNumPy.input_vector('Input the ĵ basis vector for the matrix: ')
            matrix_1 = [[i_hat[0], j_hat[0]], [i_hat[1], j_hat[1]]]
            print('Determinant:', VectorMathsNoNumPy.determinant_2x2_matrix(matrix_1))
        case "9":
            i_hat = VectorMathsNoNumPy.input_vector('Input the î basis vector for the matrix: ')
            j_hat = VectorMathsNoNumPy.input_vector('Input the ĵ basis vector for the matrix: ')
            k_hat = VectorMathsNoNumPy.input_vector('Input the k̂ basis vector for the matrix: ')
            matrix_1 = [[i_hat[0], j_hat[0], k_hat[0]], [i_hat[1], j_hat[1], k_hat[1]], [i_hat[2], j_hat[2], k_hat[2]]]
            print('Determinant:', VectorMathsNoNumPy.determinant_3x3_matrix(matrix_1))
if __name__ == '__main__':
    main()