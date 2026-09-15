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

def input_vector(input_text):
    while True:
        try:
            userInput = input(input_text)
            if userInput == '':
                sys.exit()
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


if __name__ == '__main__':
    main()