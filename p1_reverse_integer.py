
import unittest


def reverse_integer(x: int) -> int:
    r = str(x)
    if r[0] == '-':
        r = r[1:]
        return int(r[::-1]) * -1
    return int(r[::-1])


class TestingBlock(unittest.TestCase):
    def test_reverse1(self):
        self.assertEqual(reverse_integer(405), 504)
        self.assertEqual(reverse_integer(-231), -132)

    def test_reverse2(self):
        self.assertEqual(reverse_integer(-106), -601)


if __name__ == '__main__':
    unittest.main()
