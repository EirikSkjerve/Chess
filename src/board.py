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
            # bool to keep track of black/white tiles
            black_tile = not black_tile

            for num in range(8):
                # the corner-coordinates of the tile
                ul = (SQUARE_SIZE*i+OFFSET_X, SQUARE_SIZE*(7-num)+OFFSET_Y)
                ur = (SQUARE_SIZE*(i+1)+OFFSET_X, SQUARE_SIZE*(7-num)+OFFSET_Y)
                dl = (SQUARE_SIZE*i+OFFSET_X, SQUARE_SIZE*(7-num+1)+OFFSET_Y)
                dr = (SQUARE_SIZE*(i+1)+OFFSET_X, SQUARE_SIZE*(7-num+1)+OFFSET_Y)

                
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

    def move_piece(self, piece, source, dest):
        x, y = self.strCoor_to_numCoor(dest)
        self.board[x][y].set_piece(piece)
        a, b = self.strCoor_to_numCoor(source)
        self.board[a][b].remove_piece()

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
                    diag_l = self.board[piece_x-1][piece_y-1]
                    diag_r = self.board[piece_x+1][piece_y-1]
                    # check if there is a piece in front of the pawn
                    if not self.board[piece_x][piece_y-1].piece:
                        # pawn moves 2 squares on first move
                        if piece_y==6:
                            self.add_if_not_check(valid_moves, (piece_x, piece_y-2))
                        # pawn moves 1 square forward
                        self.add_if_not_check(valid_moves, (piece_x, piece_y-1))

                    # if diagonal piece is of opposite color, pawn can take
                    if diag_l.piece and diag_l.piece.color != piece.color:
                        self.add_if_not_check(valid_moves, diag_l.coordinate)
                    if diag_r.piece and diag_r.piece.color != piece.color:
                        self.add_if_not_check(valid_moves, diag_r.coordinate)

                if piece.color=="w":
                    diag_l = self.board[piece_x-1][piece_y+1]
                    diag_r = self.board[piece_x+1][piece_y+1]
                    if not self.board[piece_x][piece_y+1].piece:

                        # pawn moves 2 squares on first move
                        if piece_y==1:
                            self.add_if_not_check(valid_moves, (piece_x, piece_y+2))
                        # pawn moves 1 square forward
                        self.add_if_not_check(valid_moves, (piece_x, piece_y+1))

                    # if diagonal piece is of opposite color, pawn can take
                    if diag_l.piece and diag_l.piece.color != piece.color:
                        self.add_if_not_check(valid_moves, diag_l.coordinate)
                    if diag_r.piece and diag_r.piece.color != piece.color:
                        self.add_if_not_check(valid_moves, diag_r.coordinate)


            case "Knight":
                pass
            case "Bishop":
                for i in range(piece_x+1, 8):
                    
                    y_temp = piece_y+(piece_x-i)
                    if not (0 <= y_temp <= 7):
                        continue
                    if self.board[i][y_temp].piece is not None and self.board[i][y_temp].piece.color == piece.color:
                        break

                    self.add_if_not_check(valid_moves, (i, y_temp))
                    # cannot move through another piece
                    if self.board[i][y_temp].piece:
                        break

                for i in range(piece_x-1, -1,-1):
                    
                    y_temp = piece_y-(piece_x-i)
                    if not (0 <= y_temp <= 7):
                        continue
                    if self.board[i][y_temp].piece is not None and self.board[i][y_temp].piece.color == piece.color:
                        break

                    self.add_if_not_check(valid_moves, (i, y_temp))
                    # cannot move through another piece
                    if self.board[i][y_temp].piece:
                        break

                for i in range(piece_x+1, 8):
                    
                    y_temp = piece_y-(piece_x-i)
                    if not (0 <= y_temp <= 7):
                        continue
                    if self.board[i][y_temp].piece is not None and self.board[i][y_temp].piece.color == piece.color:
                        break

                    self.add_if_not_check(valid_moves, (i, y_temp))
                    # cannot move through another piece
                    if self.board[i][y_temp].piece:
                        break

                for i in range(piece_x-1, -1,-1):
                    
                    y_temp = piece_y+(piece_x-i)
                    if not (0 <= y_temp <= 7):
                        continue
                    if self.board[i][y_temp].piece is not None and self.board[i][y_temp].piece.color == piece.color:
                        break

                    self.add_if_not_check(valid_moves, (i, y_temp))
                    # cannot move through another piece
                    if self.board[i][y_temp].piece:
                        break



            case "Rook":
                # check to the right
                for i in range(piece_x+1, 8):
                    
                    if self.board[i][piece_y].piece and self.board[i][piece_y].piece.color == piece.color:
                        break

                    self.add_if_not_check(valid_moves, (i, piece_y))
                    # cannot move through another piece
                    if self.board[i][piece_y].piece:
                        break

                # check to the left
                for i in range(piece_x-1, -1, -1):
                    if self.board[i][piece_y].piece and self.board[i][piece_y].piece.color == piece.color:
                        break

                    self.add_if_not_check(valid_moves, (i, piece_y))
                    if self.board[i][piece_y].piece:
                        break

                # check upwards
                for j in range(piece_y+1, 8):
 
                    if self.board[piece_x][j].piece and self.board[i][piece_y].piece.color == piece.color:
                        break

                    self.add_if_not_check(valid_moves, (piece_x, j))
                    if self.board[piece_x][j].piece:
                        break

                # check below
                for j in range(piece_y-1, -1,-1):
                    if self.board[piece_x][j].piece and self.board[i][piece_y].piece.color == piece.color:
                        break


                    self.add_if_not_check(valid_moves, (piece_x, j))
                    if self.board[piece_x][j].piece:
                        break


            case "Queen":
                pass
            case "King":
                pass
        
        return valid_moves

    def get_all_valid_moves(self, color):
        pass

    # adds a move to the list if the move does not introduce check to the color's king
    def add_if_not_check(self, moves, move):
        # TODO implement checking for check when king is implemented
        if type(move)==str:
            moves.append(move)
        else:
            moves.append(self.numCoor_to_strCoor(move))

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

    def set_piece(self, piece):
        self.piece = piece
    def remove_piece(self):
        self.piece = None
