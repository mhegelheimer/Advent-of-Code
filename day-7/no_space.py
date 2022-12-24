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
    size: int = 0  #
    parent: Any = None  #
    children: dict = field(default_factory=lambda: {})
    # is_root: bool = False   #

    def __post_init__(self):
        if self.size:
            _node, _child, _child_size = self, self.name, self.size
            while _node.parent:
                print(
                    f"Incrementing Node `{_node.parent.name}` size += {_child_size} (from child {_child})"
                )
                _node.parent.size += _child_size
                print(f"Node {_node.parent.name} size: {_node.parent.size}")
                _node = _node.parent

    def add_child(self, dnode):
        assert isinstance(dnode, Node)
        self.children[dnode.name] = dnode

    def get_child(self, dname):
        return self.children.get(dname)

    def get_children(self):
        return self.children


def main():

    # mmmm yummy input data
    with open("input.txt") as rf:
        data = rf.readlines()
        # data = TEST.splitlines()
        data = [l.strip().split(" ") for l in data]

    # input is guaranteed to start at top-level directory so
    # initialized a base node outside of the loop to start with
    base_dir = Node(name="/", ntype=NodeType.DIR)

    # current working directory
    curr_dir = None

    curr_line, last_line = 0, len(data)
    while curr_line < last_line:

        if (cmd := data[curr_line][1]) and cmd == "cd":
            tdir = data[curr_line][2]

            if tdir == "/":
                curr_dir = base_dir
            elif tdir == "..":
                curr_dir = curr_dir.parent
            else:
                if target := curr_dir.get_child(tdir):
                    curr_dir = target
            curr_line += 1

        elif cmd == "ls":

            if (line := data[curr_line]) and line[0] == "$":
                curr_line += 1

            # parse `ls` output until next command ("$" token)
            while (curr_line < last_line) and data[curr_line][0] != "$":

                # for each line, verify dir/file exists otherwise create a
                # node to represent. potential cases:
                #   (1.) "dir <name>"
                #   (2.) "size:<int>, name:<str>"

                if data[curr_line][0] == "dir":
                    dname = data[curr_line][1]
                    if dname not in curr_dir.get_children():
                        curr_dir.add_child(
                            Node(name=dname, ntype=NodeType.DIR, parent=curr_dir)
                        )

                else:
                    size, fname = data[curr_line]
                    if fname not in curr_dir.get_children():
                        curr_dir.add_child(
                            Node(
                                name=fname,
                                ntype=NodeType.FILE,
                                size=int(size),
                                parent=curr_dir,
                            )
                        )
                        # print(f"{curr_dir.name} -> {fname}")

                curr_line += 1

        else:
            raise Exception("not great")

    return base_dir


if __name__ == "__main__":
    base_dir = main()

    all_dirs = [(base_dir.name, base_dir.size)]

    def gather_dirs(base_node):
        for d in base_node.get_children().values():
            if d.ntype == NodeType.DIR:
                all_dirs.append((d.name, d.size))
                gather_dirs(d)

    gather_dirs(base_dir)
    print(all_dirs)

    # P1: find the sum of all the directories with a total size of at most 100000
    print(sum(filter(lambda v: v <= 100000, map(lambda y: y[1], all_dirs))))

    TOTAL_DISK_SPACE = 70000000
    UNUSED_SPACE_TARGET = 30000000

    total_used_space = base_dir.size
    current_unused_space = TOTAL_DISK_SPACE - total_used_space
    minimum_remove_amout = UNUSED_SPACE_TARGET - current_unused_space

    # P2: find the smallest directory that results in target unused space
    #     what is the total size of that directory?
    print(f"Minimum dir size to remove {minimum_remove_amout}")

    all_dirs.sort(key=lambda pair: pair[1])  # sort by size ascending in place
    for idx, pair in enumerate(all_dirs):
        name, size = pair
        if size > minimum_remove_amout:
            print(f"Dir: {name}, Size: {size}")
            break
