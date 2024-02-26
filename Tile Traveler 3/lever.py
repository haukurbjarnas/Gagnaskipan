import random

class Lever:
    
    def initialize_levers(self, grid_size, max_levers):
        levers = set()
        while len(levers) < max_levers:  
            x = random.randint(1, grid_size)
            y = random.randint(1, grid_size)
            if (x, y) not in [(1, 1), (grid_size, 1)]:  
                levers.add((x, y))
        return levers

    def pull_lever(self, coins, coin_value):
        print("You see a lever.")
        if input("PULL LEVER? (y/n): ").lower() == 'y':
            add=coin_value + random.randint(0, 3)
            coins += add
            print("You received", add,"gold coins!")
        return coins