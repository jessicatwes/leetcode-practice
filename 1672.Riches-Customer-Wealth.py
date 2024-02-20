# https://leetcode.com/problems/richest-customer-wealth/description/
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i customer has in the j bank. Return the wealth that the richest customer has.

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ''' Given a list of accounts, find the max
        accout[i][j]: int[customer][$ in bank]
        '''
        max_wealth = 0
        for i in accounts:
            currentwealth = sum(i)
            max_wealth = max(max_wealth, currentwealth)
        return max_wealth  

# Test case accounts=[[1,5],[7,3],[3,5]]
# maximumWealth(accounts) #10
