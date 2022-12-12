class pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def changepos(self, p):
        self.x += p.x
        self.y += p.y
    def setpos(self, x, y):
        self.x = x
        self.y = y
    def printpos(self):
        print(f"x: {self.x}, y: {self.y}")
    def getpos(self):
        return f"({self.x},{self.y})"

dir = {'R': pos(1,0), 'L': pos(-1,0), 'U': pos(0, 1), 'D': pos(0,-1)}

def follow(pos1, pos2):
    if (abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y))>=4:
        pos2.setpos(pos1.x - 1 if pos1.x - pos2.x > 1 else pos1.x+1, pos1.y - 1 if pos1.y - pos2.y > 1 else pos1.y+1)
    if (pos1.x - pos2.x) >= 2: 
        pos2.setpos(pos1.x-1, pos1.y)
    if (pos1.x - pos2.x) <= -2: 
        pos2.setpos(pos1.x+1, pos1.y)
    if (pos1.y - pos2.y) >= 2: 
        pos2.setpos(pos1.x, pos1.y-1)
    if (pos1.y - pos2.y) <= -2: 
        pos2.setpos(pos1.x, pos1.y+1)
    return pos2

def part1(file):
    file = file.split('\n')
    tail = pos(0,0)
    head = pos(0,0)
    positions = ['(0,0)']
    for command in file:
        command = command.split(' ')
        for move in range(int(command[1])):
            head.changepos(dir[command[0]])
            if (head.x - tail.x) >= 2: 
                tail.setpos(head.x-1, head.y)
            if (head.x - tail.x) <= -2: 
                tail.setpos(head.x+1, head.y)
            if (head.y - tail.y) >= 2: 
                tail.setpos(head.x, head.y-1)
            if (head.y - tail.y) <= -2: 
                tail.setpos(head.x, head.y+1)
            positions.append(tail.getpos())
    print(len(list(set(positions))))

def printstate(head, tail):
    print("")
    for y in range(26):
        for x in range(26):
            if head.x == x-10 and head.y == y-10:
                print('H', end="")
            elif len([t for t in tail if t.x == x-10 and t.y == y-10])>=1:
                print('t', end="")
            else:
                print('.', end="")
        print("")

def part2(file):
    file = file.split('\n')
    tail = []
    for i in range(9):
        tail.append(pos(0,0))
    head = pos(0,0)
    positions = ['(0,0)']
    for command in file:
        command = command.split(' ')
        for move in range(int(command[1])):
            head.changepos(dir[command[0]])
            for i, piece in enumerate(tail):
                if i == 0:
                    tail[i] = follow(head,piece)
                else:
                    tail[i] = follow(tail[i-1], piece)
            positions.append(tail[8].getpos())
    print(len(list(set(positions))))


if __name__ == '__main__':
    file = open('D9/input.txt', 'r').read().strip()
    part1(file)
    part2(file)