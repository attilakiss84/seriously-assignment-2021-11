from abc import ABC, abstractmethod
from typing import List, Type


class Product(ABC):

    @property
    @abstractmethod
    def name() -> str:
        pass

    @property
    @abstractmethod
    def price() -> int:
        pass


class Stock:

    def __init__(self, product: Type[Product], amount: int) -> None:
        self.product = product
        self.amount = amount


class VendingMachine:

    __slots: List[Stock]
    __slotCount: int
    __slotDepth: int

    def __init__(self, slots: int, slotDepth: int) -> None:
        assert slots > 0, "Vending machine must have at least one slot for products"
        assert slotDepth > 0, "Selling slots must have at least capacity for one product"

        self.__slots = [None] * slots
        self.__slotCount = slots
        self.__slotDepth = slotDepth

    def load(self, slot: int, amount: int) -> None:
        assert slot >= 0 and slot < self.__slotCount and self.__slots[slot] is not None, "Invalid slot"

        projectedStockSize = self.__slots[slot].amount + amount

        assert projectedStockSize >= 0, f"There are only {self.slots[slot].amount} items in the product channel"
        assert projectedStockSize <= self.__slotDepth, f"Only {projectedStockSize - self.__slotDepth} fewer items can be loaded still into the machine"

        self.__slots[slot].amount = projectedStockSize

    def addProduct(self, product: Type[Product], slot: int) -> None:
        assert self.__slots[slot] is None, "The selling slot is already in use"

        self.__slots[slot] = Stock(product, 0)

    def removeProduct(self, slot: int) -> None:
        assert self.__slots[slot] is not None, "Slot is already empty"

        self.__slots[slot] = None

    def listProducts(self) -> None:
        print("Available products:")

        for i, slot in enumerate(self.__slots):
            if slot is not None and slot.amount > 0:
               print(f"{i}: {slot.product.name} - {slot.product.price} EUR")

    @property
    def slots(self) -> List[Stock]:
        return self.__slots
