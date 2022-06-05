import random


def settings():
    """Funkcja pobiera ilość losowanych liczb, maksymalną losowaną wartość
    oraz ilość prób. Pozwala określić stopień trudności gry."""
    while True:
        try:
            amountOfNumbers = int(input("Podaj ilość typowanych liczb: "))
            maxNumber = int(input("Podaj maksymalną losowaną liczbę: "))
            if amountOfNumbers > maxNumber:
                print("Błędne dane!")
                continue
            numberOfDraws = int(input("Ile losowań: "))
            return (amountOfNumbers, maxNumber, numberOfDraws)
        except ValueError:
            print("Błędne dane!")
            continue


def drawNumbers(amountOfNumbers, maxNumber):
    """Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks"""
    numbers = []
    i = 0
    while i < amountOfNumbers:
        number = random.randint(1, maxNumber)
        if numbers.count(number) == 0:
            numbers.append(number)
            i = i + 1
    return numbers


def getUserNumbers(amountOfNumbers, maxNumber):
    """Funkcja pobiera od użytkownika jego typy wylosowanych liczb"""
    print("Wytypuj %s z %s liczb: " % (amountOfNumbers, maxNumber))
    userNumbers = set()
    i = 0
    while i < amountOfNumbers:
        try:
            userNumber = int(input("Podaj liczbę %s: " % (i + 1)))
        except ValueError:
            print("Błędne dane!")
            continue

        if 0 < userNumber <= maxNumber and userNumber not in userNumbers:
            userNumbers.add(userNumber)
            i = i + 1
    return userNumbers