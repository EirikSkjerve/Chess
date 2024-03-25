import pygame 
'''
Main loop for the window
'''

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the base color in the window
        screen.fill((40, 40, 40))
        # for some reason this is needed to render on screen
        pygame.display.flip()

        # TODO display a menu

    pygame.quit()
if __name__ == "__main__":
    main()