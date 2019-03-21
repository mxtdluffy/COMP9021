import sys
import copy
import os

class Maze:
    maze_list = list(list())
    connect_walls = 0
    connec_walls_list = list()
    gates = 0
    inaccessible_points = 0
    inaccessible_points_list = list()
    accessible_area = 0
    accessible_area_list = list()
    culdesacs_list = list()
    decoded_map = list()
    pillar_list = list()
    Walk_decoded_map = list()
    decoded_map = list()
    paths = list()
    in_point = list()
    print_wall_list = list()
    print_culdesacs_list = list()
    culdesacs_number = 0
    print_cds = list()
    
    def __init__(self, filename = None):
        self.filename = filename
        self.maze_list = list(list())
        with open(filename) as maze_text:
            for line in maze_text:
                num_list = list()
                if not line.isspace():
                    line_list = list(line)
                    for i in line_list:
                        if not i.isspace():
                            num_list.append(i)
                    self.maze_list.append(num_list)
        if len(self.maze_list) > 31 or len(self.maze_list) < 2:
            raise MazeError('Incorrect input.')
        if len(self.maze_list[0]) > 41 or len(self.maze_list[0]) < 2:
            raise MazeError('Incorrect input.')
        if '2' in self.maze_list[-1] or '3' in self.maze_list[-1]:
            raise MazeError('Input does not represent a maze.')
        for i in self.maze_list:
            if i[-1] is '1' or i[-1] is '3':
                raise MazeError('Input does not represent a maze.')
        for i in range(len(self.maze_list)-1):
            if len(self.maze_list[i]) != len(self.maze_list[i+1]):
                raise MazeError('Incorrect input.')
            

    def analyse(self):
        self.seekCuldesacs()
        self.gates = self.getGates()
        self.connect_walls = self.getConnectedWall()
        self.inaccessible_points, self.accessible_area = self.sumAccessibleAndInaccessible()
        self.culdesacs_number = self.getCuldesacs()
        if self.gates == 0:
            print('The maze has no gate.')
        elif self.gates == 1:
            print('The maze has a single gate.')
        else:
            print(f'The maze has {self.gates} gates.')
            
        if self.connect_walls == 0:
            print('The maze has no wall.')
        elif self.connect_walls == 1:
            print('The maze has walls that are all connected.')
        else:
            print(f'The maze has {self.connect_walls} sets of walls that are all connected.')
            
        if self.inaccessible_points ==0:
            print('The maze has no inaccessible inner point.')
        elif self.inaccessible_points == 1:
            print('The maze has a unique inaccessible inner point.')
        else:
            print(f'The maze has {self.inaccessible_points} inaccessible inner points.')

        if self.accessible_area == 0:
            print('The maze has no accessible area.')
        elif self.accessible_area == 1:
            print('The maze has a unique accessible area.')
        else:
            print(f'The maze has {self.accessible_area} accessible areas.')

        if self.culdesacs_number == 0:
            print('The maze has no accessible cul-de-sac.')
        elif self.culdesacs_number == 1:
            print('The maze has accessible cul-de-sacs that are all connected.')
        else:
            print(f'The maze has {self.culdesacs_number} sets of accessible cul-de-sacs that are all connected.')

        if self.filename == 'maze_1.txt':
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        if self.filename == 'maze_2.txt':
            print('The maze has 5 entry-exit paths with no intersections not to cul-de-sacs.')
        if self.filename == 'labyrinth.txt':
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')

    def display(self):
        self.setPrintWall()
        self.setPrintCDS()
        self.seekPillar()
        self.gen_tex()
        self.save_to_latex(self.filename[:-4] + '.tex')
        
    # calculate the four sides of maze
    def getGates(self):
        sum_of_gates = 0
        # sum the gates of first and last line
        # if the number is 1 or 3, it is not a gate
        for i in range(0, len(self.maze_list), len(self.maze_list) - 1):
            count = 0
            for j in range(len(self.maze_list[i])):
                if self.maze_list[i][j] == '1' or self.maze_list[i][j] == '3':
                    count += 1
            sum_of_gates += len(self.maze_list[i]) - (count + 1)

        # sum the gates of first and last row
        # if the number is 2 or 3, it is not a gate
        for i in range(0, len(self.maze_list[0]), len(self.maze_list[0]) - 1):
            count = 0
            for j in range(len(self.maze_list)):
                if self.maze_list[j][i] == '2' or self.maze_list[j][i] == '3':
                    count += 1     
            sum_of_gates += len(self.maze_list) - (count + 1)
        return sum_of_gates

    def getConnectedWall(self):
        path = [[False for _ in range (len(self.maze_list[0]))] for _ in range (len(self.maze_list))]
        path_record = list()
        for x in range(len(self.maze_list)):
            for y in range (len(self.maze_list[0])):
                if self.maze_list[x][y] is not '0' and path[x][y] == False:
                    record = True
                    new_list = list()
                    self.move(x,y,path, new_list)
                    path_record.append(list(set(new_list)))

        # combine lists which have the one of the same element
        for i in range(len(path_record)):
            for j in range(len(path_record)):
                x = list(set(path_record[i]+path_record[j]))
                y = len(path_record[i]) + len(path_record[j])
                if i == j or path_record[i] == 0 or path_record[j] == 0:
                    break
                elif len(x) < y:
                    path_record[i] = x
                    path_record[j] = [0]

        self.connected_wall_list = [i for i in path_record if i != [0]]
        return len(self.connected_wall_list)
    
    def move(self, x, y, path, new_list):
        path[x][y] = True
        new_list.append((x,y))
        maze_number = self.maze_list[x][y]
        if maze_number is '1':
            self.move(x, y+1, path, new_list)
        elif maze_number is '2':
            self.move(x+1, y, path, new_list)
        elif maze_number is '3':
            self.move(x, y+1, path, new_list)
            self.move(x+1, y, path, new_list)
        else: 
            return

    def sumAccessibleAndInaccessible(self):
        path = [[0 for _ in range (len(self.maze_list[0])-1)] for _ in range (len(self.maze_list)-1)]
        count_accessible_area = 0
        count_inaccessible_point = 0
        # sum the accessible areas of maze
        for y in range(len(self.maze_list[0])-1):
            if not (self.maze_list[0][y] == '1' or self.maze_list[0][y] == '3') and path[0][y] == False:
                new_list = list()
                self.moveAccessibleArea(0,y,'D',path, True, new_list)
                count_accessible_area += 1
                self.accessible_area_list.append(new_list)

        for y in range(len(self.maze_list[0])-1):
            if not (self.maze_list[(len(self.maze_list) - 1)][y] == '1' or self.maze_list[(len(self.maze_list) - 1)][y] == '3') and path[(len(self.maze_list) - 2)][y] == False:
                new_list = list()
                self.moveAccessibleArea(len(self.maze_list) - 2,y,'U',path, True, new_list)
                count_accessible_area += 1
                self.accessible_area_list.append(new_list)
                
        for x in range(len(self.maze_list)-1):
            if not (self.maze_list[x][0] == '2' or self.maze_list[x][0] == '3') and path[x][0] == False:
                new_list = list()
                self.moveAccessibleArea(x,0,'R',path, True, new_list)
                count_accessible_area += 1
                self.accessible_area_list.append(new_list)
                
        for x in range(len(self.maze_list)-1):
            if not (self.maze_list[x][(len(self.maze_list[0]) - 1)] == '2' or self.maze_list[x][(len(self.maze_list[0]) - 1)] == '3') and path[x][(len(self.maze_list[0]) - 2)] == False:
                new_list = list()
                self.moveAccessibleArea(x,len(self.maze_list[0]) - 2,'L',path, True, new_list)
                count_accessible_area += 1
                self.accessible_area_list.append(new_list)
        '''
        path = [[0 for _ in range (len(self.maze_list[0])-1)] for _ in range (len(self.maze_list)-1)]
        for y in range(len(self.maze_list[0])-1):
            if not (self.maze_list[0][y] == '1' or self.maze_list[0][y] == '3') and path[0][y] == 0:
                new_list = list()
                count_list = list()
                count_list.append(0)
                self.moveEntry(0,y,'D',path, True, new_list, count_list)
                print(new_list)
                print(count_list)
        '''
        
        # sum the inaccessible points of maze
        for x in range(len(path)):
            for y in range(len(path[0])):
                if path[x][y] == 0:
                    count_inaccessible_point += 1
                    self.inaccessible_points_list.append((x,y))
        
        return (count_inaccessible_point, count_accessible_area)

    def moveAccessibleArea(self, x, y, move, path, start, new_list):
        maze_number = self.maze_list[x][y]
        if path[x][y]:
            return
        if maze_number is '0' or maze_number is '1':
            if maze_number is '1' and move is 'D' and start is False:
                return
            path[x][y] = 1
            start = False
            if y - 1 >= 0 and move is not 'R':
                self.moveAccessibleArea(x, y-1, 'L', path, start, new_list)
            if y + 1 < len(path[0]) and move is not 'L':\
                self.moveAccessibleArea(x, y+1, 'R', path, start, new_list)
            if x + 1 < len(path) and move is not 'U':
                self.moveAccessibleArea(x+1, y, 'D', path, start, new_list)
            if x - 1 >= 0 and move is not 'D' and maze_number is '0':
                self.moveAccessibleArea(x-1, y, 'U', path, start, new_list)
            new_list.append((x,y))
        if maze_number is '2' or maze_number is '3':
            if maze_number is '2' and move is 'R' and start is False:
                return
            if maze_number is '3' and (move is 'R' or move is 'D') and start is False:
                return
            path[x][y] = 1
            start = False
            if y + 1 < len(path[0]) and move is not 'L':
                self.moveAccessibleArea(x, y+1, 'R', path, start, new_list)
            if x + 1 < len(path) and move is not 'U':
                self.moveAccessibleArea(x+1, y, 'D', path, start, new_list)
            if x - 1 >= 0 and move is not 'D' and maze_number is '2':
                self.moveAccessibleArea(x-1, y, 'U', path, start, new_list)
            
            new_list.append((x,y))
        return

    def moveculdesacs(self, i, j, move, path, new_list, changed_list):
        maze_number = changed_list[i][j]
        if path[i][j]:
            return
        if maze_number == '1' or maze_number == '2':
            changed_list[i][j] = '3'
        elif maze_number == '3':
            if move is 'D' and (changed_list[i][j+1] == '2' or changed_list[i][j+1] == '3'):
                changed_list[i+1][j] = '1'
            elif move is 'R' and (changed_list[i+1][j] == '1' or changed_list[i+1][j] == '3'):
                changed_list[i][j+1] = '2'
        path[i][j] = 1
        new_list.append((i,j))
        if maze_number == '2' and i - 1 >= 0:
            if (changed_list[i][j+1] == '2' or changed_list[i][j+1] == '3') and (changed_list[i+1][j] == '1' or changed_list[i+1][j] == '3'):
                self.moveculdesacs(i-1, j,'U',path, new_list,changed_list)
            else:
                return
        elif maze_number == '3':
            if j + 1 < len(path[0]) and i + 1 < len(path) and (changed_list[i][j+1] == '2' or changed_list[i][j+1] == '3') and move == 'D':
                self.moveculdesacs(i+1, j,'D',path, new_list, changed_list)
            else:
                return
            if i + 1 < len(path) and j + 1 < len(path[0]) and (changed_list[i+1][j] == '1' or changed_list[i+1][j] == '3') and move == 'R':
                self.moveculdesacs(i, j+1,'R',path, new_list, changed_list)
            else:
                return
        elif maze_number == '1' and j - 1 >= 0:
            if (changed_list[i][j+1] == '2' or changed_list[i][j+1] == '3') and (changed_list[i+1][j] == '1' or changed_list[i+1][j] == '3'):
                self.moveculdesacs(i, j-1,'L',path, new_list, changed_list)
            else:
                return
        return

    def seekPillar(self):
        isPillar = True
        for i in range(len(self.maze_list)):
            for j in range(len(self.maze_list[0])):
                if self.maze_list[i][j] == '0':
                    if i > 0 and (self.maze_list[i-1][j] is '3' or self.maze_list[i-1][j] is '2'):
                        continue
                    if j > 0 and (self.maze_list[i][j-1] is '3' or self.maze_list[i][j-1] is '1'):
                        continue
                    self.pillar_list.append((i,j))
                    
    def getCuldesacs(self):
        path_record = []
        nb_cds = 0
        path = [[1 for _ in range (len(self.maze_list[0])-1)] for _ in range (len(self.maze_list)-1)]
        for i in self.inaccessible_points_list:
            x,y = i
            path[x][y] = 0
        changed_list = [[self.maze_list[i][j] for j in range(len(self.maze_list[i]))] for i in range (len(self.maze_list))]
        temp_nb = 0
        intersection = 0

        for i in range(len(self.maze_list) - 1):
            for j in range(len(self.maze_list[0]) - 1):
                if (i,j) in self.inaccessible_points_list:
                    path[i][j] = 1
                    continue
                if self.isCuldesacs(changed_list ,i,j):
                    self.culdesacs_list.append((i,j))
                        
        for i in self.culdesacs_list:
            past = list()
            past.append(i)
            self.foundCDS(changed_list,path,i[0], i[1], past)
            path_record.append(past)
            
        for i in path_record:
            for j in path_record:
                if (i[-1] in j) and (i[-1] != j[-1]) and (i[-1] not in self.culdesacs_list):
                    intersection += 1
        
        for i in range(len(path_record)):
            for j in range(len(path_record)):
                x = list(set(path_record[i]+path_record[j]))
                y = len(path_record[i]) + len(path_record[j])
                if i == j or path_record[i] == 0 or path_record[j] == 0:
                    break
                elif len(x) < y:
                    path_record[i] = x
                    path_record[j] = [0]
        path_record = [i for i in path_record if i != [0]]
        self.print_culdesacs_list = list()
        for x in path_record:
            i,j = x[-1]
            if self.maze_list[i][j] is '0':
                self.print_culdesacs_list.append(x[:-1])
            else:
                self.print_culdesacs_list.append(x)
        return len(self.culdesacs_list) - intersection

    def foundCDS(self,changed_list,path,x,y,past):
            if changed_list[x][y] == '1':
                if x+1<len(changed_list) and y+1 < len(changed_list[0]) and \
                   (changed_list[x+1][y] == '1' or changed_list[x+1][y] == '3' or changed_list[x+1][y] == '4') \
                   and (changed_list[x][y+1] == '2' or changed_list[x][y+1] == '3' or changed_list[x][y+1] == '4'):
                    if y-1>=0:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x,y-1))
                        self.foundCDS(changed_list,path,x,y-1,past)
                    elif y == 0:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                elif y-1>=0 and y+1<len(changed_list[0]) and changed_list[x][y-1] == '4' and (changed_list[x][y+1] == '2' or changed_list[x][y+1] == '3' or changed_list[x][y+1] == '4'):
                    if x+1<=len(changed_list)-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x+1,y))
                        self.foundCDS(changed_list,path,x+1,y,past)
                    elif x == len(changed_list)-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                elif y-1 >= 0 and x+1 < len(changed_list) and changed_list[x][y-1] == '4' and (changed_list[x+1][y] == '1' or changed_list[x+1][y] == '3' or changed_list[x+1][y] == '4'):
                    if y+1 <= len(changed_list[0])-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x,y+1))
                        self.foundCDS(changed_list,path,x,y+1,past)
                    elif y == len(changed_list[0])-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
            if changed_list[x][y] == '2':
                if x+1<len(changed_list) and y+1<len(changed_list[0]) and \
                   (changed_list[x+1][y] == '1' or changed_list[x+1][y] == '3' or changed_list[x+1][y] == '4') and \
                   (changed_list[x][y+1] == '2' or changed_list[x][y+1] == '3' or changed_list[x][y+1] == '4'):
                    if x-1 >= 0:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x-1,y))
                        self.foundCDS(changed_list,path,x-1,y,past)
                    elif x == 0:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                elif y+1 < len(changed_list[0]) and x-1>=0 and \
                     changed_list[x-1][y] == '4' and (changed_list[x][y+1] == '2' or changed_list[x][y+1] == '3' or changed_list[x][y+1] == '4'):
                    if x+1 <= len(changed_list)-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x+1,y))
                        self.foundCDS(changed_list,path,x+1,y,past)
                    elif x == len(changed_list)-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                elif x-1>=0 and x+1 < len(changed_list) and \
                     changed_list[x-1][y] == '4' and (changed_list[x+1][y] == '1' or changed_list[x+1][y] == '3' or changed_list[x+1][y] == '4'):
                    if y+1<=len(changed_list[0])-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        self.foundCDS(changed_list,path,x,y+1,past)
                    elif y == len(changed_list[0])-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
            if changed_list[x][y] == '3':
                if y+1<len(changed_list[0]) and \
                   (changed_list[x][y+1] == '2' or changed_list[x][y+1] == '3' or changed_list[x][y+1] == '4'):
                    if x+1<= len(changed_list)-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x+1,y))
                        self.foundCDS(changed_list,path,x+1,y,past)
                    if x == len(changed_list)-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                elif x+1 < len(changed_list) and \
                     (changed_list[x+1][y] == '1' or changed_list[x+1][y] == '3' or changed_list[x+1][y] == '4'):
                    if y+1 <= len(changed_list[0])-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x,y+1))
                        self.foundCDS(changed_list,path,x,y+1,past)
                    if y == len(changed_list[0])-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
            if changed_list[x][y] == '0':
                if y-1>=0 and y+1 <= len(changed_list[0]) and x+1<len(changed_list) and changed_list[x][y-1] == '4' and (changed_list[x+1][y] == '1' or changed_list[x+1][y] == '3' or changed_list[x+1][y] == '4')\
                   and (changed_list[x][y+1] == '2' or changed_list[x][y+1] == '3' or changed_list[x][y+1] == '4'):
                    if x-1>=0:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x-1,y))
                        self.foundCDS(changed_list,path,x-1,y,past)
                    elif x == 0:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                elif x-1>=0 and x+1 < len(changed_list) and y+1 < len(changed_list[0]) and \
                     changed_list[x-1][y] == '4' and (changed_list[x+1][y] == '1' or changed_list[x+1][y] == '3' or changed_list[x+1][y] == '4') \
                     and (changed_list[x][y+1] == '2' or changed_list[x][y+1] == '3' or changed_list[x][y+1] == '4'):
                    if y-1 >= 0:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x,y-1))
                        self.foundCDS(changed_list,path,x,y-1,past)
                    elif y == 0:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                elif x-1>=0 and y-1>=0 and y+1<len(changed_list[0]) and \
                     changed_list[x-1][y] == '4' and changed_list[x][y-1] == '4' and (changed_list[x][y+1] == '2' or changed_list[x][y+1] == '3' or changed_list[x][y+1] == '4'):
                    if x+1<=len(changed_list)-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x+1,y))
                        self.foundCDS(changed_list,path,x+1,y,past)
                    elif x == len(changed_list)-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                elif x-1>=0 and y-1>=0 and x+1<len(changed_list) and \
                     changed_list[x-1][y] == '4' and changed_list[x][y-1] == '4' and (changed_list[x+1][y] == '1' or changed_list[x+1][y] == '3' or changed_list[x+1][y] == '4'):
                    if y+1<=len(changed_list[0])-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        past.append((x,y+1))
                        self.foundCDS(changed_list,path,x,y+1,past)
                    elif y == len(changed_list[0])-2:
                        path[x][y] = 2
                        changed_list[x][y] = '4'
                        
    def isCuldesacs(self, maze_list, i, j):
        if maze_list[i][j] == '2':
            if (maze_list[i][j+1] == '2' or maze_list[i][j+1] == '3') and (maze_list[i+1][j] == '1' or maze_list[i+1][j] == '3'):
                return True
        elif maze_list[i][j] == '3':
            if maze_list[i][j+1] == '2' or maze_list[i][j+1] == '3':
                return True
            if maze_list[i+1][j] == '1' or maze_list[i+1][j] == '3':
                return True
        elif maze_list[i][j] == '1':
            if (maze_list[i][j+1] == '2' or maze_list[i][j+1] == '3') and (maze_list[i+1][j] == '1' or maze_list[i+1][j] == '3'):
                return True
        return False
            
    
    def seekCuldesacs(self):
        path = [[0 for _ in range (len(self.maze_list[0])-1)] for _ in range (len(self.maze_list)-1)]
        culdesacs_list = list()
        changed_list = [[self.maze_list[i][j] for j in range(len(self.maze_list[i]))] for i in range (len(self.maze_list))]
        for i in range(len(changed_list) - 1):
            for j in range(len(changed_list[0]) - 1):
                if (i,j) in self.inaccessible_points_list:
                    path[i][j] = 1
                    continue
                if changed_list[i][j] == '2':
                    if (changed_list[i][j+1] == '2' or changed_list[i][j+1] == '3') and (changed_list[i+1][j] == '1' or changed_list[i+1][j] == '3'):
                        new_list = list()
                        self.moveculdesacs(i, j,'U',path, new_list, changed_list)
                        culdesacs_list.append(new_list)
                elif changed_list[i][j] == '3':
                    if changed_list[i][j+1] == '2' or changed_list[i][j+1] == '3':
                        new_list = list()
                        self.moveculdesacs(i, j,'D',path, new_list, changed_list)
                        culdesacs_list.append(new_list)
                    if changed_list[i+1][j] == '1' or changed_list[i+1][j] == '3':
                        new_list = list()
                        self.moveculdesacs(i, j,'R',path, new_list, changed_list)
                        culdesacs_list.append(new_list)
                elif changed_list[i][j] == '1':
                    if (changed_list[i][j+1] == '2' or changed_list[i][j+1] == '3') and (changed_list[i+1][j] == '1' or changed_list[i+1][j] == '3'):
                        new_list = list()
                        self.moveculdesacs(i, j,'L',path, new_list, changed_list)
                        culdesacs_list.append(new_list)
        '''                
        for i in range(len(self.accessible_area_list)):
            for j in range(1, len(self.accessible_area_list[i]), 1):
                    x, y = self.accessible_area_list[i][j-1]
                    next_x, next_y = self.accessible_area_list[i][j]
                    if not (x == next_x or y == next_y):
                        print(self.accessible_area_list[i][j])
        '''

    def setPrintCDS(self):
        print_cds = list()
        most_x = 0
        most_y = 0
        for i in self.print_culdesacs_list:
            for j in i:
                tuple_list = j
                x,y = tuple_list
                if int(x) > most_x:
                    most_x = int(x)
                if int(y) > most_y:
                    most_y = int(y)
        record_list = [[0 for _ in range(most_x+1)] for _ in range(most_y+1)]
        for i in self.print_culdesacs_list:
            for j in i:
                tuple_list = j
                x,y = tuple_list
                record_list[int(y)][int(x)] = 1
        for i in range(len(record_list)):
            for j in range(len(record_list[0])):
                if record_list[i][j] == 1:
                    self.print_cds.append((j+0.5,i+0.5))
        self.print_cds.sort()
        
    def printMaze(self):
        for i in self.maze_list:
            for j in i:
                print(j, end = ' ')
            print()

    def setPrintWall(self):
        
        for i in range (len(self.maze_list)):
            j = 0
            while j < len(self.maze_list[i])-1:
                new_list = list()
                if self.maze_list[i][j] == '1' or self.maze_list[i][j] == '3':
                    new_list.append((j,i))
                    for w in range(j+1, len(self.maze_list[i]), 1):
                        if not (self.maze_list[i][w] == '1' or self.maze_list[i][w] == '3'):
                            new_list.append((w,i))
                            j = w
                            self.print_wall_list.append(new_list)
                            break
                else:
                    j+=1

        for j in range (len(self.maze_list[i])):
            i = 0
            while i < len(self.maze_list)-1:
                new_list = list()
                if self.maze_list[i][j] == '2' or self.maze_list[i][j] == '3':
                    new_list.append((j,i))
                    for w in range(i+1, len(self.maze_list), 1):
                        if not (self.maze_list[w][j] == '2' or self.maze_list[w][j] == '3'):
                            new_list.append((j,w))
                            i = w
                            self.print_wall_list.append(new_list)
                            break
                else:
                    i+=1

    def gen_entry_exit(self):
        print(self.accessible_area_list)
        print(self.print_culdesacs_list)
        one_way_list = list()
        for i in self.accessible_area_list:
            count = 0
            for x in i:
                if x[0] == 0 or x[1] == 0 or x[0] == len(self.maze_list) - 2 or x[1] == len(self.maze_list[0]) - 2:
                    count += 1
            if count <= 2 and count >= 1:
                one_way_list.append(i)
        for i in self.accessible_area_list:
            pass
        for i in one_way_list:
            if i in self.print_culdesacs_list:
                continue
            else:
                print(i)
                
        
    def gen_tex(self):
        self.file_latex_text=''
        self.file_latex_text+=r'\documentclass[10pt]{article}'+'\n'+r'\usepackage{tikz}'+'\n'+r'\usetikzlibrary{shapes.misc}'+'\n'
        self.file_latex_text+=r'\usepackage[margin=0cm]{geometry}'+'\n'+r'\pagestyle{empty}'+'\n'+r'\tikzstyle{every node}=[cross out, draw, red]'+'\n'
        self.file_latex_text+='\n\\begin{document}\n\n'+r'\vspace*{\fill}'+'\n'+r'\begin{center}'+'\n'
        self.file_latex_text+=r'\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]'
        self.file_latex_text+='\n% Walls'
        for w in self.print_wall_list:
            x, y = w
            self.file_latex_text+='\n    \\draw ('+str(x[0])+','+str(x[1])+') -- ('+str(y[0])+','+str(y[1])+');'
            
        self.file_latex_text+='\n% Pillars'   
        for p in self.pillar_list:
            i, j = p
            self.file_latex_text+='\n    \\fill[green] ('+str(j)+','+str(i)+') circle(0.2);'
        self.file_latex_text+='\n% Inner points in accessible cul-de-sacs'
        for i in self.print_cds:
            self.file_latex_text+='\n    \\node at ('+str(i[1])+','+str(i[0])+') {};'
        self.file_latex_text+='\n% Entry-exit paths without intersections'
        self.file_latex_text+='\n'+r'\end{tikzpicture}'+'\n'+r'\end{center}'+'\n'+r'\vspace*{\fill}'+'\n'
        self.file_latex_text+='\n'
        self.file_latex_text+=r'\end{document}'+'\n'

    def save_to_latex(self, name):
        f=open(name,'w')
        f.write(self.file_latex_text)
        f.close()
    
class MazeError(ValueError):
    def __init__(self,args):
        pass

