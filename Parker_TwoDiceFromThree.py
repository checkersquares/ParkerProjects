# turn a throw of 3 six sided dice into a fair result of 2 dice
def getTwoDiceFromThree(dice1, dice2, dice3):
    max = 6
    # fill dice list with absolute values, trim to max and sort by size
    dice = [
        abs(dice1 - 1 % max) + 1,
        abs(dice2 - 1 % max) + 1,
        abs(dice3 - 1 % max) + 1,
    ]
    dice.sort()
    # case 1.1: all dice are consecutive
    if areConsecutiveDice(dice):
        # the "middle" dice is always the only dice as even or odd as the sum of all 3
        odd = sum(dice) % 2
        for x in dice:
            if x % 2 == odd:
                return x, x
    # case 1.2: 2 dice are consecutive
    if areConsecutiveDice([dice[0], dice[1]]):
        if (dice[1] + 1) % max + 1 == dice[2]:
            return dice[1], dice[2]
        else:
            return dice[0], dice[1]
    elif areConsecutiveDice([dice[1], dice[2]]):
        if (dice[2] + 1) % max + 1 == dice[0]:
            return dice[0], dice[2]
        else:
            return dice[1], dice[2]
    elif areConsecutiveDice([dice[2], dice[0]]):
        if (dice[0] + 1) % max + 1 == dice[1]:
            return dice[0], dice[1]
        else:
            return dice[0], dice[2]
    # case 2: equilateral triangle
    if dice[0] + 2 == dice[1] and dice[1] + 2 == dice[2]:
        return dice[0], (dice[0] + round(max / 2))
    # case 3.1: all dice are the same
    if dice[0] == dice[1] and dice[0] == dice[2]:
        return (
            round(max / 2),
            max,
        )  # 3,6 normally. Written like this in case I want to expand the method
    # case 3.2: 2 dice are the same
    if dice[0] == dice[1] or dice[1] == dice[2]:
        if dice[0] == dice[1]:
            return dice[0], dice[2]
        else:
            return dice[0], dice[1]
    # if there's something wrong, return 0,0 - this should be unreachable
    return 0, 0


def areConsecutiveDice(numbers):
    return areConsecutive(numbers, True, 1, 6)


# takes a range of numbers and checks if they are consecutive
# if "canwrap=True" then min/max count as consecutive
def areConsecutive(numbers, canwrap=False, min=0, max=0):
    nbrs = numbers.copy()
    nbrs.sort()
    # max and min are only important if numberchain can wrap, so this is evaluated here
    if canwrap and len(nbrs) > (max - min + 1):
        return False
    wraps = canwrap and nbrs[0] == min and nbrs[len(nbrs) - 1] == max
    # run 1 or 2 loops, depending on if chain is evalated to wrap
    runs = 1 + int(wraps)
    for _ in range(runs):
        while len(nbrs) > 1:
            if nbrs[0] + 1 == nbrs[1]:
                nbrs.remove(nbrs[0])
            else:
                nbrs.remove(nbrs[0])
                break
        else:
            nbrs.remove(nbrs[0])
    if len(nbrs) < 1:
        return True
    else:
        return False


def asPercentage(number, total, decimal=2, oneBased = False):
    perc = number/total if oneBased else number/total*100
    perc = round(perc * (10 * decimal)) / (10 * decimal)
    return perc

def runRolls(runs):
    import random
    random.seed()
    rolls = {}
    diceTotals = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    rollTotals = {}
    for x in range(runs):
        dice = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        roll = getTwoDiceFromThree(dice[0], dice[1], dice[2])

        rolls[x+1] = roll

        if rollTotals.get(str(roll)) == None:
            rollTotals[str(roll)] = 0
        rollTotals[str(roll)] = rollTotals[str(roll)] + 1

        diceTotals[roll[0]] = diceTotals[roll[0]] + 1
        diceTotals[roll[1]] = diceTotals[roll[1]] + 1

    return rolls, rollTotals, diceTotals

def graphRolls(data, title, description):
    import matplotlib.pyplot as plt

    runs = sum(data.values())

    li = {k: v for k,v in sorted(data.items(), key=lambda item: item[0])}
    labels = li.keys()
    x = li.values()
    width = 0.9

    w = len(li) * 0.7
    h = 5
    _, ax = plt.subplots(figsize=(w,h))
    plt.subplots_adjust(left=1/(len(li)+1),bottom=(0.5/h),right=0.98,top=0.98)
    fig = plt.gcf()
    fig.canvas.set_window_title(title)
    
    ax.bar(labels, x, width)
    ax.set_ylabel(description + " out of " + str(runs))
    ax.set_xlabel(description)

    plt.show()

data = runRolls(10000)
graphRolls(data[1], "Dice rolls", "Rolls")