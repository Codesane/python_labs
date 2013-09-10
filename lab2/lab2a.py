# lab2a.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 1A from: www.ida.liu.se/~TDDC66/python/la/la1.shtml


# Inkludera alla de grafiska funktionerna samt funktionen sleep.
from graphics import *
from time import sleep

# Funktion som returnerar ett nytt rutnät med bredden BREDD och höjden HÖJD.
def skapa_rutnät(bredd, höjd):
    
    rutnät = []
    
    for y in range(höjd):
        rutnät.append([])
        for x in range(bredd):
            rutnät[y].append(False)
    
    return rutnät

# Funktion som returnerar antalet levande grannar cellen med positionen (X, Y)
# har i rutnätet RUTNÄT.
def antal_levande_grannar(rutnät, x, y):
    
    # Grannarnas x-koordinater (inklusive cellens egna).
    bredd = len(rutnät[0])
    grannar_x = [x]
    if x != 0:
        grannar_x.append(x-1)
    if x != bredd-1:
        grannar_x.append(x+1)
    
    # Grannarnas y-koordinater (inklusive cellens egna).
    höjd = len(rutnät)
    grannar_y = [y]
    if y != 0:
        grannar_y.append(y-1)
    if y != höjd-1:
        grannar_y.append(y+1)
    
    # Beräkna antalet levande grannar (inklusive cellen själv).
    antal = 0
    for granne_y in grannar_y:
        for granne_x in grannar_x:
            if rutnät[granne_y][granne_x]:
                antal += 1
    
    # Om cellen själv lever, dra bort 1, så den inte själv räknas som en granne.
    if rutnät[y][x]:
        antal -= 1
    
    return antal

# Funktion som returnerar hur nästa generations celler ser ut i rutnätet RUTNÄT.
def nästa_generation(rutnät):
    
    bredd = len(rutnät[0])
    höjd = len(rutnät)
    
    nyttRutnät = skapa_rutnät(bredd, höjd)
    
    for y in range(höjd):
        for x in range(bredd):
            
            antal = antal_levande_grannar(rutnät, x, y)
            
            if not rutnät[y][x] and antal == 3:
                nyttRutnät[y][x] = True
            elif rutnät[y][x] and (antal < 2 or 3 < antal):
                nyttRutnät[y][x] = False
            else:
                nyttRutnät[y][x] = rutnät[y][x]
    
    return nyttRutnät

# Funktion som målar upp rutnätet RUTNÄT i fönstret FÖNSTER.
def måla(fönster, rutnät, size):
    
    bredd = len(rutnät[0])
    höjd = len(rutnät)
    rectBkg = Rectangle(Point(0, 0), Point(170*50, 170*50))
    rectBkg.setFill('white')
    rectBkg.draw(fönster)

    # Kod som ska skrivas i uppgift 2A.
    for x in range(0, len(rutnät)):
        for y in range(0, len(rutnät[x])):
            if rutnät[x][y] == True:
                rektangel = Rectangle(Point(x*size, y*size), Point(x*size+size, y*size+size))
                rektangel.setFill('green')
                rektangel.draw(fönster)
            

# Huvudprogrammet
def main():
    
    # Bredd och höjd på rutnätet.
    bredd = 17
    höjd = 17
    
    # Varje cells storlek (i pixlar) då de ritas ut i fönstret.
    cell_storlek = 50
    
    rutnät = skapa_rutnät(bredd, höjd)
    
    # Lägg in True på de positioner vars cell ska leva från början.
    # Just nu ett mönster som upprepas var tredje generation.
    rutnät[2][4] = True
    rutnät[2][5] = True
    rutnät[2][6] = True
    rutnät[2][10] = True
    rutnät[2][11] = True
    rutnät[2][12] = True
    rutnät[4][2] = True
    rutnät[4][7] = True
    rutnät[4][9] = True
    rutnät[4][14] = True
    rutnät[5][2] = True
    rutnät[5][7] = True
    rutnät[5][9] = True
    rutnät[5][14] = True
    rutnät[6][2] = True
    rutnät[6][7] = True
    rutnät[6][9] = True
    rutnät[6][14] = True
    rutnät[7][4] = True
    rutnät[7][5] = True
    rutnät[7][6] = True
    rutnät[7][10] = True
    rutnät[7][11] = True
    rutnät[7][12] = True
    rutnät[9][4] = True
    rutnät[9][5] = True
    rutnät[9][6] = True
    rutnät[9][10] = True
    rutnät[9][11] = True
    rutnät[9][12] = True
    rutnät[10][2] = True
    rutnät[10][7] = True
    rutnät[10][9] = True
    rutnät[10][14] = True
    rutnät[11][2] = True
    rutnät[11][7] = True
    rutnät[11][9] = True
    rutnät[11][14] = True
    rutnät[12][2] = True
    rutnät[12][7] = True
    rutnät[12][9] = True
    rutnät[12][14] = True
    rutnät[14][4] = True
    rutnät[14][5] = True
    rutnät[14][6] = True
    rutnät[14][10] = True
    rutnät[14][11] = True
    rutnät[14][12] = True
    
    # Skapa fönstret rutnätet ska visas i.
    fönster = GraphWin('Game of Life', bredd*cell_storlek, höjd*cell_storlek)
    
    # Så länge man inte klickar i fönstret.
    while True:
        
        måla(fönster, rutnät, cell_storlek)
        rutnät = nästa_generation(rutnät)
        
        # Vänta (minst) en sekund innan exekveringen fortsätter.
        sleep(1)

main()
