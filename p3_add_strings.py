import unittest


def add_strings(s1, s2) -> str:
    return str(int(s1)+(int(s2)))


class TestingBlock(unittest.TestCase):
    def test1(self):
        num1 = '364'
        num2 = '1836'
        self.assertEqual(add_strings(num1, num2), '2200')


if __name__ == '__main__':
    unittest.main()