# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
# Solution - Given an array, I use a dictionary to store the array value  and corresponding i. I then iteratea across the array and ask if value of target - numis present in the dictionary. If complement_target_num value is found, return the index of complement_target_num and i.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement_target_num = target - num
            if complement_target_num in num_dict:
                return (num_dict[complement_target_num], i)
            num_dict[num] = i

# Test case num_array = [2, 7, 11, 15], target = 13
# twoSum(num_array, target)
