import pygame, sys, random  
from pygame.locals import *  
import numpy as np
  
# 變數宣告  
BACKGROUNDCOLOR = (255, 255, 255)  
BLUE = (0, 0, 255)  
BLACK = (0, 0, 0)  
FPS = 40  
  
VHNUMS = 2 
CELLNUMS = VHNUMS*VHNUMS    
  
#  退出
def terminate():  
    pygame.quit()  
    sys.exit()  
      
# 隨機生成拼圖畫面
def newGameBoard():  
    board = np.random.permutation(CELLNUMS)  
    for i in range(CELLNUMS):  
        if board[i] == (CELLNUMS-1):
            blackCell = i
            board[i] = -1
            break
    return board, blackCell  
  
  
# 判斷是否完成  
def isFinished(board, blackCell):  
    for i in range(CELLNUMS-1):  
        if board[i] != i:  
            return False  
    return True  
  
# 初始化  
pygame.init()  
mainClock = pygame.time.Clock()  
  
# 加載圖片  
gameImage = pygame.image.load('syhuang.jpg')  
gameImage = pygame.transform.scale(gameImage, (800, 600))
gameRect = gameImage.get_rect()  
      
  
# 設置遊戲視窗
windowSurface = pygame.display.set_mode((gameRect.width, gameRect.height))  
pygame.display.set_caption('拼圖遊戲')  
  
cellWidth = int(gameRect.width / VHNUMS)  
cellHeight = int(gameRect.height / VHNUMS)  
  
finish = False  
  
gameBoard, blackCell = newGameBoard()  
print(gameBoard)
print(blackCell)

# 遊戲主程式  
while True:
  
    for event in pygame.event.get():  
        if event.type == QUIT:  
            terminate()  
        if event.type == MOUSEBUTTONDOWN and event.button == 1:  
            x, y = pygame.mouse.get_pos()  
            col = int(x / cellWidth)  
            row = int(y / cellHeight)  
            index = col + row*VHNUMS  
            if (index == blackCell-1 or index == blackCell+1 or index == blackCell-VHNUMS or index == blackCell+VHNUMS):  
                gameBoard[blackCell], gameBoard[index] = gameBoard[index], gameBoard[blackCell]  
                blackCell = index
                print(gameBoard)
                print(blackCell)
  
    if (isFinished(gameBoard, blackCell)):  
        gameBoard[blackCell] = CELLNUMS-1  
        finish = True 
        print ("You win the game!!!")
      
    windowSurface.fill(BACKGROUNDCOLOR)  
      
    for i in range(CELLNUMS): 
        if gameBoard[i] == -1:  
            continue 

        rowDst = int(i / VHNUMS)  
        colDst = int(i % VHNUMS)  
        rectDst = pygame.Rect(colDst*cellWidth, rowDst*cellHeight, cellWidth, cellHeight)  

        rowArea = int(gameBoard[i] / VHNUMS)  
        colArea = int(gameBoard[i] % VHNUMS)  
        rectArea = pygame.Rect(colArea*cellWidth, rowArea*cellHeight, cellWidth, cellHeight)  
        windowSurface.blit(gameImage, rectDst, rectArea)  
  
    for i in range(VHNUMS+1):  
        pygame.draw.line(windowSurface, BLACK, (i*cellWidth, 0), (i*cellWidth, gameRect.height))  
    for i in range(VHNUMS+1):  
        pygame.draw.line(windowSurface, BLACK, (0, i*cellHeight), (gameRect.width, i*cellHeight))  
  
    pygame.display.update()  
    mainClock.tick(FPS)  