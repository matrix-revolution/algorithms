class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_prices = len(prices)
        price_diff = []
        for i in range(0, len_prices-1):
            price_diff.append(prices[i+1] - prices[i])

        max_update = []
        max_val = 0
        for i in range(0, len(price_diff)):
            if i == 0:
                max_update.append(price_diff[i])
                max_val = price_diff[i]
            else:
                max_update.append(max(max_update[i-1]+price_diff[i], price_diff[i]))
                max_val = max(max_val, max_update[i])

        if max_val < 0:
            return 0

        return max_val




def main():
    sol = Solution()
    prices = [5, 2, 1, 10, 12, 1, 9, 8, 2]
    out = sol.maxProfit(prices)
    print out

if __name__ == '__main__':
    main()