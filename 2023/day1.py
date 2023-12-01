SAMPLE = """1abc2
pqr3stu8vwx
a1b2c3d4e5
treb7uchet"""

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def part1():
    total = 0
    # for line in SAMPLE.splitlines():
    with open(os.path.join(__location__,'data.txt'), 'r') as rf:
        for line in rf.readlines():
            # increment a pointer from each direction until they both find an integer
            # create a two-digit number by combining each digit (cheat using string concat)

            lptr, rptr = 0, len(line) - 1
            while not line[lptr].isdigit():
                lptr += 1
            while not line[rptr].isdigit():
                rptr -= 1
            
            total += int(f"{line[lptr]}{line[rptr]}")
    
    print(f"Total: {total}")


PUZZLE2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

INT_STR_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
INT_STRS = list(INT_STR_MAP.keys())

def is_intstring(string):
    return string in INT_STRS

def is_intstring_substring(string):
    for key in INT_STR_MAP:
        if string in key:
            return True
    return False


def part2():
    total = 0
    with open(os.path.join(__location__,'data.txt'), 'r') as rf:

        # Similar but two pointers from both directions
        for line in rf.readlines():

            ll, lr = 0, 0
            while not (ll == lr and line[ll].isdigit()):
                lr += 1

                if is_intstring(line[ll: lr]):
                    break

                while not is_intstring_substring(line[ll: lr]) and ll < lr:
                    ll += 1

                if line[lr].isdigit():
                    ll = lr
                    break

                # if both pointers are at the end of the string, and the last character is a digit
                if ll == lr and ll == len(line):
                    ll -= 1
                    lr -= 1

            rr, rl = len(line) - 1, len(line) - 1
            while not (rr == rl and line[rr].isdigit()) and not is_intstring(line[rl: rr + 1]):
                rl -= 1
                if line[rl].isdigit():
                    rr = rl
                    break
                while not is_intstring_substring(line[rl: rr + 1]) and rr > rl:
                    rr -= 1

            lval = INT_STR_MAP[line[ll: lr]] if lr != ll else line[ll]
            rval = INT_STR_MAP[line[rl: rr + 1]] if rl != rr else line[rl]

            # print(f"String: {line}, Value: {lval}{rval}")
            total += int(f"{lval}{rval}")
        
    print(f"Total: {total}")


if __name__ == "__main__":
    part1()
    part2()
