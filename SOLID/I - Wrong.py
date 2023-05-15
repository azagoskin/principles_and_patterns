# Interface Segregation Principle
# WRONG EXAMPLE

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def roar(self):
        pass


class Lion(Animal):
    def __init__(self):
        self.name = 'lion'
        self.legs = 4

    def roar(self):
        return 'ARRRRRR'


class Tiger(Animal):
    def __init__(self):
        self.name = 'tiger'
        self.legs = 4

    def roar(self):
        return 'MYARRR'


class Fish(Animal):
    def __init__(self):
        self.name = 'fish'
        self.legs = 0

    def roar(self):
        # OOPS, we don't need this interface
        return None

