"""
python -m unittest task_1/solution.py
"""
import unittest


def strict(func):
    def wrap(*args, **kwargs):
        func_ann = func.__annotations__.get("return")
        is_good = all(isinstance(elem, func_ann) for elem in args)
        if not is_good:
            raise TypeError
        return func(*args, **kwargs)

    return wrap


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError

class SumTwoTest(unittest.TestCase):

    def test_sum_two_int(self):
        result = sum_two(1, 2)
        self.assertEqual(3, result, f'Error on test case {self._testMethodName}, got {result}, expected {3}')

    def test_sum_two_wrong_types(self):
        self.assertRaises(TypeError, sum_two, (1, 2.4))

    def test_sum_two_float(self):
        self.assertRaises(TypeError, sum_two, (1.2, 2.4))

    def test_sum_two_bool(self):
        self.assertRaises(TypeError, sum_two, (True, True))

    def test_sum_two_str(self):
        self.assertRaises(TypeError, sum_two, ('foo', "bar"))
