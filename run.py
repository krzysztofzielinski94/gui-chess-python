import pygame

pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)

COLUMN_COUNT = 10
ROW_COUNT = 12
SQUARE_SIZE = 50

pygame.display.set_caption('Chess')
icon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(icon)

# Pieces
#K_img = pygame.image.load('./assets/icon.png')
# knight()
X = 370
Y = 480

# Font 
font = pygame.font.SysFont("monospace", 40)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN = (204, 255, 204)
DARK_GREEN = (93, 206, 157)
GREY = (219, 219, 219)

def knight():
    screen.blit(K_img, (X, Y))

def draw_board():
    header = 'XABCDEFGHX'
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if c == 0 or c==COLUMN_COUNT-1 or r==0 or r == ROW_COUNT-1:
                pygame.draw.rect(screen, GREY, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif (c + r) % 2 == 0: 
                pygame.draw.rect(screen, GREEN, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, DARK_GREEN, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            label = font.render(header[c], 1, BLACK)
            screen.blit(label, (c*SQUARE_SIZE+12, r*SQUARE_SIZE+SQUARE_SIZE+5))
    pygame.display.update()

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_board()