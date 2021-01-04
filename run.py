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
w_pawn = pygame.image.load('./assets/w_pawn.png')
b_pawn = pygame.image.load('./assets/b_pawn.png')
w_rook = pygame.image.load('./assets/w_rook.png')
b_rook = pygame.image.load('./assets/b_rook.png')
w_knight = pygame.image.load('./assets/w_knight.png')
b_knight = pygame.image.load('./assets/b_knight.png')
w_bishop = pygame.image.load('./assets/w_bishop.png')
b_bishop = pygame.image.load('./assets/b_bishop.png')
w_queen = pygame.image.load('./assets/w_queen.png')
b_queen = pygame.image.load('./assets/b_queen.png')
w_king = pygame.image.load('./assets/w_king.png')
b_king = pygame.image.load('./assets/b_king.png')

def draw_image(name, x, y):
    if name == 'WP':
        screen.blit(w_pawn, (x, y))
    elif name == 'BP':
        screen.blit(b_pawn, (x, y))
    elif name == 'WN':
        screen.blit(w_knight, (x, y))
    elif name == 'BN':
        screen.blit(b_knight, (x, y))
    elif name == 'WR':
        screen.blit(w_rook, (x, y))
    elif name == 'BR':
        screen.blit(b_rook, (x, y))
    elif name == 'WB':
        screen.blit(w_bishop, (x, y))
    elif name == 'BB':
        screen.blit(b_bishop, (x, y))
    elif name == 'WQ':
        screen.blit(w_queen, (x, y))
    elif name == 'BQ':
        screen.blit(b_queen, (x, y))
    elif name == 'WK':
        screen.blit(w_king, (x, y))
    elif name == 'BK':
        screen.blit(b_king, (x, y))

# Font 
font = pygame.font.SysFont("monospace", 40)
# Colors
BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN = (204, 255, 204)
DARK_GREEN = (93, 206, 157)
GREY = (219, 219, 219)
YELLOW = (203, 255, 50)


def draw_board(from_move, to_move, board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if c == 0 or c==COLUMN_COUNT-1 or r==0 or r == ROW_COUNT-1:
                pygame.draw.rect(screen, BLACK, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, GREY, (c*SQUARE_SIZE+1, r*SQUARE_SIZE+SQUARE_SIZE+1, SQUARE_SIZE-2, SQUARE_SIZE-2))
                label = font.render(str(board[r][c]), 1, BLACK)
                screen.blit(label, (c*SQUARE_SIZE+12, r*SQUARE_SIZE+SQUARE_SIZE+5))
            elif (c + r) % 2 == 0: 
                pygame.draw.rect(screen, GREEN, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                draw_image(str(board[r][c]), c*SQUARE_SIZE+9, r*SQUARE_SIZE+SQUARE_SIZE+9)
            else:
                pygame.draw.rect(screen, DARK_GREEN, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                draw_image(str(board[r][c]), c*SQUARE_SIZE+9, r*SQUARE_SIZE+SQUARE_SIZE+9)

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
    screen.fill(DARK_GREEN)
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
   
    #pygame.display.update()