class CreditCard :
    __id = 0
    def __init__(self,type_card, card_name, number, pin_number):
        CreditCard.__id += 1
        self.__id = CreditCard.__id
        self.__card_name = card_name
        self.__type_card = type_card
        self.__number = number
        self.__pin_number = pin_number
        self.__money = 10000000

    @property
    def number(self):
        return self.__number
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money):
        self.__money = money
    @property
    def id(self):
        return self.__id