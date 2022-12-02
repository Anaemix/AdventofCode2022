z = {"A": {"X": 3,"Y": 6,"Z":0}, "B": {"X": 0,"Y": 3,"Z":6}, "C": {"X": 6,"Y": 0,"Z":3}}
bonus = {'X': 1, 'Y': 2, 'Z': 3}
count = lambda x: z[x.split(' ')[0]][x.split(' ')[1]] + bonus[x.split(' ')[1]]
with open('D2/input.txt', 'r') as file:
    points = [count(point) for point in file.read().split('\n')]
print(sum(points))