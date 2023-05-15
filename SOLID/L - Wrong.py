# Liskov substitution principle
# WRONG EXAMPLE

class Animal:
    def __init__(self, name: str, legs: int):
        self.name = name
        self.legs = legs

    def show_leg(self) -> int:
        return self.legs


class Lion(Animal):
    def __init__(self):
        super().__init__('lion', 4)


class Fish(Animal):
    def __init__(self):
        super().__init__('fish', 0)

    # this function breaks LSP and should be removed
    def show_leg(self) -> None:
        raise ValueError('fish don\'t have legs')


# methods that use objects of the parent class must also use objects of the child class
animals = [Animal('human', 2), Lion(), Fish()]
for animal in animals:
    print(f'{animal.name}, legs = {animal.show_leg()}')
