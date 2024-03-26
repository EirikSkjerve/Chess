import pygame 
from board import Board
from piece import Piece

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
            tile = gameboard.board[x][y]
            #print(tile.coordinate)
            tile_top, tile_left = tile.ul
            rect = pygame.Rect(tile_top, tile_left, SQUARE_SIZE,SQUARE_SIZE)
            pygame.draw.rect(SCREEN, dark_square_color if tile.color == "b" else light_square_color, rect, SQUARE_SIZE)

            # draw coordinate
            tileText = font.render(tile.coordinate, True, (255, 255, 255) if tile.color == "b" else (35, 35, 35))
            tileTextRect = tileText.get_rect() 
            tileTextRect.center = (tile_top+10, tile_left+10)
            SCREEN.blit(tileText, tileTextRect)
            
            

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
    gameboard.print_board()
    for x in range(8):
        for y in range(8):
            tile = gameboard.board[y][x]
    # initialize the font to be used

    # initialize pygame instance
    pygame.init()

    # SCREEN is now the "surface" object on which to draw on
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
                print(event.type)

        # fill the base color in the window
        SCREEN.fill((40, 40, 40))

        draw_board()
        pygame.display.update()

        # TODO display a menu

    pygame.quit()
if __name__ == "__main__":
    main()