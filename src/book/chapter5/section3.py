from book.data_structures import Array
from solutions.chapter5.section1.exercise2 import random
from util import range_of


def randomly_permute(A: Array, n: int) -> None:
    """Permutes an array in place, producing a uniform random permutation.

    Implements:
        Randomly-Permute

    Args:
        A: the array to permute
        n: the number of elements in array A
    """
    for i in range_of(1, to=n):
        # if we used two calls to Random(i, n) in the swap instruction, each call could generate a different value
        j = random(i, n)
        A[i], A[j] = A[j], A[i]
