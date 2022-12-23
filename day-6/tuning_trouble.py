def main():
    # data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    # data = "nppdvjthqldpwncqszvftbrmjlhg"
    # data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    # data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    with open("input.txt") as fh:
        data = fh.readlines()[0].strip()

    marker = []
    for idx, c in enumerate(data):

        # escape case (also conveniently using next idx to cheat 1-indexed problem statement)
        if len(marker) == 4:
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
