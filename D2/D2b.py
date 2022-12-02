z = {"A": {"X": 3,"Y": 1,"Z":2}, "B": {"X": 1,"Y": 2,"Z":3}, "C": {"X": 2,"Y": 3,"Z":1}}
win = {'X': 0, 'Y': 3, 'Z': 6}
count = lambda x: z[x.split(' ')[0]][x.split(' ')[1]] + win[x.split(' ')[1]]
with open('D2/input.txt', 'r') as file:
    points = [count(point) for point in file.read().split('\n')]
print(sum(points))