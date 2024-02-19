### https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums

class Solution:
     def runningSum(self, nums: List[int]) -> List[int]:
        ''' Given an array nums, returnng an array that is running sum of num
        nums: array of int  
        runningsum: array of int '''
        sum = 0
        runningsum = []
        for i in nums:
            sum += i
            runningsum.append(sum)
        return runningsum
