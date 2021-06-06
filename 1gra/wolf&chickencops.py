import pygame
import random

WIDTH=800
HEIGHT=571
FPS=50

#IMAGES

    #menu background
menubackground=pygame.image.load('obrazki/tlomenu.jpg')
game_title=pygame.image.load('obrazki/menutitle.png')

    #buttons
play_button=pygame.image.load('obrazki/buttonplay.png')
highscores_button=pygame.image.load('obrazki/buttonhighscores.png')
about_button=pygame.image.load('obrazki/buttonabout.png')
back_button=pygame.image.load('obrazki/buttonback.png')


about_info=pygame.image.load('obrazki/about.png')
highscores_info=pygame.image.load('obrazki/highscores.png')

go=pygame.image.load('obrazki/gameover.jpg')
gameover=pygame.transform.scale(go,(WIDTH,HEIGHT))

void=pygame.image.load('obrazki/nic.png')

    #game background
bg = pygame.image.load('obrazki/Tlo.jpg')
background=pygame.transform.scale(bg,(WIDTH,HEIGHT))

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
e3=pygame.image.load('obrazki/UR_3.png')
e4=pygame.image.load('obrazki/UL_4.png')
e5=pygame.image.load('obrazki/UL_5.png')

egg_1=pygame.transform.scale(e1,(60,60))
egg_2=pygame.transform.scale(e2,(60,60))
egg_3=pygame.transform.scale(e3,(60,60))
egg_4=pygame.transform.scale(e4,(60,60))
egg_5=pygame.transform.scale(e5,(60,60))

#MUSIC
generate_soundtrack=random.choice(['muza/music1.mp3','muza/music2.mp3','muza/music3.mp3','muza/music4.mp3'])


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
first_pos=0

end_game=False


name='Username: (press any key to add)'

highscores_text=open('highscores.txt','r')
highscores_lines=highscores_text.readlines()
highscores_help=[]
lines_help=[]
highscores_text.close()

for line in highscores_lines:
    try:
        a=line.split('...')
        a[0]=int(a[0])
        highscores_help.append(a)
    except:
        pass
print(highscores_help)

#FUNCTIONS
def points(score,colour,place):
    font = pygame.font.SysFont("comicsansms", 41)
    text=font.render(str(score), True, colour)
    screen.blit(text,place)

    
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
        if end_game:
            self.image=void
            self.rect=self.image.get_rect()
            self.rect.center=(WIDTH/2,HEIGHT/2)
            

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
        if end_game:
            self.image=void
            self.rect=self.image.get_rect()
            self.rect.center=(WIDTH/2,HEIGHT/2)
        
            
