from .drink import Drink
from .food import Food

class Order:
    """
    Class representing an order of items (drinks and food). An order calculates the total price
    and generates a receipt for all items.
    """
    def __init__(self):
        """
        Initializes an empty order.
        """
        self._items = []

    def add_item(self, item):
        """
        Adds an item (drink or food) to the order.

        Args:
            item (Drink or Food): The item to add.

        Raises:
            TypeError: If the item is not an instance of Drink or Food.
        """
        if not isinstance(item, (Drink, Food)):
            raise TypeError("Item must be an instance of Drink or Food.")
        self._items.append(item)

    def remove_item(self, index):
        """
        Removes an item from the order by its index.

        Args:
            index (int): The index of the item to remove.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= len(self._items):
            raise IndexError("Invalid index. No item to remove.")
        self._items.pop(index)

    def get_items(self):
        """
        Returns the list of items in the order.

        Returns:
            list: List of items in the order.
        """
        return self._items

    def get_total(self):
        """
        Calculates the total price for the order.

        Returns:
            float: The total price of the order.
        """
        return sum(item.get_price() for item in self._items)

    def get_receipt(self):
        """
        Generates a receipt for the order.

        Returns:
            str: A formatted receipt including all items and the total price.
        """
        receipt = []
        for index, item in enumerate(self._items):
            if isinstance(item, Drink):
                receipt.append(
                    f"Drink {index + 1}: Base - {item.get_base()}, Flavors - {', '.join(item.get_flavors())}, Total: ${item.get_price():.2f}"
                )
            elif isinstance(item, Food):
                receipt.append(
                    f"Food {index + 1}: Type - {item.get_type()}, Toppings - {', '.join(item.get_toppings())}, Total: ${item.get_price():.2f}"
                )

        receipt.append(f"Total: ${self.get_total():.2f}")
        return "\n".join(receipt)
