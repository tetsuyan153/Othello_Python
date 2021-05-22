from xmlrpc.client import Boolean
from stone import Stone, Color

BOARD_SIZE = 8

class ReversiBoard:
    def __init__(self):
        self._cells:Stone = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        cnterPos:int = BOARD_SIZE // 2
        self._cells[cnterPos][cnterPos] = Stone(Color.BLACK)
        self._cells[cnterPos - 1][cnterPos] = Stone(Color.WHITE)
        self._cells[cnterPos][cnterPos - 1] = Stone(Color.WHITE)
        self._cells[cnterPos - 1][cnterPos - 1] = Stone(Color.BLACK)
    

    def printBoard(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                print("%10s" % self._cells[row][col], end="")
            print()