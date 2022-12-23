"""

Parse filesystem output into a tree-like structure?

Commands (all start with '$' in input file and are mostly consistent with *nix systems.
    - `cd x` --> moves in one level to directory `x`
    - `cd ..` --> moves out one level to parent directory of current directory
    - `cd /` --> moves to outermost (top level) directory
    - `ls`
            `123 abc` --> file name: abc, file size: 123 
            `dir xyz` --> current directory contains sub directory `xyz`

Solution:
    1. Parse all content of input file into directory tree
                    (/)
           /    |       |        \
        a     b.txt    c.dat      d
     / | | \                 /  |   |   \ 
    e  f g  h               j d.log d.ext k
   /
  i    

    Use 'Dir' and 'File' Node Types 

    2. Calculate the size of all directories (total and with sub-directories re-counted, per the example)
"""
from dataclasses import dataclass, field

# from enum import Enum
from typing import Any


TEST = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


@dataclass(frozen=True)
class NODE_TYPE:
    FILE = "File"
    DIR = "Directory"


NodeType = NODE_TYPE()


@dataclass()
class Node:
    name: str  #
    ntype: NodeType  #
    size: int = None  #
    parent: Any = None  #
    children: dict = field(default_factory=lambda: {})
    # is_root: bool = False   #

    def add_child(self, dnode):
        assert isinstance(Node, dnode)
        self.children[dnode.name] = dnode

    def get_child(self, dname):
        return self.children.get(dname)

    def get_children(self):
        return self.children


def main():

    # mmmm yummy input data
    with open("input.txt") as rf:
        data = TEST.splitlines()
        # data = [l.strip().split(" ") for l in rf.readlines()]

    # input is guaranteed to start at top-level directory so we initialized
    # a base node outside of the loop to fill data in from
    base_dir = Node(name="/", ntype=NodeType.TOP)

    # current working directory
    curr_dir = None

    # parsing through via pointer (enables consuming output of `ls`
    # immediately,for example, instead of tracking previous cmd.
    curr_line, last_line = 0, len(data)
    while curr_line <= last_line:

        cmd = data[1]
        if cmd == "cd":
            tdir = data[2]

            # move to top-level dir
            if tdir == "/":
                pass

            # move to parent dir
            elif tdir == "..":
                pass

            # check if target directory (`tdir`) exists, else create
            else:
                pass

        elif cmd == "ls":
            # increment pointer until next command ("$" token)
            while (line := data[curr_line]) and not line.startswith("$"):

                # for each line, verify dir/file exists otherwsie
                # create node to represent
                # "dir <name>"" or "size:<int>, name:<str>"

                # increment
                curr_line += 1

        else:
            raise Exception("not great")

    return base_dir


if __name__ == "__main__":
    main()
