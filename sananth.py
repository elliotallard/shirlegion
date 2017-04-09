# Stephanie K. Ananth (sananth)
    # Elliot Allard (eallard)
    # Annette Guo (amguo)
    # Angela Sun (angelas1)

import os
import sys
import math
import random
import pygame

class Struct(object): pass
data = Struct()

def init(data):
    data.goal = 128
    data.folder = 'images'
    data.staffNumber = 52
    data.values = makeValuesList(data.goal)
    data.staffByRole = dictStaffByRole(data.folder)
    data.valuesByStaff = dictValuesByStaff(data)
    data.staffByValues = dictStaffByValues(data)

    data.colors = dictColorsByValue(data)
    data.width = data.height = 600
    data.screen = pygame.display.set_mode((data.width, data.height))

    data.testRowsCols = math.ceil(math.sqrt(data.staffNumber))
    data.testRowWidthColHeight = data.width // data.testRowsCols
    data.testMargin = data.testRowWidthColHeight // 10
    data.testSide = data.testRowWidthColHeight - 2*data.testMargin

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
                value = data.values[1]
            elif (role == 'headTAs'):
                value = data.values[2]
            elif (role == 'assHeadTAs'):
                value = data.values[3]
            else:
                value = random.choice(data.values[4:])
            result[staffMember] = value
    return result

def dictStaffByValues(data):
    result = dict()
    result[data.values[0]] = 'display42'
    for value in data.values[1:]:
        result[value] = set()
    for staffPerson in data.valuesByStaff:
        result[data.valuesByStaff[staffPerson]].add(staffPerson)
    return result

def dictColorsByValue(data):
    result = dict()
    maxColor = 255
    delta = maxColor // (len(data.values[3:]) - 1)
    for i in range(len(data.values[3:])):
        result[data.values[i+3]] = (0, maxColor-delta*i, delta*i)
    result[data.values[0]] = (0, 0, maxColor)
    result[data.values[1]] = (maxColor, 0, 0)
    result[data.values[2]] = (maxColor, maxColor, 0)
    result[data.values[3]] = (0, maxColor, 0)
    result[data.values[-1]] = (0, 0, maxColor)
    return result

def testDisplayStaff(data):
    pygame.init()
    x = y = 0
    for role in data.staffByRole:
        for staffMember in data.staffByRole[role]:
            color = data.colors[data.valuesByStaff[staffMember]]
            x1 = x
            x2 = x1 + 2*data.testMargin + data.testSide
            y1 = y
            y2 = y1 + 2*data.testMargin + data.testSide
            pygame.draw.rect(data.screen, color, (x1, y1, x2, y2))
            pygame.draw.rect(data.screen, (0, 0, 0), (x1, y1, x2, y2), 1)
            path = data.folder + os.sep + role + os.sep + staffMember + '.jpg'
            staffImg = pygame.image.load(path)
            staffImg = pygame.transform.scale(staffImg,
                                              (data.testSide, data.testSide))
            data.screen.blit(staffImg, (x+data.testMargin, y+data.testMargin))
            pygame.display.update()
            x += data.testRowWidthColHeight
            if (x >= data.width):
                x = 0
                y += data.testRowWidthColHeight

init(data)
testDisplayStaff(data)