#!/usr/bin/env python3
import logging, unittest

logging.basicConfig(
    filename="53.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

def maxSubArrayBF(nums: list[int]) -> int:
    logging.info(f"Array - {nums}")
    max = -100000
    for i in range(len(nums)):
        logging.debug(f"Index i - {i}")
        for j in range(i,len(nums)):
            logging.debug(f"End index j - {j}")
            slice = nums[i:j+1]
            logging.debug(f"Slice/subarray - {slice}")
            s = sum(slice)
            logging.debug(f"Sum of subarray - {s}")
            if s > max:
                max = s
                logging.debug(f"New max - {max}")
    logging.debug(f"Max sum - {max}")
    return max

def maxSubArrayDC(nums: list[int]) -> int:
    def max_sum_from_start(nums):
        "This function finds the maximum contiguous sum of array from 0 index"
        array_sum = 0
        max_sum = float("-inf")
        for num in nums:
            array_sum += num
            if array_sum > max_sum:
                max_sum = array_sum
        return max_sum
    def max_cross_array_sum(nums, left, mid, right):
        "This function finds the maximum contiguous sum of left and right arrays"
        max_sum_of_left = max_sum_from_start(nums[left : mid + 1][::-1])
        max_sum_of_right = max_sum_from_start(nums[mid + 1 : right + 1])
        return max_sum_of_left + max_sum_of_right
    def max_subarray_sum(nums, left, right):
        "Maximum contiguous sub-array sum, using divide and conquer method"
        # base case: array has only one element
        if left == right:
            return nums[right]
        # Recursion
        mid = (left + right) // 2
        left_half_sum = max_subarray_sum(nums, left, mid)
        right_half_sum = max_subarray_sum(nums, mid + 1, right)
        cross_sum = max_cross_array_sum(nums, left, mid, right)
        return max(left_half_sum, right_half_sum, cross_sum)
    nums_len = len(nums)
    return max_subarray_sum(nums, 0, nums_len - 1)

def max_subarray_Kandane(nums):
    """Find the largest sum of any contiguous subarray."""
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(current_sum, 0) + num
        max_sum = max(max_sum, current_sum)
    return max_sum

class TextMaxSubarray(unittest.TestCase):

    def test_small(self):
        nums = [-1]
        exp = -1
        act = max_subarray_Kandane(nums)
        self.assertEqual(act, exp)
    
    def test_simple(self):
        nums = [5,4,-1,7,8]
        exp = 23
        act = max_subarray_Kandane(nums)
        self.assertEqual(act, exp)
    
    def test_signs(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        exp = 6
        act = max_subarray_Kandane(nums)
        self.assertEqual(act, exp)

if __name__ == "__main__":
    unittest.main()
