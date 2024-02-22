# https://leetcode.com/problems/move-zeroes/
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.
# Solution - Define counter to set up the two pointers. Loop through and if i is 0, ignore if statement. When i != 0, trade position based on pointer which moves 0 down in position.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        nums: array of int
	nums: array return altered in-place
        '''
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1

# Test case nums = [0,1,0,3,12]
# moveZeroes(nums) #[1,3,12,0,0]
