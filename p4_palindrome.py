import unittest


def palindrome(s: str) -> bool:
    return s == s[::-1]


class TestingBlock(unittest.TestCase):
    def test1(self):
        self.assertEqual(palindrome('racecar'), True)

    def test2(self):
        self.assertEqual(palindrome('know'), False)

    def test3(self):
        self.assertEqual(palindrome('topotopot'), True)


if __name__ == '__main__':
    unittest.main()