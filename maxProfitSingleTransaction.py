class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')
        for p in prices:
            min_price = min(p,min_price)
            max_profit = max(p-min_price, max_profit)
        return max_profit