class MazeError(Exception):
    def __init__(self, message):
            self.message = message
class Maze:
    def MazeError(self):
        def __init__(self,message):
            self.message = message
    def __init__(self, filename):
        L = []
        with open(filename) as f:
            for line in f.readlines():
                line = line.strip()
                M = list(line)
                while ' ' in M:
                    M.remove(' ')
                L.append(M)
        while [] in L:
            L.remove([])
        self.file = L
        self.get_input()
        self.get_input_2()
    def get_input(self):
        if len(self.file) < 2 or len(self.file) > 41:
            raise MazeError('Incorrect input.')
        for e in self.file:
            if len(e) < 2 or len(e) > 31:
                raise MazeError('Incorrect input.')
        for e in self.file:
            for i in self.file:
                if len(e) != len(i):
                    raise MazeError('Incorrect input.')
        for e in self.file:
            for i in e:
                if i not in {'0','1','2','3'}:
                    raise MazeError('Incorrect input')
        return True
    def get_input_2(self):
        if self.get_input():
            for e in self.file:
                if e[-1] == '1' or e[-1] == '3':
                    raise MazeError('Input does not represent a maze.')
            for e in self.file[-1]:
                if e == '2' or e == '3':
                    raise MazeError('Input does not represent a maze.')
    def analyse(self):
        ## number of gates
        gate_nb = 0
        #top
        for e in range(len(self.file[0]) - 1):
            if self.file[0][e] == '0' or self.file[0][e] == '2':
                gate_nb += 1
        #left
        for e in range(len(self.file) - 1):
            if self.file[e][0] == '1' or self.file[e][0] == '0':
                gate_nb += 1
        #bot
        for e in range(len(self.file[-1]) - 1):
            if self.file[-1][e] == '0':
                gate_nb += 1
        #right
        for e in range(len(self.file) - 1):
            if self.file[e][-1] == '0':
                gate_nb += 1
        if gate_nb == 0:
            print('The maze has no gate.')
        elif gate_nb == 1:
            print('The maze has a single gate.')
        else:
            print(f'The maze has {gate_nb} gates.')

        ## number of walls
        L = self.file
        grid = []
        for e in range(2 * len(L)):
            grid.append([])
        for e in grid:
            for i in range(2 * len(L[0])):
                e.append(0)

        for e in range(len(self.file)):
            for i in range(len(self.file[0])):
                if L[e][i] == '0':
                    grid[2 * e][2 * i] = 1
                    grid[2 * e][2 * i + 1] = 1
                    grid[2 * e + 1][2 * i] = 1
                    grid[2 * e + 1][2 * i + 1] = 1
                    if i - 1>= 0:
                        if L[e][i - 1] == '1' or L[e][i - 1] == '3':
                            grid[2 * e][2 * i] = 0
                    if e - 1 >= 0:
                      if L[e-1][i] == '2' or L[e-1][i]=='3':
                        grid[2 * e][2 * i] = 0
                if L[e][i] == '1':
                    grid[2 * e][2 * i] = 0
                    grid[2 * e][2 * i + 1] = 0
                    grid[2 * e + 1][2 * i] = 1
                    grid[2 * e + 1][2 * i + 1] = 1
                if L[e][i] == '2':
                    grid[2 * e][2 * i] = 0
                    grid[2 * e][2 * i + 1] = 1
                    grid[2 * e + 1][2 * i] = 0
                    grid[2 * e + 1][2 * i + 1] = 1
                if L[e][i] == '3':
                    grid[2 * e][2 * i] = 0
                    grid[2 * e][2 * i + 1] = 0
                    grid[2 * e + 1][2 * i] = 0
                    grid[2 * e + 1][2 * i + 1] = 1
        for e in grid:
            e.pop(-1)
        grid = grid[: -1]
        def findwalls():
            count = 0
            listofij = list()
            def walls(args = []):
                list2 = list()
                list1 = [0,1,-1]
                if len(args) != 0:
                    for e in range(len(args)):
                        (x,y) = args[e]
                        for i in list1:
                            for j in list1:
                                if (x + i) >= 0 and (x + i) <= (len(grid) - 1) and (y + j) >= 0 and (y + j) <= (len(grid[0]) - 1) and abs(i) != abs(j) and grid[x + i][y + j] == 0:
                                    list2.append(((x + i),(y+j)))
                        grid[x][y] = 1
                    walls(list2)
                else:
                    return        
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        listofij = [(i,j)]
                        count += 1
                        walls(listofij)
            return count
        nb_walls = findwalls()
        if nb_walls == 0:
            print('The maze has no wall.')
        elif nb_walls == 1:
            print('The maze has walls that are all connected.')
        else:
            print(f'The maze has {nb_walls} sets of walls that are all connected.')

        #number of accessible area and inaccessible point
        path = []
        for e in range(len(self.file)-1):
            path.append([])
        for e in range(len(path)):
            for i in range(len(self.file[0])-1):
                path[e].append(0)
        nb_area = 0
        nb_point = 0
        def move_path(x, y, derection, path):
            maze_number = self.file[x][y]
            if path[x][y] == 1:
                return
            if maze_number == '0' or maze_number == '1':
                if maze_number == '1' and derection == 'B':
                    return
                path[x][y] = 1
                if y - 1 >= 0 and derection != 'R':
                    move_path(x, y-1, 'L', path)
                if y + 1 < len(path[0]) and derection != 'L':
                    move_path(x, y+1, 'R', path)
                if x + 1 < len(path) and derection != 'T':
                    move_path(x+1, y, 'B', path)
                if x - 1 >= 0 and derection != 'B' and maze_number == '0':
                    move_path(x-1, y, 'T', path)
            if maze_number == '2' or maze_number == '3':
                if maze_number == '2' and derection == 'R':
                    return
                if maze_number == '3' and (derection == 'R' or derection == 'B'):
                    return
                path[x][y] = 1
                if y + 1 < len(path[0]) and derection != 'L':
                    move_path(x, y+1, 'R', path)
                if x + 1 < len(path) and derection != 'T':
                    move_path(x+1, y, 'B', path)
                if x - 1 >= 0 and derection != 'B' and maze_number == '2':
                    move_path(x-1, y, 'T', path)
            return
        
        # number of the accessible areas of maze        
        for x in range(len(self.file)-1):
            if not (self.file[x][0] == '2' or self.file[x][0] == '3') and path[x][0] == 0:
                move_path(x,0,'R',path)
                nb_area += 1
                        
        for y in range(len(self.file[0])-1):
            if not (self.file[0][y] == '1' or self.file[0][y] == '3') and path[0][y] == 0:
                move_path(0,y,'B',path)
                nb_area += 1

        for x in range(len(self.file)-1):
            if not (self.file[x][(len(self.file[0]) - 1)] == '2' or self.file[x][(len(self.file[0]) - 1)] == '3') and path[x][(len(self.file[0]) - 2)] == 0:
                move_path(x,len(self.file[0]) - 2,'L',path)
                nb_area += 1
                
        for y in range(len(self.file[0])-1):
            if not (self.file[(len(self.file) - 1)][y] == '1' or self.file[(len(self.file) - 1)][y] == '3') and path[(len(self.file) - 2)][y] == 0:
                move_path(len(self.file) - 2,y,'T',path)
                nb_area += 1
                    
        # number of the inaccessible points of maze
        for line in path:
            nb_point += line.count(0)
        
        #output of number of accessible area and inaccessible point    
        if nb_point == 0:
            print('The maze has no inaccessible inner point.')
        elif nb_point == 1:
            print('The maze has a unique inaccessible inner point.')
        else:
            print(f'The maze has {nb_point} inaccessible inner points.')
        if nb_area == 0:
            print('The maze has no accessible area.')
        elif nb_area == 1:
            print('The maze has a unique accessible area.')
        else:
            print(f'The maze has {nb_area} accessible areas.')

        #accessible cul-de-sacs that are all connected
        nb_cds = 0
        M = path
        N = self.file
        past = []
        def cds(m):
            x=m[0]
            y=m[1]
            if N[x][y] == '1':
                if x+1<len(N) and y+1 < len(N[0]) and \
                   (N[x+1][y] == '1' or N[x+1][y] == '3' or N[x+1][y] == '4') \
                   and (N[x][y+1] == '2' or N[x][y+1] == '3' or N[x][y+1] == '4'):
                    if y-1>=0:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x,y-1))
                        cds((x,y-1))
                    elif y == 0:
                        M[x][y] = 2
                        N[x][y] = '4'
                elif y-1>=0 and y+1<len(N[0]) and \
                     N[x][y-1] == '4' and (N[x][y+1] == '2' or N[x][y+1] == '3' or N[x][y+1] == '4'):
                    if x+1<=len(N)-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x+1,y))
                        cds((x+1,y))
                    elif x == len(N)-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                elif y-1 >= 0 and x+1 < len(N) and \
                     N[x][y-1] == '4' and (N[x+1][y] == '1' or N[x+1][y] == '3' or N[x+1][y] == '4'):
                    if y+1 <= len(N[0])-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x,y+1))
                        cds((x,y+1))
                    elif y == len(N[0])-2:
                        M[x][y] = 2
                        N[x][y] = '4'
            if N[x][y] == '2':
                if x+1<len(N) and y+1<len(N[0]) and \
                   (N[x+1][y] == '1' or N[x+1][y] == '3' or N[x+1][y] == '4') and \
                   (N[x][y+1] == '2' or N[x][y+1] == '3' or N[x][y+1] == '4'):
                    if x-1 >= 0:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x-1,y))
                        cds((x-1,y))
                    elif x == 0:
                        M[x][y] = 2
                        N[x][y] = '4'
                elif y+1 < len(N[0]) and x-1>=0 and \
                     N[x-1][y] == '4' and (N[x][y+1] == '2' or N[x][y+1] == '3' or N[x][y+1] == '4'):
                    if x+1 <= len(N)-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x+1,y))
                        cds((x+1,y))
                    elif x == len(N)-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                elif x-1>=0 and x+1 < len(N)and \
                     N[x-1][y] == '4' and (N[x+1][y] == '1' or N[x+1][y] == '3' or N[x+1][y] == '4'):
                    if y+1<=len(N[0])-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x,y+1))
                        cds((x,y+1))
                    elif y == len(N[0])-2:
                        M[x][y] = 2
                        N[x][y] = '4'
            if N[x][y] == '3':
                if y+1<len(N[0]) and \
                   (N[x][y+1] == '2' or N[x][y+1] == '3' or N[x][y+1] == '4'):
                    if x+1<= len(N)-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x+1,y))
                        cds((x+1,y))
                    if x == len(N)-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                elif x+1 < len(N) and \
                     (N[x+1][y] == '1' or N[x+1][y] == '3' or N[x+1][y] == '4'):
                    if y+1 <= len(N[0])-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x,y+1))
                        cds((x,y+1))
                    if y == len(N[0])-2:
                        M[x][y] = 2
                        N[x][y] = '4'
            if N[x][y] == '0':
                if y-1>=0 and y+1 <= len(N[0]) and x+1<len(N) and \
                   N[x][y-1] == '4' and (N[x+1][y] == '1' or N[x+1][y] == '3' or N[x+1][y] == '4')\
                   and (N[x][y+1] == '2' or N[x][y+1] == '3' or N[x][y+1] == '4'):
