class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        Time: O(M*N)
        Space: O(M*N)

        As it moves to the right, evertime it hits an obstacle (an edge or a previously visited cell), it'll either down, left, or up.
        So its directions are always in the same order: right, down, left up. Starting with right, it'll move to the next direction no matter what type of obstacle it is.

        """
        if not matrix:
            return []

        seen = [[False for _ in range(len(matrix[0]))]
                for _ in range(len(matrix))]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # [(row increment, col increment), ....], right, down, left, up.
        res = []
        r, c = 0, 0  # initial location on matrix
        nextDirection = 0  # The position in the directions list, which will be cycled through.
        totalCells = len(matrix) * len(matrix[0])
        for _ in range(totalCells):
            seen[r][c] = True
            res.append(matrix[r][c])
            future_r, future_c = r + directions[nextDirection][0], c + directions[nextDirection][1]  # Continue moving in existing direction ( assuming no obstacle)
            if 0 <= future_r < len(matrix) and 0 <= future_c < len(matrix[0]) and not seen[future_r][future_c]:  # NOT hitting an edge and not visited before.
                r, c = future_r, future_c
            else:
                nextDirection = (nextDirection + 1) % 4  # the future_r,future_c is an obstacle (seen or edge), so it needs to change direction, so just pick the next direction in the cycle.
                r, c = r + directions[nextDirection][0], c + directions[nextDirection][1]  # update r and c locations according to new direction.

        return res

sol = Solution()
print (sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
