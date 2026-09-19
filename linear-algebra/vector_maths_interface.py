from abc import ABC, abstractmethod

class VectorMaths(ABC):
    @abstractmethod
    def add_vectors(vector1, vector2):
        pass

    def subtract_vectors(vector1, vector2):
        pass

    def scalar_multiply(vector, scalar):
        pass

    def is_linear_dependent(vector1, vector2):
        pass

    def linear_combination(vectors, scalars): 
        pass

    def multiply_vector_2x2_matrix(matrix_2x2, vector):
        pass

    def multiply_2x2_matrix(matrix_1, matrix_2):
        pass

    def input_vector(input_text, kill_program = True):
        pass