##                    print(N[x][y-1])
                    if x-1>=0:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x-1,y))
                        cds((x-1,y))
                    elif x == 0:
                        M[x][y] = 2
                        N[x][y] = '4'
                elif x-1>=0 and x+1 < len(N) and y+1 < len(N[0]) and \
                     N[x-1][y] == '4' and (N[x+1][y] == '1' or N[x+1][y] == '3' or N[x+1][y] == '4') \
                     and (N[x][y+1] == '2' or N[x][y+1] == '3' or N[x][y+1] == '4'):
                    if y-1 >= 0:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x,y-1))
                        cds((x,y-1))
                    elif y == 0:
                        M[x][y] = 2
                        N[x][y] = '4'
                elif x-1>=0 and y-1>=0 and y+1<len(N[0]) and \
                     N[x-1][y] == '4' and N[x][y-1] == '4' and (N[x][y+1] == '2' or N[x][y+1] == '3' or N[x][y+1] == '4'):
                    if x+1<=len(N)-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x+1,y))
                        cds((x+1,y))
                    elif x == len(N)-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                elif x-1>=0 and y-1>=0 and x+1<len(N) and \
                     N[x-1][y] == '4' and N[x][y-1] == '4' and (N[x+1][y] == '1' or N[x+1][y] == '3' or N[x+1][y] == '4'):
                    if y+1<=len(N[0])-2:
                        M[x][y] = 2
                        N[x][y] = '4'
                        past.append((x,y+1))
                        cds((x,y+1))
                    elif y == len(N[0])-2:
                        M[x][y] = 2
                        N[x][y] = '4' 
        temp_nb = 0
        C = []
        for x in range(len(M)):
            for y in range(len(M[0])):
                if M[x][y] != 0:
                    if x+1 <= len(N) and y+1 <= len(N[0]):
                        if (N[x][y] == '1' and (N[x][y+1] == '2' or N[x][y+1] == '3') and (N[x+1][y] == '1' or N[x+1][y] == '3'))\
                           or (N[x][y] == '2' and (N[x][y+1] == '2' or N[x][y+1] == '3') and (N[x+1][y] == '1' or N[x+1][y] == '3'))\
                           or (N[x][y] == '3' and (N[x][y+1] == '2' or N[x][y+1] == '3'))\
                           or (N[x][y] == '3' and (N[x+1][y] == '1' or N[x+1][y] == '3')):
                            M[x][y] = 2
                            C.append((x,y))
        pp = []
        for e in C:
            past = []
