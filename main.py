import pygame
from board import Board  # Ensure this points to your refactored Board class

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Checkers")

# Create Board instance
board_instance = Board(50, 50, screen)
clock = pygame.time.Clock()
running = True
mouse_button_down = False


x,y = 0, 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not mouse_button_down: 
            board_instance.select_piece()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_button_down = False

    screen.fill("red")
    board_instance.draw_board()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()