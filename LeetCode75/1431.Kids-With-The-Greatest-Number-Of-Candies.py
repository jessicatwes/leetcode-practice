# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/ 
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have. Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Solution - Find the max to use for comparison. For each kid, add the extra candies to ask if it is more than the max and return a boolean of if the extra candies would give that kid greatest number of candies amongst kids.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
	'''
	candies: array of int
	extraCandies: int
	kids_candies: array of boolean values
	'''
        max_candies = max(candies)
        kids_candies = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                kids_candies.append(True)
            else:
                kids_candies.append(False)
        return kids_candies

# Test case candies = [2,3,5,1,3], extraCandies = 3
# kidsWithCandies(candies, extraCandies) #[True, True, True, False, True]
