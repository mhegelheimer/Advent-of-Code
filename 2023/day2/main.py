import os

SAMPLE = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


TARGET_MAP = {
    "red": 12,
    "green": 13,
    "blue": 14
}


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


DEBUG = False
def dprint(s):
    if DEBUG:
        print(s)


def part1():
    total = 0

    # for line in SAMPLE.splitlines():
    with open(os.path.join(__location__,'data.txt'), 'r') as rf:

        for line in rf.readlines():
            game, info = line.split(":")
            is_valid_game = True
            dprint(game)

            sets = info.split(";")
            for idx, subset in enumerate(sets, 1):
                dprint(f"Subset {idx}")
                groups = subset.split(",")
                for group in groups:                    
                    count, color = group.strip(" ").strip("\n").split(" ")
                    
                    if int(count) > TARGET_MAP[color]:
                        is_valid_game = False
                    dprint(f"{count}, {color}")
            
            if is_valid_game:
                _, game_num = game.split(" ")
                total += int(game_num)
    
    print(f"Total: {total}")


def part2():
    total = 0

    # for line in SAMPLE.splitlines():
    with open(os.path.join(__location__,'data.txt'), 'r') as rf:
        for line in rf.readlines():
            game, info = line.split(":")
            dprint(game)

            min_color_bag_count = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            sets = info.split(";")
            for idx, subset in enumerate(sets, 1):
                dprint(f"Subset {idx}")
                groups = subset.split(",")
                for group in groups:                    
                    count, color = group.strip(" ").strip("\n").split(" ")

                    min_color_bag_count[color] = max(min_color_bag_count[color], int(count))                

            dprint(f"Min Color Count Bag Counts: {min_color_bag_count}")            
            acc = 1
            for val in min_color_bag_count.values():
                acc *= val

            dprint(f"Power: {acc}")
            total += acc

    print(f"Total: {total}")


part1()
part2()