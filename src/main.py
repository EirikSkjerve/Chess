import pygame 
from board import Board
from piece import Piece
'''
Main loop for the window
'''
def menu():
    pass

def draw_board():

    # depending on what color the player is, this should be false/true for white/black
    draw_dark = True
    index_x = 0
    index_y = 0
    for x in range(OFFSET_X, BOARD_DIM + OFFSET_X, SQUARE_SIZE): 
        draw_dark = not draw_dark
        for y in range(OFFSET_Y, BOARD_DIM + OFFSET_Y, SQUARE_SIZE):
            rect = pygame.Rect(x,y,SQUARE_SIZE, SQUARE_SIZE)
            piece = gameboard.board[index_y][index_x]

            if draw_dark:
                pygame.draw.rect(SCREEN, dark_square_color,rect,SQUARE_SIZE)
                draw_dark = not draw_dark
            else:
                pygame.draw.rect(SCREEN, light_square_color,rect,SQUARE_SIZE)
                draw_dark = not draw_dark

            if piece:
                # do something to center it here
                piece_surf = pygame.Surface((SQUARE_SIZE-30, SQUARE_SIZE-30))
                piece_surf.fill((50, 255, 50))
                SCREEN.blit(piece_surf, (x, y))

            index_y += 1
        index_y = 0
        index_x += 1

def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, dark_square_color, light_square_color, SQUARE_SIZE, OFFSET_X, OFFSET_Y, BOARD_DIM, gameboard
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 1000
    dark_square_color = (64, 64, 64)
    light_square_color = (200, 200, 200)

    SQUARE_SIZE = min(SCREEN_WIDTH-150, SCREEN_HEIGHT-150)//8
    OFFSET_X = 75
    OFFSET_Y = (SCREEN_HEIGHT-(8*SQUARE_SIZE))//2
    BOARD_DIM = SQUARE_SIZE*8
    
    gameboard = Board()
    for i in range(5):
        piece = Piece("Pawn", 10, f'a{i+1}', 'b')
        gameboard.set(piece.position, piece)
    gameboard.print_board()
    
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
        # for some reason this is needed to render on SCREEN
        pygame.display.update()

        # TODO display a menu

    pygame.quit()
if __name__ == "__main__":
    main()