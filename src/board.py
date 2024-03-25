class Board:

    def __init__(self):
        self.board = [[None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8]

        self.let_to_num = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

        black_tile = True
        letters = ['a','b','c','d','e','f','g','h']


        for i, let in enumerate(letters[::-1]):
            black_tile = not black_tile

            for num in range(8):
                tile = Tile("b" if black_tile else "w", let+str(num+1))
                self.board[i][num] = tile
                black_tile = not black_tile
                if i == 0 or num == 3:
                    tile.piece = "Pawn"
    def get(self,coors):
        x, y = self.strCoor_to_numCoor(coors)
        if not(0 < x < 7) or not(0 < y < 7):
            raise ValueError
        return self.board[x][y]

    def set(self, coors, piece):
        x, y = self.strCoor_to_numCoor(coors)
        if not(0 <= x <= 7) or not(0 <= y <= 7):
            raise ValueError
        self.board[x][y] = piece

    def strCoor_to_numCoor(self, coors):
        x, y = 7-(int(coors[1])-1) ,self.let_to_num.get(coors[0])
        return (x, y)

    def print_board(self):
        for row in self.board:
            print(row)

class Tile():

    def __init__(self, color, coordinate, piece=None):
        self.color = color
        self.coordinate = coordinate
        self.piece = piece

if __name__ == "__main__":
    testBoard = Board()
    testBoard.print_board()