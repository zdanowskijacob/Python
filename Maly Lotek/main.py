import random

number = random.randint(1, 10)

for i in range(3):
    print("turn number", i+1)
    response = input("insert number ")
    if number == int(response):
        print("Congratulations")
        break
    elif i == 2:
        print("The number was:", number)
    else:
        print("wrong number")
