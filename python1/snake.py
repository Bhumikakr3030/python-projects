import random


def roll_dice():
    return random.randint(1, 6)


def move_player(position, dice_roll, snakes, ladders):
    new_position = position + dice_roll
    if new_position in snakes:
        print(f"Oh no! A snake at {new_position} bites! Moving down to {snakes[new_position]}")
        return snakes[new_position]
    elif new_position in ladders:
        print(f"Great! A ladder at {new_position} climbs up to {ladders[new_position]}")
        return ladders[new_position]
    return new_position


def play_game():
    snakes = {17: 7, 54: 34, 62: 19, 98: 79}
    ladders = {3: 38, 24: 33, 42: 93, 72: 84}
    player_positions = {"Player 1": 0, "Player 2": 0}

    while True:
        for player in player_positions:
            input(f"{player}, press Enter to roll the dice...")
            dice_roll = roll_dice()
            print(f"{player} rolled a {dice_roll}")
            player_positions[player] = move_player(player_positions[player], dice_roll, snakes, ladders)
            print(f"{player} is now at position {player_positions[player]}")

            if player_positions[player] >= 100:
                print(f"Congratulations! {player} wins!")
                return


if __name__ == "__main__":
    play_game()