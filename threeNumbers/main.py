firstNumber, secondNumber, thirdNumber = input("insert three numbers split with space ").split(" ")

list = [firstNumber, secondNumber, thirdNumber]

smallestNumber = firstNumber

for i in range(len(list)):
    if smallestNumber > list[i]:
        smallestNumber = list[i]

print(smallestNumber)

