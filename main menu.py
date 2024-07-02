import pygame
import random
from pygame import mixer

pygame.init()

#start screen 
def Start():
    global running1,a,b,score0,font0

    # start window
    start = pygame.display.set_mode((1000, 600))

    # title and icon
    pygame.display.set_caption("Flying Bird")
    icon = pygame.image.load('robin.png')
    pygame.display.set_icon(icon)

    
    #background 
    background = pygame.image.load('cloud.png')
    backgroundsizex = 1000
    backgroundsizey = 600
    backgroundsize = (backgroundsizex,backgroundsizey)
    background = pygame.transform.scale(background,backgroundsize)

    # player
    playerimage = pygame.image.load('dove1.png')
    playerx = 150
    playery = 250
    playersizex = 50
    playersizey = 50
    playery_change = 0
    playerx_change = 0
    playersize = (playersizex,playersizey)
    playerimage = pygame.transform.scale(playerimage,playersize)

    # obsticle
    obs =  pygame.image.load('pipe.png')
    obs1 = pygame.image.load('pipe1.png')
    obs2 = pygame.image.load('pipe2.png')
    obs3 = pygame.image.load('pipe3.png')
    obs4 = pygame.image.load('pipe4.png')
    obs5 = pygame.image.load('pipe5.png')
    obs6 = pygame.image.load('pipe6.png')
    obs7 = pygame.image.load('pipe7.png')

    obsticle1x = 300
    obsticle1y = -250

    obsticle2x = 300
    obsticle2y = 350

    obsticle3x = 600
    obsticle3y = -250

    obsticle4x = 600
    obsticle4y = 350

    obsticle5x = 900
    obsticle5y = -250

    obsticle6x = 900
    obsticle6y = 350

    size1x = 300
    size2x = 300
    size3x = 300
    size4x = 300

    size1y = 500
    size2y = 500
    size3y = 500
    size4y = 500

    obsize = (size1x, size1y)
    obsize1 = (size2x, size2y)
    obsize2 = (size3x, size3y)
    obsize3 = (size4x, size4y)

    obs = pygame.transform.scale(obs, obsize)
    obs1 = pygame.transform.scale(obs1, obsize)

    obs2 = pygame.transform.scale(obs2, obsize1)
    obs3 = pygame.transform.scale(obs3, obsize1)

    obs4 = pygame.transform.scale(obs4, obsize2)
    obs5 = pygame.transform.scale(obs5, obsize2)

    obs6 = pygame.transform.scale(obs6, obsize3)
    obs7 = pygame.transform.scale(obs7, obsize3)

    obsticle1x_change = 2
    obsticle2x_change = 2

    obsticle3x_change = 2
    obsticle4x_change = 2

    obsticle5x_change = 2
    obsticle6x_change = 2

    # obsticle control
    x = 1
    y = 1
    z = 1


    def player(playerx, playery):
        start.blit(playerimage, (playerx, playery))


    def obsticle():
        start.blit(obs, (obsticle1x, obsticle1y))
        start.blit(obs1, (obsticle2x, obsticle2y))
        start.blit(obs2, (obsticle3x, obsticle3y))
        start.blit(obs3, (obsticle4x, obsticle4y))
        start.blit(obs4, (obsticle5x, obsticle5y))
        start.blit(obs5, (obsticle6x, obsticle6y))

    

    font0 = pygame.font.SysFont("Times New Roman",50)



    # running window
    running = True
    while running:

        start.blit(background,(0,0))

        playercube = pygame.Rect(playerx,playery,50,50)
        obsticle1cube = pygame.Rect(obsticle1x + 90,obsticle1y,120,500)
        obsticle2cube = pygame.Rect(obsticle2x + 90,obsticle2y,120,500)
        obsticle3cube = pygame.Rect(obsticle3x + 90,obsticle3y,120,500)
        obsticle4cube = pygame.Rect(obsticle4x + 90,obsticle4y,120,500)
        obsticle5cube = pygame.Rect(obsticle5x + 90,obsticle5y,120,500)
        obsticle6cube = pygame.Rect(obsticle6x + 90,obsticle6y,120,500)
        rectmm = pygame.Rect(400,310,240,40)
        # events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                running1 = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playery_change = -3

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    playery_change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playery_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playerx_change = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    playerx_change = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rectmm.collidepoint(event.pos):
                   
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    obsticle1x_change = 0
                    obsticle2x_change = 0
                    obsticle3x_change = 0
                    obsticle4x_change = 0
                    obsticle5x_change = 0
                    obsticle6x_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    obsticle1x_change = 2
                    obsticle2x_change = 2

                    obsticle3x_change = 2
                    obsticle4x_change = 2

                    obsticle5x_change = 2
                    obsticle6x_change = 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        playery += playery_change
        playerx += playerx_change

        

        obsticle1x -= obsticle1x_change
        obsticle2x -= obsticle2x_change

        obsticle3x -= obsticle3x_change
        obsticle4x -= obsticle4x_change

        obsticle5x -= obsticle5x_change
        obsticle6x -= obsticle6x_change

        if obsticle1x == 100:
            x = x + 1
            x = x % 2

        if obsticle3x == 100:
            y = y + 1
            y = y % 2

        if obsticle5x == 100:
            z = z + 1
            z = z % 2

        if playerx <= 0:
            playerx = 2

        elif playerx >= 970:
            playerx = 970

        if obsticle1x <= 0 and x == 0:
            obsticle1x = 950
            a = random.randint(70, 100)
            obsticle1y = obsticle1y - a

        elif obsticle2x <= 0 and x == 0:
            obsticle2x = 950
            obsticle2y = obsticle2y - a

        if obsticle1x <= 0 and x == 1:
            obsticle1x = 950
            a = random.randint(70, 100)
            obsticle1y = obsticle1y + a

        elif obsticle2x <= 0 and x == 1:
            obsticle2x = 950
            obsticle2y = obsticle2y + a

        if obsticle3x <= 0 and y == 0:
            obsticle3x = 950
            b = random.randint(70, 100)
            obsticle3y = obsticle3y + b

        elif obsticle4x <= 0 and y == 0:
            obsticle4x = 950
            obsticle4y = obsticle4y + b

        if obsticle3x <= 0 and y == 1:
            obsticle3x = 950
            b = random.randint(70, 100)
            obsticle3y = obsticle3y - b

        elif obsticle4x <= 0 and y == 1:
            obsticle4x = 950
            obsticle4y = obsticle4y - b

        if obsticle5x <= 0 and z == 0:
            obsticle5x = 950
            c = random.randint(70, 100)
            obsticle5y = obsticle5y - c

        elif obsticle6x <= 0 and z == 0:
            obsticle6x = 950
            obsticle6y = obsticle6y - c

        if obsticle5x <= 0 and z == 1:
            obsticle5x = 950
            c = random.randint(70, 100)
            obsticle5y = obsticle5y + c

        elif obsticle6x <= 0 and z == 1:
            obsticle6x = 950
            obsticle6y = obsticle6y + c

        
        player(playerx, playery)
        obsticle()
        score = font0.render("Score:",True,'white')
        score1 = font0.render(str(score0),True,'white')
        start.blit(score,(0,0))
        start.blit(score1,(130,0))

        if playerx == obsticle1x+100 or playerx == obsticle3x+100 or playerx == obsticle5x+100:
            score0 += 5

        #collision detection 
        
        if playercube.colliderect(obsticle1cube) or playercube.colliderect(obsticle2cube) or playercube.colliderect(obsticle3cube) or playercube.colliderect(obsticle4cube) or playercube.colliderect(obsticle5cube) or playercube.colliderect(obsticle6cube):
       
            gm=(0,0,0)
            start.fill(gm)
            obsticle1x_change = 0
            obsticle2x_change = 0
            obsticle3x_change = 0
            obsticle4x_change = 0
            obsticle5x_change = 0
            obsticle6x_change = 0
            playerx_change = 0
            playery_change = 0

            score0 += 0    
            font1 = pygame.font.SysFont("Times New Roman",70)
            font2 = pygame.font.SysFont("Times New Roman",50)

            gameover = font1.render("Game Over",True,'white')
            mm = font2.render("Main Menu",True,'white')
            
            start.blit(gameover,(350,200))
            button3 = pygame.Rect(450,260,100,50)
            #start = font.render("Start",True,'black')
            start.blit(score,(0,0))
            start.blit(score1,(130,0))
            start.blit(mm,(400,300))
            
        pygame.display.update()


