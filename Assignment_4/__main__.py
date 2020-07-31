import pygame
import math 
import sys
from perspective_projection import perspective_projection

def main():
    height = 1000
    width = 1000

    screen = pygame.display.set_mode((width, height))
    p_p = perspective_projection()

    print("type an external file to use")
    externalfile = input()
    file_matrix = p_p.InputLines(externalfile)
    p_p.DisplayPixels(screen, file_matrix, 2.5, 50, 500, 500, 500, 500)

    i = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        
        if(i > 0):
            print('Please input a command')
            str = input()
            if(str == 'quit'):
                break
            else:
                file_matrix = p_p.command_line(str, file_matrix)
                p_p.DisplayPixels(screen, file_matrix, 2.5, 50, 500, 500, 500, 500)
        i += 1 #do-while loop
        pygame.display.update()

if __name__ == "__main__":
    main()
