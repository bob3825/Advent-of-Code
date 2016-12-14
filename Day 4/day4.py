from collections import Counter

in_file = open('input', 'r')


def main():
    sum = 0
    for line in in_file:
        splits = line.split('-')
        checksum = splits[-1][-7:-2]
        sector_id = splits[-1][:-8]
        del splits[-1]
        letters = ''.join(splits)
        sum += isRoom(letters, checksum, sector_id)
    print sum


def isRoom(letters, checksum, sector_id):
    most = Counter(letters)
    highest = ''
    ones = ''
    print most
    for elem in most.keys():
        if most.get(elem) == 1:
            ones += elem
        else:
            highest += elem
    print highest
    print ones
    print ' '
    return 0





    for letter in letters:
        if letter in most.keys():
            most[letter] += 1
        else:
            most[letter] = 1

    print Counter(letters)


    new_sorted = ''
    new_sorted_ones = ''
    new_sorted_list = []
    new_sorted_ones_list = []
    for key, value in sorted(most.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        if value == 1:
            new_sorted_ones_list.append((key, value))
            new_sorted_ones += key
        else:
            new_sorted_list.append((key, value))
            new_sorted += key

    print new_sorted_list
    print new_sorted
    print new_sorted_ones_list
    print new_sorted_ones
    print checksum
    print sector_id
    print checksum[:len(new_sorted)]
    if len(new_sorted) > 0 and new_sorted == checksum[:len(new_sorted)]:
        return int(sector_id)
    return 0


if __name__ == "__main__":
    main()
