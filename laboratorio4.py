import pygame

class Life(object):
    def __init__(self, screen):
        _, _, self.width, self.height = screen.get_rect()
        self.screen = screen

    def clear(self):
        self.screen.fill((0, 0, 0))

    def pixel(self, x, y, color):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_turn = self.screen.copy()

    def render(self):
        for x in range(self.width):
            for y in range(self.height):
                contador = 0
                lista = [-1, 1]
                
                for i in lista:
                    if self.prev_turn.get_at(((x+i)%300, y))[0] == 255:
                        contador += 1
                    
                for i in lista:
                    if self.prev_turn.get_at((x, (y+i)%300))[0] == 255:
                        contador += 1
                        
                for i in lista:
                    if self.prev_turn.get_at(((x+i)%300, (y+i)%300))[0] == 255:
                        contador += 1

                for i, j in lista, reversed(lista):
                    if self.prev_turn.get_at(((x+j)%300, (y+i)%300))[0] == 255:
                        contador += 1
                
                if contador < 2 and self.prev_turn.get_at((x, y))[0] == 255 or contador > 3 :
                    self.pixel(x, y, negro)

                if ( 2 <=  contador <= 3 and self.prev_turn.get_at((x, y))[0] == 255) or (contador == 3 and self.prev_turn.get_at((x, y))[0] == 0):
                    self.pixel(x, y, blanco)

negro = (0,0,0)
blanco = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((300, 300))
r = Life(screen)

patron = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

patron2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [1,1,0,1,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]]

patron3 = [[0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0],
                    [1,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0],
                    [1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0],
                    [1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [1,1,0,1,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]]


for y in range(0, len(patron)):
    for x in range(0, len(patron[y])):
        if(patron[y][x] == 1):
            r.pixel(x+100, y+100, blanco)

for y in range(0, len(patron2)):
    for x in range(0, len(patron2[y])):
        if(patron2[y][x] == 1):
            r.pixel(x+200, y+200, blanco)

for y in range(0, len(patron)):
    for x in range(0, len(patron[y])):
        if(patron[y][x] == 1):
            r.pixel(x+30, y+30, blanco)

for y in range(0, len(patron)):
    for x in range(0, len(patron[y])):
        if(patron[y][x] == 1):
            r.pixel(x+100, y+50, blanco)

for y in range(0, len(patron2)):
    for x in range(0, len(patron2[y])):
        if(patron2[y][x] == 1):
            r.pixel(x+150, y+150, blanco)

for y in range(0, len(patron2)):
    for x in range(0, len(patron2[y])):
        if(patron2[y][x] == 1):
            r.pixel(x+50, y+250, blanco)

for y in range(0, len(patron)):
    for x in range(0, len(patron[y])):
        if(patron[y][x] == 1):
            r.pixel(x+80, y+200, blanco)

for y in range(0, len(patron)):
    for x in range(0, len(patron[y])):
        if(patron[y][x] == 1):
            r.pixel(x+50, y+125, blanco)

for y in range(0, len(patron3)):
    for x in range(0, len(patron3[y])):
        if(patron3[y][x] == 1):
            r.pixel(x+220, y+125, blanco)

for y in range(0, len(patron)):
    for x in range(0, len(patron[y])):
        if(patron[y][x] == 1):
            r.pixel(x+220, y+50, blanco)

for y in range(0, len(patron3)):
    for x in range(0, len(patron3[y])):
        if(patron3[y][x] == 1):
            r.pixel(x+140, y+245, blanco)

while True:
  r.copy()
  r.clear()
  r.render()
  pygame.display.flip()
