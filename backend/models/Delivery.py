class Delivery :
    def __init__(self):
        self.__delivery_status = None
        self.__company = "TOEY_DY_ROT_group"
        self.__phone_sender = "010-101-1101"

    def updete_status(self, status):
        self.__delivery_status = status
        return {"data" : "Done"}

    @property
    def delivery_status(self):
        return  self.__delivery_status