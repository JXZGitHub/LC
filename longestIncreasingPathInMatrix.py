class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int

        Recursive DFS + Memoization (DP)

        Time: O(R*C)
        Space: Stack Frame: O(R*C). Heap: O(R*C)
        """
        cache = {}  # key is (r,c), and value is the longest increasing path starting from this location.
        maxLen = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                maxLen = max(self.recurse(matrix, r, c, cache), maxLen)
        return maxLen

    def recurse(self, matrix, r, c, cache):
        if (r, c) in cache:
            return cache[(r, c)]
        maxLen = 1
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            newR = r + dr
            newC = c + dc
            if newR == len(matrix) or newR < 0 or newC == len(matrix[0]) or newC < 0:
                continue  # The next location is out of bounds, don't go there. Skip to try next direcion.
            if matrix[r][c] >= matrix[newR][newC]:
                continue  # The next location is not increasing, don't go there. Skip to try next direcion.

            # The next location is increasing, keep count of it
            currLen = 1 + self.recurse(matrix, newR, newC, cache)

            maxLen = max(currLen, maxLen)  # At each given node, it can have multiple length in multiple directions, so only keep the longest.

        cache[(r, c)] = maxLen #Base case, r,c has nowhere to go, so longest path from r,c is maxLen which is initialized at 1.
        return maxLen