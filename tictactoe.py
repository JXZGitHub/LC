class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.size = n

        # n lists of rows and columns, each list has 2 elements for the 2 players to populate
        self.rows = [[0,0] for _ in range(n)]
        self.columns = [[0,0] for _ in range(n)]

        #single list of diagnonal and reverse-diagonal as there's only one each regardless of grid size.
        self.diagonal = [0,0]
        self.reverse_diagonal = [0,0]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param i The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        i = player - 1 #converts (1 or 2) into (0 or 1) for populating the lists of rows/cols/diagonals/reverse-diagonals

        # eg: for (row,col) = (1,1), increment each row/col list at the player's (0 or 1)'s location.
        self.rows[row][i] += 1
        self.columns[col][i] +=1

        if row == col:
            self.diagonal[i] +=1
        if row == self.size - col - 1:
            #Reverse diagonal's row and col locations are always opposite ends
            self.reverse_diagonal[i] += 1
        if any([self.rows[row][i] == self.size, self.columns[col][i] == self.size,
                self.diagonal[i] == self.size, self.reverse_diagonal[i] == self.size]):
            return player
        else:
            return 0

print ("-----------size 3x3 ---------")
toe = TicTacToe(3)
print (toe.move(0, 0, 1))
print (toe.move(0, 0, 2))
print (toe.move(2, 2, 1))
print (toe.move(1, 1, 2))
print (toe.move(2, 0, 1))
print (toe.move(1, 0, 2))
print (toe.move(2, 1, 1))
print ("-----------size 2x2 ---------")
toe = TicTacToe(2)
print (toe.move(0, 1, 2))
print (toe.move(1, 0, 1))
print (toe.move(1, 1, 2))

