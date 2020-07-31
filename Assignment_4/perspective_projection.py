import pygame
import math

class perspective_projection:

    '''Applys matrix multiplication to 1x4 X 4x4 matrices'''
    def matrix_multi(self, m1, m2):
        result = [[0,0,0,0]]

        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    result[i][j] += m1[i][k]*m2[k][j]

        return result
            
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
            screen.set_at((x_point, y_point), (R,G,B))
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy

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
        print(file_matrix)
        return file_matrix
    
    '''creates new file based on current file_matrix contents'''
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

    '''applies perspective projection to 3D matrix -> becomes 2D matrix'''
    def transform(self, D, S, Vsx, Vsy, Vcx, Vcy, file_matrix):
        new_matrix = []
        '''this is gonna do excessive computation
        because it is gonna compute each point multiple 
        times'''
        for line in file_matrix:
            x0 = ((D*line[0])/(S*line[2]))*Vsx+Vcx
            y0 = ((D*line[1])/(S*line[2]))*Vsy+Vcy
            x1 = ((D*line[3])/(S*line[5]))*Vsx+Vcx
            y1 = ((D*line[4])/(S*line[5]))*Vsy+Vcy
            new_matrix.append([x0, y0, x1, y1])

        return new_matrix

    '''each time we display a new shape, convert 3D matrix to 2D matrix'''
    def DisplayPixels(self, screen, file_matrix, D, S, Vsx, Vsy, Vcx, Vcy):
        file_matrix = self.transform(D, S, Vsx, Vsy, Vcx, Vcy, file_matrix)
        for lines in file_matrix:
            coor = list(map(int, lines)) #converts string list into int list
            self.bresenham_alg(screen, coor[0], coor[1], coor[2], coor[3], 255, 255, 255)

    '''applies transformation matrix to 2D file_matrix'''
    def ApplyTransformation(self, matrix, file_matrix):
        i = 0
        for lines in file_matrix:
            list0 = [[file_matrix[i][0],file_matrix[i][1],file_matrix[i][2],1]]
            list1 = [[file_matrix[i][3],file_matrix[i][4],file_matrix[i][5],1]]
            m0 = self.matrix_multi(list0, matrix)
            file_matrix[i][0] = m0[0][0]
            file_matrix[i][1] = m0[0][1]
            file_matrix[i][2] = m0[0][2]
            m1 = self.matrix_multi(list1, matrix)
            file_matrix[i][3] = m1[0][0]
            file_matrix[i][4] = m1[0][1]
            file_matrix[i][5] = m1[0][2]
            i += 1

        print(file_matrix)
        return file_matrix

    '''Returns translation matrix'''
    def Translation(self, file_matrix, Tx, Ty, Tz):
        matrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[Tx,Ty,Tz,1]]
        return self.ApplyTransformation(matrix, file_matrix)

    '''Returns basic scale matrix'''
    def Scale(self, file_matrix, Sx, Sy, Sz):
        matrix = [[Sx,0,0,0],[0,Sy,0,0],[0,0,Sz,0],[0,0,0,1]]
        return self.ApplyTransformation(matrix, file_matrix)
    
    '''Returns basic rotation about z-axis matrix'''
    def Rotation_Z(self, file_matrix, angle):
        radian = math.radians(angle)

        matrix = [[math.cos(radian),math.sin(radian),0,0],[-math.sin(radian),math.cos(radian),0,0],[0,0,1,0],[0,0,0,1]]
        return self.ApplyTransformation(matrix, file_matrix)

    '''Returns basic rotation about y-axis matrix'''
    def Rotation_Y(self, file_matrix, angle):
        radian = math.radians(angle)
        
        matrix = [[math.cos(radian),0,-math.sin(radian),0],[0,1,0,0],[math.sin(radian),0,math.cos(radian),0],[0,0,0,1]]
        return self.ApplyTransformation(matrix, file_matrix)

    '''Returns basic rotation about x-axis matrix'''
    def Rotation_X(self, file_matrix, angle):
        radian = math.radians(angle)
        
        matrix = [[1,0,0,0], [0,math.cos(radian),math.sin(radian),0], [0,-math.sin(radian),math.cos(radian),0], [0,0,0,1]]
        return self.ApplyTransformation(matrix, file_matrix)

    '''Creates command line interface'''
    def command_line(self, str, file_matrix):
        str_list = str.split()
        if(str_list[0] == "Translation"):
            return self.Translation(file_matrix, int(str_list[1]), int(str_list[2]), int(str_list[3]))
        elif(str_list[0] == "Scale"):
            return self.Scale(file_matrix, int(str_list[1]), int(str_list[2]), int(str_list[3]))
        elif(str_list[0] == "Rotation_Z"):
            return self.Rotation_Z(file_matrix, int(str_list[1]))
        elif(str_list[0] == "Rotation_Y"):
            return self.Rotation_Y(file_matrix,int(str_list[1]))
        elif(str_list[0] == "Rotation_X"):
            return self.Rotation_X(file_matrix,int(str_list[1]))
        elif(str_list[0] == "OutputLines"):
            print("enter a filename")
            file = input()
            self.OutputLines(file, file_matrix)
