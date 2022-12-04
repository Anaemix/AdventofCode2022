with open('D3/input.txt', 'r') as file:
    lines = file.read().strip().split("\n")

def comp(inp):
    return inp[int(inp.__len__()/2):], inp[:int(inp.__len__()/2)]

def prio(item):
    return ord(item)-65+27 if ord(item)<92 else ord(item)-97+1

tot = 0
n = []
k = []
for z,line in enumerate(lines):
    if(z%3 == 0 and k != []):
        n.append(k)
        k = []
    k.append(line)
n.append(k)

for group in n:
    for ch in group[0]:
        if(ch in group[1] and ch in group[2]):
            tot += prio(ch)
            break
print(tot)
