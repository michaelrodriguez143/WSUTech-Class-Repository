import unittest
from .drink import Drink
from .order import Order


class TestDrink(unittest.TestCase):
    """
    Test case class for the Drink class. This class tests the functionality of all methods
    provided by the Drink class, including base and flavor manipulation.
    """
    def test_set_base(self):
        """
        Test setting a valid base for a drink.
        """
        drink = Drink()
        drink.set_base("sprite")
        self.assertEqual(drink.get_base(), "sprite")

    def test_add_flavor(self):
        """
        Test adding a valid flavor to a drink.
        """
        drink = Drink()
        drink.add_flavor("lemon")
        self.assertIn("lemon", drink.get_flavors())

    def test_invalid_base(self):
        """
        Test setting an invalid base for a drink. This should raise a ValueError.
        """
        drink = Drink()
        with self.assertRaises(ValueError):
            drink.set_base("cola")

    def test_invalid_flavor(self):
        """
        Test adding an invalid flavor to a drink. This should raise a ValueError.
        """
        drink = Drink()
        with self.assertRaises(ValueError):
            drink.add_flavor("vanilla")

    def test_set_flavors(self):
        """
        Test setting multiple flavors for a drink using the set_flavors method.
        """
        drink = Drink()
        drink.set_flavors(["cherry", "lime"])
        self.assertEqual(drink.get_flavors(), ["cherry", "lime"])


class TestOrder(unittest.TestCase):
    """
    Test case class for the Order class. This class tests the functionality of all methods
    provided by the Order class, including adding/removing drinks and calculating totals.
    """
    def test_order_initialization(self):
        """
        Test the initialization of an empty order.
        """ 
        order = Order()
        self.assertEqual(order.get_items(), [])
        self.assertEqual(order.get_total(), 0.0)

    def test_add_item(self):
        """
        Test adding a drink to the order.
        """
        order = Order()
        drink = Drink()
        drink.set_base("sprite")
        order.add_item(drink)
        self.assertEqual(order.get_num_items(), 1)

    def test_remove_item(self):
        """
        Test removing a drink from the order by index.
        """
        order = Order()
        drink = Drink()
        drink.set_base("sprite")
        order.add_item(drink)
        order.remove_item(0)
        self.assertEqual(order.get_num_items(), 0)

    def test_get_receipt(self):
        """
        Test generating a receipt for an order
        """
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
