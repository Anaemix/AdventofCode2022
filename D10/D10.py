def update_x(X, cycle, add):
    cycle+=1
    calc=0
    if (cycle+20) % 40 == 0:
        print(f"cycle {cycle}:",X* cycle, X, cycle)
        calc=X* cycle
    X = X+add
    return X, cycle, calc

def update_screen(X, cycle, add):
    cycle+=1
    calc=0
    X = X+add
    if(cycle <6):
        #print(X, cycle)
        pass
    if(X+1 >= cycle%40 and X-1<= cycle%40):
        print("#", end="")
    else:
        print(".", end="")
    if (cycle) % 40 == 0:
        print("")
    return X, cycle, calc

def part1(file):
    file = file.split('\n')
    X=1
    cycle=0
    total=0
    for line in file:
        if line == "noop":
            X, cycle, calc = update_x(X, cycle, 0)
            total+=calc
        else:
            x=int(line.split(" ")[1])
            X, cycle, calc = update_x(X, cycle, 0)
            total+=calc
            X, cycle, calc = update_x(X, cycle, x)
            total+=calc
    print(total)

def part2(file):
    file = file.split('\n')
    X=1
    cycle=0
    total=0
    for line in file:
        if line == "noop":
            X, cycle, calc = update_screen(X, cycle, 0)
            total+=calc
        else:
            x=int(line.split(" ")[1])
            X, cycle, calc = update_screen(X, cycle, 0)
            total+=calc
            X, cycle, calc = update_screen(X, cycle, x)
            total+=calc


if __name__ == '__main__':
    file = open('D10/test.txt', 'r').read().strip()
    part1(file)
    part2(file)