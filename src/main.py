import pygame 
from board import Board
from piece import Piece
'''
Main loop for the window
'''
def menu():
    pass

def draw_board():

    font = pygame.font.Font('src/Utils/arial.ttf', 18)
 
    for y in range(8):
        for x in range(8):
            # draw the square
            rect = pygame.Rect(SQUARE_SIZE*(x)+OFFSET_X, SQUARE_SIZE*(y)+OFFSET_Y, SQUARE_SIZE, SQUARE_SIZE)
            tile = gameboard.board[7-x][7-y]
            pygame.draw.rect(SCREEN, dark_square_color if tile.color == "b" else light_square_color, rect, SQUARE_SIZE)

            if y==7:
                tileText = font.render(tile.coordinate[0], True, (255, 255, 255) if tile.color == "b" else (35, 35, 35))
                # draw tile coordinates
                tileTextRect = tileText.get_rect() 
                tileTextRect.center = (SQUARE_SIZE*(x+1.5), SQUARE_SIZE*(y+0.85)+OFFSET_Y)
                SCREEN.blit(tileText, tileTextRect)
            if x==0:
                tileText = font.render(tile.coordinate[1], True, (255, 255, 255) if tile.color == "b" else (35, 35, 35))
                # draw tile coordinates
                tileTextRect = tileText.get_rect() 
                tileTextRect.center = (SQUARE_SIZE*(x)+OFFSET_X+13, SQUARE_SIZE*(y)+OFFSET_Y+17)
                SCREEN.blit(tileText, tileTextRect)

            # TODO draw piece if piece on the tile
            if tile.piece:
                print(tile.coordinate)
                piece_surf = pygame.Surface((SQUARE_SIZE-30, SQUARE_SIZE-30))
                piece_surf.fill((50, 255, 50))
                SCREEN.blit(piece_surf, (SQUARE_SIZE*x+OFFSET_X, SQUARE_SIZE*y+OFFSET_Y))

def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, dark_square_color, light_square_color, SQUARE_SIZE, OFFSET_X, OFFSET_Y, BOARD_DIM, gameboard
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    dark_square_color = (64, 64, 64)
    light_square_color = (200, 200, 200)

    SQUARE_SIZE = min(SCREEN_WIDTH-150, SCREEN_HEIGHT-150)//8
    OFFSET_X = 75
    OFFSET_Y = (SCREEN_HEIGHT-(8*SQUARE_SIZE))//2
    BOARD_DIM = SQUARE_SIZE*8
    
    gameboard = Board()
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
        pygame.display.update()

        # TODO display a menu

    pygame.quit()
if __name__ == "__main__":
    main()