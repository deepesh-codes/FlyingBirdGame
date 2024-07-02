import pygame
#from Tools.demo.sortvisu import WIDTH
from pygame import draw

pygame.init()

BGcolor = (0, 0, 0)
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("flying bird")
icon = pygame.image.load('bird.png')
pygame.display.set_icon(icon)

screen.fill(BGcolor)
pygame.display.flip()

# High score display on option screen
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

High_scoreX = 280
High_scoreY = 100


# label of score
def show_score(x, y):
    score = font.render("High Score :" + str(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))

Sound_value = 0
# label of sound
def show_Sound(x, y):
    score = pygame.font.SysFont("monospace", 200)


SoundX = 280
SoundY = 150

# add sound
bgSound = pygame.mixer.music.load('whisper.mp3')
pygame.mixer.music.play(-1)

label = font.render("Sound", (Sound_value),True, (255, 255, 0))
screen.blit(label, (SoundX, SoundY))


class Button(pygame.sprite.Sprite):
    def _init_(self, img, scale, x, y):
        super(Button, self)._init_()

        self.image = img
        self.scale = scale
        self.image = pygame.transform.scale(self.image, self.scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        def blit(self, screen):
            screen.blit(self.image, self.rect)

SoundOn = pygame.image.load('sound on.png')
SoundOn_btn = Button(SoundOn, (24, 24), 24, 24)

MusicX = 280
MusicY = 150

Music_label = font.render("Music", 1, (255, 255, 0))
screen.blit(label, (MusicX, MusicY))


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

High_scoreX = 280
High_scoreY = 100

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K -quit() or \
                    event.key == pygame.K_ESCAPE:
                running = False
    show_score(High_scoreX, High_scoreY)
    #show_Sound.blit(SoundX, SoundY)
    #show_Music(MusicX,MusicY)
    #SoundOn_btn.rect.(screen)
    pygame.display.update()