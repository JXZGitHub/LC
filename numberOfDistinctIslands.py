class Solution:
    """
    Time: O(M*N)
    Space: O(M*N)

    """
    def numDistinctIslands(self, grid: 'List[List[int]]') -> 'int':
        visited, distincts, islands = set(), [], set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                self.traverse(distincts, visited, grid, r, c, r, c)
                if distincts:
                    islands.add(tuple(distincts))
                    distincts = []
        return len(islands)

    def traverse(self, distincts, visited, grid, r0, c0, r, c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == 1 and (r, c) not in visited:
            visited.add((r, c))
            distincts.append((r - r0, c - c0))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r + dr, c + dc
                self.traverse(distincts, visited, grid, r0, c0, newR, newC)


sol = Solution()
print (sol.numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))