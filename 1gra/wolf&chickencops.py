import pygame
import random

WIDTH=800
HEIGHT=574
FPS=50

#IMAGES
    #menu
mbg=pygame.image.load('obrazki/tlomenu.jpg')
menubackground=pygame.transform.scale(mbg,(WIDTH,HEIGHT))
gt=pygame.image.load('obrazki/menutitle.png')
game_title=pygame.transform.scale(gt,(WIDTH,HEIGHT))
play_button=pygame.image.load('obrazki/buttonplay.png')
highscores_button=pygame.image.load('obrazki/buttonhighscores.png')
about_button=pygame.image.load('obrazki/buttonabout.png')
about_info=pygame.image.load('obrazki/about.png')
back_button=pygame.image.load('obrazki/buttonback.png')

    #game bg
bg = pygame.image.load('obrazki/Tlo.jpg')
background=pygame.transform.scale(bg,(WIDTH,HEIGHT))
void=pygame.image.load('obrazki/nic.png')

    #lives
l3=pygame.image.load('obrazki/3lives.png')
l2=pygame.image.load('obrazki/2lives.png')
l1=pygame.image.load('obrazki/1lives.png')

lives_3=pygame.transform.scale(l3,(235,95))
lives_2=pygame.transform.scale(l2,(235,95))
lives_1=pygame.transform.scale(l1,(235,95))

    #wolf
UL=pygame.image.load('obrazki/LG.png')
UR=pygame.image.load('obrazki/PG.png')
DL=pygame.image.load('obrazki/LD.png')
DR=pygame.image.load('obrazki/PD.png')

wolf_UL=pygame.transform.scale(UL,(290,290))
wolf_DL=pygame.transform.scale(DL,(290,290))
wolf_UR=pygame.transform.scale(UR,(275,275))
wolf_DR=pygame.transform.scale(DR,(275,275))

    #eggs
e1=pygame.image.load('obrazki/UL_1.png')
e2=pygame.image.load('obrazki/UL_2.png')
e3=pygame.image.load('obrazki/UL_3.png')
e4=pygame.image.load('obrazki/UL_4.png')
e5=pygame.image.load('obrazki/UL_5.png')

egg_1=pygame.transform.scale(e1,(60,60))
egg_2=pygame.transform.scale(e2,(60,60))
egg_3=pygame.transform.scale(e3,(60,60))
egg_4=pygame.transform.scale(e4,(60,60))
egg_5=pygame.transform.scale(e5,(60,60))

#PARAMETERS
i=0
j=-1
n=125
speed=[]
for _ in range(23):
    speed.append(n)
    n-=5
n_copied=speed[i]
n_mod=int(n_copied/5)
    
score=0
lives=3
skip=[0]
first_pos=0

#FUNCTIONS
def points(score):
    font = pygame.font.SysFont("comicsansms", 41)
    text=font.render(str(score), True, (0,0,0))
    screen.blit(text,(440,7))
    
#CLASSES
class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=void
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/2,HEIGHT/2)
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.image=wolf_UL
            self.rect=self.image.get_rect()
            self.rect.center=(WIDTH/2,HEIGHT/2)
        if keys[pygame.K_a]:
            self.image=wolf_DL
            self.rect=self.image.get_rect()
            self.rect.center=(WIDTH/2,HEIGHT/2)
        if keys[pygame.K_p]:
            self.image=wolf_UR
            self.rect=self.image.get_rect()
            self.rect.center=(450,300)
        if keys[pygame.K_l]:
            self.image=wolf_DR
            self.rect=self.image.get_rect()
            self.rect.center=(450,300)

class PhantomWolf(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=void
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/2,HEIGHT/2)
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.image=void
            self.rect.center=(0,0)
        if keys[pygame.K_a]:
            self.image=void
            self.rect.center=(0,HEIGHT)
        if keys[pygame.K_p]:
            self.image=void
            self.rect.center=(WIDTH,0)
        if keys[pygame.K_l]:
            self.image=void
            self.rect.center=(WIDTH,HEIGHT)
        
            
