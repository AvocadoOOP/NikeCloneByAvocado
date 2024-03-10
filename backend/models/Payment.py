class Payment :
    def __init__(self):
        self.__credit_card = None
        self.__payment_status = None

    def pay_money(self, credit_card, price):
        if price <= credit_card.money :
            credit_card.money -= price
            self.__payment_status = "Already paid"
            self.__credit_card = credit_card
            return {"data": "successfull"}
        return {"data": "Not enough money"}
    
    @property
    def payment_status(self):
        return self.__payment_status