class Eggs(pygame.sprite.Sprite):
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
            egg_sound1.play()

        if self.updated_UL1==True and n==n_copied-1*n_mod:
            self.image=egg_2
            self.rect.center=(150,125)
            self.updated_UL1=False
            self.updated_UL2=True
            egg_sound2.play()
            
        if self.updated_UL2==True and n==n_copied-2*n_mod:
            self.image=egg_3
            self.rect.center=(190,170)
            self.updated_UL2=False
            self.updated_UL3=True
            egg_sound3.play()
            
        if self.updated_UL3==True and n==n_copied-3*n_mod:
            self.image=egg_4
            self.rect.center=(230,200)
            self.updated_UL3=False
            self.updated_UL4=True
            egg_sound4.play()
            
        if self.updated_UL4==True and n==n_copied-4*n_mod:
            self.image=egg_5
            self.rect.center=(275,220)
            self.updated_UL4=False
            self.updated_UL_phantom=True
            egg_sound5.play()

        if self.updated_UL_phantom==True and n==1:
            self.image=void
            self.rect.center=(0,0)
            self.updated_UL_phantom=False
            
        #down-left egg
        if first_pos==2:
            self.image=egg_1
            self.rect.center=(75,325)
            self.updated_DL1=True
            egg_sound1.play()
            
        if self.updated_DL1==True and n==n_copied-1*n_mod:
            self.image=egg_2
            self.rect.center=(140,325)
            self.updated_DL1=False
            self.updated_DL2=True
            egg_sound2.play()
            
        if self.updated_DL2==True and n==n_copied-2*n_mod:
            self.image=egg_3
            self.rect.center=(175,325)
            self.updated_DL2=False
            self.updated_DL3=True
            egg_sound3.play()
            
        if self.updated_DL3==True and n==n_copied-3*n_mod:
            self.image=egg_4
            self.rect.center=(215,315)
            self.updated_DL3=False
            self.updated_DL4=True
            egg_sound4.play()
            
        if self.updated_DL4==True and n==n_copied-4*n_mod:
            self.image=egg_5
            self.rect.center=(260,320)
            self.updated_DL4=False
            self.updated_DL_phantom=True
            egg_sound5.play()

        if self.updated_DL_phantom==True and n==1:
            self.image=void
            self.rect.center=(0,HEIGHT)
            self.updated_DL_phantom=False
            
        #upper-right egg
        if first_pos==3:
            self.image=egg_2
            self.rect.center=(700,100)
            self.updated_UR1=True
            egg_sound1.play()

        if self.updated_UR1==True and n==n_copied-1*n_mod:
            self.image=egg_1
            self.rect.center=(675,125)
            self.updated_UR1=False
            self.updated_UR2=True
            egg_sound2.play()
            
        if self.updated_UR2==True and n==n_copied-2*n_mod:
            self.image=egg_3
            self.rect.center=(625,160)
            self.updated_UR2=False
            self.updated_UR3=True
            egg_sound3.play()
            
        if self.updated_UR3==True and n==n_copied-3*n_mod:
            self.image=egg_4
            self.rect.center=(600,180)
            self.updated_UR3=False
            self.updated_UR4=True
            egg_sound4.play()
            
        if self.updated_UR4==True and n==n_copied-4*n_mod:
            self.image=egg_5
            self.rect.center=(575,195)
            self.updated_UR4=False
            self.updated_UR_phantom=True
            egg_sound5.play()
            
        if self.updated_UR_phantom==True and n==1:
            self.image=void
            self.rect.center=(WIDTH,0)
            self.updated_UR_phantom=False

        #down-right egg
        if first_pos==4:
            self.image=egg_1
            self.rect.center=(720,350)
            self.updated_DR1=True
            egg_sound1.play()
            
        if self.updated_DR1==True and n==n_copied-1*n_mod:
            self.image=egg_2
            self.rect.center=(670,335)
            self.updated_DR1=False
            self.updated_DR2=True
            egg_sound2.play()
            
        if self.updated_DR2==True and n==n_copied-2*n_mod:
            self.image=egg_3
            self.rect.center=(625,325)
            self.updated_DR2=False
            self.updated_DR3=True
            egg_sound3.play()
            
        if self.updated_DR3==True and n==n_copied-3*n_mod:
            self.image=egg_4
            self.rect.center=(580,315)
            self.updated_DR3=False
            self.updated_DR4=True
            egg_sound4.play()
            
        if self.updated_DR4==True and n==n_copied-4*n_mod:
            self.image=egg_5
            self.rect.center=(550,305)
            self.updated_DR4=False
            self.updated_DR_phantom=True
            egg_sound5.play()
            
        if self.updated_DR_phantom==True and n==1:
            self.image=void
            self.rect.center=(WIDTH,HEIGHT)
            self.updated_DR_phantom=False

        if end_game==True:
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
            
            



#GAME
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Wolf & Chicken cops')
clock=pygame.time.Clock()

music=pygame.mixer.music.load(generate_soundtrack)
pygame.mixer.music.set_volume(0.02)
pygame.mixer.music.play(-1)

beep=pygame.mixer.Sound('muza/cursor.wav')
beep.set_volume(0.008)
egg_sound1=pygame.mixer.Sound('muza/egg_sound1.wav')
egg_sound2=pygame.mixer.Sound('muza/egg_sound2.wav')
egg_sound3=pygame.mixer.Sound('muza/egg_sound3.wav')
egg_sound4=pygame.mixer.Sound('muza/egg_sound4.wav')
egg_sound5=pygame.mixer.Sound('muza/egg_sound5.wav')
egg_cracking=pygame.mixer.Sound('muza/egg_cracking.wav')
collect=pygame.mixer.Sound('muza/collect.wav')


all_sprites= pygame.sprite.Group()
eggs=pygame.sprite.Group()

wolf=Wolf()
phantomwolf=PhantomWolf()
all_sprites.add(wolf)
all_sprites.add(phantomwolf)

eggs.add(Eggs())

