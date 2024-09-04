import pygame as pg
from grid import Grid
from snake import Snake

pg.init()

WINDOW_SIZE = (800,600)
wn = pg.display.set_mode(WINDOW_SIZE)

grid = Grid(30,30)
grid.set_bounds((0,0,450,450))

snake = Snake((15,15), grid)

apple_pos = grid.get_random_pos_with([0])

grid.set_element(*apple_pos, 2)

def move_snake(keys, snake):
    global apple_pos
    new_head = snake.head
    if keys[pg.K_UP]:
        new_head = (snake.head[0], snake.head[1] - 1)
    elif keys[pg.K_DOWN]:
        new_head = (snake.head[0], snake.head[1] + 1)
    elif keys[pg.K_LEFT]:
        new_head = (snake.head[0] - 1, snake.head[1])
    elif keys[pg.K_RIGHT]:
        new_head = (snake.head[0] + 1, snake.head[1])
    
    # see if the snake hits a wall using try-except
    try:
        if snake.grid.get_element(*new_head) == 1:
            new_head = snake.head
    except IndexError:
        return False #game over

    if snake.grid.get_element(*new_head) == 2:
        new_apple_pos = grid.get_random_pos_with([0])
        snake.grid.set_element(*apple_pos, 0)
        snake.grid.set_element(*new_apple_pos, 2)
        apple_pos = new_apple_pos
        snake.move_to(new_head, True) #grow if food is eaten (head is 2)
    else:
        snake.move_to(new_head)

    return True

snake.add_tick_function(move_snake)

clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    wn.fill((0,0,0))
    
    mouse_pos = pg.mouse.get_pos()
    keys = pg.key.get_pressed()
    #print(mouse_pos)
    
    if grid.is_mouse_inside(mouse_pos):
        grid_pos = grid.get_mouse_pos(mouse_pos)
        grid.set_element(*grid_pos)

    #tick

    if snake.is_alive():    
        snake.tick()
    
    snake.draw_to_grid(grid)            
    grid.blit_to_screen(wn)
    
    pg.display.update()
    
    clock.tick(10)
pg.quit()
grid.print_info()
grid.print_grid()