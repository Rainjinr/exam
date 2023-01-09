class Tomato: # 1. Создайте класс Tomato
    states = 1 # 2. Создайте статистическое свойство states

    def __init__(self, _index, _state=states, states_info = states): # Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
        self._index = _index
        self._state = _state
        self.states_info = states_info
    def info (self):

        print(T._state)
        print(self.states_info)


    def grow(self, next_st = int(input())):
        self.next_st = next_st
        self.next_st =self.next_st + 1
        print  (self.next_st)

    def is_ripe(self):
        if self.next_st == 3:
            print( "Созрел!")
        else:
            print ("Еще не созрел!")


class TomatoBush:
    tomatoes = []

    def __init__(self, Tomato = 3):
        self.Tomato = Tomato

    def grow_all():
        for i in TomatoBush.tomatoes:
            i = i + 1
        print( TomatoBush.tomatoes )

    def all_are_ripe():
        ripe = 0

        for i in TomatoBush.tomatoes:
            if i >= 3:
                ripe = ripe + 1
            if ripe >= len(TomatoBush.tomatoes):
                print(True)

    def give_away_all():
        TomatoBush.tomatoes = []




class Gardener:
    def __init__(self, name, _plant = 0):
        self.name = name
        self._plant = _plant
    def work():
        for i in TomatoBush.tomatoes:
            i = i + 1
        print(TomatoBush.tomatoes)

    def harvest():
        ripe = 0
        if i >= 3:
            ripe = ripe + 1
        if ripe >= len(TomatoBush.tomatoes):
            TomatoBush.tomatoes = []
    #
    # def grow(self):
    #     if self._state < 3:
    #         self._state += 1
T = Tomato(5)
T.info()
T.grow()
T.is_ripe()



