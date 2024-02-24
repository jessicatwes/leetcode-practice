# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Solution - Use two pointers to find the lowest value on the left side for buying and right side for selling to find maximum profit. As move down to find selling price if a lower value is found, replace the buying pointer and move forward with selling.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_buy, right_sell = 0,1
        max_profit = 0
        while right_sell < len(prices):
            if prices[low_buy] < prices[right_sell]:
                profit = prices[right_sell] - prices[low_buy]
                max_profit = max(max_profit, profit)
            else:
                low_buy = right_sell
            right_sell += 1
        return max_profit

# Test case prices = [7,1,5,3,6,4]
# maxProfit(prices) #5
