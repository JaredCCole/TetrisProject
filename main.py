import pygame
import random
import copy


pygame.init()

pygame.display.set_caption("TETRIS")

clock = pygame.time.Clock()

win = pygame.display.set_mode((500, 700))

colors = [(0, 255, 255), (255, 0, 0), (255, 128, 0), (204, 0, 255), (255, 255, 0), (0, 0, 255), (0, 255, 0)]

nextX = 360
nextY = 200


class tetrimino(object):
    def __init__(self, type):
        if type == 0:
            self.tet0 = [
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            self.tet1 = [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0]
            ]
            self.tet2 = self.tet0
            self.tet3 = self.tet1
        elif type == 1:
            self.tet0 = [
                [0, 2, 2, 0],
                [0, 2, 2, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            self.tet1 = self.tet0
            self.tet2 = self.tet0
            self.tet3 = self.tet0
        elif type == 2:
            self.tet0 = [
                [0, 3, 3, 3],
                [0, 0, 0, 3],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            self.tet1 = [
                [0, 0, 3, 0],
                [0, 0, 3, 0],
                [0, 3, 3, 0],
                [0, 0, 0, 0]
            ]
            self.tet2 = [
                [0, 3, 0, 0],
                [0, 3, 3, 3],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            self.tet3 = [
                [0, 0, 3, 3],
                [0, 0, 3, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 0]
            ]
        elif type == 3:
            self.tet0 = [
                [0, 0, 0, 4],
                [0, 4, 4, 4],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            self.tet1 = [
                [0, 0, 4, 0],
                [0, 0, 4, 0],
                [0, 0, 4, 4],
                [0, 0, 0, 0]
            ]
            self.tet2 = [
                [0, 4, 4, 4],
                [0, 4, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            self.tet3 = [
                [0, 4, 4, 0],
                [0, 0, 4, 0],
                [0, 0, 4, 0],
                [0, 0, 0, 0]
            ]
        elif type == 4:
            self.tet0 = [
                [0, 0, 5, 5],
                [0, 5, 5, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            self.tet1 = [
                [0, 0, 5, 0],
                [0, 0, 5, 5],
                [0, 0, 0, 5],
                [0, 0, 0, 0]
            ]
            self.tet2 = self.tet0
            self.tet3 = self.tet1
        elif type == 5:
            self.tet0 = [
                [0, 0, 6, 0],
                [0, 6, 6, 6],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            self.tet1 = [
                [0, 0, 6, 0],
                [0, 0, 6, 6],
                [0, 0, 6, 0],
                [0, 0, 0, 0]
            ]
            self.tet2 = [
                [0, 0, 0, 0],
                [0, 6, 6, 6],
                [0, 0, 6, 0],
                [0, 0, 0, 0]
            ]
            self.tet3 = [
                [0, 0, 6, 0],
                [0, 6, 6, 0],
                [0, 0, 6, 0],
                [0, 0, 0, 0]
            ]
        else:
            self.tet0 = [
                [0, 7, 7, 0],
                [0, 0, 7, 7],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            self.tet1 = [
                [0, 0, 0, 7],
                [0, 0, 7, 7],
                [0, 0, 7, 0],
                [0, 0, 0, 0]
            ]
            self.tet2 = self.tet0
            self.tet3 = self.tet1

    def nextRotate(self, tet):
        if tet == self.tet0:
            tet = self.tet1
        elif tet == self.tet1:
            tet = self.tet2
        elif tet == self.tet2:
            tet = self.tet3
        else:
            tet = self.tet0
        return tet

    def previousRotate(self, tet):
        if tet == self.tet0:
            tet = self.tet3
        elif tet == self.tet1:
            tet = self.tet0
        elif tet == self.tet2:
            tet = self.tet1
        else:
            tet = self.tet2
        return tet


board = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def delete_tetrimino(board, t, position):
    """
    Given a board, tetrimino, and top left position, return the board without the tetrimino.
    """
    b = board
    try:
        for yb in range(4):
            for xb in range(4):
                    if board[yb+position[1]][xb+position[0]] != 0:
                        if t[yb][xb] != 0:
                            b[yb + position[1]][xb + position[0]] = 0
    except IndexError:
        for yb in range(4):
            for xb in range(3):
                try:
                    if board[yb + position[1]][xb + position[0]] != 0:
                        if t[yb][xb] != 0:
                            b[yb + position[1]][xb + position[0]] = 0
                except IndexError:
                    return b
    return b


def move_tetrimino(board, t, direction):
    global position
    new_board = delete_tetrimino(board, t, position)
    new_position = (position[0]+direction[0], position[1]+direction[1])
    position = new_position
    for y in range(4):
        for x in range(4):
            if t[y][x] != 0:
                new_board[y + new_position[1]][x + new_position[0]] = t[y][x]
    return new_board


def downCollision(board, t):
    global placed
    global position
    temp = False
    if t == [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]
    ]:
        if board[position[1] + 4][position[0] + 2] != 0:
            temp = True
    else:
        for y in range(4):
            for x in range(4):
                if t[y][x] != 0 and t[y+1][x] == 0 and board[position[1]+y+1][position[0]+x] != 0:
                    temp = True
    placed = temp


def leftCollision(board, t):
    if t == [
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]:
        if board[position[1]][position[0]-1] != 0:
            return False
    else:
        for y in range(4):
            for x in range(4):
                if t[y][x] != 0 and t[y][(x-1)] == 0 and board[position[1]+y][position[0]+(x-1)] != 0:
                    return False
    return True


def rightCollision(board, t):
    if t == [
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]:
        if board[position[1]][position[0] + 4] != 0:
            return False
    else:
        for y in range(4):
            for x in range(4):
                if x == 3:
                    if t[y][x] != 0 and board[position[1] + y][position[0] + (x + 1)] != 0:
                        return False
                elif t[y][x] != 0 and t[y][(x + 1)] == 0 and board[position[1] + y][position[0] + (x + 1)] != 0:
                    return False
    return True


def falling_tet(board, t, timeDelay):
    global flagFall
    global starttime
    global placed
    if not flagFall and not placed:
        starttime = pygame.time.get_ticks()
        flagFall = True
        board = move_tetrimino(board, t, (0, 1))
    if flagFall == True and pygame.time.get_ticks() - starttime >= timeDelay:
        flagFall = False
    return board


def instaPlace(board, t):
    global placed
    while not placed:
        board = move_tetrimino(board, t, (0, 1))
        downCollision(board, t)
    return board


def isCleared(board):
    b = copy.deepcopy(board)
    for y in range(20):
        for x in range(1, 11):
            if board[y][x] == 0:
                break
            if x == 10 and board[y][x] != 0:
                b.pop(y)
                b = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]] + b
    return b


def drawNextTet(t):
    for y in range(4):
        for x in range(4):
            if t[y][x] != 0:
                pygame.draw.rect(win, colors[t[y][x] - 1], (nextX + x * 35, nextY + 35 + y * 35, 35, 35))

def checkLost(t, board, position):
    """Returns True if player tops out, else False"""
    for y in range(4):
            for x in range(4):
                if t[y][x] != 0 and board[y][position[0] + x] != 0:
                    return True
    return False



def drawBoard(win, board):
    for y in range(20):
        for x in range(1, 11):
            if board[y][x] in range(1, 8):
                pygame.draw.rect(win, colors[board[y][x] - 1], ((x-1) * 35, y * 35, 35, 35))


def redrawGameWindow(board):
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (0, 0, 350, 700), width=1)
    pygame.draw.rect(win, (255, 0, 0), (nextX, nextY, 140, 140), width=1)
    drawNextTet(nextTet.tet0)
    drawBoard(win, board)
    pygame.display.update()


tet = tetrimino(random.randrange(7))
nextTet = tetrimino(random.randrange(7))
t = tet.tet0 # initial tetrimino is tet0
tprevious = None
position = (3, 0) #initial position is at the middle top of screen
inputFlag = False
flagFall = False
starttime = 0
rotatedelay = 0
moveDelay = 0
placedTime = 0
placed = False
board = move_tetrimino(board, t, (0, 0))  # places initial tetrimino
redrawGameWindow(board)
pygame.time.delay(500) # initial tetrimino holding for half a second at the top
run = True

while run:
    clock.tick(60)
    if placed and pygame.time.get_ticks() - placedTime >= 200:
        placedTime = 0
        tet = nextTet
        nextTet = tetrimino(random.randrange(7))
        t = tet.tet0
        position = (3, 0)
        if checkLost(t, board, position):
            break
        board = move_tetrimino(board, t, (0, 0))
        redrawGameWindow(board)
        pygame.time.delay(200)
        placed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if rotatedelay > 0:
        rotatedelay += 1
    if rotatedelay > 10:
        rotatedelay = 0
    if keys[pygame.K_UP] and rotatedelay == 0:
        cancelRotate = False
        rotatedelay = 1
        prevBoard = copy.deepcopy(board)
        delete_tetrimino(board, t, position)
        t = tet.nextRotate(t)

        for y in range(4):
            for x in range(4):
                if t[y][x] != 0 and board[position[1] + y][position[0] + x] != 0:
                    cancelRotate = True#places flag to see if new location to rotate is not allowed
        if cancelRotate:
            board = prevBoard
            t = tet.previousRotate(t)#returns board and current tetrimino rotation to original if flag found
        else:
            move_tetrimino(board, t, (0, 0))#else places new rotated tetrimino in position

    if moveDelay > 0:
        moveDelay += 1
    if moveDelay > 10:
        moveDelay = 0
    if keys[pygame.K_LEFT] and moveDelay == 0 and leftCollision(board, t):
        moveDelay = 1
        board = move_tetrimino(board, t, (-1, 0))
    elif keys[pygame.K_RIGHT] and moveDelay == 0 and rightCollision(board, t):
        moveDelay = 1
        board = move_tetrimino(board, t, (1, 0))

    if keys[pygame.K_DOWN]:
        falling_tet(board, t, 30)
    elif keys[pygame.K_SPACE]:
        board = instaPlace(board, t)
        placedTime = -1 #this ensures there is no place delay

    else:
        falling_tet(board, t, 200)
    downCollision(board, t)
    if placed:
        board = isCleared(board)
        if placedTime == 0:
            placedTime = pygame.time.get_ticks()
    redrawGameWindow(board)

pygame.quit()
