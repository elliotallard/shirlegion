# Shirlegion
    # Elliot Allard (eallard)
    # Stephanie Ananth (sananth)
    # Annette Guo (amguo)
    # Angela Sun (angelas1)

import pygame
import time
import random
import math
import os

class Struct(object): pass
data = Struct()

def init(data):
    # Model
    data.folder = 'images'
    data.goal = 128
    data.staffNumber = 52
    data.rows = data.cols = 4
    data.board = newBoard(data.rows, data.cols)
    data.randomPieces = [2, 2, 4]
    for i in range(0, 2): generatePiece(data)
    data.values = makeValuesList(data.goal)
    data.staffByRole = dictStaffByRole(data.folder)
    data.valuesByStaff = dictValuesByStaff(data)
    data.staffByValues = dictStaffByValues(data)

    # View
    pygame.init()
    data.width = data.height = 600
    data.margin = data.width // 100
    data.padding = data.margin * 10
    data.side = (data.width - 2*data.padding - 2*data.margin)//4 - 2*data.margin
    data.screen = pygame.display.set_mode((data.width, data.height))
    data.font = pygame.font.Font(None, 30)
    data.bigFont = pygame.font.Font(None, 48)
    data.message = ''
    data.BLUE = (0, 0, 255)
    data.BLACK = (0, 0, 0)
    data.DARK_GRAY = (50, 50, 50)
    data.LIGHT_GRAY = (200, 200, 200)
    data.WHITE = (255, 255, 255)
    data.colors = dictColorsByValue(data)

    # Controller
    data.clock = pygame.time.Clock()
    data.mode = 'home'
    data.isPlaying = True

    while (data.isPlaying):
        pygame.display.update()
        data.time = data.clock.tick(50)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                data.isPlaying = False
            elif (event.type == pygame.KEYDOWN):
                keyPressed(data, event.key)
        data.screen.fill(data.WHITE)
        redrawAll(data)
        pygame.display.flip()
    drawGameOver(data)
    pygame.quit()
    print('Bye!')

# Model
def newBoard(rows, cols):
    result = []
    for row in range(rows):
        rowResult = []
        for col in range(cols):
            rowResult += [[0, None]]
        result += [rowResult]
    return result

def makeValuesList(goal):
    result = []
    while (goal >= 2):
        result += [goal]
        goal //= 2
    return result

def dictStaffByRole(folder):
    result = dict()
    for role in os.listdir(folder):
        for staffMember in os.listdir(folder + os.sep + role):
            if (role in result):
                result[role].add(staffMember.split('.')[0])
            else:
                result[role] = set([staffMember.split('.')[0]])
    return result

def dictValuesByStaff(data):
    result = dict()
    for role in data.staffByRole:
        for staffMember in data.staffByRole[role]:
            if (role == 'profs'):
                value = (role, data.values[1])
            elif (role == 'headTAs'):
                value = (role, data.values[2])
            elif (role == 'assHeadTAs'):
                value = (role, data.values[3])
            else:
                value = (role, random.choice(data.values[4:]))
            result[staffMember] = value
    return result

def dictStaffByValues(data):
    result = dict()
    result[data.values[0]] = 'display42'
    for value in data.values[1:]:
        result[value] = set()
    for staffPerson in data.valuesByStaff:
        result[data.valuesByStaff[staffPerson][1]].add(staffPerson)
    return result

def generatePiece(data):
    randomChoices = []
    for row in range(data.rows):
        for col in range(data.cols):
            if (data.board[row][col][0] == 0):
                randomChoices += [(row, col)]
    if (randomChoices == []): return 0
    place = random.choice(randomChoices)
    data.board[place[0]][place[1]][0] = random.choice(data.randomPieces)

def dictColorsByValue(data):
    result = dict()
    maxColor = 255
    delta = maxColor // (len(data.values[3:]) - 1)
    for i in range(len(data.values[3:])):
        result[data.values[i+3]] = (maxColor-delta*i, maxColor-delta*i, delta*i)
    result[data.values[0]] = (0, 0, maxColor)
    result[data.values[1]] = (maxColor, 0, 0)
    result[data.values[2]] = (maxColor, maxColor, 0)
    result[data.values[3]] = (0, maxColor, 0)
    result[data.values[-1]] = (0, 0, maxColor)
    return result

# View
def redrawAll(data):
    if (data.mode == 'home'):
        data.message = 'Press space to play!'
        drawHomeMessage(data)
    elif (data.mode == 'playGame'):
        data.message = 'Not playGame42'
        drawGame(data)
        drawGameMessage(data)

