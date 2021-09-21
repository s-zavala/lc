#!/usr/bin/env python3
import logging
import unittest

logging.basicConfig(
    filename="88.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)


def merge_quicksort(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Change nums1 in place to a sorted array of all items in nums1 and nums2.
    Uses quicksort.
    Parameters:
    m - length of nums1
    n - length of nums2
    nums1 - sorted list of integers + n slots of 0
    nums2 - sorted list of integers
    Return:
    None
    """
    for i in range(0, n):
        nums1[m+i] = nums2[i]
    
    def quicksort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return quicksort(less) + [pivot] + quicksort(greater)
    sorted = quicksort(nums1)
    for i in range(m+n):
        nums1[i] = sorted[i]

def merge_the_algorithms(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(0, n):
        nums1[m+i] = nums2[i]

    def merge_sort(collection: list) -> list:
        """Pure implementation of the merge sort algorithm in Python
        :param collection: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
        Examples:
        >>> merge_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> merge_sort([])
        []
        >>> merge_sort([-2, -5, -45])
        [-45, -5, -2]
        """

        def merge(left: list, right: list) -> list:
            """merge left and right
            :param left: left collection
            :param right: right collection
            :return: merge result
            """

            def _merge():
                while left and right:
                    yield (left if left[0] <= right[0] else right).pop(0)
                yield from left
                yield from right
            return list(_merge())

        if len(collection) <= 1:
            logging.info(f"Sublist - {collection}")
            return collection
        mid = len(collection) // 2
        logging.info(f"Midpoint - {mid}")
        return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))

    return merge_sort(collection=nums1)

def merge_sort2(nums1: list[int], m: int, nums2: list[int], n: int):
    """ Merge sort."""
    def merge_in_place():
        for i in range(n):
            nums1[m+i] = nums2[i]

    def merge_sort(array):
        logging.info(f"Splitting - {array}")
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]
            # Recursion
            merge_sort(left_half)
            merge_sort(right_half)
            # Indexes
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[i]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k +=1
        logging.info(f"Merging - {array}")

    merge_in_place()
    merge_sort(nums1)
    print(nums1)

def merge_sort3(nums1: list[int], m: int, nums2: list[int], n: int):
    while n > 0 and m > 0:
        # Compare the largest integer from both.
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    while n > 0:
        nums1[n - 1] = nums2[n - 1]
        n -= 1

class TestMerge(unittest.TestCase):

    def test_eg1(self):
        nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
        exp = [1,2,2,3,5,6]
        merge_sort3(nums1, m, nums2, n)
        act = nums1
        self.assertEqual(act, exp)

    def test_eg2(self):
        nums1 = [1]; m = 1; nums2 = []; n = 0
        exp = [1]
        merge_sort3(nums1, m, nums2, n)
        act = nums1
        self.assertEqual(act, exp)

if __name__ == "__main__":
    unittest.main()
