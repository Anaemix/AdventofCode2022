with open('D1\input.txt', 'r') as file:
    elves = [sum([int(cal) for cal in elf.split("\n")]) for elf in file.read().split("\n\n")]
print(elves[elves.index(max(elves))])