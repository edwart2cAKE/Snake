import pygame as pg
class Snake:
    def __init__(self, head=(0, 0), grid=None):
        self.body = [head]

        self.head = head
        self.grid = grid
        self.tick_functions = []
        self.alive = True

    def add_head(self, pos):
        self.head = pos
        self.body.insert(0, pos)

    def add_grid(self, grid):
        self.grid = grid

    def move_to(self, pos, grow=False):
        self.head = pos

        if not grow:
            self.body.pop()
        self.body.insert(0, pos)

    def draw_to_grid(self, grid=None):
        if self.grid == None:
            if grid == None:
                raise Exception("Grid not set")
            self.add_grid(grid)
        self.grid.fill(0, 2)
        for pos in self.body:
            self.grid.set_element(*pos, 1)

    def add_tick_function(self, func):
        self.tick_functions.append(func)

    def tick(self):
        keys = pg.key.get_pressed()
        alive = True
        for func in self.tick_functions:
            alive *= func(keys=keys, snake=self)
        self.alive = alive

    def is_alive(self):
        return self.alive
