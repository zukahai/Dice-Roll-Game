from typing import Tuple
import pygame, random

class game:
    def __init__(self):
        pygame.init()
        self.NImageVideo = 200
        self.game_W = 600
        self.game_H = 450
        self.N_dice = 3
        self.screen = pygame.display.set_mode((self.game_W, self.game_H))
        self.done = False
        self.clock = pygame.time.Clock()
        self.x = 30
        self.y = 30
        self.BLACK = 0, 0, 0
        self.button = pygame.Rect(self.game_W / 3, 3.6 * self.game_H / 5, self.game_W / 3, self.game_H / 5)
        self.roll = [0] * self.N_dice
        self.dice = [0] * 200
        pygame.display.set_caption('Dice roll game | HaiZuka')
        self.initDice()
        self.initVideoDice()
        
        
    def pickNumber(self):
        diceroll = random.randint(1, 6)
        nameImage = ['one', 'two', 'three', 'four', 'five', 'six']
        dice = pygame.image.load('images/dice/' + nameImage[diceroll - 1] + ".png")
        dice = pygame.transform.scale(dice, (145, 145))
        return {'dice': dice, 'diceroll': diceroll}
    
    def initDice(self):
        for i in range(0, self.N_dice):
            self.roll[i] = self.pickNumber()

    def initVideoDice(self):
        for i in range(0, self.NImageVideo):
            self.dice[i] = pygame.image.load('images/sprite/' + str(i + 1) + ".png")
            self.dice[i] = pygame.transform.scale(self.dice[i], (145, 145)) 
    
    def draw(self):
        space = (self.game_W - self.N_dice * self.roll[0]['dice'].get_size()[0]) / (self.N_dice  + 1)
        for i in range(0, self.N_dice):
            self.screen.blit(self.roll[i]['dice'], ((i + 1) * space + i * self.roll[0]['dice'].get_size()[0], space))
        pygame.draw.rect(self.screen, self.BLACK, self.button)
        pygame.display.flip()
        
        
    def runVideo(self, index, start):
        for i in range(0, self.N_dice):
            self.roll[i] = {'dice': self.dice[(index + start[i]) % self.NImageVideo], 'diceroll': 1}
        
            
    def run(self):
        click = False
        while self.done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button.collidepoint(mouse_pos) and click == False:
                    start = [random.randint(1, self.NImageVideo)] * self.N_dice
                    for j in range(0, 5):
                        for i in range(0, self.NImageVideo):
                            self.runVideo(i, [10, 50, 100])
                            self.draw()
                            pygame.time.wait(4)
                    self.initDice()
                    click = True
                    self.draw()
                    print ([e['diceroll'] for e in self.roll])
            self.draw()
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
            self.screen.fill((255, 255, 255))
     
 
 
 
        pygame.quit()
    
        
g = game()
g.run()