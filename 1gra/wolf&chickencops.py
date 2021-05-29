import pygame
import random

WIDTH=800
HEIGHT=574
FPS=50

#IMAGES
bg = pygame.image.load('obrazki/Tlo.jpg')
background=pygame.transform.scale(bg,(WIDTH,HEIGHT))
void=pygame.image.load('obrazki/nic.png')
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

#FUNCTIONS
n=250
m=250

#CLASSES
class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=wolf_UL
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/2,HEIGHT/2)
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.image=wolf_UL
            self.rect.center=(WIDTH/2,HEIGHT/2)
        if keys[pygame.K_a]:
            self.image=wolf_DL
            self.rect.center=(WIDTH/2,HEIGHT/2)
        if keys[pygame.K_p]:
            self.image=wolf_UR
            self.rect.center=(450,300)
        if keys[pygame.K_l]:
            self.image=wolf_DR
            self.rect.center=(450,300)
            
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

        self.updated_DL1=False
        self.updated_DL2=False
        self.updated_DL3=False
        self.updated_DL4=False

        self.updated_UR1=False
        self.updated_UR2=False
        self.updated_UR3=False
        self.updated_UR4=False

        self.updated_DR1=False
        self.updated_DR2=False
        self.updated_DR3=False
        self.updated_DR4=False
        
    def update(self):
        #upper-left egg
        if first_pos==1:
            self.image=egg_1
            self.rect.center=(100,100)
            self.updated_UL1=True

        if self.updated_UL1==True and m==200:
            self.image=egg_2
            self.rect.center=(150,125)
            self.updated_UL1=False
            self.updated_UL2=True
            
        if self.updated_UL2==True and m==150:
            self.image=egg_3
            self.rect.center=(190,170)
            self.updated_UL2=False
            self.updated_UL3=True
            
        if self.updated_UL3==True and m==100:
            self.image=egg_4
            self.rect.center=(230,200)
            self.updated_UL3=False
            self.updated_UL4=True
            
        if self.updated_UL4==True and m==50:
            self.image=egg_5
            self.rect.center=(275,220)
            self.updated_UL4=False
            
        #down-left egg
        if first_pos==2:
            self.image=egg_1
            self.rect.center=(75,325)
            self.updated_DL1=True
            
        if self.updated_DL1==True and m==200:
            self.image=egg_2
            self.rect.center=(140,325)
            self.updated_DL1=False
            self.updated_DL2=True
            
        if self.updated_DL2==True and m==150:
            self.image=egg_3
            self.rect.center=(175,325)
            self.updated_DL2=False
            self.updated_DL3=True
            
        if self.updated_DL3==True and m==100:
            self.image=egg_4
            self.rect.center=(215,315)
            self.updated_DL3=False
            self.updated_DL4=True
            
        if self.updated_DL4==True and m==50:
            self.image=egg_5
            self.rect.center=(260,320)
            self.updated_DL4=False
            
        #upper-right egg
        if first_pos==3:
            self.image=egg_2
            self.rect.center=(700,100)
            self.updated_UR1=True

        if self.updated_UR1==True and m==200:
            self.image=egg_1
            self.rect.center=(675,125)
            self.updated_UR1=False
            self.updated_UR2=True
            
        if self.updated_UR2==True and m==150:
            self.image=egg_3
            self.rect.center=(625,160)
            self.updated_UR2=False
            self.updated_UR3=True
            
        if self.updated_UR3==True and m==100:
            self.image=egg_4
            self.rect.center=(600,180)
            self.updated_UR3=False
            self.updated_UR4=True
            
        if self.updated_UR4==True and m==50:
            self.image=egg_5
            self.rect.center=(575,195)
            self.updated_UR4=False

        #down-right egg
        if first_pos==4:
            self.image=egg_1
            self.rect.center=(720,350)
            self.updated_DR1=True
            
        if self.updated_DR1==True and m==200:
            self.image=egg_2
            self.rect.center=(670,335)
            self.updated_DR1=False
            self.updated_DR2=True
            
        if self.updated_DR2==True and m==150:
            self.image=egg_3
            self.rect.center=(625,325)
            self.updated_DR2=False
            self.updated_DR3=True
            
        if self.updated_DR3==True and m==100:
            self.image=egg_4
            self.rect.center=(580,315)
            self.updated_DR3=False
            self.updated_DR4=True
            
        if self.updated_DR4==True and m==50:
            self.image=egg_5
            self.rect.center=(550,305)
            self.updated_DR4=False

        #empty
        if first_pos==5:
            self.image=void




#GAME
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Wolf & Chicken cops')
clock=pygame.time.Clock()

all_sprites= pygame.sprite.Group()
eggs=pygame.sprite.Group()

wolf=Wolf()
all_sprites.add(wolf)


eggs.add(Egg_pos1())

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
        n=250
        first_pos=random.choice([1,2,3,4])
        print(first_pos)
        
    #timer2
    if m>1:
        m-=1
    else:
        m=250

        
    all_sprites.update()
    eggs.update()
    

    all_sprites.draw(screen)
    eggs.draw(screen)


    pygame.display.update()





pygame.quit()


















