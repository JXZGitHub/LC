class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]

        Similar to surrounded regions. Start from border and mark visitable cells.
        Time: O(M*N)
        Space: O(M*N)

        """
        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        # Matrix of booleans to denote reachable cells from pacific and atlantic (border cells)
        pacific = [[False for _ in range(cols)]
                   for _ in range(rows)]
        atlantic = [[False for _ in range(cols)]
                    for _ in range(rows)]
        res = []

        # Mark all cells reachable from the borders
        for i in range(rows):
            self.traverse(i, 0, pacific, matrix)
            self.traverse(i, cols - 1, atlantic, matrix)

        # Mark all cells reachable from the borders
        for i in range(cols):
            self.traverse(0, i, pacific, matrix)
            self.traverse(rows - 1, i, atlantic, matrix)

        # Find reachable cells from both atlantic and pacific
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        return res

    def traverse(self, r, c, visited, matrix):
        if visited[r][c]:
            return
        visited[r][c] = True
        for dr, dc in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            newr, newc = r + dr, c + dc
            if not (0 <= newr < len(matrix) and 0 <= newc < len(matrix[0])) or visited[newr][newc]:
                continue
            if matrix[newr][newc] >= matrix[r][c]:
                self.traverse(newr, newc, visited, matrix)


