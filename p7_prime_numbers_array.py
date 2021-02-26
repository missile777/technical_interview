
import unittest


def prime_numbers_array(n: int) -> list:
    return [i for i in range(n) if i % 2 == 1]


class TestingBlock(unittest.TestCase):
    def test1(self):
        self.assertEqual(prime_numbers_array(10), [1, 3, 5, 7, 9])

    def test2(self):
        self.assertEqual(prime_numbers_array(5), [1, 3])

    def test3(self):
        self.assertEqual(prime_numbers_array(15), [1, 3, 5, 7, 9, 11, 13])


if __name__ == '__main__':
    unittest.main()