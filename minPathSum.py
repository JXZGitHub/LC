class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
        the sum of all numbers along its path.
        Note: You can only move either down or right at any point in time.

        Example 1:
        [[1,3,1],
         [1,5,1],
         [4,2,1]]
        Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.

        Dynamic programing: Create a dp matrix of same dimension as grid. Set all to 0.

        Non edge case: the value of a cell in dp represents the min path sum from that cell to the destination (bottom right most cell)
        dp[row][col] = grid[row][col] + min(dp[row+1][col],dp[row][col+1])

        Base case: The bottom right most cell (destination)'s dp value is simpyl its grid value.
        Edge cases: each cell on the bottom most row and each cell on the right most column is just its current grid value + its previous dp value(previous means right neighbor for bottom edge, and bottom neighbor for right edge.)
        Then we start visiting each node of dp matrix right to left and bottom to top.

        dp[0][0]'s value will be the answer.

        """
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(dp)-1, -1, -1):#Backwards looping: Loops from last index, all the way to -1 (because range is exclusive on the right), step size -1.
            for col in range(len(dp[row])-1, -1, -1):
                if row == len(grid) - 1 and col < len(grid[row]) - 1:
                    # Fill in dp values for bottom edge row
                    dp[row][col] = grid[row][col] + dp[row][col + 1]
                elif row < len(grid) - 1 and col == len(grid[row]) - 1:
                    # Fill in dp values for right edge col
                    dp[row][col] = grid[row][col] + dp[row + 1][col]
                elif row == len(grid) - 1 and col == len(grid[row]) - 1:
                    # Fill in the bottom right (destination) dp, which is simply its value.
                    dp[row][col] = grid[row][col]
                else:
                    # The non-edge case
                    dp[row][col] = grid[row][col] + min(dp[row + 1][col], dp[row][col + 1])

        return dp[0][0]
sol = Solution()
print (sol.minPathSum([[1,3,1], [1,5,1], [4,2,1]]))