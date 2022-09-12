import pygame, random
 
pygame.init()
screen = pygame.display.set_mode((600, 450))
done = False
clock = pygame.time.Clock()
x = 30
y = 30
 
BLACK = 0, 0, 0
 
button = pygame.Rect(150, 150, 120, 80)
 
def pickNumber():
    diceroll = random.randint(1, 6)
    nameImage = ['one', 'two', 'three', 'four', 'five', 'six']
    dice = pygame.image.load('images/' + nameImage[diceroll - 1] + ".png")
         
    return (dice, diceroll)
 
dice, diceroll = pickNumber()
print(dice.get_size()[0])
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
             
        if button.collidepoint(mouse_pos):
            dice, diceroll = pickNumber()
            screen.blit(dice, (0, 0))
            print(diceroll)
            
    screen.blit(dice, (0, 0))
 
    pygame.draw.rect(screen, BLACK, button)
         
 
    pygame.display.flip()
 
    screen.fill((255, 255, 255))
     
 
 
 
pygame.quit()