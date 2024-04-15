class Bank:
    def __init__(self, name,  age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    def set_name(self, name):...

    def get_name(self):...
class Bank2 (Bank):

    def __init__(self, name, age, money, key):
        super().__init__(name, age, money, key)

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money):
        self.__money = money

    @property
    def key(self):
        return self.__key
    @key.setter
    def key(self, key):
        self.__key = key