TEST = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


# debug helper
def sprint(stacks):
    for s in stacks:
        print(s)


def chunks_of_four(l):
    return ([v.strip() for v in l[pos : pos + 4]] for pos in range(0, len(l), 4))


def main():

    """
    TEST (see above) intiial stack state
    [
        1  [[Z], [N]]
        2  [[M], [C], [D]]
        3  [[P]]
    ]
    """
    stacks = []

    # parse fist part, create stack state, leave a pointer to where we left off
    with open("input.txt") as rf:
        data = rf.readlines()
        # data = TEST.split("\n")

    end_idx = 0
    for idx, line in enumerate(data):

        # initialize stacks
        if idx == 0:
            stacks.extend([[] for _ in range(len(line) // 3)])

        # verify stack count
        if "1" in line:
            end_idx = idx
            break

        # parse through each line in chunks of 3
        for idx, chars in enumerate(chunks_of_four(line)):
            if char := list(filter(lambda x: x.isalpha(), chars)):
                assert len(char) == 1
                stacks[idx].append(char[0])

    [l.reverse() for l in stacks]
    sprint(stacks)

    # do some movements!
    for line in data[end_idx + 2 :]:

        # parse instruction
        # example: "move 1 from 2 to 1"
        chars = line.strip().split(" ")
        mv_count, init_loc, end_loc = int(chars[1]), int(chars[3]), int(chars[5])

        # update `stacks` state
        for _ in range(mv_count):
            stacks[end_loc - 1].append(stacks[init_loc - 1].pop())

        sprint(stacks)

    # top of stacks
    return list(map(lambda s: s[-1], filter(lambda x: x, stacks)))
    # return [s[-1] for s in stacks]


if __name__ == "__main__":
    top_items = main()
    print(f"The top items in each stack are: {top_items}")
    print(f"Condensed: {''.join(top_items)}")
