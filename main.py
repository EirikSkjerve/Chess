import pygame 
'''
Main loop for the window
'''
def menu():
    pass

# if board is none, draw empty grid
def draw_board(board=None):
    square_size = max(SCREEN_WIDTH-100, SCREEN_HEIGHT-100)//8
    draw_dark = True
    for x in range(0, max(SCREEN_WIDTH-100, SCREEN_HEIGHT-100), square_size):
        for y in range(0, max(SCREEN_HEIGHT-100, SCREEN_WIDTH -100), square_size):
            rect = pygame.Rect(x,y,square_size,square_size)
            if draw_dark:
                pygame.draw.rect(SCREEN, dark_square_color,rect,square_size)
                draw_dark = False
            else:
                pygame.draw.rect(SCREEN, light_square_color,rect,square_size)
                draw_dark = True
def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, dark_square_color, light_square_color
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 1000
    dark_square_color = (64, 64, 64)
    light_square_color = (200, 200, 200)

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