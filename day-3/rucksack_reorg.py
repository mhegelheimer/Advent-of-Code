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
            prioritized.append((val, ord(val) - 96))
        else:
            prioritized.append((val, ord(val) - 38))
    return prioritized


def chunks_of_three(l):
    return ([v.strip() for v in l[pos : pos + 3]] for pos in range(0, len(l), 3))


def main():

    # determine shared value in each rucksack
    items = []
    with open("input.txt") as rf:
        for chunk in chunks_of_three(rf.readlines()):
            shared = set()
            for char in chunk[0]:
                if char in chunk[1] and char in chunk[2]:
                    shared.add(char)

            items.extend(list(shared))

        # -- commented out remanants of p1 of the problem --
        # for line in chunk:
        #     s = line.strip()
        #     first_compartment, second_compartment = s[:len(s)//2], s[len(s)//2:]

        #     shared = set()
        #     for chr in first_compartment:
        #         if chr in second_compartment:
        #             shared.add(chr)

        #     items.extend(list(shared))

    prioritized = determine_priority(items)
    return sum(map(lambda v: v[1], prioritized))


if __name__ == "__main__":
    total = main()
    print(
        f"{total} is the prioritized sum of duplicate rucksack items (in both compartments)"
    )
