from drawModule import settings, drawNumbers, getUserNumbers


def main(args):
    # ustawienia gry
    amountOfNumbers, maxNubmer, numberOfDraws = settings()

    # losujemy liczby
    numbers = drawNumbers(amountOfNumbers, maxNubmer)

    # pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
    for i in range(numberOfDraws):
        typy = getUserNumbers(amountOfNumbers, maxNubmer)
        hits = set(numbers) & typy
        if hits:
            print("\nIlość trafień: %s" % len(hits))
            print("Trafione liczby: %s" % hits)
        else:
            print("Brak trafień. Spróbuj jeszcze raz!")

        print("\n" + "x" * 40 + "\n")  # wydrukuj 40 znaków x

    print("Wylosowane liczby:", numbers)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))