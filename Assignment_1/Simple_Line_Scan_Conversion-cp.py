import pygame
import math
import random
import time

def basic_alg(screen, x0, y0, x1, y1, R, G, B):
    if x1>x0:
        dx=x1-x0
        if y1>y0:
            dy=y1-y0
            if dx>dy:
                for i in range(dx):
                    x=x0+i
                    y=(dy/dx)*i+y0
                    y=math.trunc(y)
                    screen.set_at((x,y), (R,G,B))
            elif dx==dy:
                for i in range(dx):
                    x=x0+i
                    y=y0+i
                    screen.set_at((x,y), (R,G,B))
            else:
                for i in range(dy):
                    x=(dx/dy)*i+x0
                    y=y0+i
                    x=math.trunc(x)
                    screen.set_at((x,y), (R,G,B))
        elif y0>y1:
            dy=y1-y0
            m=dy/dx
            if dx>dy:
                for i in range(dx):
                    x=x0+i
                    y=m*i+y0
                    y=math.trunc(y)
                    screen.set_at((x,y), (R,G,B))
            elif dy>dx:
                for i in range(abs(dy)):
                    y=y0-i
                    x=abs((1/m))*i+x0
                    x=math.trunc(x)
                    screen.set_at((x,y), (R,G,B))
            else:
                for i in range(dx):
                    x=x0+i
                    y=y0-i
                    screen.set_at((x,y), (R,G,B))
        else:
            for i in range(dx): #horizontal line
                x=x0+i
                y=y0
                screen.set_at((x,y), (R,G,B))
    elif x1<x0:
        dx=x1-x0
        if y1>y0:
            dy=y1-y0
            m=dy/dx
            if abs(dy)>abs(dx):
                for i in range(dy):
                    x=(-1/m)*i+x1
                    y=y1-1
                    x=math.trunc(x)
                    screen.set_at((x,y), (R,G,B))
            elif abs(dx)>abs(dy):
                for i in range(dx):
                    x=x1+i
                    y=m*i+y1
                    y=math.trunc(y)
                    screen.set_at((x,y), (R,G,B))
            else:
                for i in range(dy):
                    x=x0-i
                    y=y0+i
                    screen.set_at((x,y), (R,G,B))
        elif y0>y1:
            dy=y1-y0
            m=dy/dx
            if abs(dy)>abs(dx):
                for i in range(abs(dx)):
                    x=x1+i
                    y=m*i+y1
                    y=math.trunc(y)
                    screen.set_at((x,y), (R,G,B))
            elif dx>dy:
                for i in range(abs(dx)):
                    x=m*i+x1
                    y=y1+i
                    x=math.trunc(x)
                    screen.set_at((x,y), (R,G,B))
            else:
                for i in range(abs(dy)):
                    x=x1+i
                    y=y1+i
                    screen.set_at((x,y), (R,G,B))
        else:
            for i in range(x0):
                x=x1+i
                y=y0
                screen.set_at((x,y), (R,G,B))
    elif x1==x0:
        if y1>y0:
            dy=y1-y0
            for i in range(abs(dy)):
                x=x0
                y=y0+i
                screen.set_at((x,y), (R,G,B))
        elif y0>y1:
            dy=y1-y0
            for i in range(abs(dy)):
                x=x0
                y=y1+i
                screen.set_at((x,y), (R,G,B))
    else: #point
        x=x0
        y=y0
        screen.set_at((x,y), (R,G,B))
    
def main():
    height = 400
    width = 400
    
    screen = pygame.display.set_mode((width, height))
    print("Enter the number of lines you'd like to generate.")
    n = input()
    
    startTime = time.time()

    '''print("x0: ")
    x0=input()
    print("x1: ")
    x1=input()
    print("y0: ")
    y0=input()
    print("y1: ")
    y1=input()
    bresenham_alg(screen, int(x0),int(y0),int(x1),int(y1),255,255,255)'''

    for i in range(int(n)):
        x0 = random.randint(0,width)
        y0 = random.randint(0,height)
        x1 = random.randint(0,width)
        y1 = random.randint(0,height)
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        basic_alg(screen, int(x0),int(y0),int(x1),int(y1),R,G,B)

    print(str(time.time()-startTime) + " seconds")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #screen.blit(background, (0, 0))
        pygame.display.flip()
    

if __name__ == '__main__': main()

