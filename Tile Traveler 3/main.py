#

from lever import Lever
from movement import Movement

walls = {
    (1, 1): ['e'],
    (2, 1): ['w', 'e'],
    (3, 1): ['w'],
    (1, 2): [],
    (2, 2): ['e', 'n'],
    (3, 2): ['w'],
    (1, 3): [],
    (2, 3): ['s'],
}

lever_class = Lever()


def main():
    position = (1, 1)
    coins = 0
    grid_size = input("Enter Grid Size: ")
    while ValueError:
        try:
            grid_size = int(grid_size)
            break
        except ValueError:
            grid_size = input("Enter Grid Size: ")
    movement_class = Movement(grid_size, walls)
    max_levers = input("Choose Max Levers: ")
    while ValueError:
        try:
            max_levers = int(max_levers)
            break
        except ValueError:
            grid_size = input("Choose Max Levers: ")
    coin_value = input("Choose Coin Value: ")
    while ValueError:
        try:
            coin_value = int(coin_value)
            break
        except ValueError:
            grid_size = input("Choose Coin Value: ")
    levers = lever_class.initialize_levers(grid_size, max_levers)
    used_levers = set()
    while position != (grid_size, 1):
        print(f"You are at {position}. You have {coins} gold coins.")
        available_directions = ['n', 's', 'e', 'w']

        valid_directions = [d for d in available_directions if movement_class.is_valid_move(position, d)]
        print(f"Available directions: {', '.join(valid_directions).upper()}")

        direction = input("Choose a direction (n/e/s/w): ").lower()

        if direction in valid_directions:
            position = movement_class.move_player(position, direction)
            if position in levers and position not in used_levers:
                coins = lever_class.pull_lever(coins, coin_value)
        else:
            print("Not a valid direction!")
        
    print(f"Congratulations! You've reached the victory tile with {coins} gold coins!")


main()