import pygame as pg,sys
from pygame.locals import *
import time

################################################################Global variables#############
XO = 'x'
winner = None
draw = False
#board setup
width = 400
height = 400
white = (255,255,255)
line_color = (10,10,10,10)

TTT = [[None]*3,[None]*3,[None]*3,[None]*3]

#initializing window
pg.init()
fps=30
CLOCK=pg.time.Clock()
screen = pg.display.set_mode((width,height+100),0,32)
pg.display.set_caption("Tic Tac Toe")

#image loading
opening = pg.load("tic tac opening.png")
x_img = pg.image.load("x.png")
o_img = pg.image.load("o.png")

#resizing image
x_img = pg.transform(x_img, (80,80))
o_img = pg.transform(o_img, (80,80))
opening = pg.transform(opening, (width,height+100))


######################################Functions############################################

def game_open():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    #vertical lines
    pg.draw.line(screen,line_color,(width/3,0), (width/3, height), 7)
    pg.draw.line(screen,line_color,(width/3*2,0)(width/3*2,height),7)
    #horizontal lines
    pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2), (width, height/3*2),7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() +" won!"
    if draw:
        message = "Game Draw"
    
    font = pg.font.Font(None,30)
    text = font.render(message, 1, (255,255,255))

    screen.fill((0,0,0), (0,400,500,100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global TTT, winner,draw
    
    #check for rows
    for row in range(0,3):
        if ((TTT [row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None)):
            winner = TTT[row][0]
            pg.draw.line(screen, (250,0,0), ((col+1)*width/3-width/6,0),((col+1)*width/3-width/6, height),4)
            break
    #check columns
    for col in range(0,3):
        if ((TTT [0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None)):
            winner = TTT[0][col]
            pg.draw.line(screen, (250,0,0), ((col+1)*width/3-width/6,0),((col+1)*width/3-width/6, height),4)
            break
    #check diagnols
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        winner = TTT[0][0]
        pg.draw.line(screen, (250,70,70), (350,50), (50,350),4)
    if(all([all(row) for row in TTT]) and winner is None):
        draw =True
    draw_status()

