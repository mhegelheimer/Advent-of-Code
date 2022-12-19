#!/user/bin/env python3


from functools import reduce
from pprint import pprint


SEP = "\n"


def main():
    
    max_elf = 1
    calorie_map = {}

    curr_elf = 1
    with open("input.txt") as rf:
        for line in rf.readlines():
            val = line.strip()

            # split out counts by elf
            if not val:
                curr_elf += 1
                continue

            # track calorie counts
            if curr_elf in calorie_map:
                calorie_map[curr_elf] += int(val)
            else:
                calorie_map[curr_elf] = int(val)
            
            # determine max
            if calorie_map[curr_elf] > calorie_map[max_elf]:
                max_elf = curr_elf

    return calorie_map, max_elf


if __name__ == "__main__":
    calories, max_elf = main()
    pprint(calories)
    print(f"elf {max_elf} held the most cals: {calories[max_elf]}")

    cals_list = [(elf, cals) for elf, cals in calories.items()]
    cals_list.sort(key=lambda v: v[1])

    top_three = cals_list[len(cals_list)-3:]
    _, top_three_cals = reduce(lambda x, y: (0, x[1] + y[1]), top_three)

    print(top_three)
    print(top_three_cals)
    