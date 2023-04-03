import numpy
from random import randint
import pygame


class Grid:

    def __init__(self, row, col):
        self.col = col
        self.row = row
        self.x = 15
        self.y = 15
        self.grid = numpy.zeros((row, col))

    def random_2d_matrix(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if randint(0, 1):
                    self.grid[i][j] = 1

    def zero_2d_matrix(self):
        self.grid = numpy.zeros((self.row, self.col))

    def play(self, screen):
        screen.fill((255, 255, 255))
        x, y = self.x, self.y
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j]:
                    pygame.draw.rect(screen, (0, 0, 20), (x * j, y * i, x, y), 1)
                else:
                    pygame.draw.rect(screen, (0, 0, 20), (x * j, y * i, x, y))
        pygame.display.update()
        self.grid = self.life()

    def new(self, position, screen):
        x, y = position
        col, row = x // 15, y // 15
        self.grid[row][col] = not self.grid[row][col]
        if self.grid[row][col]:
            pygame.draw.rect(screen, (255, 255, 255), (15 * col, 15 * row, 15, 15))
            pygame.draw.rect(screen, (0, 0, 20), (15 * col, 15 * row, 15, 15), 1)
        else:
            pygame.draw.rect(screen,(0, 0, 20), (15 * col, 15 * row, 15, 15))
        pygame.display.flip()




    def life(self):
        board = self.grid
        result = numpy.zeros([self.row, self.col])
        for i in range(len(board)):
            for j in range(len(board[i])):
                n = 0
                j_m = j > 0
                j_p = j + 1 < len(board[0])
                i_m = i > 0
                i_p = i + 1 < len(board)
                if i_m:
                    n += board[i - 1][j]
                    if j_m:
                        n += board[i - 1][j - 1]
                    if j_p:
                        n += board[i - 1][j + 1]
                if i_p:
                    n += board[i + 1][j]
                    if j_m:
                        n += board[i + 1][j - 1]
                    if j_p:
                        n += board[i + 1][j + 1]
                if j_p:
                    n += board[i][j + 1]
                if j_m:
                    n += board[i][j - 1]

                if board[i][j]:
                    if n == 2 or n == 3:
                        result[i][j] = 1
                elif n == 3:
                    result[i][j] = 1
        return result
