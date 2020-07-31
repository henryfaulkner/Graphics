
def create_file_from_vertices(coordinate_list):
    print("input a filename")
    filename = input()
    file = open(filename, 'w') #should create file w write access
    
    print("input list of vertices separated by a whitespace")
    vertices_str = input()
    vertices_list = vertices_str.split()

    for vertices in vertices_list:
        #linear search for both vertices and write x y
        #does not matter which order a vertex is found
        for lists in coordinate_list:
            if(lists[0] == vertices[0]): #first string == first char
                file.write(lists[1] + ' ') #x
                file.write(lists[2] + ' ') #y
                file.write(lists[3] + ' ') #z
            elif(lists[0] == vertices[1]): #first string == second char
                file.write(lists[1] + ' ') #x
                file.write(lists[2] + ' ') #y
                file.write(lists[3] + ' ') #z
        file.write('\n')

def main():
    print("Enter \'coordinate_name x y z\'") #name must be single char
    str = input()
    str_list = str.split()
    coordinate_list = [str_list]
    while(str != 'next'):
        str = input()
        if(str != 'next'):
            str_list = str.split()
            coordinate_list.append(str_list)
    print(coordinate_list)
    create_file_from_vertices(coordinate_list)

if __name__ == "__main__":
    main()
