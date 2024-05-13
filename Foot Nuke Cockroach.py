import random


def whoWins(userChoice, computerChoice, wins, ties, rounds):
    rounds += 1
    if userChoice == "Nuke" and computerChoice == "Nuke":
        print("Both LOSE!")
    elif userChoice == computerChoice:
        print("It is a tie!")
        ties += 1
    elif (
        (userChoice == "Foot" and computerChoice == "Cockroach")
        or (userChoice == "Nuke" and computerChoice == "Foot")
        or (userChoice == "Cockroach" and computerChoice == "Nuke")
    ):
        print("You WIN!")
        wins += 1
    else:
        print("You LOSE!")
    return wins, ties, rounds


def main():
    wins = 0
    ties = 0
    rounds = 0
    variants = ["Cockroach", "Foot", "Nuke"]
    userChoice = ""
    while userChoice != "Quit":
        userChoice = input("Foot, Nuke or Cockroach? (Quit ends): ")
        if userChoice == "Quit":
            print(
                f"You played {rounds} rounds, and won {wins} rounds, playing tie in {ties} rounds."
            )
            continue
        if not userChoice in variants:
            print("Incorrect selection.")
            continue

        print("You chose:", userChoice)
        computerChoice = variants[random.randint(0, 2)]
        print("Computer chose:", computerChoice)
        wins, ties, rounds = whoWins(userChoice, computerChoice, wins, ties, rounds)


if __name__ == "__main__":
    main()