from abc import ABC, abstractmethod

class VectorMaths(ABC):
    @staticmethod
    @abstractmethod
    def add_vectors(vector1, vector2):
        pass

    @staticmethod
    @abstractmethod
    def subtract_vectors(vector1, vector2):
        pass

    @staticmethod
    @abstractmethod
    def scalar_multiply(vector, scalar):
        pass

    @staticmethod
    @abstractmethod
    def is_linear_dependent(vector1, vector2):
        pass

    @staticmethod
    @abstractmethod
    def linear_combination(vectors, scalars): 
        pass

    @staticmethod
    @abstractmethod
    def multiply_vector_2x2_matrix(matrix_2x2, vector):
        pass

    @staticmethod
    @abstractmethod
    def multiply_2x2_matrix(matrix_1, matrix_2):
        pass

    @staticmethod
    @abstractmethod
    def determinant_2x2_matrix(matrix):
        pass

    @staticmethod
    @abstractmethod
    def determinant_3x3_matrix(matrix):
        pass

    @staticmethod
    @abstractmethod
    def input_vector(input_text, kill_program = True):
        pass
    