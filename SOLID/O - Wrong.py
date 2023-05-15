# Open-Closed Principle
# WRONG EXAMPLE

class Animal:
    def __init__(self, name):
        self.name = name


class Lion(Animal):
    def __init__(self):
        super().__init__('lion')


class Fish(Animal):
    def __init__(self):
        super().__init__('fish')


def show_leg(lst: list[Animal]):
    for animal in lst:
        # if there are other child classes, the "if-elif-else" construct will increase
        if isinstance(animal, Lion):
            print(f'{animal.name}, legs = 4')
        elif isinstance(animal, Fish):
            print(f'{animal.name}, legs = 0')


animals = [Lion(), Fish()]
show_leg(animals)
