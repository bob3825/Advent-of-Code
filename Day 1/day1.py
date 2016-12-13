from enum import Enum


class Direction(Enum):
    up = 1
    down = 2
    right = 3
    left = 4

input = ['L3', 'R2', 'L5', 'R1', 'L1', 'L2', 'L2', 'R1', 'R5', 'R1', 'L1', 'L2', 'R2', 'R4', 'L4', 'L3', 'L3', 'R5',
         'L1', 'R3', 'L5', 'L2', 'R4', 'L5', 'R4', 'R2', 'L2', 'L1', 'R1', 'L3', 'L3', 'R2', 'R1', 'L4', 'L1', 'L1',
         'R4', 'R5', 'R1', 'L2', 'L1', 'R188', 'R4', 'L3', 'R54', 'L4', 'R4', 'R74', 'R2', 'L4', 'R185', 'R1', 'R3',
         'R5', 'L2', 'L3', 'R1', 'L1', 'L3', 'R3', 'R2', 'L3', 'L4', 'R1', 'L3', 'L5', 'L2', 'R2', 'L1', 'R2', 'R1',
         'L4', 'R5', 'R4', 'L5', 'L5', 'L4', 'R5', 'R4', 'L5', 'L3', 'R4', 'R1', 'L5', 'L4', 'L3', 'R5', 'L5', 'L2',
         'L4', 'R4', 'R4', 'R2', 'L1', 'L3', 'L2', 'R5', 'R4', 'L5', 'R1', 'R2', 'R5', 'L2', 'R4', 'R5', 'L2', 'L3',
         'R3', 'L4', 'R3', 'L2', 'R1', 'R4', 'L5', 'R1', 'L5', 'L3', 'R4', 'L2', 'L2', 'L5', 'L5', 'R5', 'R2', 'L5',
         'R1', 'L3', 'L2', 'L2', 'R3', 'L3', 'L4', 'R2', 'R3', 'L1', 'R2', 'L5', 'L3', 'R4', 'L4', 'R4', 'R3', 'L3',
         'R1', 'L3', 'R5', 'L5', 'R1', 'R5', 'R3', 'L1']


def main():
    curr_block = (0, 0)
    last_direction = Direction.up
    for move in input:
        if move[0:1] == 'L':
            curr_block, last_direction = move_left(curr_block, int(move[1:]), last_direction)
        elif move[0:1] == 'R':
            curr_block, last_direction = move_right(curr_block, int(move[1:]), last_direction)
        else:
            print 'Not Found'
    print 'The last position is ' + str(curr_block)
    print 'You are %d blocks away' % (abs(0-curr_block[0]) + abs(0-curr_block[1]))


def move_right(curr_block, num_of_blocks, last_direction):
    if last_direction == Direction.up:
        curr_block = (curr_block[0] + num_of_blocks, curr_block[1])
        last_direction = Direction.right
    elif last_direction == Direction.down:
        curr_block = (curr_block[0] - num_of_blocks, curr_block[1])
        last_direction = Direction.left
    elif last_direction == Direction.right:
        curr_block = (curr_block[0], curr_block[1] - num_of_blocks)
        last_direction = Direction.down
    elif last_direction == Direction.left:
        curr_block = (curr_block[0], curr_block[1] + num_of_blocks)
        last_direction = Direction.up
    else:
        print 'Not a valid direction'
        print 'Can\'t continue'
        exit(0)
    return curr_block, last_direction


def move_left(curr_block, num_of_blocks, last_direction):
    if last_direction == Direction.up:
        curr_block = (curr_block[0] - num_of_blocks, curr_block[1])
        last_direction = Direction.left
    elif last_direction == Direction.down:
        curr_block = (curr_block[0] + num_of_blocks, curr_block[1])
        last_direction = Direction.right
    elif last_direction == Direction.right:
        curr_block = (curr_block[0], curr_block[1] + num_of_blocks)
        last_direction = Direction.up
    elif last_direction == Direction.left:
        curr_block = (curr_block[0], curr_block[1] - num_of_blocks)
        last_direction = Direction.down
    else:
        print 'Not a valid direction'
        print 'Can\'t continue'
        exit(0)
    return curr_block, last_direction

if __name__ == '__main__':
    main()
