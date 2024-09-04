import pygame as pg
import random

class Grid:
    def __init__(self, cols, rows, default=0) -> None:
        self.rows = rows
        self.cols = cols
        self.default = default
        self.grid = [[default for i in range(cols)] for j in range(rows)]
        self.bounds = None

        self.color_map = {0: (0, 0, 0), 1: (255, 255, 255), 2: (255, 0, 0)}

    def print_grid(self):
        for row in self.grid:
            print_str = ""
            for col in row:
                print_str = print_str + str(col) + " "
            print(print_str)

        # print(self.grid)

    def set_bounds(self, bounds):
        self.bounds = bounds
        self.ge_height = int((self.bounds[3] - self.bounds[1]) / self.rows)
        self.ge_width = int((self.bounds[2] - self.bounds[0]) / self.cols)

    def blit_to_screen(self, surface: pg.Surface):
        if self.bounds == None:
            self.set_bounds((0, 0, surface.get_height(), surface.get_width()))

        for rn, row in enumerate(self.grid):
            for cn, col in enumerate(row):
                pg.draw.rect(
                    surface,
                    self.color_map[col],
                    (
                        cn * self.ge_width,
                        rn * self.ge_height,
                        self.ge_width,
                        self.ge_height,
                    ),
                )

    def set_element(self, col, row, n=1):
        self.grid[row][col] = n

    def get_element(self, col, row):
        return self.grid[row][col]

    def get_grid(self):
        return self.grid

    def get_mouse_pos(self, pos):
        if self.bounds == None:
            self.set_bounds((0, 0, 100, 100))

        row = (pos[1] - self.bounds[1]) / self.ge_height
        col = (pos[0] - self.bounds[0]) / self.ge_width

        return (int(row), int(col))

    def is_mouse_inside(self, pos):
        if self.bounds == None:
            self.set_bounds((0, 0, 100, 100))
        return (
            self.bounds[0] <= pos[0] < self.bounds[2]
            and self.bounds[1] <= pos[1] < self.bounds[3]
        )

    def fill(self, num, keep_num=2):
        for rn, row in enumerate(self.grid):
            for cn, col in enumerate(row):
                if col != keep_num:
                    self.grid[rn][cn] = num

    def set_color_map(self, color_map):
        self.color_map = color_map

    def print_info(self):
        print("bounds:", self.bounds)
        print("grid element height:", self.ge_height)
        print("grid element width:", self.ge_width)

    def get_random_pos_with(self, c_with=[], c_without=[]):
        if c_with == [] and c_without == []:
            raise Exception("Both c_with and c_without cannot be Empty")
        
        i = 0
        while i < 1000:
            i += 1
            pos = (random.randint(0, self.cols - 1), random.randint(0, self.rows - 1))
            el = self.get_element(*pos)
            
            if el in c_with and el not in c_without:
                return pos
        return pos
