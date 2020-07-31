import pygame
import math
from Transformations import transformations
from GUI import Window_1
from PyQt5.QtWidgets import QApplication
import sys

def main():
    height = 400
    width = 400

    screen = pygame.display.set_mode((width, height))
    transform = transformations()    

    print('Please type a external file to use')
    externalFile = input()
    
    print('Please define a viewport using the format: \'x0 y0 x1 y1\'')
    viewport_specs = input()
    viewport_specs_list = viewport_specs.split() #parses string by spaces, converts to list
    coor = list(map(int, viewport_specs_list)) #converts string list into int list
    transform.viewport_spec(screen, coor[0], coor[1], coor[2], coor[3])
    file_matrix = transform.InputLines(externalFile)
    transform.DisplayPixels(screen, file_matrix)
    
    #main loop
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
                file_matrix = transform.command_line(str, file_matrix)
                transform.DisplayPixels(screen, file_matrix)
        i += 1 #do-while loop
        pygame.display.update()
    

if __name__ == "__main__":
    '''app = QApplication(sys.argv)
    GUI = Window_1()
    app.exec_()'''
    main()