def game_over():

    global score
    
    running=True
    while running:
        screen.blit(gameover,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    running=False

        points(score,(255,0,0),(540,280))

        pygame.display.update()
                
def game_intro():
    
    global name
    global highscores_help
    global highscores_lines
    
    beep_play=0
    k=0
    
    
    intro = True
    while intro:
        screen.blit(menubackground,(0,0))
        screen.blit(game_title,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if k==0:
                    name=name[:-22]
                    k+=1
                if event.key==pygame.K_BACKSPACE:
                    if len(name)>10:
                        name=name[:-1]
                else:
                    if len(name)<29:
                        name+=event.unicode
        
        font = pygame.font.SysFont("comicsansms", 20)
        text=font.render(name, True, (255,0,0))
        screen.blit(text,(270,500))
                

        screen.blit(play_button,(195,160))
        #pygame.draw.ellipse(screen,(0,0,0),(200,170,400,60))
        screen.blit(highscores_button,(217,250))
        #pygame.draw.ellipse(screen,(0,0,0),(220,250,360,60))
        screen.blit(about_button,(245,330))
        #pygame.draw.ellipse(screen,(0,0,0),(240,330,320,60))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 200<mouse[0]<600 and 170<mouse[1]<230:
            pygame.draw.circle(screen,(0,0,0),(180,200),10)
            pygame.draw.circle(screen,(0,0,0),(630,200),10)
            if beep_play==0:
                beep.play()
                beep_play=1
            
            if click[0]==1:
                
                game_loop()
                i=0
                j=-1
                n=125
                n_copied=speed[i]
                n_mod=int(n_copied/5)
                    
                score=0
                lives=3
                first_pos=0
                
        elif 220<mouse[0]<580 and 250<mouse[1]<310:
            pygame.draw.circle(screen,(0,0,0),(200,280),10)
            pygame.draw.circle(screen,(0,0,0),(610,280),10)
            if beep_play==0:
                beep.play()
                beep_play=1
            if click[0]==1:
                game_highscores()
            
        elif 240<mouse[0]<560 and 330<mouse[1]<390:
            pygame.draw.circle(screen,(0,0,0),(225,360),10)
            pygame.draw.circle(screen,(0,0,0),(575,360),10)
            if beep_play==0:
                beep.play()
                beep_play=1
            if click[0]==1:
                game_about()
        else:
            beep_play=0

        highscores_help=sorted(highscores_help,key=lambda sc: sc[0],reverse=True)
        highscores_help=highscores_help[:10]
        highscores_text=open('highscores.txt','w+')
        
        for hh in highscores_help:
            new=str(hh[0])+'...'+hh[1]
            highscores_text.write(new)
        highscores_text.close()
        
        
        pygame.display.update()
                
    
def game_loop():
    
    global highscores_help
    global name
    global first_pos
    global i
    global j
    global n
    global speed
    global n_copied
    global n_mod
    global score
    global lives
    global end_game
    
    beep_play=0
   
    running=True
    while running:
        screen.blit(background,(0,0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                highscores_help.append([score,name[10:]+'\n'])
                i=0
                j=-1
                n=125
                score=0
                lives=3
                first_pos=0
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
            collect.play()
        if n==1 and not pygame.sprite.spritecollide(phantomwolf,eggs,False):
            lives-=1
            if lives!=2:
                egg_cracking.play()
        if lives==2 or lives==3:
            screen.blit(lives_3,(390,475))
        if lives==1:
            screen.blit(lives_2,(390,475))
        if lives==0:
            screen.blit(lives_1,(390,475))
        if lives==-1:
            end_game=True
            all_sprites.update()
            all_sprites.draw(screen)
            eggs.update()
            end_game=False
            highscores_help.append([score,name[10:]+'\n'])
            game_over()
            i=0
            j=-1
            n=125
            score=0
            lives=3
            first_pos=0
            
            running=False
            
        all_sprites.draw(screen)
        
        eggs.draw(screen)
        points(score,(0,0,0),(440,7))


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
            if beep_play==0:
                beep.play()
                beep_play=1
            if click[0]==1:
                about=False
        else:
            beep_play=0
                
        pygame.display.update()

def game_highscores():

    global highscores_help
    beep_play=0
    
    running= True
    while running:
        screen.blit(menubackground,(0,0))
        screen.blit(highscores_info,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        highscores_text=open('highscores.txt')
        highscores_display=highscores_text.readlines()
        #print(highscores_display)


        k=0
        font = pygame.font.SysFont("comicsansms", 20)
        for line in highscores_display:
            text=font.render(line.rstrip("\n"), True, (0,0,0))
            screen.blit(text,(285,120+k))
            k+=25
                
        #pygame.draw.ellipse(screen,(0,0,0),(260,400,290,60))
        screen.blit(back_button,(260,400))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 260<mouse[0]<550 and 400<mouse[1]<460:
            pygame.draw.circle(screen,(0,0,0),(245,430),8)
            pygame.draw.circle(screen,(0,0,0),(560,430),8)
            if beep_play==0:
                beep.play()
                beep_play=1
            if click[0]==1:
                highscores_text.close()
                running=False
        else:
            beep_play=0
                
        pygame.display.update()

    


game_intro()

pygame.quit()

