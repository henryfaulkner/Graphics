import pygame
import random
import time

'''code is referenced from https://github.com/encukou/bresenham'''
def bresenham_alg(screen, x0, y0, x1, y1, R, G, B):
    dx=x1-x0
    dy=y1-y0

    if dx>0: #stores whether dx is positive or negative
        xsign=1
    else:
        xsign=-1

    if dy>0: #stores whether dx is positive or negative 
        ysign=1
    else:
        ysign=-1

    dx=abs(dx) 
    dy=abs(dy)

    if dx > dy:
        xx=xsign #increments/decrements the xpoint by ysign*xindex 
        xy=0
        yx=0
        yy=ysign #increments/decrements the ypoint by ysign*yindex
    else:
        xx=0
        xy=ysign #increments/decrements the ypoint by ysign*xindex
        yx=xsign #increments/decrements the xpoint by xsign*yindex
        yy=0

    if dx == 0 and dy == 0: #point 
        screen.set_at((x0,y0), (R,G,B)) 
    elif dx > dy: #horizontal and diagonal lines when dx > dy
        y=0
        E=2*dy-dx #calculates error in y-direction
        for i in range(dx+1):
            x_point=x0+i*xx+y*yx
            y_point=y0+i*xy+y*yy
            screen.set_at((x_point, y_point), (R,G,B))
            if E >= 0:
                y+=1
                E-=2*dx
            E+=2*dy
    else: #vertical and diagonal lines when dy > dx
        y=0
        E=2*dx-dy #calculates error in x-direction
        for i in range(dy+1):
            x_point=x0+i*xx+y*yx
            y_point=y0+i*xy+y*yy
            screen.set_at((x_point, y_point), (R,G,B))
            if E >= 0:
                y+=1
                E-=2*dy
            E+=2*dx

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
        R=random.randint(0,255)
        G=random.randint(0,255)
        B=random.randint(0,255)
        
        x0=random.randint(0,width)
        y0=random.randint(0,height)
        x1=random.randint(0,width)
        y1=random.randint(0,height)
        
        bresenham_alg(screen,int(x0),int(y0),int(x1),int(y1),R,G,B)

    print(str(time.time()-startTime) + " seconds")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #screen.blit(background, (0, 0)) 
        pygame.display.flip()
    
    
if __name__ == '__main__': main()
