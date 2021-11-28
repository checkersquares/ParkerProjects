#Miller-Rabin Prime test

def main():
    while True:
        run = True
        isPrime = False
        i = input("Enter your number:")
        number = int(i)
        run = preliminaryChecks(number)
        if run:
            witnesses = getWitnesses(number)
            isPrime = checkTestimony(number, witnesses)
            if isPrime:
                print("This is a Prime!")
            else:
                print("Not a prime...")
        
def preliminaryChecks(number):
    if number < 4:
        print("Yes that's prime... (and the developer thought of this edge case)")
        return False
    if number % 2 == 0:
        print("that's an even number, so no, not prime.")
        return False
    return True

def getWitnesses(number):
    witnesses = [2]
    if number >= 4:
        witnesses.append(3)
    if number >= 1373653:
        witnesses.append(5)
    if number >= 25326001:
        witnesses.append(7)
        witnesses.append(11)
    if number >= 2152302898747:
        witnesses.append(13)
        witnesses.append(17)
        witnesses.append(19)
        witnesses.append(23)
        witnesses.append(29)
        witnesses.append(31)
        witnesses.append(37)
    if number >= 318665857834031151167461:
        print("Your number is too big for the scope of this module")
        return []
    return witnesses

def getTestimony(number, witness):
    n = number - 1
    dval = n / 2
    rbn = witness ** int(dval)
    testimony = rbn % number
    if testimony == 1 or testimony == n:
        return True
    else:
        return False
    
def checkTestimony(number, witnesses):
    testimony = False
    for witness in witnesses:
        testimony = getTestimony(number, witness)
        if not testimony:
            break
    return testimony
            

main()