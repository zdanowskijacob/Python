print("Alphabet: ")
x = 0
for i in range(65, 91):
    char = chr(i)
    x += 1
    tmp = char + " => " + char.lower()
    if i > 65 and x == 5:
        x = 0
        tmp += "\n"
    print(tmp, end=" ")

x = -1
print("\nReversed alphabet: ")
for i in range(122, 96, -1):
    char = chr(i)
    x += 1
    if x == 5:
        x = 0
        print("\n", end=" ")
    print(char.upper(), "=>", char, end=" ")