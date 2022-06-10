import math


def printGrades(grades, subject):
    print(subject)
    for i in grades:
        print(i, end=" ")


def mean(grades):
    suma = sum(grades)
    return suma / float(len(grades))


def median(grades):
    grades.sort()
    if len(grades) % 2 == 0:
        half = int(len(grades) / 2)
        return float(sum(grades[half - 1:half + 1])) / 2.0
    else:
        return grades[int(len(grades) / 2)]


def variance(grades, mean):
    sigma = 0.0
    for grade in grades:
        sigma += (grade - mean) ** 2
    return sigma / len(grades)


def deviation(grades, mean):
    w = variance(grades, mean)
    return math.sqrt(w)