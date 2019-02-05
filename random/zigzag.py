def extract(arr):
    idx = 0
    dir = None
    start = arr[0]
    zz = [start]
    for val in arr[1:]:
        idx += 1
        if val > start:
            if dir is None or dir == 'down':
                dir = 'up'
            else:
                return zz, idx
        elif val < start:
            if dir is None or dir == 'up':
                dir = 'down'
            else:
                return zz, idx
        else:
            return zz, idx
        zz.append(val)
        start = val
    return zz, idx


def zigzag(arr):
    zzs = []
    idx = 0
    while True:
        zz, idx = extract(arr)
        zzs.append(zz)
        arr = arr[idx - 1:]
        if not arr or len(arr) == 2:
            break
    zzs = sorted(zzs, key=lambda x:len(x), reverse=True)
    print(zzs)
    return zzs[0]


def main():
    assert zigzag([1, 2, 3]) == [1, 2]
    assert zigzag([1, 2, -1, 7, 8]) == [1, 2, -1, 7]
    assert zigzag([1, 2, -1, -2, 1, 0, 1]) == [-1, -2, 1, 0, 1]


if __name__ == '__main__':
    main()
