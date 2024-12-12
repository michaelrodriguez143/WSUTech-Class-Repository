import unittest
from .drink import Drink
from .food import Food
from .order import Order
from .icestorm import IceStorm


class TestDrink(unittest.TestCase):
    """
    Test case class for the Drink class. This class tests the functionality of all methods
    provided by the Drink class, including base and flavor manipulation.
    """

    def test_set_base(self):
        """Test setting a valid base for a drink."""
        drink = Drink()
        drink.set_base("sprite")
        self.assertEqual(drink.get_base(), "sprite")

    def test_add_flavor(self):
        """Test adding a valid flavor to a drink."""
        drink = Drink()
        drink.add_flavor("lemon")
        self.assertIn("lemon", drink.get_flavors())

    def test_invalid_base(self):
        """Test setting an invalid base for a drink. This should raise a ValueError."""
        drink = Drink()
        with self.assertRaises(ValueError):
            drink.set_base("cola")

    def test_invalid_flavor(self):
        """Test adding an invalid flavor to a drink. This should raise a ValueError."""
        drink = Drink()
        with self.assertRaises(ValueError):
            drink.add_flavor("vanilla")

    def test_set_flavors(self):
        """Test setting multiple flavors for a drink using the set_flavors method."""
        drink = Drink()
        drink.set_flavors(["cherry", "lime"])
        self.assertEqual(drink.get_flavors(), ["cherry", "lime"])


class TestFood(unittest.TestCase):
    """
    Test case class for the Food class. This class tests the functionality of all methods
    provided by the Food class, including type, topping manipulation, and pricing.
    """

    def test_set_type(self):
        """Test setting a valid food type."""
        food = Food()
        food.set_type("hotdog")
        self.assertEqual(food.get_type(), "hotdog")

    def test_invalid_type(self):
        """Test setting an invalid food type. This should raise a ValueError."""
        food = Food()
        with self.assertRaises(ValueError):
            food.set_type("burger")

    def test_add_topping(self):
        """Test adding a valid topping to a food item."""
        food = Food()
        food.set_type("french fries")
        food.add_topping("ketchup")
        self.assertIn("ketchup", food.get_toppings())

    def test_invalid_topping(self):
        """Test adding an invalid topping to a food item. This should raise a ValueError."""
        food = Food()
        food.set_type("nacho chips")
        with self.assertRaises(ValueError):
            food.add_topping("salsa")

    def test_get_price(self):
        """Test calculating the price of a food item with toppings."""
        food = Food()
        food.set_type("ice cream")
        food.add_topping("caramel sauce")
        food.add_topping("chocolate sauce")
        self.assertAlmostEqual(food.get_price(), 4.0)  # Base price + toppings


class TestOrder(unittest.TestCase):
    """
    Test case class for the Order class. This class tests the functionality of all methods
    provided by the Order class, including adding/removing items, calculating totals, and generating receipts.
    """

    def test_order_initialization(self):
        """Test the initialization of an empty order."""
        order = Order()
        self.assertEqual(order.get_items(), [])
        self.assertEqual(order.get_total(), 0.0)

    def test_add_drink_item(self):
        """Test adding a drink to the order."""
        order = Order()
        drink = Drink()
        drink.set_base("sprite")
        order.add_item(drink)
        self.assertEqual(order.get_num_items(), 1)

    def test_add_food_item(self):
        """Test adding a food item to the order."""
        order = Order()
        food = Food()
        food.set_type("hotdog")
        food.add_topping("ketchup")
        order.add_item(food)
        self.assertEqual(order.get_num_items(), 1)

    def test_remove_item(self):
        """Test removing an item (drink or food) from the order by index."""
        order = Order()
        drink = Drink()
        drink.set_base("sprite")
        order.add_item(drink)
        order.remove_item(0)
        self.assertEqual(order.get_num_items(), 0)

    def test_get_total(self):
        """Test calculating the total price of an order with drinks and food."""
        order = Order()

        drink = Drink()
        drink.set_base("sprite")
        drink.add_flavor("lemon")
        order.add_item(drink)

        food = Food()
        food.set_type("french fries")
        food.add_topping("ketchup")
        food.add_topping("bacon bits")
        order.add_item(food)

        self.assertAlmostEqual(order.get_total(), 3.45)  # Drink + Food price

    def test_get_receipt(self):
        """Test generating a receipt for an order with drinks and food."""
        order = Order()

        drink = Drink()
        drink.set_base("sprite")
        drink.add_flavor("lime")
        order.add_item(drink)

        food = Food()
        food.set_type("onion rings")
        food.add_topping("chili")
        order.add_item(food)

        receipt = order.get_receipt()
        self.assertIn("Drink 1: Base - sprite, Flavors - lime", receipt)
        self.assertIn("Food 2: Type - onion rings, Toppings - chili", receipt)
        self.assertIn("Total: $3.35", receipt)

class TestIceStorm(unittest.TestCase):
    """Unit tests for the IceStorm class."""

    def test_initialization(self):
        """Test the initialization of an Ice Storm."""
        storm = IceStorm()
        self.assertIsNone(storm.get_flavor())
        self.assertEqual(storm.get_toppings(), [])
        self.assertEqual(storm.get_total(), 0.0)

    def test_add_flavor(self):
        """Test adding a valid flavor to an Ice Storm."""
        storm = IceStorm()
        storm.add_flavor("Chocolate")
        self.assertEqual(storm.get_flavor(), "Chocolate")

    def test_invalid_flavor(self):
        """Test adding an invalid flavor raises a ValueError."""
        storm = IceStorm()
        with self.assertRaises(ValueError):
            storm.add_flavor("Strawberry")

    def test_add_topping(self):
        """Test adding a valid topping to an Ice Storm."""
        storm = IceStorm()
        storm.add_topping("Cherry")
        self.assertIn("Cherry", storm.get_toppings())

    def test_invalid_topping(self):
        """Test adding an invalid topping raises a ValueError."""
        storm = IceStorm()
        with self.assertRaises(ValueError):
            storm.add_topping("Sprinkles")

    def test_get_total(self):
        """Test calculating the total price of an Ice Storm."""
        storm = IceStorm()
        storm.add_flavor("Chocolate")
        storm.add_topping("Cherry")
        storm.add_topping("Caramel Sauce")
        self.assertAlmostEqual(storm.get_total(), 3.50)

    def test_str_representation(self):
        """Test the string representation of an Ice Storm."""
        storm = IceStorm()
        storm.add_flavor("S'more")
        storm.add_topping("Chocolate Sauce")
        self.assertIn("S'more", str(storm))
        self.assertIn("Chocolate Sauce", str(storm))


if __name__ == "__main__":
    unittest.main()
