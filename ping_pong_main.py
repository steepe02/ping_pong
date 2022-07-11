from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.x < 520:
            self.rect.y += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_DOWN] and self.rect.x < 520:
            self.rect.x += self.speed

player_l = Player('rocket.png', 30, 200, 5, 50, 100)
player_r = Player('rocket.png', 520, 200, 5, 50, 100)

#ball = GameSprite('ball.jpg', 200, 200, 5, 40, 40)

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
background = (200, 255, 255)
window.fill(background)

finish = False
game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        player_l.update_l()
        player_l.reset()

        player_r.update_r()
        player_r.reset()

        #if sprite.spritecollide(player_l, ball, False):

        #if sprite.spritecollide(player_r, ball, False):
        
        #if ball.self.x <= 0 or ball.self.x >= 600:
            #finish = True

    display.update()
    clock.tick(FPS)
