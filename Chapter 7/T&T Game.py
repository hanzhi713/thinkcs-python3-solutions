import random


def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    #  See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first={0},  winner={1} "
          .format(human_plays_first, result))
    return result


def main():
    AIScore = 0
    HumanScore = 0
    GameDrawn = 0
    while 1:
        result = play_once(random.uniform(-1, 1))
        if result == -1:
            print("You win!")
            HumanScore += 1
        elif result == 0:
            print("Game drawn!")
            GameDrawn += 1
        elif result == 1:
            print("Computer wins!")
            AIScore += 1
        SumScores = HumanScore + AIScore + GameDrawn
        print(
            "Your win rate is {0}/{1}, {2}%".format(str(HumanScore), str(SumScores), str(HumanScore / SumScores * 100)))
        if input("Do you want to play again?") == "Yes":
            None
        else:
            break
    print("Goodbye")


main()
