from .drink import Drink

class Order:
    TAX_RATE = 0.0725  # Tax rate of 7.25%

    def __init__(self):
        self._items = []

    # Getter methods
    def get_items(self):
        return self._items

    def get_total(self):
        total = sum(drink.get_total() for drink in self._items)
        tax = total * Order.TAX_RATE
        return total + tax

    def get_num_items(self):
        return len(self._items)

    def get_receipt(self):
        receipt = []
        total = 0
        for index, drink in enumerate(self._items):
            drink_total = drink.get_total()
            receipt.append(f"Drink {index + 1}: Base - {drink.get_base().title()}, Size - {drink.get_size().title()}, Total - ${drink_total:.2f}")
            total += drink_total
        tax = total * Order.TAX_RATE
        receipt.append(f"Subtotal: ${total:.2f}")
        receipt.append(f"Tax (7.25%): ${tax:.2f}")
        receipt.append(f"Total: ${total + tax:.2f}")
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
