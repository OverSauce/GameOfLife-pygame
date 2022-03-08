import pygame
from cells import cells, window

pygame.init()

def main():
    run = True
    clock = pygame.time.Clock()

    CELLS = cells()

    while run:
        clock.tick(60)
        window.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    CELLS.check_neighbours()
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_c:
                    CELLS.kill_all()
            if event.type == pygame.MOUSEBUTTONDOWN:
                CELLS.check_mouse_click(event.pos)

        CELLS.draw()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
