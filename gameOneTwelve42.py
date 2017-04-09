# Elliot Allard (eallard)
# Stephanie K. Ananth (sananth)
# Annette Guo (amguo)
# Angela Sun (angelas1)

import os
import sys
import math
import pygame

def makeStaffDict(folder):
    staff = dict()
    for staffRole in os.listdir(folder):
        for staffMember in os.listdir(folder + os.sep + staffRole):
            if (staffRole in staff):
                staff[staffRole].add(staffMember.split('.')[0])
            else:
                staff[staffRole] = set([staffMember.split('.')[0]])
    return staff

def displayStaff(staff):
    pygame.init()
    width = height = 600
    screen = pygame.display.set_mode((width, height))
    staffNumber = 52
    rows = cols = math.ceil(math.sqrt(staffNumber))
    rowWidth = rowHeight = math.floor(width/rows)
    x = y = 0
    for staffRole in staff:
        print(staffRole)
        for staffMember in staff[staffRole]:
            print(staffMember)
            staffImage = pygame.image.load('images' + os.sep + staffRole + os.sep + staffMember + '.jpg')
            staffImage = pygame.transform.scale(staffImage, (rowWidth, rowHeight))
            screen.blit(staffImage, (x, y))
            x += rowWidth
            if (x >= width):
                x = 0
                y += rowHeight
            pygame.display.update()

displayStaff(makeStaffDict('images'))