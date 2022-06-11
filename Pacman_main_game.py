import random
from pygame import *

font.init()

font_score = font.Font('Tkachev - Lugatype.ttf', 24)
coins_count = 0

font_end = font.Font('Tkachev - Lugatype.ttf', 50)

class GameSprite(sprite.Sprite):
    def __init__(self, images, x, y, width, height, speed):
        super().__init__()

        #img = image.load(image)
        self.image = transform.scale(image.load(images), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self, window):
        window.blit(self.image, self.rect)
        
class Hero(GameSprite):
    def update(self):
        print('TODO: Update Hero')
        
    def move(self, keyPressed):
        side = None
        
        if keyPressed[K_LEFT] and self.rect.left > 5:
            self.rect.x -= self.speed
            if sprite.spritecollide(self, walls, False):
                side = 'Right'
                self.rect.x += 3
                
        if keyPressed[K_RIGHT] and self.rect.right < win_width:
            self.rect.x += self.speed
            if sprite.spritecollide(player, walls, False):
                side = 'Left'
                self.rect.x -= 3
                
        if keyPressed[K_UP] and self.rect.top > 5:
            self.rect.y -= self.speed
            if sprite.spritecollide(self, walls, False):
                side = 'Down'
                self.rect.y += 3
                
        if keyPressed[K_DOWN] and self.rect.bottom < win_height:
            self.rect.y += self.speed
            if sprite.spritecollide(self, walls, False):
                side = 'Up'
                self.rect.y -= 3

        if side:
           print('Hero collision:', side)
                
        if self.rect.right > win_width-10 and 300 < self.rect.top < 330:
            self.rect.left = 10 

        elif self.rect.left < 10 and 300 < self.rect.top < 330:
            self.rect.right = win_width-10
        
        if sprite.spritecollide(self, ghosts, False):
            if len(health) == 3:
                heart3.kill()
                self.rect.x, self.rect.y = 10, 302
            elif len(health) == 2:
                heart2.kill()
                self.rect.x, self.rect.y = 10, 302
            elif len(health) == 1:
                heart1.kill()
                self.rect.x, self.rect.y = 10, 302
                
class Enemy(GameSprite):

    def __init__(self, image, x, y, width, height, speed):
        super().__init__(image, x, y, width, height, speed)
        
        self.move_list = ['right', 'left', 'up', 'down']

        self.direction = random.choice(self.move_list)

    def move(self):
        if self.direction == 'right':
            if not sprite.spritecollide(self, walls, False):
                self.rect.x += speed
            else:
                self.rect.x -= 2
                self.direction = random.choice(self.move_list)
        elif self.direction == 'left':
            if not sprite.spritecollide(self, walls, False):
                self.rect.x -= speed
            else:
                self.rect.x += 2
                self.direction = random.choice(self.move_list)
        elif self.direction == 'up':
            if not sprite.spritecollide(self, walls, False):
                self.rect.y -= speed
            else:
                self.rect.y += 2
                self.direction = random.choice(self.move_list)
        elif self.direction == 'down':
            if not sprite.spritecollide(self, walls, False):
                self.rect.y += speed
            else:
                self.rect.y -= 2
                self.direction = random.choice(self.move_list)
    
class Wall(sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()

        self.color = color
        self.width = width
        self.height = height
        
        self.image = Surface((self.width, self.height))
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self, window):
        window.blit(self.image, self.rect)

