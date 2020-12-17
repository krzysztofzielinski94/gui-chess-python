import pygame
from chess import Game

pygame.init()
#Screen size
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)

COLUMN_COUNT = 10
ROW_COUNT = 10
SQUARE_SIZE = 50

pygame.display.set_caption('Chess')
icon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(icon)

# Pieces
#K_img = pygame.image.load('./assets/icon.png')
#def knight():
#    screen.blit(K_img, (X, Y))
# knight()
X = 370
Y = 480

# Font 
font = pygame.font.SysFont("monospace", 40)
# Colors
BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN = (204, 255, 204)
DARK_GREEN = (93, 206, 157)
GREY = (219, 219, 219)
YELLOW = (203, 255, 50)

#board = (
#    [['X','A','B','C','D','E','F','G','H','X'],
#     ['8','R','N','B','K','K','B','N','R','8'],
#     ['7','P','P','P','P','P','P','P','P','7'],
#     ['6','-','-','-','-','-','-','-','-','6'],
#     ['5','-','-','-','-','-','-','-','-','5'],
#     ['4','-','-','-','-','-','-','-','-','4'],
#     ['3','-','-','-','-','-','-','-','-','3'],
#     ['2','P','P','P','P','P','P','P','P','2'],
#     ['1','R','N','Q','Q','K','B','N','R','1'],
#     ['X','A','B','C','D','E','F','G','H','X']]
#)

def draw_board(from_move, to_move, board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if c == 0 or c==COLUMN_COUNT-1 or r==0 or r == ROW_COUNT-1:
                pygame.draw.rect(screen, BLACK, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, GREY, (c*SQUARE_SIZE+1, r*SQUARE_SIZE+SQUARE_SIZE+1, SQUARE_SIZE-2, SQUARE_SIZE-2))
            elif (c + r) % 2 == 0: 
                pygame.draw.rect(screen, GREEN, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, DARK_GREEN, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            #if (c == clicked[0] and r == clicked[1]) and (c != 0 and c != COLUMN_COUNT-1 and r !=0 and r != ROW_COUNT-1):
            #    pygame.draw.rect(screen, YELLOW, (c*SQUARE_SIZE+1, r*SQUARE_SIZE+SQUARE_SIZE+1, SQUARE_SIZE-2, SQUARE_SIZE-2))
                

            label = font.render(str(board[r][c]), 1, BLACK)
            screen.blit(label, (c*SQUARE_SIZE+2, r*SQUARE_SIZE+SQUARE_SIZE+2))
    pygame.display.update()

def calc_tile(x, y):
    return [int((y - 50) / SQUARE_SIZE), int(x / SQUARE_SIZE)]

running = True

# 
game = Game()
board = game.get_board()
#
from_move = [-1, -1]
to_move = [-1, -1]
draw_board(from_move, to_move, board)
draging = False



while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            draging = True
            pos = pygame.mouse.get_pos()
            x, y = pygame.mouse.get_pos()
            from_move = calc_tile(x, y)
            print ('from move', from_move)
        if event.type == pygame.MOUSEBUTTONUP:
            draging = False
            x, y = pygame.mouse.get_pos()
            to_move = calc_tile(x, y)
            print ('to move', to_move)
            game.upate_board(from_move, to_move)
            board = game.get_board()
            if from_move != to_move:
                draw_board(from_move, to_move, board)
            
            