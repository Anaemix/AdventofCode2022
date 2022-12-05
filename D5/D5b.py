file = open('D5/input.txt','r').read().split("\n\n")

def get_piles(data):
    rows = data.split('\n')
    chunks = []
    for row in rows:
        chunks.append([row[i:i+4].strip() for i in range(0, len(row), 4)])
    chunks = list(reversed(chunks))
    piles = {}
    for i in chunks[0]:
        piles[int(i)] = []
    for chunk in chunks[1:]:
        for i in range(len(chunk)):
            if(chunk[i]!=''):
                piles[i+1].append(chunk[i])
    return piles

def do_order(piles, order):
    order = [int(i.strip()) for i in order.replace('move ','').replace('from ','').replace('to ','').split(' ')]
    piles[order[2]] += piles[order[1]][len(piles[order[1]])-order[0]:]
    piles[order[1]] = piles[order[1]][:-order[0]]

    return piles

def message(piles):
    for i in piles:
        print(piles[i][-1:][0][1], end='')

orders = file[1].split("\n")
piles = get_piles(file[0])
for order in orders:
    piles = do_order(piles, order)
message(piles)
