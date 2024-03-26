from piece import Piece, Pawn

class Board:

    def __init__(self, SQUARE_SIZE, OFFSET_X, OFFSET_Y):
        self.board = [[None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8]

        self.let_to_num = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
        self.num_to_let = {0:'a', 1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}

        black_tile = False
        letters = ['a','b','c','d','e','f','g','h']

        for i, let in enumerate(letters):
            print(i)

            black_tile = not black_tile

            for num in range(8):
                # the corner-coordinates of the tile
                ul = (SQUARE_SIZE*i+OFFSET_X, SQUARE_SIZE*(7-num)+OFFSET_Y)
                ur = (SQUARE_SIZE*(i+1)+OFFSET_X, SQUARE_SIZE*(7-num)+OFFSET_Y)
                dl = (SQUARE_SIZE*i+OFFSET_X, SQUARE_SIZE*(7-num+1)+OFFSET_Y)
                dr = (SQUARE_SIZE*(i+1)+OFFSET_X, SQUARE_SIZE*(7-num+1)+OFFSET_Y)

                if (i==1 or i ==2 or i==4) and (num == 1 or num == 4):
                    testPawn = Pawn("w" if not black_tile else "b")
                    tile = Tile("b" if black_tile else "w", let+str((num)+1), (ul, ur, dl, dr), piece=testPawn)
                else:
                    tile = Tile("b" if black_tile else "w", let+str((num)+1), (ul, ur, dl, dr))

                self.board[i][num] = tile
                black_tile = not black_tile

    def get(self,coors):
        x, y = self.strCoor_to_numCoor(coors)
        if not(0 <= x <= 7) or not(0 <= y <= 7):
            raise ValueError
        return self.board[x][y]

    def set(self, coors, piece):
        x, y = self.strCoor_to_numCoor(coors)
        if not(0 <= x <= 7) or not(0 <= y <= 7):
            raise ValueError
        self.board[x][y] = piece

    def strCoor_to_numCoor(self, coors):
        y, x = (int(coors[1])-1) ,self.let_to_num.get(coors[0])
        return (x, y)

    def numCoor_to_strCoor(self, coors):
        x, y = coors
        return self.num_to_let.get(x) + str(y+1)

    def get_valid_moves(self, piece_coor):
        '''
        Get valid moves for a piece on a given coordinate
        piece as input
        '''
        valid_moves = []
        piece_x, piece_y = self.strCoor_to_numCoor(piece_coor)
        tile = self.board[piece_x][piece_y]
        piece = tile.piece
        if not piece:
            print(f"Not a piece here")
            return
        match piece.name:
            case "Pawn":
                if piece.color=="b":
                    if piece_y==1:
                        valid_moves.append(self.numCoor_to_strCoor((piece_x, piece_y-2)))
                    if not self.get(piece_x, piece_y-1):
                        pass
                if piece.color=="w":
                    if piece_y==1:
                        valid_moves.append(self.numCoor_to_strCoor((piece_x, piece_y+2)))
                    if not self.get(piece_x, piece_y-1):
                        pass

                pass
            case "Knight":
                pass
            case "Bishop":
                pass
            case "Rook":
                pass
            case "Queen":
                pass
            case "King":
                pass
        
        return valid_moves

    def get_all_valid_moves(self, color):
        pass

    def print_board(self):
        for row in self.board:
            print(''.join([c.coordinate for c in row]))

class Tile():

    def __init__(self, color, coordinate, screen_coordinates, piece=None):
        self.color = color
        self.coordinate = coordinate
        self.piece = piece

        ul,ur,dl,dr = screen_coordinates  # as (x, y) tuple
        self.ul = ul  # up left
        self.ur = ur  # up right
        self.dl = dl  # down left
        self.dr = dr  # down right