##            print(e)
            past.append(e)
            cds(e)
            pp.append(past)
            temp_nb += 1
        c = 0
        for e in pp:
            for i in pp:
                if e[-1] in i and e[-1] != i[-1] and i[-1] not in C:
                    c += 1
        nb_cds = temp_nb - c
        print(C)
        if nb_cds == 0:
            print('The maze has no accessible cul-de-sac.')
        elif nb_cds == 1:
            print('The maze has accessible cul-de-sacs that are all connected.')
        else:
            print(f'The maze has {nb_cds} sets of accessible cul-de-sacs that are all connected.')

        #entry-exit

        gate = []
        #top
        for e in range(len(self.file[0]) - 1):
            if self.file[0][e] == '0' or self.file[0][e] == '2':
                gate.append((0,e))
        #left
        for e in range(len(self.file) - 1):
            if self.file[e][0] == '1' or self.file[e][0] == '0':
                gate.append((e,0))
        #bot
        for e in range(len(self.file[-1])):
            if self.file[-1][e] == '0':
                gate.append((len(self.file)-1,e))
        #right
        for e in range(len(self.file)):
            if self.file[e][-1] == '0':
                gate.append((e,len(self.file[0])-1))
        gate = list(set(gate))
        gate = sorted(gate)
####maze = Maze('labyrinth.txt')
maze = Maze('maze_2.txt')
maze.analyse()
##Maze('not_a_maze_1.txt')


