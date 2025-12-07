class Кошелёк:
    def __init__(self):
        self._баланс = 0
    def баланс(self):
        return self._баланс
    def пополнить(self, сумма):
        if(сумма > 0):
            self._баланс += сумма
        else:
            print("Сумма должна быть юольше 0 !!!")
    def снять(self, money):
        if self._баланс > money and money > 0:
            self._баланс -= money
        else:
            print("Нехвтает денег на балансе или сумма < 0")
wallet = Кошелёк()
wallet.пополнить(1000) 
print(wallet.баланс()) 