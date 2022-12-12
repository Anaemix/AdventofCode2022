def unique(last4):
    return True if (len(set(last4)) == len(last4)) else False

def Day6(data, num):
    data = open('D6/input.txt', 'r').read().strip()
    span = [i for i in data[:num]]
    i = num
    data = data[num:]
    for char in data:
        if(unique(span)):
            break
        i+=1
        span.pop(0)
        span.append(char)
    return i
def part1(data):
    print(Day6(data,4))
def part2(data): 
    print(Day6(data,14))


data = open('D6/input.txt', 'r').read().strip()
part1(data)
part2(data)