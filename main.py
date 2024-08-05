import pygame as game

size = width, height = 640, 480

screen = game.display.set_mode(size)

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            exit()
        elif event.type == game.MOUSEBUTTONUP:
            pos = game.mouse.get_pos()
            col = (0,255,255)
            game.draw.circle(screen, col, pos, 20, 5)
            game.display.update()
    game.display.flip()