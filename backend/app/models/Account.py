class Account :
    __id = 0
    def __init__(self, email, password):
        Account.__id += 1
        self.__id = Account.__id
        self.__password = password
        self.__email = email
        
    @property
    def email(self):
        return self.__email
    @property
    def password(self):
        return self.__password
    @property
    def id(self):
        return self.__id
