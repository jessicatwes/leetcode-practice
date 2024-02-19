### https://leetcode.com/problems/running-sum-of-1d-array/
def runningSum(self, nums):
    ''' Given an array nums, returnng a running sum of array 
    nums: list[int]
    runningsum: list[int] '''
    sum = 0
    runningsum = []
    for i in nums:
        sum += i
        runningsum.append(sum)
        print(i, nums, sum)
    return runningsum

