from abc import abstractmethod


class Lion:
    def __init__(self):
        self.hungry = True

    @abstractmethod
    def eat(self, meat: int) -> int:
        pass


class Simba(Lion):
    def eat(self, meat: int):
        if meat > 2:
            self.hungry = False
            meat -= 2
            print('Simba is full')
        else:
            print('Simba is hungry')

        return meat


class Sarabi(Lion):
    def eat(self, meat: int):
        if meat > 10:
            self.hungry = False
            meat -= 10
            print('Sarabi is full')
        else:
            print('Sarabi is hungry')

        return meat


class Mufasa(Lion):
    def eat(self, meat: int):
        if meat > 25:
            self.hungry = False
            meat -= 25
            print('Mufasa is full')
        else:
            print('Mufasa is hungry')

        return meat


class Pride:
    def __init__(self):
        self.group: list[Lion] = []

    def add_member(self, lion: Lion):
        self.group.append(lion)

    def eat_meat(self, meat):
        for lion in self.group:
            meat = lion.eat(meat)


pride = Pride()
pride.add_member(Simba())
pride.add_member(Sarabi())
pride.add_member(Mufasa())

pride.eat_meat(4)
print()
pride.eat_meat(38)
