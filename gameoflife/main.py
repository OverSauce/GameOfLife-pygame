import pygame
from cells import cells

pygame.init()

# Screen resolution, font

width, height = 1080, 720
window = pygame.display.set_mode((width, height))
text = pygame.font.SysFont("comicsans", 20)

def main():
    run = True
    clock = pygame.time.Clock() # FPS

    CELLS = cells(width, height, window)

    while run:
        clock.tick(60)
        window.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    CELLS.check_neighbours()
            if event.type == pygame.MOUSEBUTTONDOWN:
                CELLS.check_mouse_click(event.pos)

        CELLS.draw()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
