''' PDB example '''


def inv(x):
    return 1.0 / x


def avg(items):
    res = 0.0
    for i in items:
        res = res + inv(i)
    return inv(res)


if __name__ == '__main__':
    import sys

    args = map(float, sys.argv[1:])
    res = avg(args)
    print(res)
