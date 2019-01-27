class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = 0
        return self.dfs(0, 0, m, n)

    #RECURSIVE, using DFS. Space is (N^2), not feasible.
    def dfs(self, row, col, m, n):
        if row == m - 1 and col == n - 1:
            return 1
        if row > m - 1 or col > n - 1:
            return 0
        if row == m - 1:
            return self.dfs(row, col + 1, m, n)
        if col == n - 1:
            return self.dfs(row + 1, col, m, n)
        return self.dfs(row, col + 1, m, n) + self.dfs(row + 1, col, m, n)


class Solution2(object):
    """
    Iterative, create a grid of m*n, with grid[i][j] representing # of ways to get to i,j from 0,0. Then populate base case
    which is 1 at 0,0. And then poulate all other cases from there.
    This can be improved by
         Speed improvement:  Populating top row and left-most columns first. Then start populating with 1x1 or by
         space improvement: Make grid one dimensional, with size being n (# of columns), because to compute each cell,
         we don't need all other cells present.
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        Time: O(M*N)
        Space: O(M*N)
        """
        dp = [[0 for _ in range(n) ] for _ in range(m) ]
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                if not (r==0 and c==0):
                    if r==0 :
                        dp[r][c] = dp[r][c-1]
                    elif c==0:
                        dp[r][c] = dp[r-1][c]
                    else:
                        dp[r][c] = dp[r][c-1] + dp[r-1][c]

        return dp[m-1][n-1]

    def uniquePaths_1dDP(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        Time: O(M*N)
        Space: O(N)
        """
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for r in range(m):
            for c in range(n):
                if not (r == 0 and c == 0):
                    if r == 0:
                        dp[c] = dp[c - 1]
                    elif c == 0:
                        dp[c] = dp[c]
                    else:
                        dp[c] = dp[c] + dp[c - 1]

        return dp[n - 1]

sol = Solution2()
print (sol.uniquePaths_1dDP(3,2))