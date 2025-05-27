import unittest


def strict(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], type(args[1])):
            raise TypeError(f"Нет соответствия типов данных.")
        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


class TestSumTwo(unittest.TestCase):
    def test_valid_ints(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sum_two(1, 'b')

    def test_valid_strings(self):
        self.assertEqual(sum_two('a', 'b'), 'ab')

    def test_valid_floats(self):
        self.assertEqual(sum_two(1.5, 2.5), 4.0)

    def test_int_and_float(self):
        with self.assertRaises(TypeError):
            sum_two(5, 3.14)


if __name__ == '__main__':
    unittest.main()