class Egg_pos1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=void
        self.rect=self.image.get_rect()
        self.rect.center=(100,100)

        self.updated_UL1=False
        self.updated_UL2=False
        self.updated_UL3=False
        self.updated_UL4=False
        self.updated_UL_phantom=False

        self.updated_DL1=False
        self.updated_DL2=False
        self.updated_DL3=False
        self.updated_DL4=False
        self.updated_DL_phantom=False

        self.updated_UR1=False
        self.updated_UR2=False
        self.updated_UR3=False
        self.updated_UR4=False
        self.updated_UR_phantom=False

        self.updated_DR1=False
        self.updated_DR2=False
        self.updated_DR3=False
        self.updated_DR4=False
        self.updated_DR_phantom=False
        
    def update(self):
        #upper-left egg
        #print(first_pos)
        if first_pos==1:
            self.image=egg_1
            self.rect.center=(100,100)
            self.updated_UL1=True

        if self.updated_UL1==True and n==n_copied-1*n_mod:
            self.image=egg_2
            self.rect.center=(150,125)
            self.updated_UL1=False
            self.updated_UL2=True
            
        if self.updated_UL2==True and n==n_copied-2*n_mod:
            self.image=egg_3
            self.rect.center=(190,170)
            self.updated_UL2=False
            self.updated_UL3=True
            
        if self.updated_UL3==True and n==n_copied-3*n_mod:
            self.image=egg_4
            self.rect.center=(230,200)
            self.updated_UL3=False
            self.updated_UL4=True
            
        if self.updated_UL4==True and n==n_copied-4*n_mod:
            self.image=egg_5
            self.rect.center=(275,220)
            self.updated_UL4=False
            self.updated_UL_phantom=True

        if self.updated_UL_phantom==True and n==1:
            self.image=void
            self.rect.center=(0,0)
            self.updated_UL_phantom=False
            
        #down-left egg
        if first_pos==2:
            self.image=egg_1
            self.rect.center=(75,325)
            self.updated_DL1=True
            
        if self.updated_DL1==True and n==n_copied-1*n_mod:
            self.image=egg_2
            self.rect.center=(140,325)
            self.updated_DL1=False
            self.updated_DL2=True
            
        if self.updated_DL2==True and n==n_copied-2*n_mod:
            self.image=egg_3
            self.rect.center=(175,325)
            self.updated_DL2=False
            self.updated_DL3=True
            
        if self.updated_DL3==True and n==n_copied-3*n_mod:
            self.image=egg_4
            self.rect.center=(215,315)
            self.updated_DL3=False
            self.updated_DL4=True
            
        if self.updated_DL4==True and n==n_copied-4*n_mod:
            self.image=egg_5
            self.rect.center=(260,320)
            self.updated_DL4=False
            self.updated_DL_phantom=True

        if self.updated_DL_phantom==True and n==1:
            self.image=void
            self.rect.center=(0,HEIGHT)
            self.updated_DL_phantom=False
            
        #upper-right egg
        if first_pos==3:
            self.image=egg_2
            self.rect.center=(700,100)
            self.updated_UR1=True

        if self.updated_UR1==True and n==n_copied-1*n_mod:
            self.image=egg_1
            self.rect.center=(675,125)
            self.updated_UR1=False
            self.updated_UR2=True
            
        if self.updated_UR2==True and n==n_copied-2*n_mod:
            self.image=egg_3
            self.rect.center=(625,160)
            self.updated_UR2=False
            self.updated_UR3=True
            
        if self.updated_UR3==True and n==n_copied-3*n_mod:
            self.image=egg_4
            self.rect.center=(600,180)
            self.updated_UR3=False
            self.updated_UR4=True
            
        if self.updated_UR4==True and n==n_copied-4*n_mod:
            self.image=egg_5
            self.rect.center=(575,195)
            self.updated_UR4=False
            self.updated_UR_phantom=True
            
        if self.updated_UR_phantom==True and n==1:
            self.image=void
            self.rect.center=(WIDTH,0)
            self.updated_UR_phantom=False

        #down-right egg
        if first_pos==4:
            self.image=egg_1
            self.rect.center=(720,350)
            self.updated_DR1=True
            
        if self.updated_DR1==True and n==n_copied-1*n_mod:
            self.image=egg_2
            self.rect.center=(670,335)
            self.updated_DR1=False
            self.updated_DR2=True
            
        if self.updated_DR2==True and n==n_copied-2*n_mod:
            self.image=egg_3
            self.rect.center=(625,325)
            self.updated_DR2=False
            self.updated_DR3=True
            
        if self.updated_DR3==True and n==n_copied-3*n_mod:
            self.image=egg_4
            self.rect.center=(580,315)
            self.updated_DR3=False
            self.updated_DR4=True
            
        if self.updated_DR4==True and n==n_copied-4*n_mod:
            self.image=egg_5
            self.rect.center=(550,305)
            self.updated_DR4=False
            self.updated_DR_phantom=True
            
        if self.updated_DR_phantom==True and n==1:
            self.image=void
            self.rect.center=(WIDTH,HEIGHT)
            self.updated_DR_phantom=False
            



