
# coding: utf-8

# In[ ]:


class game:
    def __init__(self):
        self.move = [[0,-1],[0,1],[-1,0],[1,0]]
        self.tank = ['^','v','<','>']
        self.uI = ['U','D','L','R','S']
        self.HW = input()
        self.H = int(self.HW.split(' ')[0])
        self.W = int(self.HW.split(' ')[1])
        self.map = []
        self.tank_x = None
        self.tank_y = None
        self.tank_cond = None
        for i in range(0,self.H):
            self.map.append([])
            for m in input():
                self.map[i].append([m])
        self.user_input_n = input()
        self.user_input = input()
        self.out = ''
        self.output_object = []
        self.output_objects = []

    def find_tank(self):
        for j in range(0,self.H):
            for k in self.tank:
                if [k] in self.map[j]:
                    try:
                        self.tank_x = self.map[j].index([k])
                    except ValueError:
                        pass
                    self.tank_y = j
                    self.tank_cond = k
    def check(self,key):
        ymove = self.tank_y+self.move[key][1]
        xmove = self.tank_x+self.move[key][0]
        if ymove != -1 and xmove != -1:
            if self.map[ymove][xmove] == ['.']:
                return 'go'
            else:
                return 'no'
        else:
            return 'no'
    def shoot(self,cond):
        drt = cond
        if drt in ['^','v']:
            yaxis = self.tank_y
            for i in range(0,self.H+1):
                try:
                    yaxis =yaxis + self.move[self.tank.index(drt)][1]
                    if yaxis == -1:
                        break
                    elif self.map[yaxis][self.tank_x]==['#']:
                        break
                    elif self.map[yaxis][self.tank_x]==['*']:
                        self.map[yaxis][self.tank_x] = ['.']
                        break
                except IndexError:
                    pass

        else:
            xaxis = self.tank_x
            for i in range(0, self.W + 1):
                try:
                    xaxis = xaxis + self.move[self.tank.index(drt)][0]
                    if xaxis == -1:
                        break
                    elif self.map[self.tank_y][xaxis] == ['#']:
                        break
                    elif self.map[self.tank_y][xaxis] == ['*']:
                        self.map[self.tank_y][xaxis] = ['.']
                        break
                except IndexError:
                    pass
    def action(self):
        for l in self.user_input:
            key = int(self.uI.index(l))
            if key !=4:
                try:
                    if self.check(key) == 'go':
                        self.map[self.tank_y + self.move[key][1]][self.tank_x + self.move[key][0]] = [self.tank[key]]
                        self.map[self.tank_y][self.tank_x] = ['.']
                    else:
                        self.map[self.tank_y][self.tank_x] = [self.tank[key]]
                except IndexError:
                    self.map[self.tank_y][self.tank_x] = [self.tank[key]]
                    pass
                self.find_tank()
            else:
                self.shoot(self.tank_cond)
                self.find_tank()
    def output(self):
        for i in self.map:
            self.out = ''
            for j in i:
                self.out = self.out+j[0]
            self.output_object.append(self.out)
        return self.output_object







    def print(self):
        for i in self.map:
            print(i)


test_number = int(input())
output = []
for i in range(0,test_number):
    gameset = game()
    gameset.find_tank()
    gameset.action()
    output.append(gameset.output())
f = open("output_1.txt", 'w')
for j in range(1,len(output)+1):
    f.write('#{0} '.format(j))
    for k in output[j-1]:
        f.write(k)
        f.write('\n')
f.close()


# q = True
# while q:
#     gameset = game()
#     gameset.find_tank()
#     gameset.action()
#     gameset.print()
#     e = int(input())
#     if e == 1:
#         q = False



# for i in range(0,tc):
#     h = int(input)
#     w = int(input)
#     map = []
#     for j in range(0,h):
#         mapObject = input()
#         map.append(mapObject)
#     userInput = input()
#     for k in userInput:

