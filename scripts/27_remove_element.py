#!/usr/bin/env python3
import logging
import unittest

logging.basicConfig(
    filename="27.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

def removeElement(nums: list[int], val: int) -> int:
    logging.info(f"int array - {nums}")
    k = 0
    unique = None
    logging.info(f"array length - {len(nums)}")
    for i in range(len(nums)):
        if nums[i] == val:
            logging.info(f"value occurance found, deleting.")
            nums[i] = None
        else:
            logging.info(f"unique int {nums[i]} found that != val.")
            unique = nums[i]
            nums[i] = None
            nums[k] = unique
            k += 1
    return k

class TestLCFunction(unittest.TestCase):

    def test_empty(self):
        nums = []
        val = 0
        exp = 0
        self.assertEqual(removeElement(nums, val), exp)
    
    def test_small(self):
        nums = [0]
        val = 0
        exp = 0
        self.assertEqual(removeElement(nums, val), exp)
    
    def test_small2(self):
        nums = [0]
        val = 1
        exp = 1
        self.assertEqual(removeElement(nums, val), exp)
    
    def test_large(self):
        nums = [0, 2, 0, 18, 4, 20, 11, 18, 14, 11]
        val = 0
        exp = 8
        self.assertEqual(removeElement(nums, val), exp)

if __name__ == "__main__":
    unittest.main()