"""

Each tree represented by a single-digit value
0 - shortest
9 - tallest

A tree is visible if all the values between it and an edge are shorter than it
(only consider trees in the same row or column - up/down/left/right from any given tree)

All trees around the edge of the grid are visible (on the edge with no trees to block)

In the example below there are only 9 interior trees for consideration

30373
25512
65332
33549
35390

visibile (left/top), visible (top/right), not visible 
top-left (5), top-middle (5), top-right (1)

visibile (right), invisible, visible (right)
left-middle (5), center (3), right-middle (3)

not visibile, visible, not visible
bottom-left (3), bottom-center (5), bottom-right(4)


 16 trees visible on edge
+ 5 trees visible in the interior
---
 21 trees visible in this arrangement 

"""

TEST = """30373
25512
65332
33549
35390
"""


def main():

    # 99x99 grid
    with open("input.txt") as rf:
        # data = rf.readlines()
        data = TEST.strip().splitlines()

    # load in grid like this:
    #
    #         |  |  |
    #         v  v  v
    #    [[3, 0, 3, 7, 3],
    # --> [2, 5, 5, 1, 2], <--
    # --> [6, 5, 3, 3, 2], <--
    # --> [3, 3, 5, 4, 9], <--
    #     [3, 5, 3, 9, 0]]
    #         ^  ^  ^
    #         |  |  |
    #
    # Initialize a results tracking array (same size multi-dim array as input)
    #  - starts at 0s
    #
    # For each internal column/row:
    #   - split at midpoint and calculate is_visible forwards and backwards
    #   - if a tree is ever visible from the outside update result array tree idx: True
    #
    # remember: once a bigger number exists on a given line (vertical/horizontal),
    # we can cross that off as a possibilitiy for the interior nodes
    #


if __name__ == "__main__":
    main()
