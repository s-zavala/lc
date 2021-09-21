#!/usr/bin/env python3
def twoSum( nums: list[int], target: int) -> list[int]:
    for i in nums:
        for n in nums[nums.index(i)+1:]:
            if i + n == target:
                index_i = nums.index(i)
                index_n = nums.index(n, (index_i+1))
                return [index_i, index_n]

def twoSum_r( nums: list[int], target: int) -> list[int]:
    remain = []
    # Iterate over indexes of nums.
    for i in range(len(nums)):
        # Is the value at nums[i] = the difference btwn target - another value.
        if nums[i] in remain:
            # Return the index of the other value and the index i.
            return [remain.index(nums[i]), i]
        remain.append(target-nums[i])

if __name__ == "__main__":
    nums_all = (
        ([3,3], 6),
        ([2,7,11,5], 13),
        ([6,6,4,9], 15)
    )
    for t in nums_all:
        print(twoSum_r(nums=t[0], target=t[1]))
