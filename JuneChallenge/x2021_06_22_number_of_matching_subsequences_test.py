import unittest
from typing import List

from x2021_06_22_number_of_matching_subsequences import Solution

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_example_1(self):
        s: str = "abcde"
        words: List[str] = ["a", "bb", "acd", "ace"]
        expected: int = 3
        result: int = self.solution.numMatchingSubseq(s,words)
        self.assertEqual(result, expected)

    def test_example_2(self):
        s: str = "dsahjpjauf"
        words: List[str] = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
        expected: int = 2
        result: int = self.solution.numMatchingSubseq(s, words)
        self.assertEqual(result, expected)

    def test_example_2(self):
        s: str = "dsahjpjauf"
        words: List[str] = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
        expected: int = 2
        result: int = self.solution.numMatchingSubseq(s, words)
        self.assertEqual(result, expected)

    def test_example_3(self):
        s: str = "a" * 50000
        words: List[str] = [chr(ord('a')+offset) * i for i in range(1,50+1) for offset in range(0,26)]
        expected: int = 50
        result: int = self.solution.numMatchingSubseq(s, words)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
