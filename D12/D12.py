import networkx
import random

def getlen(data):
    height = len(data)
    width = len(data[0])
    graph = networkx.DiGraph()

    for y, h in enumerate(data):
        #print(h)
        for x, w in enumerate(h):
            if w == "S":
                #print(".", end="")
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
                    if data[ty][tx] <= data[y][x] + 1:
                        graph.add_edge((x, y), (tx, ty))
    p = networkx.shortest_path(graph, (startX, startY), (endX, endY))
    return (len(p)-1)

data = [list(k) for k in open('D12/input.txt', 'r').read().split("\n")]

print("part1:",getlen(data))
data = [list(k) for k in open('D12/input.txt', 'r').read().replace("S", 'a').split("\n")]
distances = []
for i in range(len(data)):
    data = [list(k) for k in open('D12/input.txt', 'r').read().replace("S", 'a').split("\n")]
    data[i][0] = 'S'
    distances.append(getlen(data))

print("part2:",min(distances))

