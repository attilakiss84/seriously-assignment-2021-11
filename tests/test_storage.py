import unittest
from vendingmachine.storage import Product
from vendingmachine.storage import VendingMachine


class TestProduct(Product):
    name = "Test"
    price = 1


class StorageTest(unittest.TestCase):

    def testVendingMachineSlotCountSetup(self):
        testSlots = 10

        testMachine = VendingMachine(testSlots, 5)

        self.assertEqual(len(testMachine.slots), testSlots, "Number of slots does not match")
        for slot in testMachine.slots:
            self.assertIsNone(slot, "Sales slot is initialized with product")

        with self.assertRaises(IndexError):
            testMachine.addProduct(TestProduct, testSlots)

    def testVendingMachineSlotAssignment(self):
        testMachine = VendingMachine(1, 1)

        testMachine.addProduct(TestProduct, 0)
        self.assertIsNotNone(testMachine.slots[0])
        self.assertEqual(testMachine.slots[0].product, TestProduct)

        testMachine.removeProduct(0)
        self.assertIsNone(testMachine.slots[0])

        with self.assertRaises(AssertionError):
            testMachine.removeProduct(0)

    def testVendingMachineSlotDepthSetup(self):
        testDepth = 1
        testMachine = VendingMachine(1, testDepth)
        testMachine.addProduct(TestProduct, 0)

        with self.assertRaises(AssertionError):
            testMachine.load(0, testDepth + 1)

        with self.assertRaises(AssertionError):
            testMachine.load(0, -1)

    def testVendingMachineSlotLoading(self):
        testDepth = 2
        testMachine = VendingMachine(1, testDepth)
        testMachine.addProduct(TestProduct, 0)

        self.assertIsNotNone(testMachine.slots[0])
        self.assertEqual(testMachine.slots[0].product, TestProduct)
        self.assertEqual(testMachine.slots[0].amount, 0, "Product is initialized with inappropriate amount")

        testMachine.load(0, testDepth - 1)
        self.assertEqual(testMachine.slots[0].amount, testDepth - 1, "Load amount is inappropriate")

        testMachine.load(0, 1)
        self.assertEqual(testMachine.slots[0].amount, testDepth, "Load amount is inappropriate")

        with self.assertRaises(AssertionError):
            testMachine.load(0, 0 - (testDepth + 1))

        testMachine.load(0, -testDepth)
        self.assertEqual(testMachine.slots[0].amount, 0, "Load amount is inappropriate")
