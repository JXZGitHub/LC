class Side:
    WHITE = 'White'
    BLACK = 'Black'

class MoveResult:
    SUCCESS = 'Success'
    ILLEGAL = 'Illegal'
    BLOCKED = 'Blocked'
    WRONGTURN = 'WrongTurn'

class Position:
    def __init__(self, row, col):
        self.row=row
        self.col=col

class Piece:
    def __init__(self,position,side):
        self.side = side #Either white or black.

    def move(self, fromPosition, toPosition):
        #From its current position, update it to a 'toPosition' if valid
        if self.legalMove(fromPosition, toPosition):
            return True
        else:
            return False

    def legalMove(self, fromPosition, toPosition):
        #Check if such a move is legal or not, to be extended.
        raise NotImplementedError()

    def coveredCells(self, fromPosition, toPosition):
        #Return a list of Positions that cover the whole trail of the piece from A to B
        raise NotImplementedError()

class Pawn (Piece):
    def legalMove(self, fromPosition, toPosition):
        #

    def coveredCells(self, fromPosition, toPosition):
        if not self.legalMove(fromPosition, toPosition):
            return []
        if self.side == Side.BLACK:
            return [ Position(row,fromPosition.col) for row in (range(fromPosition.row-1, toPosition.row+1)) ]
        elif self.side == Side.WHITE:
            return [ Position(row,fromPosition.col) for row in (range(fromPosition.row+1, toPosition.row-1))]

class MoveHandler():
    def __init__(self, board, fromP, toP):
        self.board = board
        self.fromP = fromP
        self.toP = toP
        self.handleMove()

    def handleMove(self):
        piece = self.board.getPiece(self.fromP)
        otherPiece = self.board.getPiece(self.toP)

        if piece.side != self.board.turn:
            return (MoveResult.WRONGTRUN, None)

        if not piece.legalMove():
            return (MoveResult.ILLEGAL, None)

        if self.isBlockedTowardsDestination(piece):
            return (MoveResult.BLOCKED, None)

        if otherPiece!='X' and otherPiece.side == piece.side:
            return (MoveResult.BLOCKED, None)
        elif otherPiece!='X':
            return (MoveResult.SUCCESS, otherPiece)
        else:
            return (MoveResult.SUCCESS, None)

    def isBlockedTowardsDestination(self, piece):
        for p in piece.coveredCells(self.fromP, self.toP):
            if not self.board.getPiece(p) == 'X':
                return True
        return False



class Board:
    def __init__(self):
        self.board = [['X' for _ in range(8)] for _ in range(8)]
        #Initialize board
        self.board[0][0] = Pawn(Side.BLACK)
        #..................
        #self.board[7][7] = Rook(Side.WHITE)
        ##########
        self.captured = []
        self.turn = Side.BLACK

    def getPiece(self, position):
        if 0 <= position.x < 8 and \
           0 <= position.y < 8:
            #Legal
            return self.board[position.row][position.col]
        else:
            return None

    def move(self, fromP, toP):
        (status,captured) = MoveHandler(self.board, fromP, toP)
        otherPiece = self.board[toP.row][toP.col]

        if status == MoveResult.SUCCESS:
            piece = self.board[fromP.row][fromP.col]
            self.board[fromP.row][fromP.col] = 'X'
            self.board[toP.row][toP.col] = piece
            self.turn = Side.WHITE if piece.side == Side.BLACK else Side.BLACK
        if captured:
            self.captured.append(otherPiece)
        print (status)