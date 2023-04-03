from grid import Grid
import pygame

weight = 800
height = 800
FPS = 20
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()
clock = pygame.time.Clock()

grid = Grid(height // 15, height // 15)
grid.random_2d_matrix()
dis = pygame.display.set_mode([weight, height], pygame.RESIZABLE)
pause = False
f_sys = pygame.font.SysFont('arial', 21)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                text = f_sys.render('Pause', 1, RED, YELLOW)
                pos = text.get_rect(center=(50, 20))
                dis.blit(text, pos)
                pygame.display.update()

            if event.key == pygame.K_UP:
                grid.random_2d_matrix()
        elif event.type == pygame.MOUSEBUTTONDOWN and pause:
            grid.new(pygame.mouse.get_pos(), dis)
            pygame.display.update()

    if not pause:
        grid.play(dis)
    clock.tick(FPS)

