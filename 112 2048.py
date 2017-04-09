import pygame
import random

#board = [[0 for i in range(4)]for j in range(4)]

def initGame(board):
    row, col = random.randint(0,3), random.randint(0,3)
    row2, col2 = random.randint(0,3), random.randint(0,3)
    while (row, col) == (row2, col2):
        row2, col2 = random.randint(0,3), random.randint(0,3)

def makeMoveUp(board):
    noComboList = []
    for row in range(1,4):
        for col in range(0,4):
            value = board[row][col]
            if value !=0:
                newRow = row - 1
                #moves up until it hits a value other than 0 or topBoard
                while board[newRow][col] == 0:
                    if newRow < 0: break
                    newRow -= 1
                board[newRow+1][col] = value
                if newRow+1 != row:
                    board[row][col] = 0
                #then compare 
                if newRow+1 > 0:
                    if board[newRow][col] == board[newRow+1][col] and (newRow, col) not in noComboList:
                        board[newRow][col] = value*2
                        noComboList.append((newRow,col))
                        board[newRow+1][col] = 0
    return board
    
def makeMoveDown(board):
    noComboList = []
    for row in range(2,-1,-1):
        for col in range(4):
            value = board[row][col]
            if value != 0:
                newRow = row +1
                while board[newRow][col]==0:
                    if newRow>3: break
                    newRow += 1
                board[newRow-1][col] = value
                if newRow-1 != row:
                    board[row][col] = 0
                if newRow-1 < 3:
                    if board[newRow][col] == board[newRow-1][col] and (newRow, col) not in noComboList:
                        board[newRow][col] = value * 2
                        noComboList.append((newRow,col))
                        board[newRow-1][col] = 0
    return board

def makeMoveLeft(board):
    noComboList = []
    for col in range(1,4):
        for row in range(4):
            value = board[row][col]
            if value !=0:
                newCol = col - 1
                #moves up until it hits a value other than 0 or topBoard
                while board[row][newCol] == 0:
                    if newCol < 0: break
                    newCol -= 1
                board[row][newCol+1] = value
                if newCol+1 != col:
                    board[row][col] = 0                
                #then compare 
                if newCol+1 > 0:
                    if board[row][newCol] == board[row][newCol+1] and (row, newCol) not in noComboList:
                        board[row][newCol] = value*2
                        noComboList.append((row, newCol))
                        board[row][newCol+1] = 0
    return board   
    
def makeMoveRight(board):
    noComboList = []
    for col in range(2,-1,-1):
        for row in range(4):
            value = board[row][col]
            if value != 0:
                newCol= col + 1
                while board[row][newCol] == 0:
                    if newCol>3: break
                    newCol +=1
                board[row][newCol-1] = value
                if newCol-1 != col:
                    board[row][col] = 0
                if newCol -1 < 3:
                    if board[row][newCol] == board[row][newCol-1] and (row, newCol) not in noComboList:
                        board[row][newCol] = value*2
                        noComboList.append((row, newCol))
                        board[row][newCol-1]=0
    return board
                
def testUp():
    
    # board = [
    # [0,2,4,2],
    # [0,0,0,2],
    # [2,2,8,2],
    # [2,4,4,2]]
    # sol = [
    # [4,4,4,4],
    # [0,4,8,4],
    # [0,0,4,0],
    # [0,0,0,0]]
    # assert(makeMoveUp(board) == sol)
    # board = [
    # [2,2,2,2],
    # [2,2,2,2],
    # [2,2,2,4],
    # [2,2,2,2]
    # ]
    # sol = [
    # [4,4,4,4],
    # [4,4,4,4],
    # [0,0,0,2],
    # [0,0,0,0]
    # ]
    # assert (makeMoveUp(board) == sol)
    # board = [
    # [4,2,0,0],
    # [8,4,0,0],
    # [2,2,0,0],
    # [0,0,0,0]]
    # sol = [
    # [4,2,0,0],
    # [8,4,0,0],
    # [2,2,0,0],
    # [0,0,0,0]
    # ]
    # assert (makeMoveUp(board) == sol)
    
    #down!
    board = [
    [0,2,4,2],
    [0,0,0,2],
    [2,2,8,2],
    [2,4,4,2]]
    sol = [
    [0,0,0,0],
    [0,0,4,0],
    [0,4,8,4],
    [4,4,4,4]]
    assert (makeMoveDown(board) == sol)
    #left
    board = [
    [0,2,4,2],
    [0,0,0,2],
    [2,2,8,2],
    [2,4,4,2]]
    sol = [
    [2,4,2,0],
    [2,0,0,0],
    [4,8,2,0],
    [2,8,2,0]]
    assert(makeMoveLeft(board) == sol)
    #right
    board = [
    [0,2,4,2],
    [0,0,0,2],
    [2,2,8,2],
    [2,4,4,2]]
    sol = [
    [0,2,4,2],
    [0,0,0,2],
    [0,4,8,2],
    [0,2,8,2]]
    assert (makeMoveRight(board) == sol)
testUp()