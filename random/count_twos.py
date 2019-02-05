
def string_count(n):
    return sum(str(i).count('2') for i in range(1, n + 1))


def twos_count(n):  # e.g. 323
    sum = 0

    ones = n % 10  # e.g. 3
    remainder = math.floor(n / 10)
    if ones >= 2:
        sum += 1



def main():
    for num in (11, 22, 172, 333333, 222222222222222222222):
        print('{}: {}'.format(num, string_count(num)))



if __name__ == '__main__':
    main()
