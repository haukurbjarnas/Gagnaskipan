# blabla

class Movement:

    def __init__(self, grid_size, walls):
        
        self.grid_size = grid_size

        self.walls = walls
        

    def is_valid_move(self, position, direction):
        if direction in self.walls.get(position, []):
            return False
        x, y = position
        if direction == 'n' and y < self.grid_size: return True
        if direction == 's' and y > 1: return True
        if direction == 'e' and x < self.grid_size: return True
        if direction == 'w' and x > 1: return True
        return False
    
    def is_valid_move(self, position, direction):
        if direction in self.walls.get(position, []):
            return False
        x, y = position
        if direction == 'n' and y < self.grid_size: return True
        if direction == 's' and y > 1: return True
        if direction == 'e' and x < self.grid_size: return True
        if direction == 'w' and x > 1: return True
        return False
    
    def move_player(self, position, direction):
        if direction == 'n': return (position[0], position[1] + 1)
        if direction == 's': return (position[0], position[1] - 1)
        if direction == 'e': return (position[0] + 1, position[1])
        if direction == 'w': return (position[0] - 1, position[1])
        return position