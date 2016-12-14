in_file = open('input', 'r')


def main():
    valid = 0
    for line in in_file:
        valid += isValid(line)
    print valid


def isValid(line):
    x = int(line[2:6])
    y = int(line[7:11])
    z = int(line[12:16])
    return isTriangle(x, y, z)


def isTriangle(x, y, z):
    if x+y <= z:
        return 0
    if x+z <= y:
        return 0
    if y+z <= x:
        return 0
    return 1


if __name__ == "__main__":
    main()
