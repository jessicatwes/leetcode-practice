# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Solution - Create a dictionary and iterate through the array and ask if the value alrady in the dictionary. If not, append the value into the dictionary.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num in num_dict.keys():
                return True
            else:
                num_dict[num] = 0
        return False

# Test case nums = [1,1,1,3,3,4,3,2,4,2]
# containsDuplicate(nums) #true
