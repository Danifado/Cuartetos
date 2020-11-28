 # -*- coding: utf-8 -*-
import pygame
import json
import unit_propagate
import codificacion
import guardar_reglas

#Para que el codigo funcione correctamente, los valores que deben haber
#el input de cada player son:
#Player1: A2 D2 D3 D4
#Pĺayer2: C2 B1 B2 A1
#Player3: B4 D1 C1 C3
#Player4: C4 B3 A3 A4
#De otra manera, cambiará la posición de las cartas pero no hará
#una recomendación adecuada

pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Cuartetos")

A1 = myfont.render('A1', False, (0, 0, 0))
A2 = myfont.render('A2', False, (0, 0, 0))
A3 = myfont.render('A3', False, (0, 0, 0))
A4 = myfont.render('A4', False, (0, 0, 0))
A = [A1,A2,A3,A4]

B1 = myfont.render('B1', False, (0, 0, 0))
B2 = myfont.render('B2', False, (0, 0, 0))
B3 = myfont.render('B3', False, (0, 0, 0))
B4 = myfont.render('B4', False, (0, 0, 0))
B = [B1,B2,B3,B4]

C1 = myfont.render('C1', False, (0, 0, 0))
C2 = myfont.render('C2', False, (0, 0, 0))
C3 = myfont.render('C3', False, (0, 0, 0))
C4 = myfont.render('C4', False, (0, 0, 0))
C = [C1,C2,C3,C4]

D1 = myfont.render('D1', False, (0, 0, 0))
D2 = myfont.render('D2', False, (0, 0, 0))
D3 = myfont.render('D3', False, (0, 0, 0))
D4 = myfont.render('D4', False, (0, 0, 0))
D = [D1,D2,D3,D4]

x = 50
y = 50
width = 40
height = 60
vel = 5

Player1 = []
Player1Letras = []
Player2 = []
Player2Letras = []
Player3 = []
Player3Letras = []
Player4 = []
Player4Letras = []

def Interpretate_Players_Info(info, player, pletras):
    temp_string_list = info.split()
    for i in temp_string_list:
        if(i == "A1"):
            player.append(A1)
            pletras.append("A1")
        elif(i == "A2"):
            player.append(A2)
            pletras.append("A2")
        elif(i == "A3"):
            player.append(A3)
            pletras.append("A3")
        elif(i == "A4"):
            player.append(A4)
            pletras.append("A4")
        elif(i == "B1"):
            player.append(B1)
            pletras.append("B1")
        elif(i == "B2"):
            player.append(B2)
            pletras.append("B2")
        elif(i == "B3"):
            player.append(B3)
            pletras.append("B3")
        elif(i == "B4"):
            player.append(B4)
            pletras.append("B4")
        elif(i == "C1"):
            player.append(C1)
            pletras.append("C1")
        elif(i == "C2"):
            player.append(C2)
            pletras.append("C2")
        elif(i == "C3"):
            player.append(C3)
            pletras.append("C3")
        elif(i == "C4"):
            player.append(C4)
            pletras.append("C4")
        elif(i == "D1"):
            player.append(D1)
            pletras.append("D1")
        elif(i == "D2"):
            player.append(D2)
            pletras.append("D2")
        elif(i == "D3"):
            player.append(D3)
            pletras.append("D3")
        elif(i == "D4"):
            player.append(D4)
            pletras.append("D4")
    print("El jugador tiene: ", temp_string_list)

def playerBox(name,x_axis, y_axis):
    pygame.draw.rect(win, (201,206,213), (x_axis,y_axis, 80, 40))
    nm = myfont.render(name, False, (0, 0, 0))
    win.blit(nm, (x_axis,y_axis))

def drawP1():
    playerBox('Player 1',350, y+370-50)

    pygame.draw.rect(win, (255,0,0), (x+200,y+370,width, height))
    win.blit(Player1[0], (x+200,y+370))

    pygame.draw.rect(win, (255,0,0), (x+200+width+40,y+370,width, height))
    win.blit(Player1[1], (x+200+width+40,y+370))

    pygame.draw.rect(win, (255,0,0), (x+200+width*2+40*2,y+370,width, height))
    win.blit(Player1[2], (x+200+width*2+40*2,y+370))

    pygame.draw.rect(win, (255,0,0), (x+200+width*3+40*3,y+370,width, height))
    win.blit(D[3], (x+200+width*3+40*3,y+370))

