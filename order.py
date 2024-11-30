from .drink import Drink

class Order:
    """
    Class representing an order of drinks. An order contains multiple drinks, and its total price is calculated
    based on the drinks in the order.
    """
    
    def __init__(self):
        """
        Initializes an empty order with no items and a total price of zero.
        """
        self._items = []

    def get_items(self):
        """
        Returns a list of all drinks in the order.

        Returns:
            list: A list of Drink objects in the order.
        """
        return self._items

    def get_total(self):
        """
        Calculates the total price for the order. The total price is based on the size and flavors of the drinks.

        Returns:
            float: The total price of the order before tax.
        """
        total = 0.0
        for drink in self._items:
            # The base price starts with the drink size cost.
            size_cost = self._get_size_cost(drink)
            total += size_cost + (0.15 * len(drink.get_flavors()))  # Add flavor cost
        return total

    def get_num_items(self):
        """
        Returns the number of drinks in the order.

        Returns:
            int: The number of drinks in the order.
        """
        return len(self._items)

    def get_receipt(self):
        """
        Returns a formatted receipt for the order. The receipt contains details of each drink, including
        its base and flavors, as well as the total price and the tax.

        Returns:
            str: The receipt as a string.
        """
        receipt = []
        subtotal = 0.0
        for index, drink in enumerate(self._items):
            base = drink.get_base()
            flavors = ", ".join(drink.get_flavors())
            size_cost = self._get_size_cost(drink)
            flavor_cost = 0.15 * len(drink.get_flavors())
            total_drink_cost = size_cost + flavor_cost
            subtotal += total_drink_cost
            receipt.append(f"Drink {index + 1}: Base - {base}, Flavors - {flavors}, Total: ${total_drink_cost:.2f}")
        
        # Calculate tax
        tax = subtotal * 0.0725
        total_with_tax = subtotal + tax
        receipt.append(f"Subtotal: ${subtotal:.2f}")
        receipt.append(f"Tax: ${tax:.2f}")
        receipt.append(f"Total: ${total_with_tax:.2f}")
        
        return "\n".join(receipt)

    def add_item(self, drink):
        """
        Adds a drink to the order.

        Args:
            drink (Drink): The drink to add to the order.

        Raises:
            TypeError: If the item is not an instance of the Drink class.
        """
        if not isinstance(drink, Drink):
            raise TypeError("Item must be an instance of Drink.")
        self._items.append(drink)

    def remove_item(self, index):
        """
        Removes a drink from the order by its index.

        Args:
            index (int): The index of the item to remove.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= len(self._items):
            raise IndexError("Invalid index. No item to remove.")
        self._items.pop(index)

    def _get_size_cost(self, drink):
        """
        Private helper method to get the cost of the size for a given drink.

        Args:
            drink (Drink): The drink whose size cost we are calculating.

        Returns:
            float: The cost of the drink's size.
        """
        size_prices = {
            "small": 1.50,
            "medium": 1.75,
            "large": 2.05,
            "mega": 2.15
        }
        
        size = drink.get_size().lower()
        if size not in size_prices:
            raise ValueError(f"Invalid size: {size}. Choose from small, medium, large, mega.")
        return size_prices[size]
