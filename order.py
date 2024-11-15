from .drink import Drink

class Order:
    def __init__(self):
        self._items = []

    # Getter methods
    def get_items(self):
        return self._items

    def get_total(self):
        # Assuming each drink has a fixed price
        return len(self._items) * 5.0  # Example price per drink

    def get_num_items(self):
        return len(self._items)

    def get_receipt(self):
        receipt = []
        for index, drink in enumerate(self._items):
            receipt.append(f"Drink {index + 1}: Base - {drink.get_base()}, Flavors - {', '.join(drink.get_flavors())}")
        receipt.append(f"Total: ${self.get_total():.2f}")
        return "\n".join(receipt)

    # Accessor methods
    def add_item(self, drink):
        if not isinstance(drink, Drink):
            raise TypeError("Item must be an instance of Drink.")
        self._items.append(drink)

    def remove_item(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Invalid index. No item to remove.")
        self._items.pop(index)
