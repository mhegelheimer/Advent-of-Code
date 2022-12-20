"""

"""

def determine_priority(shared: list[str]) -> list[tuple]:
    """
    ord("A") = 65
    ord("Z") = 90
    ord("a") = 97
    ord("z") = 122
    """
    prioritized = []
    for val in shared:
        if val.islower():
            prioritized.append((val, ord(val)-96))
        else:
            prioritized.append((val, ord(val)-38))
    return prioritized


def main():

    # determine shared value in each rucksack
    items = []
    with open("input.txt") as rf:
        for line in rf.readlines():
            s = line.strip()
            first_compartment, second_compartment = s[:len(s)//2], s[len(s)//2:]

            shared = set() 
            for chr in first_compartment:
                if chr in second_compartment:
                    shared.add(chr)

            items.extend(list(shared))

    # prioritize
    prioritized = determine_priority(items)
    return sum(map(lambda v: v[1], prioritized))


if __name__ == "__main__":
    total = main()
    print(f"{total} is the prioritized sum of duplicate rucksack items (in both compartments)")