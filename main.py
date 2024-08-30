import pygame
from board import Board  # Ensure this points to your refactored Board class

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Checkers")

# Create Board instance
board_instance = Board(125, 125, screen)
clock = pygame.time.Clock()
running = True
mouse_button_down = False
mbd = False
test = None 
global piece
piece = None
x,y = 0, 0
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not mouse_button_down: 
            board_instance.select_piece()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_button_down = False

    # Clear screen and draw board
    screen.fill("red")
    board_instance.draw_board()
    
    # Draw the piece if test is not None
    #if test is not None:
        #print(test)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
