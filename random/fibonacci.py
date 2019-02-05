import sys
import time


def fibonnaci(n):
    """ 0, 1, 1, 2, 3, 5, 8, ... """
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        last = fibonnaci(n - 1)
        return last + [sum(last[-2:])]


def fib_accumulator(n, acc=None):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        if acc:
            return acc + [sum(acc[-2:])]
        else:
            acc = fib_accumulator(n -1)
            return fib_accumulator(n, acc)


def main():
    input = int(sys.argv[1])
    print('Input: {}'.format(input))

    tic = time.clock()
    for _ in range(10000):
        result = fibonnaci(input)
    toc = time.clock()
    print('Elapsed: {}'.format(toc - tic))
    print(result)

    tic = time.clock()
    for _ in range(10000):
        result = fib_accumulator(input)
    toc = time.clock()
    print('Elapsed: {}'.format(toc - tic))
    print(result)


if __name__ == '__main__':
    main()
