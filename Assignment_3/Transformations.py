import pygame
import math
#from GUI import Window_1
#from PyQt5.QtWidgets import QApplication
import sys

class transformations:
    '''draws viewport. (Vx0, Vy0) is bottom-left coordinate.
    (Vx1, Vy1) is top-right coordinate'''
    def viewport_spec(self, screen, Vx0, Vy0, Vx1, Vy1):
        self.viewport_specs = [Vx0, Vy0, Vx1, Vy1] #class's viewport
        self.bresenham_alg(screen, Vx0, Vy0, Vx1, Vy0, 0, 0, 255) # bottom line
        self.bresenham_alg(screen, Vx0, Vy0, Vx0, Vy1, 0, 0, 255) # left line
        self.bresenham_alg(screen, Vx0, Vy1, Vx1, Vy1, 0, 0, 255) # top line
        self.bresenham_alg(screen, Vx1, Vy0, Vx1, Vy1, 0, 0, 255) # right line
        
    '''Checks if a pixels x & y coordinates are within viewport.
    This may be inefficient means to calculate within viewport
    because we individually check points within the main drawing loop.
    We also assume Vx0<Vx1 & Vy0<Vy1 '''
    def check_in_viewport(self, x, y, Vx0, Vy0, Vx1, Vy1):
        if(x>=Vx0 and x<=Vx1 and y>=Vy0 and y<=Vy1):
            return True
        return False

    '''Create own function by final'''
    def three_by_three_multi(self, m1, m2):
        result = [[0,0,0]]
        
    #iterate through rows of m1
        for i in range(len(m1)):
        #iterate through columns of m2
            for j in range(len(m2[0])):
            #iterate through rows of m2
                for k in range(len(m2)):
                    result[i][j] += m1[i][k]*m2[k][j]

        return result

    def print_matrix_coordinates(self, matrix):
        x=matrix[0][0]+matrix[1][0]+matrix[2][0]
        y=matrix[0][1]+matrix[1][1]+matrix[2][1]
        print("x: " + str(x) + "; y: " + str(y)) 

    '''assumes that datalines is an external input file (string)'''
    def InputLines(self, externalFile):
        externalFile = open(externalFile, 'r')
        original_lines = externalFile.readlines()
        file_matrix = []
        count = 0
        for lines in original_lines:
            line = lines.strip()
            coordinates = line.split()
            coordinates = list(map(float, coordinates)) #convert string list to float list
            file_matrix.append(coordinates)
    
        externalFile.close()
        #print(file_matrix)
        return file_matrix

    '''code is referenced from https://github.com/encukou/bresenham'''
    '''DisplayPixels'''
    def bresenham_alg(self, screen, x0, y0, x1, y1, R, G, B):
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2*dy - dx
        y = 0

        for x in range(dx + 1):
            x_point=x0+x*xx+y*yx
            y_point=y0+x*xy+y*yy
            #here is where we check if the point is within the viewport
            if(self.check_in_viewport(x_point, y_point, self.viewport_specs[0], self.viewport_specs[1], self.viewport_specs[2], self.viewport_specs[3])):
                screen.set_at((x_point, y_point), (R,G,B))
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy
        

    def ApplyTransformation(self, matrix, file_matrix):
        i = 0
        for lines in file_matrix:
            list0 = [[file_matrix[i][0],file_matrix[i][1],1]]
            list1 = [[file_matrix[i][2],file_matrix[i][3],1]]
            m0 = self.three_by_three_multi(list0, matrix)
            #print(m0)
            file_matrix[i][0] = m0[0][0]
            file_matrix[i][1] = m0[0][1]
            m1 = self.three_by_three_multi(list1, matrix)
            file_matrix[i][2] = m1[0][0]
            file_matrix[i][3] = m1[0][1]
            #print(m1)
            i += 1

        print(file_matrix)
        return file_matrix

    def DisplayPixels(self, screen, file_matrix):
        for lines in file_matrix:
            coor = list(map(int, lines)) #converts string list into int list
            self.bresenham_alg(screen, coor[0], coor[1], coor[2], coor[3], 255, 255, 255)

    def OutputLines(self, newfile, file_matrix):
        new_file = open(newfile, 'w')
        print(file_matrix)
        for line in file_matrix:
            for coor in line:
                new_file.write(str(coor))
                new_file.write(' ')
            new_file.write('\n')
        
        new_file.close()
        return file_matrix
    
    '''returns matrix for transformation'''
    def BasicTranslation(self, datalines, Tx, Ty):
        matrix = [[1,0,0], [0,1,0], [Tx,Ty,1]]
        return self.ApplyTransformation(matrix, datalines)

    def BasicScale(self, datalines, Sx, Sy):
        matrix = [[Sx,0,0], [0,Sy,0], [0,0,1]]
        return self.ApplyTransformation(matrix, datalines)

    def BasicRotation(self, datalines, angle):
        radian = math.radians(angle) #converts angle from degrees to radians
        
        matrix = [[math.cos(radian), -math.sin(radian), 0],
                  [math.sin(radian), math.cos(radian), 0],
                  [0, 0, 1]]
        return self.ApplyTransformation(matrix, datalines)

    def Scale(self, file_matrix, Sx, Sy, Cx, Cy):
        step1 = [[1,0,0], [0,1,0], [-Cx,-Cy,1]]
        step2 = [[Sx,0,0], [0,Sy,0], [0,0,1]]
        step3 = [[1,0,0], [0,1,0], [Cx,Cy,1]]
        file_matrix = self.ApplyTransformation(step1, file_matrix)
        file_matrix = self.ApplyTransformation(step2, file_matrix)
        return self.ApplyTransformation(step3, file_matrix)

    def Rotation(self, file_matrix, angle, Cx, Cy):
        radian = math.radians(angle)
        step1 = [[1,0,0], [0,1,0], [-Cx,-Cy,1]]
        step2 = [[math.cos(radian), -math.sin(radian), 0],
                 [math.sin(radian), math.cos(radian), 0],
                 [0, 0, 1]]
        step3 = [[1,0,0], [0,1,0], [Cx,Cy,1]]
        file_matrix = self.ApplyTransformation(step1, file_matrix)
        file_matrix = self.ApplyTransformation(step2, file_matrix)
        return self.ApplyTransformation(step3, file_matrix)
    
    '''formatted  \'[transformation] [coordinates] [center coordinates]\''''
    def command_line(self, str, file_matrix):
        str_list = str.split()
        if(str_list[0] == 'BasicTranslation'):
            return self.BasicTranslation(file_matrix, int(str_list[1]), int(str_list[2])) #Tx, Ty
        elif(str_list[0] == 'BasicScale'):
            return self.BasicScale(file_matrix, float(str_list[1]), float(str_list[2])) #Sx, Sy
        elif(str_list[0] == 'BasicRotation'):
            return self.BasicRotation(file_matrix, int(str_list[1])) #angle
        elif(str_list[0] == 'Scale'):
            return self.Scale(file_matrix, float(str_list[1]), float(str_list[2]), float(str_list[3]), float(str_list[4])) #Sx, Sy, Cx, Cy
        elif(str_list[0] == 'Rotation'):
            return self.Rotation(file_matrix, int(str_list[1]), int(str_list[2]), int(str_list[3])) #angle, Cx, Cy
        elif(str_list[0] == 'OutputFile'):
            print('Please input a filename.')
            str = input()
            return self.OutputLines(str, file_matrix)
            
