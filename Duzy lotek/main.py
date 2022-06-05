import random

amountOfNumbers = int(input("How many numbers want you to draw "))
maxNumber = int(input("insert max number we can draw "))

print("draw %s numbers and the max number is %s" % (amountOfNumbers, maxNumber))

drawnNumbers = []
givenNumbers = []

i = 0
while i < amountOfNumbers:
    number = random.randint(1, maxNumber)
    if drawnNumbers.count(number) == 0:
        drawnNumbers.append(number)
        i = i + 1

print("input your numbers")

userNumbers = set()
i = 0

while i < amountOfNumbers:
    userNumber = int(input("insert %d number " % (i + 1)))
    if userNumber not in userNumbers:
        userNumbers.add(userNumber)
        i = i + 1

hit = set(drawnNumbers) & userNumbers
if hit:
    print("htis: %s" % len(hit))
    print("correct numbers ", hit)
else:
    print("There's ain't correct numbers")

