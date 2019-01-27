class Solution:
    def numberOfLiveNeighbors(self, r, c, board):
        count = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            newR, newC = r + dr, c + dc
            if 0 <= newR < len(board) and 0 <= newC < len(board[0]):
                if board[newR][newC] in (1, 'Zero'):
                    # You can also do:
                    # if board[newR][newC] in (1,2):
                    count += 1
        return count

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.

        Time: O(M*N)
        Space: O(1)

        Search for live neighbors in each cell, and update cell to a 'temporary' value.
        Then traverse matrix again and translate temporray value into either 1 or 0 (alive or dead for next round)

        The temporary value can be 2 for 0, 3 for 1.
        And translation is temporary value % 2. Or temporary value >> 1 (bit wise right shift.)

        Or temporary value can be any string.

        """
        for r in range(len(board)):
            for c in range(len(board[r])):
                liveNeighbors = self.numberOfLiveNeighbors(r, c, board)
                if board[r][c] == 1 and liveNeighbors not in (2, 3):
                    board[r][c] = 'Zero'
                    # You can also do:
                    # board[r][c] = 2
                elif board[r][c] == 0 and liveNeighbors == 3:
                    board[r][c] = 'One'
                    # You can also do:
                    # board[r][c] = 3
        for r in range(len(board)):
            for c in range(len(board[r])):
                # You can also do:
                # board[r][c] = board[r][c] % 2 # 3 will result in 1(alive), 2 will result in 0 (dead)
                if board[r][c] == 'One':
                    board[r][c] = 1
                elif board[r][c] == 'Zero':
                    board[r][c] = 0

