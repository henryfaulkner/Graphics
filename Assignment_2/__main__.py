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
    #transform.OutputLines(externalFile)
    file_matrix = transform.InputLines(externalFile)
    print(file_matrix)
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
