import pygame 
from board import Board
from piece import Piece, Pawn

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

            tile_down, tile_right = tile.dr
            # draw coordinate on each tile
            tileText = font.render(tile.coordinate, True, (255, 255, 255) if tile.color == "b" else (35, 35, 35))
            tileTextRect = tileText.get_rect() 
            tileTextRect.center = (tile_down-10, tile_right-10)
            SCREEN.blit(tileText, tileTextRect)

            # TODO draw pieces

            if tile.piece is not None:
                piece = tile.piece
                piece_surf = pygame.Surface((SQUARE_SIZE//2, SQUARE_SIZE//2))
                piece_surf.fill((50, 255, 50) if piece.color == "w" else (255,50,50))
                SCREEN.blit(piece_surf, (tile_down-50, tile_right-50))
            
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

def handle_tile_click(tile_cliked):
    tile = gameboard.get(tile_cliked)
    if tile.piece:
        piece = tile.piece
        print(f"Piece {piece.name} on tile {tile.coordinate}. Valid moves are: {', '.join(gameboard.get_valid_moves(tile.coordinate))}")

def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, dark_square_color, light_square_color, SQUARE_SIZE, OFFSET_X, OFFSET_Y, BOARD_DIM, gameboard, font
    SCREEN_WIDTH = 1300
    SCREEN_HEIGHT = 700
    dark_square_color = (64, 64, 64)
    light_square_color = (200, 200, 200)

    SQUARE_SIZE = min(SCREEN_WIDTH-150, SCREEN_HEIGHT-150)//8
    OFFSET_X = 75
    OFFSET_Y = (SCREEN_HEIGHT-(8*SQUARE_SIZE))//2
    BOARD_DIM = SQUARE_SIZE*8
    
    # initialize the (empty) game board
    gameboard = Board(SQUARE_SIZE, OFFSET_X, OFFSET_Y)
    whitePawn = Pawn("w")
    blackPawn = Pawn("b")

    gameboard.board[3][2].set_piece(whitePawn)
    gameboard.board[2][3].set_piece(blackPawn)
    gameboard.board[4][3].set_piece(blackPawn)

    # initialize pygame instance
    pygame.init()

    # SCREEN is now the "surface" object on which to draw on
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        
        tile_cliked_down = None
        tile_released = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                tile_cliked_down = get_tile_clicked(event)
                handle_tile_click(tile_cliked_down)
        # fill the base color in the window
        SCREEN.fill((40, 40, 40))

        draw_board()
        pygame.display.update()

        # TODO display a menu

    pygame.quit()
if __name__ == "__main__":
    main()