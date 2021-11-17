from vendingmachine.interface import PurchaseProcess
from vendingmachine.storage import Product, VendingMachine
from vendingmachine.payment import CashPayment, CardPayment

class Tupla(Product):
    name = "Tupla bar (50g)"
    price = 3

class Geisha(Product):
    name = "Geisha bar (40g)"
    price = 2

class Smarties(Product):
    name = "Smarties pack (20g)"
    price = 1


if __name__ == "__main__":
    candyMachine = VendingMachine(10, 5)
    candyMachine.addProduct(Tupla, 0)
    candyMachine.load(0, 5)
    candyMachine.addProduct(Tupla, 2)
    candyMachine.load(2, 1)
    candyMachine.addProduct(Geisha, 4) # Out of stock, but set
    candyMachine.addProduct(Smarties, 6)
    candyMachine.load(6, 2)

    PurchaseProcess(candyMachine, CashPayment)
