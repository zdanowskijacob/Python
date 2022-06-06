import math

data = input("insert the length of the sides of the triangle: ")

print(data)

list = []

for i in data.split(" "):
    list.append(int(i))
a, b, c = list

if a + b > c and a + c > b and b + c > a:
    print("Perimeter = ", (a + b + c))
    p = (a + b + c)/2
    field = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("field = ", field)
else:
    print("Cannot build triangle")
