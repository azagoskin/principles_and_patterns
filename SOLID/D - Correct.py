from abc import abstractmethod, ABC


class Group(ABC):
    @abstractmethod
    def retrive_members(self):
        pass


class Lion:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Pride(Group):
    def __init__(self):
        self.group: list[Lion] = []

    def add_lion(self, member: Lion):
        self.group.append(member)

    def retrive_members(self):
        for lion in self.group:
            yield lion


class Analysis:
    def __init__(self, pride: Pride):
        max_weight = 0
        fattest_lion = None

        # now we do not depend on the implementation of the class 'Pride'
        for lion in pride.retrive_members():
            if lion.weight > max_weight:
                max_weight = lion.weight
                fattest_lion = lion

        print(f'The fattest lion is {fattest_lion.name}')


lion1 = Lion('Simba', 1)
lion2 = Lion('Scar', 100)
lion3 = Lion('Sarabi', 50)
pride = Pride()
pride.add_lion(lion1)
pride.add_lion(lion2)
pride.add_lion(lion3)

Analysis(pride)
