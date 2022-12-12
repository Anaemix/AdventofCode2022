from ast import operator


def get_monkies(file):
    monkeys = [i.split("\n") for i in file.split("\n\n")]
    monkeysdict = {}
    for monkey in monkeys:    
        num = int(monkey[0].replace(":", "").split(" ")[1])
        items = [int(item) for item in monkey[1].replace("  Starting items: ", "").split(", ")]
        operation = monkey[2].replace("  Operation: new = old ", "").split(" ")
        test = int(monkey[3].replace("  Test: divisible by ", ""))
        t = int(monkey[4].replace("    If true: throw to monkey ", ""))
        f = int(monkey[5].replace("    If false: throw to monkey ", ""))
        monkeysdict[num] = {'items': items, 'op': operation, 'test': test, 'true': t, 'false': f, 'inspected': 0}
    return monkeysdict

def get_LCD(inputs):
    tot = 1
    for i in inputs:
        tot*=i
    return tot

def part1(file):
    monkeys = get_monkies(file)
    for _ in range(20):
        for monkey in monkeys:
            for item in monkeys[monkey]['items']:
                monkeys[monkey]['inspected'] += 1
                if monkeys[monkey]['op'][0] == "*":
                    worry = item * item if not monkeys[monkey]['op'][1].isnumeric() else item * int(monkeys[monkey]['op'][1])
                else:
                    worry =  item + item if not monkeys[monkey]['op'][1].isnumeric() else item + int(monkeys[monkey]['op'][1])
                worry = int(worry/3)
                if(worry % monkeys[monkey]["test"] == 0):
                    monkeys[monkeys[monkey]["true"]]['items'].append(worry)
                else:
                    monkeys[monkeys[monkey]["false"]]['items'].append(worry)
            monkeys[monkey]['items'] = []
    tot = 1
    insp = [monkeys[m]['inspected'] for m in monkeys]
    insp.sort(reverse=True)
    print(insp[0] *insp[1])


def part2(file):
    monkeys = get_monkies(file)
    lcd = get_LCD([monkeys[m]['test'] for m in monkeys])
    print(lcd)
    for u in range(10000):
        for monkey in monkeys:
            for item in monkeys[monkey]['items']:
                monkeys[monkey]['inspected'] += 1
                if monkeys[monkey]['op'][0] == "*":
                    worry = item * item if not monkeys[monkey]['op'][1].isnumeric() else item * int(monkeys[monkey]['op'][1])
                else:
                    worry =  item + item if not monkeys[monkey]['op'][1].isnumeric() else item + int(monkeys[monkey]['op'][1])
                worry = worry%lcd
                if(worry % monkeys[monkey]["test"] == 0):
                    monkeys[monkeys[monkey]["true"]]['items'].append(worry)
                else:
                    monkeys[monkeys[monkey]["false"]]['items'].append(worry)
                
            monkeys[monkey]['items'] = []
    insp = [monkeys[m]['inspected'] for m in monkeys]
    insp.sort(reverse=True)

    print(insp, insp[0] *insp[1])

if __name__ == '__main__':
    file = open('D11/input.txt', 'r').read().strip()
    #part1(file)
    part2(file)