# it keeps single coin so name `Coin` without `s` seems better        
class Coin(sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        
        self.image = Surface((self.width, self.height))
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
    def draw(self, window):
        window.blit(self.image, self.rect)
        

# --- main ---

win_height = 700
win_width = 700

init()  # pygame.init()       

window = display.set_mode((win_width, win_height))
display.set_caption('Pacman Game')

#back = transform.scale(image.load('photo_2022-06-05_21-28-54.jpg'), (700, 700))

super_point = GameSprite('super_point.png', 345, 640, 20, 25, 1)
player = Hero('full_open_mouth.png', 10, 302, 24, 24, 1)

ghost_chise = Enemy('21575-4-pac-man-ghost-image.png', 350, 309, 25, 25, 4)
ghost_other = Enemy('pacman-ghost-galaxy.png', 350, 309, 20, 25, 4)
ghost_third = Enemy('PacmanGhost.png', 350, 309, 20, 25, 4)

heart1 = GameSprite('health.png', 605, 2, 25, 25, 1)
heart2 = GameSprite('health.png', 630, 2, 25, 25, 1)
heart3 = GameSprite('health.png', 655, 2, 25, 25, 1)

health = sprite.Group()
health.add(heart1, heart2, heart3)

walls = [
    Wall( (169,169,169), 0, 0, 700, 31), 
    Wall( (169,169,169), 0, 20, 31, 210), 
    Wall( (169,169,169), 0, 200, 145, 31), 
    Wall( (169,169,169), 115, 200, 31, 95), 
    Wall( (169,169,169), 0, 270, 145, 31), 
    Wall( (169,169,169), 670, 20, 31, 210), 
    Wall( (169,169,169), 556, 200, 145, 31), 
    Wall( (169,169,169), 556, 200, 31, 95), 
    Wall( (169,169,169), 556, 270, 150, 31), 
    Wall( (169,169,169), 335, 0, 31, 95), 
    Wall( (169,169,169), 187, 70, 110, 31), 
    Wall( (169,169,169), 406, 70, 110, 31), 
    Wall( (169,169,169), 187, 470, 110, 31), 
    Wall( (169,169,169), 406, 470, 110, 31), 
    Wall( (169,169,169), 190, 335, 31, 95), 
    Wall( (169,169,169), 485, 335, 31, 95), 
    Wall( (169,169,169), 0, 670, 700, 31), 
    Wall( (169,169,169), 0, 400, 31, 280), 
    Wall( (169,169,169), 0, 400, 145, 31), 
    Wall( (169,169,169), 115, 340, 31, 70), 
    Wall( (169,169,169), 0, 334, 145, 31), 
    Wall( (169,169,169), 670, 400, 31, 280), 
    Wall( (169,169,169), 556, 340, 31, 70), 
    Wall( (169,169,169), 556, 334, 145, 31), 
    Wall( (169,169,169), 556, 400, 150, 31), 
    Wall( (169,169,169), 16, 531, 60, 31), 
    Wall( (169,169,169), 624, 531, 60, 31), 
    Wall( (169,169,169), 260, 340, 180, 31), 
    Wall( (169,169,169), 260, 135, 180, 31), 
    Wall( (169,169,169), 260, 531, 180, 31), 
    Wall( (169,169,169), 260, 400, 180, 31), 
    Wall( (169,169,169), 190, 135, 31, 160), 
    Wall( (169,169,169), 335, 135, 31, 95), 
    Wall( (169,169,169), 335, 405, 31, 95), 
    Wall( (169,169,169), 335, 542, 31, 95), 
    Wall( (169,169,169), 190, 535, 31, 95), 
    Wall( (169,169,169), 485, 535, 31, 95), 
    Wall( (169,169,169), 485, 135, 31, 160), 
    Wall( (169,169,169), 75, 70, 70, 31), 
    Wall( (169,169,169), 75, 133, 70, 31), 
    Wall( (169,169,169), 555, 70, 70, 31), 
    Wall( (169,169,169), 555, 133, 70, 31), 
    Wall( (169,169,169), 555, 470, 70, 31), 
    Wall( (169,169,169), 75, 470, 70, 31), 
    Wall( (169,169,169), 115, 470, 31, 95), 
    Wall( (169,169,169), 555, 470, 31, 95), 
    Wall( (169,169,169), 75, 600, 220, 31), 
    Wall( (169,169,169), 405, 600, 220, 31), 
    Wall( (169,169,169), 215, 200, 85, 31), 
    Wall( (169,169,169), 405, 200, 85, 31), 
    Wall( (169,169,169), 260, 270, 30, 31), 
    Wall( (169,169,169), 410, 270, 30, 31), 
    Wall( (169,169,169), 260, 275, 31, 95), 
    Wall( (169,169,169), 410, 275, 31, 95), 
]

coins = sprite.Group()

coins.add([
    Coin( (255,255,0), 130, 309, 5, 5), 
    Coin( (255,255,0), 240, 309, 5, 5), 
    Coin( (255,255,0), 340, 250, 5, 5), 
    Coin( (255,255,0), 460, 309, 5, 5), 
    Coin( (255,255,0), 570, 309, 5, 5), 
    Coin( (255,255,0), 240, 180, 5, 5), 
    Coin( (255,255,0), 460, 180, 5, 5), 
    Coin( (255,255,0), 310, 111, 5, 5), 
    Coin( (255,255,0), 390, 111, 5, 5), 
    Coin( (255,255,0), 60, 180, 5, 5), 
    Coin( (255,255,0), 640, 180, 5, 5), 
    Coin( (255,255,0), 60, 50, 5, 5), 
    Coin( (255,255,0), 640, 50, 5, 5), 
    Coin( (255,255,0), 160, 409, 5, 5), 
    Coin( (255,255,0), 240, 380, 5, 5), 
    Coin( (255,255,0), 340, 380, 5, 5), 
    Coin( (255,255,0), 460, 380, 5, 5), 
    Coin( (255,255,0), 530, 409, 5, 5), 
    Coin( (255,255,0), 460, 450, 5, 5), 
    Coin( (255,255,0), 240, 450, 5, 5), 
    Coin( (255,255,0), 390, 450, 5, 5), 
    Coin( (255,255,0), 310, 450, 5, 5), 
    Coin( (255,255,0), 630, 450, 5, 5), 
    Coin( (255,255,0), 50, 450, 5, 5), 
    Coin( (255,255,0), 600, 520, 5, 5), 
    Coin( (255,255,0), 90, 520, 5, 5), 
    Coin( (255,255,0), 530, 570, 5, 5), 
    Coin( (255,255,0), 160, 570, 5, 5), 
    Coin( (255,255,0), 60, 640, 5, 5), 
    Coin( (255,255,0), 640, 640, 5, 5),  
])

ghosts = sprite.Group()
ghosts.add(ghost_chise, ghost_other, ghost_third)

finish = False
game = True

coins_count = 0
speed = 1

clock = time.Clock()

print(len(health))

while game:
    display.set_icon(image.load("pacman-html-canvas-.ico"))
    for e in event.get():
        if e.type == QUIT:
            exit()
    # GHOSTS
    ghost_chise.move()
    ghost_other.move()            
    ghost_third.move()
    
    # PACMAN
    keyPressed = key.get_pressed()
    
    player.move(keyPressed)

    if sprite.spritecollide(player, coins, True):
        coins_count += 100
    #ANIMATION
    if player.rect.x % 2 == 1:
        player = Hero('full_open_mouth.png', player.rect.x, player.rect.y, 24, 24, 1)
    if player.rect.x % 2 == 0:
        player = Hero('close_mounth.png', player.rect.x, player.rect.y, 24, 24, 1)
    # UPDATE SCREEN    
    if finish != True:
        window.fill((0, 0, 0))
        
        for w in walls:
            w.draw(window)
        score = font_score.render('Score : ', False, (255, 255, 0))
        score_num = font_score.render(str(coins_count), False, (255, 255, 0))
        window.blit(score, (30, 1))
        window.blit(score_num, (95, 2))
            
        coins.draw(window)
        
        player.draw(window)
        
        ghosts.draw(window)

        super_point.draw(window)

        health.draw(window)

        display.update()
        clock.tick(60)
    elif finish:
        lvl_lose = font_end.render('Level is not complete!', False, (255, 0, 0))
        window.blit(lvl_lose, (300, 300))
    if len(health) == 0:
        finish = True