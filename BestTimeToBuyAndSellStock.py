__author__ = 'rajeevkumar'

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        totalProfit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] - prices[i] > 0:
                totalProfit += prices[i+1] - prices[i]
        return totalProfit