def drawHomeMessage(data):
    text = data.font.render(data.message, True, data.BLUE)
    data.screen.blit(text, (data.width//2 - text.get_width()//2, 
                            data.height//2*0.6 - text.get_height()*2))
    text = data.bigFont.render('Welcome to not playGame42!', True, data.BLUE)
    data.screen.blit(text, (data.width//2 - text.get_width()//2, 
                            data.height//2*0.4 - text.get_height()*2))
def drawGameMessage(data):
    text = data.font.render(data.message, True, data.WHITE)
    data.screen.blit(text, (data.width//2 - text.get_width()//2,
                            data.height//10 - text.get_height()*2))
def drawGameOver(data):
    text = data.font.render('Game Over!', True, data.BLACK)
    data.screen.blit(text, (data.width//2 - text.get_width()//2,
                            data.height - text.get_height()*2))
def drawGame(data):
    pygame.draw.rect(data.screen, data.DARK_GRAY, (0, 0, data.width, 
                                                         data.height))
    pygame.draw.rect(data.screen, data.WHITE, (data.padding, data.padding,
                     data.width-2*data.padding, data.height-2*data.padding))
    for row in range(data.rows):
        for col in range(data.cols):
            x0 = y0 = data.padding + data.margin*2
            dx = dy = data.margin*2 + data.side
            pygame.draw.rect(data.screen, data.LIGHT_GRAY, (x0 + dx*col,
                             y0 + dy*row, data.side, data.side))
            if (data.board[row][col][0] != 0):
                value = data.board[row][col][0]
                pygame.draw.rect(data.screen, data.colors[value], (x0 + dx*col,
                                 y0 + dy*row, data.side, data.side))
                if (data.board[row][col][1] == None):
                    staffMember = random.sample(data.staffByValues[value], 1)[0]
                    data.board[row][col][1] = staffMember
                else:
                    staffMember = data.board[row][col][1]
                path = (data.folder + os.sep +
                        data.valuesByStaff[staffMember][0] + os.sep +
                        staffMember + '.jpg')
                img = pygame.image.load(path)
                img = pygame.transform.scale(img, (data.side-4*data.margin,
                                             data.side-4*data.margin))
                data.screen.blit(img, (x0 + dx*col + 2*data.margin,
                                 y0 + dy*row + 2*data.margin,
                                 data.side - 2*data.margin,
                                 data.side - 2*data.margin))

# Controller
def keyPressed(data, key):
    if (data.mode == 'home'):
        if (key == pygame.K_SPACE):
            data.mode = 'playGame'
    elif (data.mode == 'playGame'):
        if (key == pygame.K_UP): moveUp(data)
        elif (key == pygame.K_DOWN): moveDown(data)
        elif (key == pygame.K_LEFT): moveLeft(data)
        elif (key == pygame.K_RIGHT): moveRight(data)

def moveUp(data):
    for col in range(data.cols):
        for row in range(data.rows):
            if (data.board[row][col][0] != 0):
                moveUpRecursively(data, row, col, data.board[row][col])
    generatePiece(data)

def moveUpRecursively(data, row, col, value):
    if (row == 0):
        data.board[row][col] = value
    elif (data.board[row-1][col][0] == 0):
        data.board[row][col] = [0, None]
        moveUpRecursively(data, row-1, col, value)
    elif (data.board[row-1][col][0] == data.board[row][col][0]):
        data.board[row][col] = [0, None]
        moveUpRecursively(data, row-1, col, [value[0] * 2, None])
    else:
        data.board[row][col] = value

def moveDown(data):
    for col in range(data.cols-1, -1, -1):
        for row in range(data.rows-1, -1, -1):
            if (data.board[row][col][0] != 0):
                moveDownRecursively(data, row, col, data.board[row][col])
    generatePiece(data)

def moveDownRecursively(data, row, col, value):
    if (row == (data.rows-1)):
        data.board[row][col] = value
    elif (data.board[row+1][col][0] == 0):
        data.board[row][col] = [0, None]
        moveDownRecursively(data, row+1, col, value)
    elif (data.board[row+1][col][0] == data.board[row][col][0]):
        data.board[row][col] = [0, None]
        moveDownRecursively(data, row+1, col, [value[0] * 2, None])
    else:
        data.board[row][col] = value

def moveLeft(data):
    for row in range(data.rows):
        for col in range(data.cols):
            if (data.board[row][col][0] != 0):
                moveLeftRecursively(data, row, col, data.board[row][col])
    generatePiece(data)

def moveLeftRecursively(data, row, col, value):
    if (col == 0):
        data.board[row][col] = value
    elif (data.board[row][col-1][0] == 0):
        data.board[row][col] = [0, None]
        moveLeftRecursively(data, row, col-1, value)
    elif (data.board[row][col-1][0] == data.board[row][col][0]):
        data.board[row][col] = [0, None]
        moveLeftRecursively(data, row, col-1, [value[0] * 2, None])
    else:
        data.board[row][col] = value

def moveRight(data):
    for row in range(data.rows-1, -1, -1):
        for col in range(data.cols-1, -1, -1):
            if (data.board[row][col][0] != 0):
                moveRightRecursively(data, row, col, data.board[row][col])
    generatePiece(data)

def moveRightRecursively(data, row, col, value):
    if (col == (data.cols-1)):
        data.board[row][col] = value
    elif (data.board[row][col+1][0] == 0):
        data.board[row][col] = [0, None]
        moveRightRecursively(data, row, col+1, value)
    elif (data.board[row][col+1][0] == data.board[row][col][0]):
        data.board[row][col] = [0, None]
        moveRightRecursively(data, row, col+1, [value[0] * 2, None])
    else:
        data.board[row][col] = value

init(data)