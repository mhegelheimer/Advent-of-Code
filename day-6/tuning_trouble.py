def main():
    # part 1 examples
    # data = "bvwbjplbgvbhsrlpgdmjqwftvncz"         # p1: 5, p2: 23
    # data = "nppdvjthqldpwncqszvftbrmjlhg"         # p1: 6, p2: 23
    # data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"    # p1: 10, p2: 29
    # data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"     # p1: 11, p2: 26
    # data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"       # p2: 19

    with open("input.txt") as fh:
        data = fh.readlines()[0].strip()

    marker = []
    for idx, c in enumerate(data):

        # escape case (also conveniently using next idx to cheat 1-indexed problem statement)
        # if len(marker) == 4:
        if len(marker) == 14:
            return marker, idx

        if c in marker:
            while c in marker:
                marker = marker[1:]
            marker.append(c)
            continue

        else:
            marker.append(c)


if __name__ == "__main__":
    marker, idx = main()
    print(f"Index of end of 4 unique chars ({marker}) is {idx}")
