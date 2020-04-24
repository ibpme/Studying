import pygame
import random

pygame.init()


screen = pygame.display.set_mode((800, 600)) # Sets the resolution of the screendows GUI
pygame.display.set_caption("SnakeGame") # Sets the title in the screendows Title Bar

runing = True

blue = (0, 0, 255)
red = (255, 0, 0)
black = (0,0,0)

x1=300
y1=300
x=[]
y=[]

x_change = 0
y_change = 0
x_food=random.randint(0,80)*10
y_food=random.randint(0,60)*10
clock = pygame.time.Clock()
food_available=False
body=1

while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                y_change = -10
                x_change = 0
            elif event.key == pygame.K_a:
                y_change = 0
                x_change = -10
            elif event.key == pygame.K_d:
                y_change = 0
                x_change = 10
            elif event.key == pygame.K_s:
                y_change = 10
                x_change = 0
    if x1<=800 and x1>=0:
        x1 += x_change
    elif x1<0:
        x1=800+x_change
    elif x1>800:
        x1=0+x_change
    if y1<=600 and y1>=0:
        y1 += y_change
    elif y1<0:
        y1=600+y_change
    elif y1>600:
        y1=0+y_change

    screen.fill(black)
    if x1==x_food and y1==y_food:
        food_available=False
        pygame.draw.rect(screen, black, [x_food, y_food, 10, 10])
        body+=1
    if len(x)>body-1 and len(y)>body-1:
        x.pop(body-1)
        y.pop(body-1)
    x.insert(0,x1)
    y.insert(0,y1)
    if food_available==False:
        x_food=random.randint(0,79)*10
        y_food=random.randint(0,59)*10
        food_available=True
    else:
        pygame.draw.rect(screen, red, [x_food, y_food, 10, 10])
    for i in range(body):
        pygame.draw.rect(screen, blue, (x[i] ,y[i], 10, 10))
    pygame.display.update()

    clock.tick(20)
pygame.quit()
quit()
