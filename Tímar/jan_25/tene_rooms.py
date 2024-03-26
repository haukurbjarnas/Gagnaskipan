import random

def distribute_lads(lads):
    random.shuffle(lads)
    rooms = [lads[i:i+2] for i in range(0, len(lads), 2)]
    
    # Ensure one room contains 3 lads
    rooms[0].append(rooms[3].pop())

    return rooms

# List of lads
all_lads = ['Haukur', 'Smári', 'Helgi', 'Óliver', 'Ægir', 'Bárður', 'Gísli', 'Hjalti', 'Hrafn']

# Distribute lads into rooms
rooms = distribute_lads(all_lads)

# Print the distribution
for i, room in enumerate(rooms, start=1):
    print(f"Room {i}: {', '.join(room)}")
