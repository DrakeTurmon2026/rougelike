import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([400, 400])

board = []

def setupboard():
    global board
    for x in range(1,10):
        board.append([])
        for y in range(1,20):
            board[x-1].append(0)

setupboard()
# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill((0, 0, 0))

    #draw a line where the board ends
    pygame.draw.rect(screen, (255,255,255), pygame.rect.Rect(200,0,1,400))

    #draw the board
    for x, column in enumerate(board):
        for y, row in enumerate(column):
            if row == 0:
                pygame.draw.rect(screen, (0,255,0), pygame.rect.Rect((x-1)*20+1,(y-1)*20+1,18,18))
            

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
