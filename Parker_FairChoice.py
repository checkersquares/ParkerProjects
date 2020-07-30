# Thue-Morse sequence choice
def fairChoice(person1, person2, options):
    pattern = {}
    p1Choices = []
    p2Choices = []
    currentList = []
    currentPerson = ""
    for x in range(len(options)):
        b = bin(x).strip('0b')
        sum = 0
        for digit in str(b):
            sum += int(digit)
        if sum%2==0:
            currentPerson = person1
            currentList = p1Choices
        else:
            currentPerson = person2
            currentList = p2Choices
        
        pattern[x] = "A" if currentPerson == person1 else "B"

        print(currentPerson +"'s turn\nOptions:")
        while True:
            for option in options:
                print(str(options.index(option)+1) + " - " + str(option))
            try:
                inp = input(currentPerson +" select an option:\n")
                if inp in ["exit","end","stop"]:
                    return ["Canceled by User"],["Canceled by User"],{1,"Canceled by User"}
                choice = int(inp)
                if choice < len(options)+1 and choice > 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Error: Not a valid input")
                
        currentList.append(options[choice-1])
        options.remove(options[choice-1])
    return p1Choices, p2Choices, pattern

p1, p2, pattern = fairChoice("P1","P2", ["A","B","C","D","E","F"])

print("player 1:")
for x in p1:
    print(x)
print("player 2:")
for x in p2:
    print(x)

p = ""
for v in pattern.values():
    p += v
print(p)