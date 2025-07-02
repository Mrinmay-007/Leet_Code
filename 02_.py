'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

# Time Complexity: O(n)
# Space Complexity: O(1)
'''


from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 1
        for i in range (1,len(nums)):
            if nums[i] != nums[index-1]:
                nums[index] = nums[i]
                index += 1
        return index
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    new_length = solution.removeDuplicates(nums)
    print("New length:", new_length)
    print("Modified array:", nums[:new_length])