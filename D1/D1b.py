with open('D1\input.txt', 'r') as file:
    elves = [sum([int(cal) for cal in elf.split("\n")]) for elf in file.read().split("\n\n")]
top3 = []
for i in range(3):
    top3.append(elves.pop(elves.index(max(elves))))
print(sum(top3))