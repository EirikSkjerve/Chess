import pygame 
from board import Board
'''
Main loop for the window
'''
def menu():
    pass

# if board is none, draw empty grid
def draw_board(board=None):

    # depending on what color the player is, this should be false/true for white/black
    draw_dark = True
    for x in range(OFFSET_X, BOARD_DIM + OFFSET_X, SQUARE_SIZE):
        
        draw_dark = not draw_dark
        for y in range(OFFSET_Y, BOARD_DIM + OFFSET_Y, SQUARE_SIZE):
            rect = pygame.Rect(x,y,SQUARE_SIZE, SQUARE_SIZE)
            if draw_dark:
                pygame.draw.rect(SCREEN, dark_square_color,rect,SQUARE_SIZE)
                draw_dark = not draw_dark
            else:
                pygame.draw.rect(SCREEN, light_square_color,rect,SQUARE_SIZE)
                draw_dark = not draw_dark

def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, dark_square_color, light_square_color, SQUARE_SIZE, OFFSET_X, OFFSET_Y, BOARD_DIM, board
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 1000
    dark_square_color = (64, 64, 64)
    light_square_color = (200, 200, 200)

    SQUARE_SIZE = min(SCREEN_WIDTH-150, SCREEN_HEIGHT-150)//8
    OFFSET_X = 75
    OFFSET_Y = (SCREEN_HEIGHT-(8*SQUARE_SIZE))//2
    BOARD_DIM = SQUARE_SIZE*8
    
    board = Board()

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