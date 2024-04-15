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

if __name__ == '__main__':
    user = Bank2('Saikal', 30, 12000, 'sakesh')
    print('До: ')
    print(user.name, user.age, user.money, user.key)

    user.age = 20
    user.money = 50000
    user.key = 'lalala'

    print('после: ')
    print(user.name, user.age, user.money, user.key)