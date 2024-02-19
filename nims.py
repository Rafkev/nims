import random

def nim():
    # Initialize the game state
    piles = [random.randint(1, 10) for _ in range(random.randint(2, 5))]  # Randomly generate piles of stones
    player_turn = 0  # Player 0 starts the game

    # Main game loop
    while True:
        print("\nCurrent Piles:", piles)
        print("Player", player_turn, "'s turn")

        # Player's move
        while True:
            pile_choice = int(input("Choose a pile (0-" + str(len(piles) - 1) + "): "))
            if 0 <= pile_choice < len(piles):
                break
            else:
                print("Invalid pile number. Please choose again.")

        while True:
            stones_to_remove = int(input("How many stones to remove from pile " + str(pile_choice) + ": "))
            if 1 <= stones_to_remove <= piles[pile_choice]:
                break
            else:
                print("Invalid number of stones. Please choose again.")

        piles[pile_choice] -= stones_to_remove

        # Check for win condition
        if all(pile == 0 for pile in piles):
            print("Player", player_turn, "wins!")
            break

        # Switch player turn
        player_turn = 1 - player_turn

# Run the game
if __name__ == "__main__":
    nim()
