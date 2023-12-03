import os
from collections import defaultdict


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

DEBUG = True
def dprint(s):
    if DEBUG:
        print(s)


def is_symbol(s: str):
    return not s.isdigit() and not s == "."


def is_symbol_adjacent(line_lptr, line_rptr, line_idx, data):
    """
    Actual Integer String == data[line_idx][line_lptr: line_rptr+1]

    Process:
        1. Check left and right chars (if they exist)
        1. Check line above and below (if they exists) with additional 1 char buffer on each side 
    """

    # determine lateral bounds to check
    line_len = len(data[line_idx])
    lbound = line_lptr-1 if (line_lptr > 0) else line_lptr
    rbound = line_rptr+1 if (line_rptr < (line_len-1)) else line_rptr
    
    # determine vertical bounds to check
    check_prev_line = True if (line_idx > 0) else False
    check_next_line = True if (line_idx < len(data) - 1) else False

    # actually perform checks 
    if lbound != line_lptr and is_symbol(data[line_idx][lbound]):
        return True

    if rbound != line_rptr and is_symbol(data[line_idx][rbound]):
        return True
    
    if check_prev_line:
        for i in data[line_idx-1][lbound: rbound+1]:
            if is_symbol(i):
                return True

    if check_next_line:
        for i in data[line_idx+1][lbound: rbound+1]:
            if is_symbol(i):
                return True

    return False



def part1():

    total = 0
    # data = SAMPLE.splitlines()
    with open(os.path.join(__location__,'data.txt'), 'r') as rf:
        data = [l.strip() for l in rf.readlines()]
    # dprint(data)

    for idx, line in enumerate(data):
        lptr, rptr = 0, 0
        while rptr < (len(line) - 1):

            if line[rptr].isdigit():
                while rptr < (len(line) - 1) and line[rptr + 1].isdigit():
                    rptr += 1

                # dprint(line[lptr: rptr + 1])
                if is_symbol_adjacent(lptr, rptr, idx, data):
                    total += int(line[lptr: rptr+1])

            rptr += 1
            lptr = rptr


    print(f"Total: {total}")


def is_symbol_adjacent_v2(line_lptr, line_rptr, line_idx, data):
    # determine lateral bounds to check
    line_len = len(data[line_idx])
    lbound = line_lptr-1 if (line_lptr > 0) else line_lptr
    rbound = line_rptr+1 if (line_rptr < (line_len-1)) else line_rptr
    
    # determine vertical bounds to check
    check_prev_line = True if (line_idx > 0) else False
    check_next_line = True if (line_idx < len(data) - 1) else False

    # actually perform checks 
    if lbound != line_lptr and is_symbol(data[line_idx][lbound]):
        return True, line_idx, lbound

    if rbound != line_rptr and is_symbol(data[line_idx][rbound]):
        return True, line_idx, rbound
    
    if check_prev_line:
        for idx, i in enumerate(data[line_idx-1][lbound: rbound+1]):
            if is_symbol(i):
                return True, line_idx-1, lbound + idx

    if check_next_line:
        for idx, i in enumerate(data[line_idx+1][lbound: rbound+1]):
            if is_symbol(i):
                return True, line_idx+1, lbound + idx

    return (False, False, False) 



def part2():

    total = 0
    gear_nums_map = defaultdict(list)
    # data = [l.strip() for l in SAMPLE.splitlines()]
    with open(os.path.join(__location__,'data.txt'), 'r') as rf:
        data = [l.strip() for l in rf.readlines()]
    # dprint(data)

    for idx, line in enumerate(data):
        lptr, rptr = 0, 0
        while rptr < (len(line) - 1):

            if line[rptr].isdigit():
                while rptr < (len(line) - 1) and line[rptr + 1].isdigit():
                    rptr += 1

                dprint(line[lptr: rptr + 1])
                
                res, line_idx, char_idx = is_symbol_adjacent_v2(lptr, rptr, idx, data)
                if res and data[line_idx][char_idx] == "*":
                    gear_nums_map[(line_idx, char_idx)].append(
                        line[lptr: rptr+1]
                    )

            rptr += 1
            lptr = rptr

    for vals in gear_nums_map.values():
        if len(vals) == 2:
            total += int(vals[0]) * int(vals[1])

    dprint(f"Gear Map: {gear_nums_map}")
    print(f"Total: {total}")


part1()
part2()