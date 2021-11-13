import pygame
pygame.init()

# Create a clock (for framerating)
clk = pygame.time.Clock()
 
# Create display
screen = pygame.display.set_mode([350,175])
background_image = pygame.image.load('image.png').convert_alpha()
 
# Generate crosshair
crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("blue"), (5,5), 5)

while True:
    
    pygame.event.pump()
     
    screen.fill([255, 255, 255])

    screen.blit(background_image, (0, 0)) 
    
    Keys=pygame.key.get_pressed()
    
    if Keys[pygame.K_a]: screen.blit(crosshair, (250, 112) )            

    if Keys[pygame.K_b]: screen.blit(crosshair, (295, 112) )

    if Keys[pygame.K_SPACE]: screen.blit(crosshair, (148, 112) )

    if Keys[pygame.K_RETURN]: screen.blit(crosshair, (193, 112) )

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0
    
    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0  

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(crosshair,((x*20)+64, (y*20)+96))
    
    pygame.display.flip()

    clk.tick(40)
