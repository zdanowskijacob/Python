import random;

list = []

for i in range(10):
    list.append(random.randint(1, 100))
print(list)
print()

print(list[1:4])
print(list[1:])
print(list[:4])
print(list[-2:])
print(list[-3])
