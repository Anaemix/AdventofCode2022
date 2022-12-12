
class dir:
    name = ""
    def __init__(self, line):
        self.name = line.split(" ")[1]
        self.files = []
    def add_file(self, line):
        self.files.append(int(line.split(" ")[0]))

def part1(data):
    data = data.split("\n")[1:]
    dirs = {"/": dir("dir /")}
    dirstructure = "/"
    for i, line in enumerate(data):
        if(line == "$ ls"):
            try:
                while(not "$" in data[i+1]):
                    x = data.pop(i+1)
                    if("dir" in x):
                        dirs[dirstructure + x.split(" ")[1]+"/"] = dir(x)
                    else:
                        dirs[dirstructure].add_file(x)
            except:
                pass
        elif("cd" in line):
            if(line == "$ cd .."):
                dirstructure = "/".join(dirstructure.split("/")[:-2]) + "/"
            else:
                dirstructure = f"{dirstructure}{line.split(' ')[2]}/"
    total = 0
    for directories in dirs:
        subtotal = sum([sum(dirs[i].files) for i in dirs if directories in i])
        if subtotal<=100000:
            total += subtotal

    print(total)

def part2(data):
    data = data.split("\n")[1:]
    dirs = {"/": dir("dir /")}
    dirstructure = "/"
    for i, line in enumerate(data):
        if(line == "$ ls"):
            try:
                while(not "$" in data[i+1]):
                    x = data.pop(i+1)
                    if("dir" in x):
                        dirs[dirstructure + x.split(" ")[1]+"/"] = dir(x)
                    else:
                        dirs[dirstructure].add_file(x)
            except:
                pass
        elif("cd" in line):
            if(line == "$ cd .."):
                dirstructure = "/".join(dirstructure.split("/")[:-2]) + "/"
            else:
                dirstructure = f"{dirstructure}{line.split(' ')[2]}/"
    total = sum([sum(dirs[i].files) for i in dirs if "/" in i])
    closest = total
    for directories in dirs:
        subtotal = sum([sum(dirs[i].files) for i in dirs if directories in i])
        if(subtotal >= total-40000000 and subtotal<closest):
            closest = subtotal
    print("final subtotal:", closest, " = empty space:", total-closest)



if __name__ == "__main__":
    data = open("D7/input.txt",'r').read().strip()
    part1(data)
    part2(data)