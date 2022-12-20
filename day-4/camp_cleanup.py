TEST = """2-4, 6-8
2-3, 4-5
5-7, 7-9
2-8, 3-7
6-6, 4-6
2-6, 4-8"""


def is_lower_bound(l: list, v: int):
    return min(l) == v


def is_upper_bound(l: list, v: int):
    return max(l) == v


def main():

    fully_contained_count = 0
    with open("input.txt") as rf:
        for line in rf.readlines():
            args = line.split(",")
            first_section, second_section = args[0], args[1].strip()

            f0, f1, s0, s1 = *first_section.split("-"), *second_section.split("-")
            vals = list(map(lambda x: int(x), [f0, f1, s0, s1]))

            if (is_lower_bound(vals, int(f0)) and is_upper_bound(vals, int(f1))) or (
                is_lower_bound(vals, int(s0)) and is_upper_bound(vals, int(s1))
            ):
                fully_contained_count += 1

    return fully_contained_count


if __name__ == "__main__":
    count = main()
    print(
        f"There are {count} assignment pairs where one range fully contains the other"
    )
