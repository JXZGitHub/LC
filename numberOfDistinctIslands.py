class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited, res = set(), set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in visited:
                    island = []
                    self.traverse(grid, visited, row, col, (0, 0), island)
                    if island:
                        res.add(tuple(island))
        return res

    def traverse(self, grid, visited, x, y, coord, island):
        if (x, y) in visited or not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] == 0:
            return
        island.append(coord)
        visited.add((x, y))
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_coord = (coord[0] + d[0], coord[1] + d[1])
            new_x, new_y = x + d[0], y + d[1]
            self.traverse(grid, visited, new_x, new_y, new_coord, island)
sol = Solution()
print (sol.numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))