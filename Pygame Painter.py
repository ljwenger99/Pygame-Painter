# Simple pygame program
 
# Import and initialize the pygame library
import random
import pygame
pygame.init()
 
# Set up the drawing window
screenwidth = 1000
screenheight = 500

screen = pygame.display.set_mode([screenwidth, screenheight])
 
# Run until the user asks to quit
running = True

color = (0,0,0)

radius = 2

position = (0,500)

speed = (0,0)

a =random.randint(0,255)
b =random.randint(0,255)
c = 0

while running:
 
    # Did the user click the window close button?
    for event in pygame.event.get():
        #change color
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = a
            a = b
            b = c
            c = x
        #move
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed = (speed[0], speed[1]-1)
            elif event.key == pygame.K_a:
                speed = (speed[0]-1, speed[1])
            elif event.key == pygame.K_s:
                speed = (speed[0], speed[1]+1)
            elif event.key == pygame.K_d:
                speed = (speed[0]+1, speed[1])
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speed = (speed[0], speed[1]+1)
            elif event.key == pygame.K_a:
                speed = (speed[0]+1, speed[1])
            elif event.key == pygame.K_s:
                speed = (speed[0], speed[1]-1)
            elif event.key == pygame.K_d:
                speed = (speed[0]-1, speed[1])
        
        elif event.type == pygame.QUIT:
            running = False


    if a != 0:
        a = random.randint(1,255)
    if b != 0:
        b = random.randint(1,255)
    if c != 0:
        c = random.randint(1,255)
    color = (a,b,c)
    
    position = (position[0]+speed[0],position[1]+speed[1])
    if position[0]>screenwidth:
        position = (screenwidth, position[1])
    elif position[0]<0:
        position = (0, position[1])
    if position[1]>screenheight:
        position = (position[0], screenheight)
    elif position[1]<0:
        position = (position[0],0)

    #Uncomment to make dots random! 
    #position = (random.randint(0,screenwidth),random.randint(0,screenheight))

    #Change the value added/subtracted to position to increase/decrease square
    masterposition = (random.randint(position[0]-25, position[0]+25), random.randint(position[1]-25,position[1]+25))
    
    # Draw circles
    # (Try commenting one out for something interesting!)
    pygame.draw.circle(screen,(255,255,255), masterposition, radius+1)
    pygame.draw.circle(screen, color, masterposition, radius)
    
    # Flip the display
    pygame.display.flip()
 
# Done! Time to quit.
pygame.quit()
