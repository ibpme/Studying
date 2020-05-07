import pygame
import random

pygame.init()


screen = pygame.display.set_mode((800, 600)) # Sets the resolution of the screendows GUI
pygame.display.set_caption("SnakeGame") # Sets the title in the screendows Title Bar

runing = True

blue = (0, 0, 255)
red = (255, 0, 0)
black = (0,0,0)
speed=15
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
tail=0

while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and y_change != 10:
                y_change = -10
                x_change = 0
            elif event.key == pygame.K_a and x_change != 10:
                y_change = 0
                x_change = -10
            elif event.key == pygame.K_d and x_change != -10:
                y_change = 0
                x_change = 10
            elif event.key == pygame.K_s and y_change != -10:
                y_change = 10
                x_change = 0
    if x1<800 and x1>=0:
        x1 += x_change
    elif x1<0:
        x1=800+x_change
    elif x1>=800:
        x1=0+x_change
    if y1<600 and y1>=0:
        y1 += y_change
    elif y1<0:
        y1=600+y_change
    elif y1>=600:
        y1=0+y_change
    for i in range (1,len(x)):
        if x1==x[i] and y1==y[i]:
            tail=0
            x=[]
            y=[]
            break
    screen.fill(black)
    if x1==x_food and y1==y_food:
        food_available=False
        pygame.draw.rect(screen, black, [x_food, y_food, 10, 10])
        tail+=1
        speed+1
    if len(x)>tail and len(y)>tail:
        x.pop(tail)
        y.pop(tail)
    x.insert(0,x1)
    y.insert(0,y1)
    if food_available==False:
        x_food=random.randint(0,79)*10
        y_food=random.randint(0,59)*10
        food_available=True
    else:
        pygame.draw.rect(screen, red, [x_food, y_food, 10, 10])
    for i in range(len(x)):
        pygame.draw.rect(screen, blue, (x[i] ,y[i], 10, 10))
    pygame.display.update()

    clock.tick(speed)
pygame.quit()
quit()
