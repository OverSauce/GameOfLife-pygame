import numpy as np
import pygame
import tkinter 

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
window = pygame.display.set_mode((width, height))

class cells():

    dx = 20         # Number of pixels for each cell (squared)

    def __init__(self):
        self.width = width
        self.height = height
        self.window = window
        self.grid = np.zeros((self.width//self.dx, self.height//self.dx), dtype=bool)
    
    def kill_all(self):
        self.grid = np.zeros((self.width//self.dx, self.height//self.dx), dtype=bool)

    def check_mouse_click(self, pos):

        x, y = pos
        if x < self.grid.shape[0]*self.dx and y < self.grid.shape[1]*self.dx:
            x, y = x//self.dx, y//self.dx
            self.grid[x, y] = not self.grid[x, y]

    def scanner(self, i, j):
        
        """ Scanning the neighbor cells of 3x3 area around 
            the particular cell. Returns the number of alive neighbors. 
            """

        alive_neighbors = 0
        
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not (x == 0 and y == 0):
                    if i+x >= 0 and i+x < self.grid.shape[0] and j+y >= 0 and j+y < self.grid.shape[1]:
                        if self.grid[i+x, j+y]:
                            alive_neighbors += 1
        return alive_neighbors

    def check_neighbours(self):

        """ Stores entire map of cells in a temporary array.
            Uses scanner function to determine wether the state 
            of the particular cell change or stays the same.
            If the alive cell has less than 2 or more than 3 alive
            neighbors, the cell will die in the next time step.
            If the dead cell has exactly 3 living neighbors will come alive.
            """

        temp = self.grid.copy()
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):

                if not self.grid[i, j]:     # DEAD CELL
                    if self.scanner(i, j) == 3:
                        temp[i, j] = True

                else:                       # ALIVE CELL
                    if self.scanner(i, j) < 2 or self.scanner(i, j) > 3:
                        temp[i, j] = False 
        self.grid = temp.copy()

    def draw(self):

        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i, j]:
                    pygame.draw.rect(self.window, (100, 100, 100), (i*self.dx, j*self.dx, self.dx, self.dx))
                else:
                    pygame.draw.rect(self.window, (200, 200, 200), (i*self.dx, j*self.dx, self.dx, self.dx))
