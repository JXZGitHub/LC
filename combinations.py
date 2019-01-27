class Solution2(object):
    """
        Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

        For example,
        If n = 4 and k = 2, a solution is:

        [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ]
        Time O(N!). Space O(N)
    """
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.traverse(n, k, 1, res, [])
        return res

    def traverse(self, n, k, startPos, res, currCombo):
        if len(currCombo) == k:
            res.append(currCombo[:])
            return
        for i in range(startPos, n + 1):
            currCombo.append(i)
            self.traverse(n, k, i + 1, res, currCombo)
            currCombo.pop()

sol = Solution2()
print (sol.combine(4,2))
# print (sol.combine(5,3))
# print (sol.combine(1,1))
# print (sol.combine(2,1))
# print (sol.combine(2,2))
# print (sol.combine(1,0))
#print (sol.combine(20,16))