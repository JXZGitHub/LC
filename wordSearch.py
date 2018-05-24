class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # visited =[ [ False for _ in range(len(board[0])) ]\
        #           for _ in range(len(board)) ]

        if not board:
            return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                res = self.dfs(board, row, col, word, 0)
                if res:
                    return True
        return False

    def dfs(self, board, row, col, word, count):
        if row > len(board) - 1 or col > len(board[0]) - 1 or row < 0 or col < 0 or board[row][col] == '*' or \
                board[row][col] != word[count]:
            return False
        if count == len(word) - 1:
            return True #If the previous conditions didn't return False, and you made it to the same length as word, then it's a match
        original = board[row][col]
        board[row][col] = '*' #Use '*' to denote visited to avoid repeating same letter during the same search.
        res = self.dfs(board, row + 1, col, word, count + 1) or \
              self.dfs(board, row - 1, col, word, count + 1) or \
              self.dfs(board, row, col + 1, word, count + 1) or \
              self.dfs(board, row, col - 1, word, count + 1)

        board[row][col] = original #Restore to be 'unvisited' once all the search from the current cell terminates.
        return res

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

