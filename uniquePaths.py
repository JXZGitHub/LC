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
        """
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if row + col != 0:
                    grid[row][col] = grid[max(row - 1, 0)][col] + grid[row][max(col - 1, 0)]

        return grid[m - 1][n - 1]

sol = Solution2()
print (sol.uniquePaths(10,7))