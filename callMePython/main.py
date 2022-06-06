acctualYear = int(input("What year is it? "))
name = input("Input your name: ")
age = int(input("Input your age: "))

pythonYear = 1989
pythonAge = acctualYear - pythonYear

result = "Call me Python, i am " + str(pythonAge) + ". Wlcome to my world " + name + ", You are "
if pythonAge > age:
    result += "younger"
else:
    result += "older"
result += " then me."

print(result)
