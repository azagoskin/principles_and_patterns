from abc import abstractmethod, ABC


class State(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass

    @abstractmethod
    def move(self) -> str:
        pass


class LionSleep(State):
    def eat(self) -> str:
        return 'lion cant eat in his sleep'

    def move(self) -> str:
        return 'lion cant move in his sleep'


class LionAwake(State):
    def eat(self) -> str:
        return 'where is lion food?'

    def move(self) -> str:
        return 'where should he run?'


class Lion:
    def __init__(self, state: State):
        self._state = state

    def eat(self):
        func = self.execute_function('eat')
        print(func())

    def move(self):
        func = self.execute_function('move')
        print(func())

    def execute_function(self, function_name: str):
        try:
            func = getattr(self._state, function_name)
            return func
        except AttributeError:
            print('lion cant do this')


lion = Lion(LionAwake())
lion.eat()
lion.move()
