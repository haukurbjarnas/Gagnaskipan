import random
import string

class Pizza:

    def __init__(self) -> None:
        self.pizzas = {}




    def pizza_id(self):
        all_ids = []

        while True:
            random_letter_1 = random.choice(string.ascii_letters)
            random_letter_2 = random.choice(string.ascii_letters)
            random_num_1 = random.randint(0, 9)
            random_num_2 = random.randint(0, 9)

            new_id = random_letter_1.upper() + random_letter_2.upper() + str(random_num_1) + str(random_num_2)

            if new_id not in all_ids:
                all_ids.append(new_id)
                # maybe needs a break here
                return new_id



    def pizza_toppings(self, new_id):

        self.pizza = []

        while True:
            try:
                self.choice = int(input('Enter amount of toppings: '))
                break
            except ValueError:
                print('ENTER A NUMBER!!!!!!!!!!!!')
        
        for i in range(1, self.choice+1):
            self.topping = input(f"Enter topping #{i}: ")
            self.pizza.append(self.topping)

        self.pizzas[new_id] = self.pizza



    def serve_a_pizza(self):
        

        print("Listing all unserved pizzas")
        for key, value in self.pizzas.items():
            print(f'Pizza: {key} {value}')
        
        while True:
            pizza_to_serve = input("Enter Pizza ID: ")
            pizza_to_serve = pizza_to_serve.upper()
            if pizza_to_serve in self.pizzas:
                break
            else:
                print('Invalid input')

        self.pizzas.pop(pizza_to_serve)

def main():
    a_pizza = Pizza()

    while True:
        print('1. Create pizza')
        print('2. Serve pizza')
        print('(Q)uit')
        command = input('Select an operation: ')

        if command == '1':
            id = a_pizza.pizza_id()

            a_pizza.pizza_toppings(id)

        elif command == '2':
            a_pizza.serve_a_pizza()
        
        elif command == 'q':
            exit()



main()

