"""
Test the factorial(n) is equal to n!
Testcases are taken from https://en.wikipedia.org/wiki/Factorial
"""

from ..factorial.factorial import factorial, factorial_loop, factorial_recursive


cases = (
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),
    (11, 39916800),
    (12, 479001600),
    (13, 6227020800),
    (14, 87178291200),
    (15, 1307674368000),
    (16, 20922789888000),
    (17, 355687428096000),
    (18, 6402373705728000),
    (19, 121645100408832000),
    (20, 2432902008176640000),
)

def notest_factorial_return():
    for case in cases:
        assert factorial(case[0]) == case[1]

def test_factorial_recursive():
    for case in cases:
        assert factorial_recursive(case[0]) == case[1], "Bad factorial return value"

def test_factorial_loop():
    for case in cases:
        assert factorial_loop(case[0]) == case[1], "Bad factorial return value"
