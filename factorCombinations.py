import math
class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.recurse(2, n, [], res)
        return res

    def recurse(self, start, n, output, res):
        for i in range(start, int(math.sqrt(n)) + 1):
                q, r = divmod(n, i)  # 8/2 ===> q=4,r=0
                if r == 0:  # If divisble
                    output.append(i)
                    output.append(q)
                    res.append(output[:])
                    output.pop()
                    self.recurse(i, q, output, res)
                    output.pop()
sol = Solution()
print (sol.getFactors(1200))