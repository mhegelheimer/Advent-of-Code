import os
from collections import defaultdict


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SAMPLE = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

DEBUG = False


def dprint(s):
    if DEBUG:
        print(s)


def part1():
    total = 0
    # data = SAMPLE.splitlines()
    with open(os.path.join(__location__, "data.txt"), "r") as rf:
        data = [l.strip() for l in rf.readlines()]
    # dprint(data)

    for line in data:
        card, data = line.split(":")
        _, card_number = list(filter(lambda i: bool(i), card.split(" ")))
        win_nums, card_nums = data.split("|")

        win_nums = list(filter(lambda i: bool(i), win_nums.split(" ")))
        card_nums = list(filter(lambda i: bool(i), card_nums.split(" ")))

        points = 0
        for num in card_nums:
            if num in win_nums:
                if points < 1: points += 1
                else: points *= 2
        
        total += points
        dprint(f"Card {card_number}: {points}")

    print(f"Total: {total}")


def part2():
    total = 0
    # data = SAMPLE.splitlines()
    with open(os.path.join(__location__, "data.txt"), "r") as rf:
        data = [l.strip() for l in rf.readlines()]

    card_multipliers = defaultdict(int)

    for line in data:
        card, data = line.split(":")
        _, card_number = list(filter(lambda i: bool(i), card.split(" ")))
        win_nums, card_nums = data.split("|")

        win_nums = list(filter(lambda i: bool(i), win_nums.split(" ")))
        card_nums = list(filter(lambda i: bool(i), card_nums.split(" ")))

        card_win_count = 0
        for num in card_nums:
            if num in win_nums:
                card_win_count += 1

        # increment total card count for this card
        card_multipliers[int(card_number)] += 1 

        # increase future card multipliers by total number of cards
        if card_win_count > 0:
            for future_card_number in range(int(card_number)+1, int(card_number)+card_win_count+1):
                card_multipliers[future_card_number] += (card_multipliers[int(card_number)])

        total += card_multipliers[int(card_number)]


    print(f"Total: {total}")


part1()
part2()
