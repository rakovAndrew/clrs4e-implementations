from book.data_structures import Matrix
from book.data_structures import Submatrix
from util import range_of


def matrix_multiply(A: Matrix, B: Matrix, C: Matrix, n: int) -> None:
    """Multiplies two square matrices and adds the result to the third square matrix.

    Implements:
        Matrix-Multiply

    Args:
        A: the first square matrix to multiply
        B: the second square matrix to multiply
        C: the matrix to add the result of the matrix multiplication
        n: the dimension of matrices A and B
    """
    for i in range_of(1, to=n):
        for j in range_of(1, to=n):
            for k in range_of(1, to=n):
                C[i, j] += A[i, k] * B[k, j]


def matrix_multiply_recursive(A: Matrix | Submatrix, B: Matrix | Submatrix, C: Matrix | Submatrix, n: int) -> None:
    """Recursively multiplies two square matrices and adds the result to the third square matrix.

    Implements:
        Matrix-Multiply-Recursive

    Args:
        A: the first square matrix to multiply
        B: the second square matrix to multiply
        C: the matrix to add the result of the matrix multiplication
        n: the dimension of matrices A and B
    """
    if n == 1:
        C[1, 1] += A[1, 1] * B[1, 1]
        return
    (A11, A12, A21, A22), (B11, B12, B21, B22), (C11, C12, C21, C22) = __partition_matrices(A, B, C, n)
    matrix_multiply_recursive(A11, B11, C11, n // 2)
    matrix_multiply_recursive(A11, B12, C12, n // 2)
    matrix_multiply_recursive(A21, B11, C21, n // 2)
    matrix_multiply_recursive(A21, B12, C22, n // 2)
    matrix_multiply_recursive(A12, B21, C11, n // 2)
    matrix_multiply_recursive(A12, B22, C12, n // 2)
    matrix_multiply_recursive(A22, B21, C21, n // 2)
    matrix_multiply_recursive(A22, B22, C22, n // 2)


def __partition_matrices(A, B, C, n):
    return __partition_matrix(A, n), \
        __partition_matrix(B, n), \
        __partition_matrix(C, n)


def __partition_matrix(M, n):
    return Submatrix(M, range_of(1, to=n // 2), range_of(1, to=n // 2)), \
        Submatrix(M, range_of(1, to=n // 2), range_of(n // 2 + 1, to=n)), \
        Submatrix(M, range_of(n // 2 + 1, to=n), range_of(1, to=n // 2)), \
        Submatrix(M, range_of(n // 2 + 1, to=n), range_of(n // 2 + 1, to=n))
