import pygame 
from board import Board
from piece import Piece, Pawn, Bishop, Rook, Knight, King, Queen

'''
Main loop for the window
'''
def menu():
    pass

def draw_board():

    font = pygame.font.Font('C:/Users/eirik/OneDrive - University of Bergen/Chess/src/Utils/arial.ttf', 18)

    for y in range(8):
        for x in range(8):
            # draw the squares
            # get the tile object
            tile = gameboard.board[x][y]
            # get its coordinates
            tile_top, tile_left = tile.ul
            # create the square for this tile
            rect = pygame.Rect(tile_top, tile_left, SQUARE_SIZE,SQUARE_SIZE)
            # draw the square with correct color
            pygame.draw.rect(SCREEN, dark_square_color if tile.color == "b" else light_square_color, rect, SQUARE_SIZE)

            # mark possible moves if a piece is clicked
            if move_indicator and tile.coordinate in move_indicator:
                indicator_surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
                indicator_surf.fill((60,60,200) if tile.color == "w" else (40,40,200))
                SCREEN.blit(indicator_surf, (tile_top, tile_left))

            tile_down, tile_right = tile.dr
            # draw coordinate on each tile
            tileText = font.render(tile.coordinate, True, (255, 255, 255) if tile.color == "b" else (35, 35, 35))
            tileTextRect = tileText.get_rect() 
            tileTextRect.center = (tile_down-10, tile_right-10)
            SCREEN.blit(tileText, tileTextRect)

            if tile.piece is not None:
                piece = tile.piece
                piece_surf = pygame.Surface((SQUARE_SIZE//2, SQUARE_SIZE//2))
                piece_surf.fill((50, 255, 50) if piece.color == "w" else (255,50,50))
                SCREEN.blit(piece_surf, (tile_down-50, tile_right-50))

                # display name of piece
                piece_text = font.render(piece.name[:2], True, (255,255,255) if piece.color == "b" else (10,10,10))
                piece_text_rect = piece_text.get_rect()
                piece_text_rect.center = (tile_down-35, tile_right-35)
                SCREEN.blit(piece_text, piece_text_rect)

def draw_game_info():
    font = pygame.font.Font('C:/Users/eirik/OneDrive - University of Bergen/Chess/src/Utils/arial.ttf', 18)

    info_box = pygame.Rect(8*SQUARE_SIZE + 2*OFFSET_X, OFFSET_Y, 7*SQUARE_SIZE, 8*SQUARE_SIZE)
    pygame.draw.rect(SCREEN, (80,80,80), info_box, 7*SQUARE_SIZE)
    if len(piece_selected) == 2:
        move_string_piece = f"Valid moves for {piece_selected[0].name} at {piece_selected[1]}:"
        move_string_pos = f"{', '.join([x for x in move_indicator])}"
    else:
        move_string_piece = ""
        move_string_pos = ""
    move_text = font.render(move_string_piece, True, (255,255,255))
    move_text_2 = font.render(move_string_pos, True, (255,255,255))
    move_text_rect = move_text.get_rect()
    text_width = move_text_rect.width
    move_text_rect_2 = move_text_2.get_rect()
    text_2_width = move_text_rect_2.width

    move_text_rect.center = (8*SQUARE_SIZE + 2*OFFSET_X + text_width//2, OFFSET_Y+10)
    move_text_rect_2.center = (8*SQUARE_SIZE + 2*OFFSET_X + text_2_width//2, OFFSET_Y+10+move_text_2.get_height()+5)
    SCREEN.blit(move_text, move_text_rect)
    SCREEN.blit(move_text_2, move_text_rect_2)

# returns the board coordinate if a tile was clicked
def get_tile_clicked(event):
    event_dict = event.dict
    mouse_pos_x, mouse_pos_y = event_dict.get('pos')
    for i in range(len(gameboard.board)):
        for j in range(len(gameboard.board[i])):
            tile = gameboard.board[i][j]
            ul, dr = tile.ul, tile.dr
            x1,y1 = ul
            x2,y2 = dr
            if x1 < mouse_pos_x < x2 and y1 < mouse_pos_y < y2:
                return(tile.coordinate)

# selects a piece or moves a piece if already selected.
def handle_tile_click(tile_cliked):
    moved = False
    tile = gameboard.get(tile_cliked)
    if len(piece_selected) == 2:
        if tile.coordinate in move_indicator and tile.coordinate != piece_selected[1]:
            gameboard.move_piece(piece_selected[0],piece_selected[1], tile.coordinate)
            moved = True
        move_indicator.clear()
        piece_selected.clear()

    if tile.piece and len(piece_selected)!=2 and not moved:
        piece = tile.piece
        piece_selected.append(piece)
        piece_selected.append(tile.coordinate)
        print(f"Piece {piece.name} on tile {tile.coordinate}. Valid moves are: {', '.join(gameboard.get_valid_moves(tile.coordinate))}")
        move_indicator.clear()
        for x in gameboard.get_valid_moves(tile.coordinate):
            move_indicator.append(x)

def initialize_board():
    for i in range(8):
        whitePawn = Pawn("w")
        blackPawn = Pawn("b")
        gameboard.board[i][1].set_piece(whitePawn)
        gameboard.board[i][6].set_piece(blackPawn)

    whiteKnight = Knight("w")
    blackKnight = Knight("b")
    whiteBishop = Bishop("w")
    blackBishop = Bishop("b")
    whiteRook = Rook("w")
    blackRook = Rook("b")
    whiteQueen = Queen("w")
    blackQueen = Queen("b")
    whiteKing = King("w")
    blackKing = King("b")

    gameboard.board[0][0].set_piece(whiteRook)
    gameboard.board[7][0].set_piece(whiteRook)

    gameboard.board[1][0].set_piece(whiteKnight)
    gameboard.board[6][0].set_piece(whiteKnight)

    gameboard.board[2][0].set_piece(whiteBishop)
    gameboard.board[5][0].set_piece(whiteBishop)

    gameboard.board[3][0].set_piece(whiteQueen)
    gameboard.board[4][0].set_piece(whiteKing)

    gameboard.board[0][7].set_piece(blackRook)
    gameboard.board[7][7].set_piece(blackRook)

    gameboard.board[1][7].set_piece(blackKnight)
    gameboard.board[6][7].set_piece(blackKnight)

    gameboard.board[2][7].set_piece(blackBishop)
    gameboard.board[5][7].set_piece(blackBishop)

    gameboard.board[3][7].set_piece(blackQueen)
    gameboard.board[4][7].set_piece(blackKing)


def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, dark_square_color, light_square_color, SQUARE_SIZE, OFFSET_X, OFFSET_Y, BOARD_DIM, gameboard, font, move_indicator
    global piece_selected, turn, beaten_pieces
    SCREEN_WIDTH = 1300
    SCREEN_HEIGHT = 700
    dark_square_color = (64, 64, 64)
    light_square_color = (200, 200, 200)

    SQUARE_SIZE = min(SCREEN_WIDTH-150, SCREEN_HEIGHT-150)//8
    OFFSET_X = 75
    OFFSET_Y = (SCREEN_HEIGHT-(8*SQUARE_SIZE))//2
    BOARD_DIM = SQUARE_SIZE*8
    
    move_indicator = []
    piece_selected = []
    turn = "w"
    # initialize the (empty) game board
    gameboard = Board(SQUARE_SIZE, OFFSET_X, OFFSET_Y)
    initialize_board()

    # initialize pygame instance
    pygame.init()

    # SCREEN is now the "surface" object on which to draw on
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    turn = 0  # 0 for white, 1 for black

    while running:
        
        tile_cliked_down = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                tile_cliked_down = get_tile_clicked(event)
                if tile_cliked_down:
                    handle_tile_click(tile_cliked_down)

            if event.type == pygame.K_c:
                move_indicator.clear()
                piece_selected.clear()
        # fill the base color in the window
        SCREEN.fill((40, 40, 40))

        draw_board()
        draw_game_info()
        pygame.display.update()

        # TODO display a menu

    pygame.quit()
if __name__ == "__main__":
    main()