import pygame
# Everygame is a computer program which is stored in a memory
pygame.init()

# Creating window
gameWindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("My first Game")

# game specific variables
exit_game=False
game_over=False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print(f"You have pressed right arrow key")
pygame.quit()
quit()