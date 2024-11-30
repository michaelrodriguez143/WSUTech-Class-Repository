import unittest
from .drink import Drink
from .order import Order


class TestDrink(unittest.TestCase):
    def test_set_base(self):
        drink = Drink()
        drink.set_base("sprite")
        self.assertEqual(drink.get_base(), "sprite")

    def test_add_flavor(self):
        drink = Drink()
        drink.add_flavor("lemon")
        self.assertIn("lemon", drink.get_flavors())

    def test_invalid_base(self):
        drink = Drink()
        with self.assertRaises(ValueError):
            drink.set_base("cola")

    def test_invalid_flavor(self):
        drink = Drink()
        with self.assertRaises(ValueError):
            drink.add_flavor("vanilla")

    def test_set_flavors(self):
        drink = Drink()
        drink.set_flavors(["cherry", "lime"])
        self.assertEqual(drink.get_flavors(), ["cherry", "lime"])


class TestOrder(unittest.TestCase):
    def test_order_initialization(self):
        order = Order()
        self.assertEqual(order.get_items(), [])
        self.assertEqual(order.get_total(), 0.0)

    def test_add_item(self):
        order = Order()
        drink = Drink()
        drink.set_base("sprite")
        order.add_item(drink)
        self.assertEqual(order.get_num_items(), 1)

    def test_remove_item(self):
        order = Order()
        drink = Drink()
        drink.set_base("sprite")
        order.add_item(drink)
        order.remove_item(0)
        self.assertEqual(order.get_num_items(), 0)

    def test_get_receipt(self):
        order = Order()
        drink1 = Drink()
        drink1.set_base("water")
        drink1.add_flavor("lemon")

        drink2 = Drink()
        drink2.set_base("sprite")
        drink2.set_flavors(["lime", "mint"])

        order.add_item(drink1)
        order.add_item(drink2)
        receipt = order.get_receipt()
        self.assertIn("Drink 1: Base - water, Flavors - lemon", receipt)
        self.assertIn("Drink 2: Base - sprite, Flavors - lime, mint", receipt)
        self.assertIn("Total: $10.00", receipt)


if __name__ == "__main__":
    unittest.main()
