import pygame
import sys
import random

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (300,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (300,random_pipe_pos - 50))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 200:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
def remove_pipes(pipes):
    for pipe in pipes:
        if pipe.centerx == -600:
            pipes.remove(pipe)
    return pipes

pipe_surface = pygame.image.load('Assets/mine_1.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400,600,800]

def menüü():
    pygame.init()    
    color = (255,255,255)   
    color_light = (170,170,170)  
    color_dark = (100,100,100)  
    width = screen.get_width()    
    height = screen.get_height()   
    smallfont = pygame.font.SysFont('Corbel',36)  
    text = smallfont.render('MÄNGI' , True , color)  

    while True:   
        for ev in pygame.event.get():  
            if ev.type == pygame.QUIT:  
                pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:    
                if width/2 -70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40:  
                    return   
        screen.fill((20,20,20))  
        mouse = pygame.mouse.get_pos()   
        if width/2 - 70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40:  
            pygame.draw.rect(screen,color_light,[width/2 - 70,height/2,140,40])  
          
        else:  
            pygame.draw.rect(screen,color_dark,[width/2 - 70,height/2,140,40])   
        screen.blit(text , (width/2 -70,height/2 + 5))  
        pygame.display.update() 
    
def põrand():
    screen.blit(floor_surface,(floor_x_pos,433))
    screen.blit(floor_surface,(floor_x_pos + 1000,433))
def miin():
    #screen.blit(takistus,(floor_x_pos,400))
    screen.blit(takistus,(floor_x_pos + 1000,375))


pygame.init()

pygame.display.set_caption("Hyppemenk")


screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()


while True:
    menüü()

    isjump = False
    cd = False

    bg_surface = pygame.image.load("Assets/Full-Background.png").convert()
    takistus = pygame.image.load("Assets/mine_1.png")
    floor_surface = pygame.image.load("Assets/Floor-Background.png").convert()
    floor_x_pos = 0
    miinpos = 0
    x = 150
    y = 410
    kass = pygame.image.load("Assets/kass.png")
    kass = pygame.transform.scale2x(kass)



    v = 10
    m = 1
    hüpe = pygame.mixer.Sound("Assets/hypp.wav")

    while True:
        kassi_hitbox = kass.get_rect(center = (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())
        keys = pygame.key.get_pressed()
        if cd == False:
            if isjump == False: 

                if keys[pygame.K_SPACE]: 
                    pygame.mixer.Sound.play(hüpe)
                    pygame.mixer.music.stop()
                    isjump = True
        pipe_list = move_pipes(pipe_list)
        pipe_list = remove_pipes(pipe_list)
        draw_pipes(pipe_list)
               
        if isjump :
        
            cd = True
 
            F =(1 / 2)*m*(v**2)

            y-= F 
 
            v = v-1

            if v<0: 
                m =-1 
            if v ==-11: 
                isjump = False
                v = 10
                m = 1
    
        if not keys[pygame.K_SPACE]:
            cd = False
    
        screen.blit(bg_surface, (0, 0))
   

        screen.blit(kass,kassi_hitbox)
        #põrand
        #if miin > 0:
        miinpos -= 10
        floor_x_pos -= 10
        miin()
        põrand()
        if floor_x_pos <= -1000:
            floor_x_pos = 0
 
        

        pygame.display.update()
        clock.tick(40)
    