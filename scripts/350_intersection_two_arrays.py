#!/usr/bin/env python3
import unittest


def intersect( nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) < len(nums2):
        short, long = nums1, nums2
    else:
        short, long = nums2, nums1
    ans = []
    for i in range(len(short)):
        for j in range(len(long)):
            if long[j] != None:
                if short[i] == long[j]:
                    ans.append(short[i])
                    long[j] = None
                    break
    return ans

def intersect2(nums1: list[int], nums2: list[int]) -> list[int]:
    # list.sort() O(nlogn)
    nums1.sort()
    nums2.sort()
    # Compare the lengths of the arrays.
    if len(nums1) < len(nums2):
        shorter, longer = nums1, nums2
    else:
        shorter, longer = nums2, nums1
    ct = {}
    # Make a hash table of integers in the shorter array. O(n)
    while shorter:
        if ct.get(shorter[-1]):
            ct[shorter[-1]] += 1
            shorter.pop()
        else:
            ct[shorter[-1]] = 1
            shorter.pop()
    # Loop over integers in longer.
    for num in longer:
        if ct.get(num):
            ct[num] -= 1
            shorter.append(num)
            if not any(ct.values()):
                break
    return shorter

class TestIntersect(unittest.TestCase):

    def test_eg1(self):
        nums1 = [1,2,2,1]; nums2 = [2,2]
        exp = [2,2]
        act = intersect2(nums1, nums2)
        self.assertCountEqual(act, exp)
    
    def test_eg2(self):
        nums1 = [4,9,5]; nums2 = [9,4,9,8,4]
        exp = [9,4]
        act = intersect2(nums1, nums2)
        self.assertCountEqual(act, exp)
    
    def test_zeroes(self):
        nums1, nums2 = [8,0,3], [0,0]
        exp = [0]
        act = intersect2(nums1, nums2)
        self.assertCountEqual(act, exp)


if __name__ == "__main__":
    unittest.main()