class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Time: O(N)
        Space: O(1)
        """
        max_profit = float('-inf')
        min_price = float('inf')
        for p in prices:
            min_price = min(p,min_price)
            max_profit = max(p-min_price, max_profit)
        return max_profit

sol =Solution()
print (sol.maxProfit([7,1,5,3,6,4]))