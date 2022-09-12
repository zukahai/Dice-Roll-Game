from typing import Tuple
import pygame, random

class game:
    def __init__(self):
        pygame.init()
        self.game_W = 600
        self.game_H = 450
        self.N_dice = 3
        self.screen = pygame.display.set_mode((self.game_W, self.game_H))
        self.done = False
        self.clock = pygame.time.Clock()
        self.x = 30
        self.y = 30
 
        self.BLACK = 0, 0, 0
 
        self.button = pygame.Rect(150, 150, 120, 80)
        self.roll = [0] * self.N_dice
        self.initDice()
        
        
    def pickNumber(self):
        diceroll = random.randint(1, 6)
        nameImage = ['one', 'two', 'three', 'four', 'five', 'six']
        dice = pygame.image.load('images/' + nameImage[diceroll - 1] + ".png")
        return {'dice': dice, 'diceroll': diceroll}
    
    def initDice(self):
        for i in range(0, self.N_dice):
            self.roll[i] = self.pickNumber()
            
    def run(self):
        while self.done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button.collidepoint(mouse_pos):
                    self.initDice()
                    print ([e['diceroll'] for e in self.roll])
    
            
            for i in range(0, self.N_dice):
                self.screen.blit(self.roll[i]['dice'], (i * 200, 0))
 
            pygame.draw.rect(self.screen, self.BLACK, self.button)
                
        
            pygame.display.flip()
        
            self.screen.fill((255, 255, 255))
     
 
 
 
        pygame.quit()
    
        
g = game()
g.run()