def drawP2():
    playerBox('Player 2',x+width+20, 250)

    pygame.draw.rect(win, (255,0,0), (x,y+50,width, height))
    win.blit(Player2[0], (x,y+50))

    pygame.draw.rect(win, (255,0,0), (x,y+50+90,width, height))
    win.blit(Player2[1], (x,y+50+90))

    pygame.draw.rect(win, (255,0,0), (x,y+90*2+50,width, height))
    win.blit(Player2[2], (x,y+90*2+50))

    pygame.draw.rect(win, (255,0,0), (x,y+90*3+50,width, height))
    win.blit(Player2[3], (x,y+90*3+50))

def drawP3():
    playerBox('Player 3',350, y+height+20)

    pygame.draw.rect(win, (255,0,0), (x+200,y,width, height))
    win.blit(Player3[0], (x+200,y))

    pygame.draw.rect(win, (255,0,0), (x+200+width+40,y,width, height))
    win.blit(Player3[1], (x+200+width+40,y))

    pygame.draw.rect(win, (255,0,0), (x+200+width*2+40*2,y,width, height))
    win.blit(Player3[2], (x+200+width*2+40*2,y))

    pygame.draw.rect(win, (255,0,0), (x+200+width*3+40*3,y,width, height))
    win.blit(Player3[3], (x+200+width*3+40*3,y))

def drawP4():
    playerBox('Player 4',800-x-width-100, 250)

    pygame.draw.rect(win, (255,0,0), (800-x-width,y+50,width, height))
    win.blit(Player4[0], (800-x-width,y+50))

    pygame.draw.rect(win, (255,0,0), (800-x-width,y+90+50,width, height))
    win.blit(Player4[1], (800-x-width,y+90+50))

    pygame.draw.rect(win, (255,0,0), (800-x-width,y+90*2+50,width, height))
    win.blit(Player4[2], (800-x-width,y+90*2+50))

    pygame.draw.rect(win, (255,0,0), (800-x-width,y+90*3+50,width, height))
    win.blit(Player4[3], (800-x-width,y+90*3+50))

def pideCarta():
    nm = myfont.render('Pídele un D a Player 3', False, (0, 0, 0))
    win.blit(nm, (260 ,250))

infoP1 = input("¿Cual es la información del jugador 1?: ")
infoP2 = input("¿Cual es la información del jugador 2?: ")
infoP3 = input("¿Cual es la información del jugador 3?: ")
infoP4 = input("¿Cual es la información del jugador 4?: ")

infoP1 = Interpretate_Players_Info(infoP1, Player1, Player1Letras)
infoP2 = Interpretate_Players_Info(infoP2, Player2, Player2Letras)
infoP3 = Interpretate_Players_Info(infoP3, Player3, Player3Letras)
infoP4 = Interpretate_Players_Info(infoP4, Player4, Player4Letras)

Regla_tmp_fclausal = []
posiciones = [Player1Letras, Player2Letras, Player3Letras, Player4Letras]
inter = {}
codificacion.reglaPosicionalTemporal(Regla_tmp_fclausal, posiciones, inter)
print("Regla temporal de posicion: ", Regla_tmp_fclausal)
print("Diccionario de interpretación: ", inter)
regla_fc = Regla_tmp_fclausal
letrasProposicionalesA = [chr(x) for x in range(256, 1000)] # Modificar de acuerdo a reglas
letrasProposicionalesB = [chr(x) for x in range(2001, 3000)] # Modificar de acuerdo a reglas
guardar_reglas.guardar_fnc(regla_fc, 'regla1', letrasProposicionalesA, letrasProposicionalesB)

with open('regla0.json', 'r') as file:
    reglas = json.load(file)

with open('regla1.json', 'r') as file:
    reglas += json.load(file)

SAT, i = unit_propagate.DPLL(reglas, inter)

print("Satisfacible? ", SAT)



run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,107,4))

    drawP1()
    drawP2()
    drawP3()
    drawP4()

    pideCarta()

    pygame.display.update()
