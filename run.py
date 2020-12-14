import pygame

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

board = (
    [['X','A','B','C','D','E','F','G','H','X'],
     ['8','R','N','B','K','K','B','N','R','8'],
     ['7','P','P','P','P','P','P','P','P','7'],
     ['6','-','-','-','-','-','-','-','-','6'],
     ['5','-','-','-','-','-','-','-','-','5'],
     ['4','-','-','-','-','-','-','-','-','4'],
     ['3','-','-','-','-','-','-','-','-','3'],
     ['2','P','P','P','P','P','P','P','P','2'],
     ['1','R','N','Q','Q','K','B','N','R','1'],
     ['X','A','B','C','D','E','F','G','H','X']]
)

def draw_board(clicked):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if c == 0 or c==COLUMN_COUNT-1 or r==0 or r == ROW_COUNT-1:
                pygame.draw.rect(screen, BLACK, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, GREY, (c*SQUARE_SIZE+1, r*SQUARE_SIZE+SQUARE_SIZE+1, SQUARE_SIZE-2, SQUARE_SIZE-2))
            elif (c + r) % 2 == 0: 
                pygame.draw.rect(screen, GREEN, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, DARK_GREEN, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            if c == clicked[0] and r == clicked[1]:
                pygame.draw.rect(screen, YELLOW, (c*SQUARE_SIZE+1, r*SQUARE_SIZE+SQUARE_SIZE+1, SQUARE_SIZE-2, SQUARE_SIZE-2))
                print(clicked)

            label = font.render(board[r][c], 1, BLACK)
            screen.blit(label, (c*SQUARE_SIZE+12, r*SQUARE_SIZE+SQUARE_SIZE+5))
    pygame.display.update()

def calc_tile(x, y):
    return [int(x / SQUARE_SIZE), int((y - 50) / SQUARE_SIZE)]

running = True
clicked = [-1, -1]
draw_board(clicked)
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pygame.mouse.get_pos()
            clicked = calc_tile(x, y)
            
            draw_board(clicked)