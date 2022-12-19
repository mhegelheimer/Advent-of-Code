from dataclasses import dataclass
from pprint import pprint


CHOICE_SCORE = {
    "A": 1,  # rock
    "B": 2,  # paper
    "C": 3   # scissors
}


@dataclass(frozen=True)
class Choice:
    """
        A - Rock
        B - Paper
        C - Scissors
    """
    value: str

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        if self.value == other.value:
            return False

        if self.defeats().value == other.value:
            return True
        return False

    def __lt__(self, other):
        if not self == other and not self > other:
            return True
        return False

    def defeats(self):
        # Winning Combos: Rock(A) - Scissors(C), Scissors(C) - Paper(B), Paper(B) - Rock(A)
        return Choice("C") if self.value == "A" else Choice("B") if self.value == "C" else Choice("A")

    def is_defeated_by(self):
        # inverse of .defeats()
        return Choice("A") if self.value == "C" else Choice("C") if self.value == "B" else Choice("B")


def determine_score(ochoice: Choice, mchoice: Choice):

    # draw: 3 
    if ochoice == mchoice:
        result_value = 3
    # loss: 0 pts
    elif ochoice > mchoice:
        result_value = 0
    # win: 6 pts
    else:
        result_value = 6

    return CHOICE_SCORE[mchoice.value] + result_value


def determine_choice(opponent, result):
    # draw
    if result == "Y":
        return Choice(opponent), Choice(opponent)

    # loss
    elif result == "X":
        return Choice(opponent), Choice(opponent).defeats()
 
    # win
    return Choice(opponent), Choice(opponent).is_defeated_by()


def main():
    total_score = 0
    with open("input.txt") as rf:
        for line in rf.readlines():
            args = line.split(" ")
            opponent, result = args[0], args[1].strip()
            opponent, me = determine_choice(opponent, result)
            total_score += determine_score(opponent, me)
    return total_score


if __name__ == "__main__":
    total_score = main()
    pprint(f"Total Score: {total_score}")