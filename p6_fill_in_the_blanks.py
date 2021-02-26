# Given an array containing None values fill in the None values with most recent
# non None value in the array

import unittest

array1 = [1, None, 2, 3, None, None, 5, None]


def fill_in_the_blanks(c: list) -> list:
    for i in range(len(c)):
        if c[i] is None:
            c[i] = c[i-1]
    return c


print(fill_in_the_blanks([1, None, 2, 3, None, None, 5, None]))


class TestingBlock(unittest.TestCase):
    def test1(self):
        self.assertEqual(fill_in_the_blanks([1, None, 2, 3, None, None, 5, None]),[1, 1, 2, 3, 3, 3, 5, 5])


if __name__ == "__main__":
    unittest.main()