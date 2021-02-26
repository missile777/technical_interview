import unittest


def move_zeroes(c: list) -> list:
    return [i for i in c if i != 0] + [i for i in c if i == 0]


class TestingBlock(unittest.TestCase):
    def test1(self):
        self.assertEqual(move_zeroes([]), [])

    def test2(self):
        self.assertEqual(move_zeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test3(self):
        self.assertEqual(move_zeroes([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]), [1, 7, 8, 10, 12, 4, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()