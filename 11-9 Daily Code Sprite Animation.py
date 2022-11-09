import pygame
pygame.init()
pygame.display.set_caption("sprite sheet") #sets the window title
screen = pygame.display.set_mode((800, 800)) #creates game screen
screen.fill((0,0,0)) #sets bg color to black
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run the game loop

Link = pygame.image.load('link.png') #load your spritesheet
Link.set_colorkey((255,0,255)) #this makes bright pink (255,0,55) transparent (sort of)

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed


#animation variables variables
frameWidth = 64
frameHeight = 96
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

while not gameover:#OMG GAME LUUP!!#####################################################################################
    clock.tick(60) #FPS
    
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
             gameover = True
            
    if event.type ==pygame.KEYDOWN: #keyboard input
        if event.key == pygame.K_LEFT:
            keys[RIGHT] = True
        elif event.key == pygame.K_RIGHT:
            keys[LEFT] = True
        elif event.key == pygame.K_UP:
            keys[UP] = True
        elif event.key == pygame.K_DOWN:
            keys[DOWN] = True
            
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            keys[RIGHT] = False
        elif event.key == pygame.K_RIGHT:
            keys[LEFT] = False
        elif event.key == pygame.K_UP:
            keys[UP] = False
        elif event.key == pygame.K_DOWN:
            keys[DOWN] = False
        
#Physics section --------------------------------------------
    #left movement
    if keys[RIGHT] == True:
        vx=-3
         
    #right movement
    elif keys[LEFT] == True:
        vx = 3
    else:
        vx = 0
        
    #up movement
    if keys[UP] == True:
        vy = -3
        
    #down movement
    elif keys[DOWN] == True:
        vy = 3
    
    #turn off velocity
    else:
        vy = 0
            
    #update position based on velocity
    xpos+=vx #update player xpos
    ypos+=vy #update player ypos
        

#Animation section --------------------------------------------

    #only animate when in motion
    if vx < 0: #left animation
        RowNum = 0
        #ticker is a spedometer. we dont want link animating as fast as the processor can process! update animation frame each time ticker goes over
        ticker+=1
        if ticker%8==0: #only changes frames every 10 ticks
            frameNum+=1
            #if we are over the number of frames in our spritem reset to 0.
        if frameNum>7:
            frameNum = 0
    elif vx > 0: #right animation
        RowNum = 1
        #ticker is a spedometer. we dont want link animating as fast as the processor can process! update animation frame each time ticker goes over
        ticker+=1
        if ticker%8==0: #only changes frames every 10 ticks
            frameNum+=1
            #if we are over the number of frames in our spritem reset to 0.
        if frameNum>7:
            frameNum = 0
    elif vy < 0: #up animation
        RowNum = 2
        #ticker is a spedometer. we dont want link animating as fast as the processor can process! update animation frame each time ticker goes over
        ticker+=1
        if ticker%8==0: #only changes frames every 10 ticks
            frameNum+=1
            #if we are over the number of frames in our spritem reset to 0.
        if frameNum>7:
            frameNum = 0
    elif vy > 0: #down animation
        RowNum = 3
        #ticker is a spedometer. we dont want link animating as fast as the processor can process! update animation frame each time ticker goes over
        ticker+=1
        if ticker%8==0: #only changes frames every 10 ticks
            frameNum+=1
            #if we are over the number of frames in our spritem reset to 0.
        if frameNum>7:
            frameNum = 0
            
#Render section --------------------------------------------
#once we've figured out what frame we are on and where we are, time to render.
            
    screen.fill((0,0,0))#wipe the screen every time it refreshes so it doesnt "smear"
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    pygame.display.flip() #this actually puts the pixel on the screen
            
#End Game Loop#OMG GAME END LUUP!!##################################################################################### --------------------------------------------
pygame.quit()