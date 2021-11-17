from abc import ABC, abstractmethod
import re


class PaymentProcess(ABC):

    _balance: int

    def __init__(self, balance: int):
        self._balance = balance

    @classmethod
    @abstractmethod
    def initPayment(self):
        pass

    @classmethod
    @abstractmethod
    def makePayment(self, amount: int):
        pass

    @classmethod
    @abstractmethod
    def giveBack(self, amount: int):
        pass


class CardPayment(PaymentProcess):

    def initPayment(self):
        print("Please, swipe your credit card and hit ENTER or type CANCEL to delete purchase")
        interaction = input()

        if (interaction == "CANCEL"):
            return False
        else:
            return self.makePayment(self._balance)

    def makePayment(self, amount: int):
        return True

    def giveBack(self, amount: int):
        raise PaymentException("Not implemented")


class CashPayment(PaymentProcess):

    __number = re.compile("^\d+$")

    def initPayment(self):
        self.__paymentsMade = 0

        while (self._balance > 0):
            print(f"Your balance is {self._balance}. Please, enter your cash amount or CANCEL to cancel the transaction")
            interaction = input().strip()

            if (interaction == "CANCEL"):
                self.giveBack(self.__paymentsMade)
                return False
            elif self.__number.match(interaction) is not None:
                amount = int(interaction, base=10)
                if (amount <= 0):
                    print("After next payment attempt with fake money your activity will be reported for the authorities")
                else:
                    self.makePayment(amount)

        self.giveBack(abs(self._balance))

        return True

    def makePayment(self, amount: int):
        self.__paymentsMade += amount
        self._balance -= amount

    def giveBack(self, amount: int):
        if (amount > 0):
            print(f'Please, take your change! ({amount})')
            self.__paymentsMade -= amount


class PaymentException(Exception):
    pass
