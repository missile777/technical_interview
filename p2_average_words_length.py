import unittest


def avg_words_len(s: str) -> float:
    s = s.replace('...', ' ') # remove ellipsis
    s = ''.join(i for i in s if i not in ',.!')
    words = s.split(' ')
    nums = [len(i) for i in words]
    return round(sum(nums)/len(nums), 2)


class TestingBlock(unittest.TestCase):
    def test1(self):
        s = "Hi all, my name is Tom...I am originally from Australia."
        self.assertEqual(avg_words_len(s), 3.82)

    def test2(self):
        s = "I need to work very hard to learn more about algorithms in Python!"
        self.assertEqual(avg_words_len(s), 4.08)


if __name__ == '__main__':
    unittest.main()
