from unittest import TestCase

from hamcrest import assert_that, is_, close_to
from hypothesis import given
from hypothesis.strategies import lists, floats
from numpy.polynomial import polynomial

from array_util import create_array
from solutions.chapter2.problem3 import polynomial_evaluate


class TestPolynomialEvaluate(TestCase):

    @given(lists(floats(min_value=-10.0, max_value=10.0), min_size=1, max_size=5),
           floats(min_value=-10.0, max_value=10.0))
    def test_polynomial_evaluate(self, coefficients, x):
        A = create_array(coefficients, start=0)
        n = len(coefficients) - 1

        actual_value = polynomial_evaluate(A, n, x)

        expected_value = float(polynomial.polyval(x, coefficients))
        assert_that(actual_value, is_(close_to(expected_value, 1e-7)))
