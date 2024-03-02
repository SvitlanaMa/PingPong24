import pygame
pygame.init()

win_w = 700
win_h = 500

FPS = 40

window = pygame.display.set_mode((win_w, win_h))

clock = pygame.time.Clock()

background = pygame.image.load("flat.jpg")
background = pygame.transform.scale(background, (win_w, win_h))

class GameSprite:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Pers(GameSprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.clip = 5

    def move(self, key_up, key_down):
        k = pygame.key.get_pressed()
        if k[key_down]:
            if self.rect.right <= win_w:
                self.rect.y += self.speed 
        elif k[key_up]:
            if self.rect.left >= 0:
                self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.rect.y += self.speed
        elif self.rect.bottom >= 500:
            self.rect.y -= self.speed
        

raketka_img = pygame.image.load("Roket.jpg")
raketka1 = Pers(20, 200, 20, 60, raketka_img, 3)

game = True
while game:
    # window.fill((0, 255, 0))
    window.blit(background, (0, 0))
    raketka1.update()
    raketka1.move(pygame.K_w, pygame.K_s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(FPS)