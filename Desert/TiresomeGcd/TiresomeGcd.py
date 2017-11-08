# https://codecombat.com/play/level/tiresome-gcd
# Calculate the secret number and get into the Treasury.
# Those two guys know keys for the password.
friends = hero.findFriends()
number1 = friends[0].secretNumber
number2 = friends[1].secretNumber
# Just to be sure that the first number is greater.
if number2 > number1:
    swap = number1
    number1 = number2
    number2 = swap

# It's simple but slow function to find gcd.
def bruteforceGCD (a, b):
    hero.say("The naive algorithm.")
    cycles = 0
    # We enumerate all possible divisors.
    counter = b
    while True:
        cycles += 1
        if cycles > 100:
            hero.say("Calculating is hard. I'm tired.")
            break
        # If both number have "counter" divisor.
        if a % counter == 0 and b % counter == 0:
            break
        counter -= 1
    hero.say("I used " + cycles + " cycles")
    return counter

# It's smart way to find gcd.
def euclidianGCD (a, b):
    cycles = 0
    while b:
        cycles += 1
        swap = b
        b = a % b
        a = swap
    hero.say("I used " + cycles + " cycles")
    return a

# Δ Maybe you need to use another function?
secretNumber = euclidianGCD(number1, number2)
hero.moveXY(48, 34)
hero.say(secretNumber)
# The treasury is open (I hope so)! Go there!
hero.moveXY(68, 34)
