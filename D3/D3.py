with open('D3/input.txt', 'r') as file:
    lines = file.read().strip().split("\n")

def comp(inp):
    return inp[int(inp.__len__()/2):], inp[:int(inp.__len__()/2)]

def prio(item):
    return ord(item)-65+27 if ord(item)<92 else ord(item)-97+1

tot = 0
for z,line in enumerate(lines):
    q = 0
    i1,i2 = comp(line)
    for i in i1:
        if(i in i2):
            tot += prio(i)
            q +=1
            break
print(tot)