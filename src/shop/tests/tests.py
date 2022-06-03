import unittest

from django.test import TestCase


# from fibonacci import *


class MyFirstTest(TestCase):
    def test_my_first_test(self):
        assert 1 == 1


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fibbonachi = Fibonacci()

    # The input tо the Fibonacci sequence must be a non-negative integer
    def test_numbers(self):
        actual_result = self.fibbonachi(n=1)
        self.assertEqual(1, actual_result)


def formatted_name(first_name, last_name, middle_name=""):
    if len(middle_name) > 0:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


class TestFormatedname(unittest.TestCase):
    def test_first_last_name(self):
        result = formatted_name("vlad", "kostiuk")
        self.assertEqual(result, "Vlad Kostiuk")

    def test_first_last_middle_name(self):
        result = formatted_name("vlad", "yurievich", "kostiuk")
        self.assertEqual(result, "Vlad Kostiuk Yurievich")