#option screen
def Option():

    global running2,bgimg,font0,font1,font2,running1,a,b

    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Flying bird")
    icon = pygame.image.load('bird.png')
    
    Birdmain = pygame.image.load("bird.png")
    Birdmainx = 50
    Birdmainy = 50
    Birdmainsize = (Birdmainx , Birdmainy)
    Birdmain = pygame.transform.scale(Birdmain,Birdmainsize)

    # Option.blit(Birdmain,(470,20))
    pygame.display.set_icon(icon)

    font = pygame.font.SysFont(('Times New Roman'),50,bold=False)
    
    

    Back = font.render('Back',True,'blue')
    

    soundon = pygame.Rect(450,280,60,60)
    soundoff = pygame.Rect(550,280,60,60)
    back1 = pygame.Rect(480,350,100,60)
    


        
    #sound off

    soundOff_Img = pygame.image.load('off.png')
    soundOff_ImgX = 550
    soundOff_Imgy = 280

    sizeOffx = 60
    sizeOffy = 60
    soundOff_ImgX_size = (sizeOffx,sizeOffy)

    soundOff_Img = pygame.transform.scale(soundOff_Img,(soundOff_ImgX_size))
  
        

    #sound on 

    soundOn_Img = pygame.image.load('on.png')
    soundOn_ImgX = 450
    soundOn_Imgy = 280

    sizeOnx = 60
    sizeOny = 60
    soundOn_ImgX_size = (sizeOnx,sizeOny)
    soundOn_Img = pygame.transform.scale(soundOn_Img,(soundOn_ImgX_size))


    
    soundtoggle = True
    running2 = True
    while running2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running2 = False
                running1 = False
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if soundon.collidepoint(event.pos):
                    soundtoggle = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if soundoff.collidepoint(event.pos):
                    soundtoggle = True

            if event.type == pygame.MOUSEBUTTONDOWN:    
                if back1.collidepoint(event.pos):
                    running2 = False

                    

        mainmenu.blit(bgimg,(0,0))
        

        if soundtoggle:
            pygame.draw.rect(mainmenu,'white',soundon)
            mixer.music.set_volume(5)
        else:
            pygame.draw.rect(mainmenu,'white',soundoff)
            mixer.music.set_volume(0)
        
        screen.blit(soundOff_Img,(soundOff_ImgX,soundOff_Imgy))
        screen.blit(soundOn_Img,(soundOn_ImgX,soundOn_Imgy))
        screen.blit(Back,(480,350))
        

        pygame.display.update()

