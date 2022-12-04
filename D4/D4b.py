lines = open('D4/input.txt', 'r').read().strip().split('\n')
pairs = [[list(range(int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])+1)),list(range(int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])+1))] for line in lines]
tot = 0
for i in pairs:
    if any(item in i[0] for item in i[1]) or all(item in i[1] for item in i[0]):
        tot +=1
print(tot)