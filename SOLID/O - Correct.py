# Open-Closed Principle
# CORRECT EXAMPLE

class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def show_leg(self):
        return self.legs


class Lion(Animal):
    def __init__(self):
        super().__init__('lion', 4)


class Fish(Animal):
    def __init__(self):
        super().__init__('fish', 0)


def show_leg(lst: list[Animal]):
    for animal in lst:
        # can add an infinite number of objects of child classes
        print(f'{animal.name}, legs = {animal.show_leg()}')


animals = [Lion(), Fish()]
show_leg(animals)
