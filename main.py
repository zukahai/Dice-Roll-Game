import pygame, random
 
pygame.init()
game_W = 600
game_H = 450
N_dice = 3
screen = pygame.display.set_mode((game_W, game_H))
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
    dice = pygame.transform.scale(dice, (300, 300)) 
    return {'dice': dice, 'diceroll': diceroll}

roll = [0] * N_dice

def initDice():
    for i in range(0, N_dice):
        roll[i] = pickNumber()
 
initDice()
# print(roll['dice'].get_size()[0])
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
             
        if button.collidepoint(mouse_pos):
            initDice()
            print ([e['diceroll'] for e in roll])
    
            
    for i in range(0, N_dice):
        screen.blit(roll[i]['dice'], (i * 200, 0))
 
    pygame.draw.rect(screen, BLACK, button)
         
 
    pygame.display.flip()
 
    screen.fill((255, 255, 255))
     
 
 
 
pygame.quit()