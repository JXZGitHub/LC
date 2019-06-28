class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited=set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                if self.recurse(r, c, board, 0, visited, word):
                    return True
        return False

    def recurse(self, r, c, matrix, index, visited, target):
        if (r,c) in visited or not (0 <= r < len(matrix) and 0 <= c < len(matrix[r])):
            return False
        if matrix[r][c] != target[index]:
            return False
        if index == len(target) - 1:
            return True
        visited.add((r,c))
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            newR = r + dr
            newC = c + dc
            if self.recurse(newR, newC, matrix, index + 1, visited, target):
                return True
        visited.remove((r,c))
        return False

    # def dfs(self, board, row, col, word):
    #     if len(word) == 0:
    #         return True
    #     if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] == '*':
    #         return False
    #     if word[0] != board[row][col]:  # Skip if first letter of the current word does not match the positions' letter
    #         return False
    #     # If it passes the above tests, it's a match for the current iteration of word
    #     tmp = board[row][col]  # Preserve what was on the board, to be restored later.
    #     board[row][col] = '*'  # Mark this as visited (so the same iteration of recursion won't try ot match it)
    #
    #     # Then, continue to search the REMAINING letters (word[1:]) of the word in the neighbors in the gird
    #     res = self.dfs(board, row + 1, col, word[1:]) or self.dfs(board, row - 1, col, word[1:]) or \
    #           self.dfs(board, row, col + 1, word[1:]) or self.dfs(board, row, col - 1, word[1:])
    #     board[row][col] = tmp
    #     return res