#background sound 

mixer.music.load('BirdSound.mp3')
mixer.music.play()


#window
mainmenu = pygame.display.set_mode((1000,600))

#window color 
#mainmenucolor = (135, 206, 235)
#icon, title
pygame.display.set_caption("Flying Bird")
icon = pygame.image.load("bird.png")
pygame.display.set_icon(icon)

#background image
bgimg = pygame.image.load("bgimg.png")
bgx = 1000
bgy = 600
bgsize = (bgx,bgy)
bgimg = pygame.transform.scale(bgimg,bgsize)


# Flying Bird Image
FBF = pygame.image.load("flying bird Font.png")
FBFx = 170 #Width
FBFy = 60 #height
FBFsize = (FBFx,FBFy)
FBF = pygame.transform.scale(FBF,FBFsize)



# bird image on main menu 
# Birdmain = pygame.image.load("bird.png")
# Birdmainx = 50
# Birdmainy = 50
# Birdmainsize = (Birdmainx , Birdmainy)
# Birdmain = pygame.transform.scale(Birdmain,Birdmainsize)

#pipes on main menu
# pipe 1 e.i, on left side of screen
pipe_image1 = pygame.image.load("pipe.png")
pipe1x = 240  #width 
pipe1y = 310 #height

pipe1_size = (pipe1x , pipe1y)
pipe_image1 = pygame.transform.scale(pipe_image1 ,pipe1_size)

# pipe 2 that is on right side of window 
pipe_image2 = pygame.image.load("pipe.png")
pipe2x = 240  #width 
pipe2y = 310 #height

pipe2_size = (pipe1x , pipe1y)
pipe_image2 = pygame.transform.scale(pipe_image1 ,pipe1_size)

#button

font = pygame.font.SysFont("Times New Roman",40)
font1 = pygame.font.SysFont("TimesNew Roman", 30)
font2 = pygame.font.SysFont("Times New Roman",60)
#font3 = pygame.font.SysFont(20)
start = font.render("Start",True,'black')
option = font.render("Option",True,'black')
exit = font.render("Exit",True,'black')
high = font1.render("Previous Score:",True,'black')


mm = font2.render("Main Menu",True,'yellow')

score0 = 0
score2 = 0 

button = pygame.Rect(450,260,100,50)
button1 = pygame.Rect(430,330,140,60)
button2 = pygame.Rect(450,400,90,50)






#main loop 
running1=True
while running1:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running1 = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button2.collidepoint(event.pos):
                pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:    
            if button.collidepoint(event.pos):
                #score0 = 0 
                Start()

        if event.type == pygame.MOUSEBUTTONDOWN:    
            if button1.collidepoint(event.pos):
                Option()
    
    mainmenu.blit(bgimg,(0,0))
    mainmenu.blit(FBF,(420,55))
    mainmenu.blit(pipe_image1,(100,150)) #left and right of pipe  #down and up of pipe #respectively
    mainmenu.blit(pipe_image2,(645,150))
    #mainmenu.blit(Birdmain,(470,20))
    a,b = pygame.mouse.get_pos() 

    score2 = score0

    hgs = font1.render(str(score2),True,'black')

    mainmenu.blit(high,(0,0))
    mainmenu.blit(hgs,(200,1))
    mainmenu.blit(start,(450,250))
    mainmenu.blit(option,(430,320))
    mainmenu.blit(exit,(450,390))
    mainmenu.blit(mm,(350,160))
    
    pygame.display.update()
