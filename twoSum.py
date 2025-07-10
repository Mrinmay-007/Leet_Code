

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    lookup = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i
    return []

# Test case
nums = [-3, 4, 3, 90]
# nums= [2,7,11,15]
target = 0
ans = twoSum(nums, target)
print(ans)
