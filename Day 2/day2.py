

in_file = open('input', 'r')

up = {
    "1": "X",
    "2": "X",
    "3": "X",
    "4": "1",
    "5": "2",
    "6": "3",
    "7": "4",
    "8": "5",
    "9": "6",
}

down = {
    "1": "4",
    "2": "5",
    "3": "6",
    "4": "7",
    "5": "8",
    "6": "9",
    "7": "X",
    "8": "X",
    "9": "X",
}

left = {
    "1": "X",
    "2": "1",
    "3": "2",
    "4": "X",
    "5": "4",
    "6": "5",
    "7": "X",
    "8": "7",
    "9": "8",
}

right = {
    "1": "2",
    "2": "3",
    "3": "X",
    "4": "5",
    "5": "6",
    "6": "X",
    "7": "8",
    "8": "9",
    "9": "X",
}


def main():
    curr = '5'
    for line in in_file:
        print 'here'
        curr += getNext(curr[-1], line)
    print curr


def getNext(curr, line):
    for direction in list(line):
        if direction == 'U':
            next = up.get(curr)
            if next != 'X':
                curr = next
        elif direction == 'D':
            next = down.get(curr)
            if next != 'X':
                curr = next
        elif direction == 'L':
            next = left.get(curr)
            if next != 'X':
                curr = next
        elif direction == 'R':
            next = right.get(curr)
            if next != 'X':
                curr = next
    return curr

if __name__ == "__main__":
    main()
