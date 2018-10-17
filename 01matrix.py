class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[-1 for c in range(len(matrix[r]))] for r in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 1:
                    distance = self.traverse(matrix, r, c, res, set())
                    res[r][c] = distance
                else:
                    res[r][c] = 0

        return res

    def traverse(self, matrix, r, c, res, visited):
        visited.add((r, c))
        distance = float('inf')
        if matrix[r][c] == 0:
            return 0
        if matrix[r][c] == 1 and res[r][c] != -1:
            return res[r][c]
        for d in [(0, -1), (1, 0), (-1, 0), (0, 1)]:
            newR, newC = r + d[0], c + d[1]
            if 0 <= newR < len(matrix) and 0 <= newC < len(matrix[0]) and (newR, newC) not in visited:
                distance = min(1 + self.traverse(matrix, newR, newC, res, visited), distance)
        return distance
sol = Solution()

print (sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))