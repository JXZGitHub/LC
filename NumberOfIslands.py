# 11110
# 11010
# 11000
# 00000

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[False for j in range(len(grid[i]))] \
                   for i in range(len(grid))]
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if not visited[row][col] and grid[row][col] == '1':
                    self.traverseIslands(row, col, grid, visited)
                    islands += 1

        return islands

    def traverseIslands(self, row, col, grid, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or visited[row][col] or grid[row][col] == '0':
            return
        else:
            visited[row][col] = 1
            self.traverseIslands(row + 1, col, grid, visited)
            self.traverseIslands(row - 1, col, grid, visited)
            self.traverseIslands(row, col + 1, grid, visited)
            self.traverseIslands(row, col - 1, grid, visited)
