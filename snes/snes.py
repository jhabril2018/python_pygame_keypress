import  pygame
pygame.init()
 
# Create a clock (for framerating)
clk = pygame.time.Clock()

# Create display
size = width, height = 389, 187
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('cnes1.png').convert()
frameRect = pygame.Rect((0, 0), (width, height))
 
# Generate crosshair
crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("black"), (5,5), 5, 0)

crosshairb = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb,pygame.Color("red"), (5,5), 5, 0)
     
while True:
    # Pump and check the events queue
    pygame.event.pump()

    screen.blit(background_image, (0, 0))
    
    Keys=pygame.key.get_pressed()
    
    if Keys[pygame.K_x]: screen.blit(crosshair, (298, 70) )

    if Keys[pygame.K_a]: screen.blit(crosshair, (335, 98) )  

    if Keys[pygame.K_b]: screen.blit(crosshair, (298, 127) )  

    if Keys[pygame.K_y]: screen.blit(crosshair, (260, 98) ) 

    if Keys[pygame.K_r]: screen.blit(crosshair, (75, 11) )

    if Keys[pygame.K_l]: screen.blit(crosshair, (295, 11) )

    if Keys[pygame.K_SPACE]: screen.blit(crosshair, (154, 108) )

    if Keys[pygame.K_RETURN]: screen.blit(crosshair, (195, 110) )

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0
    
    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0  

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
 
    screen.blit(crosshairb,((x*20)+80-5,(y*20)+105-5))
    
    pygame.display.flip()
    
    clk.tick(40)
