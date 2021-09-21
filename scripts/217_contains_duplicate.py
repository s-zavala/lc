#!/usr/bin/env python3
import logging, unittest

logging.basicConfig(
    filename="217.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

def containsDuplicate(nums: list[int]) -> bool:
    seen = {}
    for n in nums:
        if seen.get(n):
            return True
        else:
            seen[n] = True
    return False

class TestContainsDuplicate(unittest.TestCase):

    def test_empty(self):
        nums = []
        expected = False
        actual = containsDuplicate(nums)
        self.assertEqual(actual, expected)
    
    def test_small_no_dup(self):
        nums = [1, 2]
        expected = False
        actual = containsDuplicate(nums)
        self.assertEqual(actual, expected)
    
    def test_small_dupes(self):
        nums = [1, 1]
        expected = True
        actual = containsDuplicate(nums)
        self.assertEqual(actual, expected)
    
    def test_large_i_small_nums_no_dup(self):
        nums = [100000000, -1]
        expected = False
        actual = containsDuplicate(nums)
        self.assertEqual(actual, expected)
    
    def test_large_i_small_nums_dupes(self):
        nums = [100000000, -10000000]
        expected = False
        actual = containsDuplicate(nums)
        self.assertEqual(expected, actual)
    
    def test_large_nums_no_dupes(self):
        nums = [1,2,3,4,5,6,7]
        exp = False
        act = containsDuplicate(nums)
        self.assertEqual(act, exp)

    def test_large_nums_dupes(self):
        nums = [1,2,3,4,5,6,7,7]
        exp = True
        act = containsDuplicate(nums)
        self.assertEqual(act, exp)

if __name__ == "__main__":
    unittest.main()
