import random
import string

class Pizza:

    def __init__(self) -> None:
        self.pizza_dict = {}
        self.id_list = []

    def pizza_id(self):
        
        while True:
            rand_int_1 = random.randint(0, 9)
            rand_int_2 = random.randint(0, 9)
            rand_let_1 = random.choice(string.ascii_uppercase)
            rand_let_2 = random.choice(string.ascii_uppercase)

            a_id = f'#{rand_int_1}{rand_int_2}{rand_let_1}{rand_let_2}'

            if a_id in self.id_list:
                pass
            else:
                self.id_list.append(a_id)
                return a_id

    def pizza_maker(self):
        
        pizza = []

        while True:
            try:
                toppings_amount = int(input('Enter amount of toppings: '))
                break
            except ValueError:
                print('You can only enter numbers!')

        counter = 1

        for _ in range(toppings_amount):

            topping = input(f'Enter topping #{counter}: ')

            pizza.append(topping)

            counter += 1

        id = self.pizza_id()

        self.pizza_dict[id] = pizza





    def serve_pizza(self):
        

        for id, pizza in self.pizza_dict.items():

            print(f'{id}: {pizza}')

        while True:
            removed_pizza = input('Enter ID of pizza: ')
            if removed_pizza in self.pizza_dict.keys():
                self.pizza_dict.pop(removed_pizza)
                break
            else:
                print('Unvalid ID')


def main():
    pizza = Pizza()

    command = ""

    while command != 'q':
        print('1. Create Pizza')
        print('2. Serve Pizza')
        print('(Q)uit')

        command = input('Select command: ')

        if command == '1':
            pizza.pizza_maker()
        elif command == '2':
            pizza.serve_pizza()
        else:
            print('Invalid input')


main()