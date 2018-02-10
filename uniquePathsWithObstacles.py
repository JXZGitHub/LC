class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        Follow up for "Unique Paths":

        Now consider if some obstacles are added to the grids. How many unique paths would there be?

        An obstacle and empty space is marked as 1 and 0 respectively in the grid.

        For example,
        There is one obstacle in the middle of a 3x3 grid as illustrated below.

        [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
        The total number of unique paths is 2.
        """

        #If starting cell is 1, then no path is possible.
        if obstacleGrid[0][0] == 1:
            return 0
        #Initialize first grid to be 1 (one way to get to this same cell from itself)
        obstacleGrid[0][0] = 1

        #Populate the first column based on the initial value, 'blocking' any '1' seen as that means its an obstacle.
        for row in range(1, len(obstacleGrid)):
            if obstacleGrid[row][0] == 0:
                obstacleGrid[row][0] += obstacleGrid[row - 1][0]
            else: #One means obstacle, no this cell is unreachable
                obstacleGrid[row][0] = 0

        #Do the same on the first row
        for col in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 0:
                obstacleGrid[0][col] += obstacleGrid[0][col - 1]
            else:
                obstacleGrid[0][col] = 0

        #Then populate the rest of the matrix (starting at 1x1 cell),
        #again blocking out the '1's but setting its paths to 0 (unreachable)
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[row])):
                if obstacleGrid[row][col] == 0:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
                else:
                    obstacleGrid[row][col] = 0

        return obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]