from typing import Type
from .storage import VendingMachine
from .payment import PaymentProcess


class PurchaseProcess:

    __vendingMachine: VendingMachine
    __selectedSlot: int
    __PaymentProcess: Type[PaymentProcess]
    __purchase: PaymentProcess

    def __init__(self, machine: VendingMachine, paymentProcess: Type[PaymentProcess]) -> None:
        self.__vendingMachine = machine
        self.__PaymentProcess = paymentProcess

        while True:
            try:
                self.__vendingMachine.listProducts()
                print("Please, select product!")
                interaction = int(input(), 10)
                self.selectProduct(interaction)
                self.__purchase = self.__PaymentProcess(self.__vendingMachine.slots[self.__selectedSlot].product.price)

                if self.__purchase.initPayment():
                    print(f'Please take your {self.__vendingMachine.slots[self.__selectedSlot].product.name}!')
                    self.__vendingMachine.load(self.__selectedSlot, -1)
            except Exception as e:
                print(e)
            finally:
                self.__purchase = None
                self.__selectedSlot = None

    def selectProduct(self, slot: int) -> None:
        assert self.__vendingMachine.slots[slot] is not None and self.__vendingMachine.slots[slot].amount > 0, "Product out of stock"

        self.__selectedSlot = slot
