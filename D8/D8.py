def creatematrix(file):
    return [[int(char) for char in line] for line in file.split("\n")]

def visible(matrix, value, x, y):
    if value > max(matrix[y][:x]):
        return True
    if value > max(matrix[y][x+1:]):
        return True
    if value > max([i[x] for i in matrix[:y]]):
        return True
    if value > max([i[x] for i in matrix[y+1:]]):
        return True
    return False

def getscore(matrix, value, x, y):
    #left
    left = 0
    for i in list(reversed(matrix[y][:x])):
        left+=1
        if i >= value:
            break
    #right
    right = 0
    for i in matrix[y][x+1:]:
        right+=1
        if i >= value:
            break
    #upp
    upp = 0
    for i in [row[x] for row in list(reversed(matrix[:y]))]:
        upp+=1
        if i >= value:
            break
    #down
    down = 0
    for i in [row[x] for row in matrix[y+1:]]:
        down+=1
        if i >= value:
            break
    return down*upp*left*right


def part1(file):
    matrix = creatematrix(file)
    total = (len(matrix)-1)*4
    for y, row in enumerate(matrix):
        if y == 0 or y == (len(matrix) - 1):
            continue
        for x, element in enumerate(row):
            if x == 0 or x == (len(matrix) - 1):
                continue
            if(visible(matrix, element, x, y)):
                total+=1
    print(total)


def part2(file):
    matrix = creatematrix(file)
    highestscore=0
    for y, row in enumerate(matrix):
        if y == 0 or y == (len(matrix) - 1):
            continue
        for x, element in enumerate(row):
            if x == 0 or x == (len(matrix) - 1):
                continue
            scenicscore = getscore(matrix, element, x, y)
            if(scenicscore>highestscore):
                highestscore=scenicscore
    print(highestscore)

if __name__ == "__main__":
    file=open("D8/input.txt", 'r').read().strip()
    part1(file)
    part2(file)