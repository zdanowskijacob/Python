def fib_iter1(n):
    expressions = (1, 1)
    a, b = expressions
    print(a, end=" ")
    while n > 1:
        print(b, end=" ")
        a, b = b, a + b
        n -= 1


def fib_iter2(n):
    a, b = 1, 1
    print("expression", 1, a)
    print("expression", 2, b)
    for i in range(1, n - 1):
        a, b = b, a + b
        print("expression", i + 2, b)

    print()
    return b


def fib_rec(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def main(args):
    n = int(input("insert expression number "))
    fib_iter1(n)
    print()
    print("=" * 40)
    fib_iter2(n)
    print("=" * 40)
    print(fib_rec(n - 1))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))