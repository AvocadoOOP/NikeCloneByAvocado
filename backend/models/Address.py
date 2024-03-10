class Address :
    def __init__(self, id_address, house_number, soi, road, province, postal_code):
        self.__id = id_address
        self.__house_number = house_number
        self.__soi = soi
        self.__road = road
        self.__province = province
        self.__postal_code = postal_code

    @property
    def postal_code(self):
        return self.__postal_code
    @property
    def house_number(self):
        return self.__house_number
    @property
    def id(self):
        return self.__id
