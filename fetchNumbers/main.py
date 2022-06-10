from random import randint

howMany = int(input("How many numbers to draw "))
list = []
for i in range(0, howMany):
    list.append(randint(0, 100))
print(list)

print("Add element to the end of list")
for i in range(0, 3):
    number = int(input("Insert number: "))
    list.append(number)
print(list)

print("list contains ([index] value):")
for i, v in enumerate(list):
    print("[", i, "]", v)

print("Reverse list")
for e in reversed(list):
    print(e, end=" ")

print()
print("Sorted list")
for e in sorted(list):
    print(e, end=" ")

print()
e = int(input("Element to delete: "))
list.remove(e)
print(list)

print("Inserting element into list")
a, i = eval(input("insert value and index splitted with comma "))
list.insert(i, a)
print(list)

print("Search and count element in list")
e = int(input("Inser number: "))
print("number of appearances: ")
print(list.count(e))
print("Index of first appearance: ")
if list.count(e):
    print(list.index(e))
else:
    print("No elements in list")

print("Get last element: ")
print(list.pop())
print(list)

print("indexes from to:")
i, j = eval(input("Insert 'from' index and 'to' index splitted with comma "))
print(list[i:j])

print()
print("Tupla is unmutable list.")
print("Trying to mute tupla generates error: ")
tupla = tuple(list)
tupla[0] = 100