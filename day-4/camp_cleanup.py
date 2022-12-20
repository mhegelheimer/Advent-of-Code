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


def is_between(low, high, v):
    return v >= low and v <= high


def is_outside(low, high, v):
    return v < low or v > high


def main():

    overlap_count = 0
    fully_contained_count = 0

    with open("input.txt") as rf:
        for line in rf.readlines():
            args = line.split(",")
            first_section, second_section = args[0], args[1].strip()

            # unpack and cast
            f0, f1, s0, s1 = *first_section.split("-"), *second_section.split("-")
            vals = list(map(lambda x: int(x), [f0, f1, s0, s1]))
            f0, f1, s0, s1 = vals

            # part 1 - check bounds (fully contains)
            if (is_lower_bound(vals, f0) and is_upper_bound(vals, f1)) or (
                is_lower_bound(vals, s0) and is_upper_bound(vals, s1)
            ):
                fully_contained_count += 1
                overlap_count += 1

            # part 2 - compute inclusive intersection
            elif (
                # s0 or s1 between f0-f1
                (is_between(f0, f1, s0) and is_outside(f0, f1, s1))
                or (is_between(f0, f1, s1) and is_outside(f0, f1, s0))
                # f0 or f1 between s0-s1
                or (is_between(s0, s1, f0) and is_outside(s0, s1, f1))
                or (is_between(s0, s1, f1) and is_outside(s0, s1, f0))
            ):
                overlap_count += 1

    return fully_contained_count, overlap_count


if __name__ == "__main__":
    contained, overlaps = main()
    print(
        f"There are {contained} assignment pairs where one range fully contains the other"
    )
    print(f"There are {overlaps} assignment pairs where the ranges overlap")
