import pygame
import random
bg = pygame.image.load('obrazki/Tlo.jpg')
#player
UL=pygame.image.load('obrazki/LG.png')
UR=pygame.image.load('obrazki/PG.png')
DL=pygame.image.load('obrazki/LD.png')
DR=pygame.image.load('obrazki/PD.png')

wolf_UL=pygame.transform.scale(UL,(290,290))
wolf_DL=pygame.transform.scale(DL,(290,290))
wolf_UR=pygame.transform.scale(UR,(275,275))
wolf_DR=pygame.transform.scale(DR,(275,275))

#eggs
UL_1=pygame.image.load('obrazki/UL_1.png')
UL_2=pygame.image.load('obrazki/UL_2.png')
UL_3=pygame.image.load('obrazki/UL_3.png')
UL_4=pygame.image.load('obrazki/UL_4.png')
UL_5=pygame.image.load('obrazki/UL_5.png')

UR_1=pygame.image.load('obrazki/UR_1.png')
UR_2=pygame.image.load('obrazki/UR_2.png')
UR_3=pygame.image.load('obrazki/UR_3.png')
UR_4=pygame.image.load('obrazki/UR_4.png')
UR_5=pygame.image.load('obrazki/UR_5.png')
    
egg_UL_1=pygame.transform.scale(UL_1,(60,60))
egg_UL_2=pygame.transform.scale(UL_2,(60,60))
egg_UL_3=pygame.transform.scale(UL_3,(60,60))
egg_UL_4=pygame.transform.scale(UL_4,(60,60))
egg_UL_5=pygame.transform.scale(UL_5,(60,60))

egg_UR_1=pygame.transform.scale(UR_1,(60,60))
egg_UR_2=pygame.transform.scale(UR_2,(60,60))
egg_UR_3=pygame.transform.scale(UR_3,(60,60))
egg_UR_4=pygame.transform.scale(UR_4,(60,60))
egg_UR_5=pygame.transform.scale(UR_5,(60,60))

posUL=(65,65)
posDL=1
posUR=(680,55)
posDR=1

counterUL=250
counterDL=250
counterUR=250
counterDR=250

class Egg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=void
        self.rect=self.image.get_rect()
        self.rect.center=(100,100)
    def update(self):
        if first_pos==1:
            self.image=egg_1
            self.rect.center=(100,100) 
        if first_pos==2:
            self.image=egg_1
            self.rect.center=(700,100)
        if first_pos==3:
            self.image=egg_1
            self.rect.center=(100,400)
        if first_pos==4:
            self.image=egg_1
            self.rect.center=(700,400)
    

#   GAME    
pygame.init()

screen=pygame.display.set_mode((800,574))
pygame.display.set_caption('wilk')
    
clock=pygame.time.Clock()

bg = pygame.image.load('obrazki/Tlo.jpg')
background=pygame.transform.scale(bg,(800,574))



all_sprites= pygame.sprite.Group()
egg=Egg()
all_sprites.add(egg)


def ruch(q,a,p,l):
    while q:
        screen.blit(wolf_UL,(240,143))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                q = False
                break
    while a:
        screen.blit(wolf_DL,(240,143))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                a = False
                break
    while p:
        screen.blit(wolf_UR,(300,160))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                p = False
                break
    while l:
        screen.blit(wolf_DR,(300,160))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                l = False
                break

#eggs
def eggs():
    first_position=random.choice([posUL,posDL,posUR,posDR])
    return first_position
        
    

running=True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #background
    screen.blit(background,(0,0))

    #update
    all_sprites.update()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_q]:
        q=True
        a=False
        p=False
        l=False
        print(q,a,p,l)
        ruch(q,a,p,l)
        #screen.blit(wolf_UL,(240,143))
        #pygame.display.update()            
    if keys[pygame.K_a]:
        q=False
        a=True
        p=False
        l=False
        ruch(q,a,p,l)
        #screen.blit(wolf_DL,(240,143))
        #pygame.display.update()
    if keys[pygame.K_p]:
        q=False
        a=False
        p=True
        l=False
        ruch(q,a,p,l)
    if keys[pygame.K_l]:
        q=False
        a=False
        p=False
        l=True
        ruch(q,a,p,l)
    

    #pygame.time.wait(1000)
    #if eggs()==posUL:
        #screen.blit(egg_UL_1,(65,65))
        #screen.blit(egg_UL_2,(108,98))
        #screen.blit(egg_UL_3,(145,135))
        #screen.blit(egg_UL_4,(185,155))
        #screen.blit(egg_UL_5,(230,190))
        #pygame.display.update()
        
    #if eggs()==posUR:
        #screen.blit(egg_UR_1,(680,55))
        #screen.blit(egg_UR_2,(630,98))
        #screen.blit(egg_UR_3,(600,130))
        #screen.blit(egg_UR_4,(560,150))
        #screen.blit(egg_UR_5,(520,170))
        #pygame.display.update()

    #keys



    #defegs


    #screen.blit(egg_UL_1,(65,65))
    #screen.blit(egg_UL_2,(108,98))
    #screen.blit(egg_UL_3,(145,135))
    #screen.blit(egg_UL_4,(185,155))
    #screen.blit(egg_UL_5,(230,190))

    all_sprites.draw(screen)
    
    pygame.display.update()



    
pygame.quit()










