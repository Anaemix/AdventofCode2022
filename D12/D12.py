data = [list(k) for k in open('D12/input.txt', 'r').read().split("\n")]
print(data)
height = len(data)
width = len(data[0])

import networkx
graph = networkx.DiGraph()

for y, h in enumerate(data):
    for x, w in enumerate(h):
        if w == "S":
            startX = x
            startY = y
            data[y][x] = 'a'
        if w == "E":
            endX = x
            endY = y
            data[y][x]='z'
        data[y][x] = ord(data[y][x])-97


for y in range(height):
    for x in range(width):
        for nx, ny in [(1,0), (-1,0), (0,1), (0,-1)]:
            tx, ty = nx+x,ny+y
            if (0<=ty<height) and (0<=tx<width):
                if abs(data[y][x] - data[ty][tx])<=1:
                    graph.add_edge((x,y),(tx,ty))
                    print(".", end="")

p = networkx.shortest_path(graph, (startX, startY), (endX, endY))
print(len(p)-1)
print(data)