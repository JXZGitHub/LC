class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int

        Recursive DFS + Memoization (DP).
        DP[r][c] = The longest increasing path starting from r,c.

        Time: O(R*C)
        Space: Stack Frame: O(R*C). Heap: O(R*C)
        """
        dp = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                res = max(res, self.traverse(matrix, r, c, dp))
        return res

    def traverse(self, matrix, r, c, dp):
        if dp[r][c] > 1:
            return dp[r][c]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newR = r + dr
            newC = c + dc
            if 0 <= newR < len(matrix) and 0 <= newC < len(matrix[0]) and matrix[newR][newC] > matrix[r][c]:
                dp[r][c] = max(dp[r][c], 1 + self.traverse(matrix, newR, newC, dp))
        return dp[r][c]