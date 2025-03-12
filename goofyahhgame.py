#!/usr/bin/env python3

import random


grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

playerX = 0
playerY = 0

gridX = 0
gridY = 0

for i in range(5):
    for j in range(5):
        grid[i][j] = ''

while gridX == 0 and gridY == 0:
    gridX = random.randint(0,4)
    gridY = random.randint(0,4)

grid[playerX][playerY] = 'p'
grid[gridX][gridY] = ''




for step in range(10):
    for i in range(len(grid)):
        print(grid[i])

    action = input()

    if action  == 's':
        if playerX == 4:
            print('no')
        else:
            grid[playerX][playerY] = ''
            playerX += 1
            grid[playerX][playerY] = 'p'
    elif action == 'w':
        if playerX == 0:
            print('no')
        else:
            grid[playerX][playerY] = ''
            playerX -= 1
            grid[playerX][playerY] = 'p'
    elif action == 'd':
        if playerY == 4:
            print('no')
        else:
            grid[playerX][playerY] = ''
            playerY += 1
            grid[playerX][playerY] = 'p'
    elif action == 'a':
        if playerY == 0:
            print('no')
        else:
            grid[playerX][playerY] = ''
            playerY -= 1
            grid[playerX][playerY] = 'p'
    
    if playerX == gridX and playerY == gridY:
        for i in range(len(grid)):
            print(grid[i])
        print('you won')
        print('steps used:',step+1)
        break


if playerX != gridX or playerY != gridY:
    print('you lost llllll')

    grid[gridX][gridY] = 'X'
    for i in range(len(grid)):
        print(grid[i])
