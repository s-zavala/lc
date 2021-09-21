#!/usr/bin/env python3


def removeDuplicates(nums: list[int]) -> int:
    # Base case 1 - empty list -> no unique integers -> k=0
    if not nums: return 0
    # Base case 2 - array of the same number
    # The array is sorted so no matter how long it is the first value is the same as the last value.
    # k = 1
    if nums[0] == nums[-1]: return 1
    # If neither base case is met then k is greater than 1.
    # Keep k=1 b/c this is the index of the second position in the array.
    k=1
    # Loop over all values in the array.
    for i in range(len(nums)):
        # Skip the first b/c you already know that this is the smallest.
        if i == 0:
            continue
        # Is nums[i] a unique number?
        if nums[i] > nums[i-1]:
            # Write nums[i] to the next place at the beginning of the array.
            nums[k] = nums[i]
            # Increment k by 1.
            k += 1
    return k
        
def removeDuplicates2(nums: list[int]) -> int:
    if len(nums) < 2: return len(nums)
    k=0
    unique = None
    for i in range(len(nums)):
        if nums[i] != unique:
            # unique points to the next unique value.
            unique = nums[i]
            # Replace nums[i] with None.
            nums[i] = None
            # Write nums[k] as the new unique value.
            nums[k] = unique
            # Increment k +1 to move it away from the start.
            k += 1
        else:
            nums[i] = None
    return k

if __name__ == "__main__":
    tests = {
        0: [],
        1: [1,1,1,1,1,1,1,1,1],
        2: [1,1,1,1,1,1,1,1,1,1,2],
        3: [34, 36, 36, 36, 46]
    }
    for ans in tests.keys():
        print(tests[ans])
        print(f"Actual answer - {removeDuplicates2(tests[ans])}")
        print(f"Expected answer - {ans}")