#GAME
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Wolf & Chicken cops')
clock=pygame.time.Clock()

all_sprites= pygame.sprite.Group()
eggs=pygame.sprite.Group()

wolf=Wolf()
phantomwolf=PhantomWolf()
all_sprites.add(wolf)
all_sprites.add(phantomwolf)

eggs.add(Egg_pos1())

def game_intro():
    intro = True
    while intro:
        screen.blit(menubackground,(0,0))
        screen.blit(game_title,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(play_button,(195,160))
        #pygame.draw.ellipse(screen,(0,0,0),(200,170,400,60))
        screen.blit(highscores_button,(217,250))
        #pygame.draw.ellipse(screen,(0,0,0),(220,250,360,60))
        screen.blit(about_button,(245,330))
        #pygame.draw.ellipse(screen,(0,0,0),(240,330,320,60))
        #pygame.display.update()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 200<mouse[0]<600 and 170<mouse[1]<230:
            pygame.draw.circle(screen,(0,0,0),(180,200),10)
            pygame.draw.circle(screen,(0,0,0),(630,200),10)
            if click[0]==1:
                game_loop()
                i=0
                j=-1
                n=125
                speed=[]
                for _ in range(23):
                    speed.append(n)
                    n-=5
                n_copied=speed[i]
                n_mod=int(n_copied/5)
                    
                score=0
                lives=3
                skip=[0]
                first_pos=0
        if 220<mouse[0]<580 and 250<mouse[1]<310:
            pygame.draw.circle(screen,(0,0,0),(200,280),10)
            pygame.draw.circle(screen,(0,0,0),(610,280),10)
        if 240<mouse[0]<560 and 330<mouse[1]<390:
            pygame.draw.circle(screen,(0,0,0),(225,360),10)
            pygame.draw.circle(screen,(0,0,0),(575,360),10)
            if click[0]==1:
                game_about()

        pygame.display.update()
                
    
def game_loop():

    global first_pos
    global i
    global j
    global n
    global speed
    global n_copied
    global n_mod
    global score
    global lives
    global skip
   
    running=True
    while running:
        screen.blit(background,(0,0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                
        #timer1
        if n>1:
            n-=1
            first_pos=0
            
        else:
            n_copied=speed[i]
            n=n_copied
            first_pos=random.choice([1,2,3,4])
            n_mod=int(n_copied/5)
            j+=1
            if j%3==0 and i<22:
                j+=1
                i+=1
            
            
        all_sprites.update()
        eggs.update()
        
        #score&lives
        if pygame.sprite.spritecollide(phantomwolf,eggs,False):
            score+=1
        if n==1 and not pygame.sprite.spritecollide(phantomwolf,eggs,False):
            lives-=1
        if lives==2 or lives==3:
            screen.blit(lives_3,(390,475))
        if lives==1:
            screen.blit(lives_2,(390,475))
        if lives==0:
            screen.blit(lives_1,(390,475))
        if lives==-1:
            i=0
            j=-1
            n=125
            score=0
            lives=3
            skip=[0]
            first_pos=0
            all_sprites.update()
            all_sprites.draw(screen)
            running=False
            
        all_sprites.draw(screen)
        
        eggs.draw(screen)
        points(score)


        pygame.display.update()
        clock.tick(FPS)

def game_about():
    about = True
    while about:
        screen.blit(menubackground,(0,0))
        screen.blit(about_info,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #pygame.draw.ellipse(screen,(0,0,0),(260,400,290,60))
        screen.blit(back_button,(260,400))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 260<mouse[0]<550 and 400<mouse[1]<460:
            pygame.draw.circle(screen,(0,0,0),(245,430),8)
            pygame.draw.circle(screen,(0,0,0),(560,430),8)
            if click[0]==1:
                about=False

        
        
        pygame.display.update()



game_intro()

pygame.quit()

