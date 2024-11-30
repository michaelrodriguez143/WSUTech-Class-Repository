class Drink:
    _valid_bases = {"water", "sprite", "poke-acola", "Mr. Salt", "hill fog", "leaf wine"}
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}
    _size_prices = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15
    }
    _flavor_price = 0.15

    def __init__(self, base, flavors, size):
        self._base = None
        self._flavors = set()
        self.set_base(base)
        self.set_flavors(flavors)
        self.set_size(size)

    # Getter methods
    def get_base(self):
        return self._base

    def get_flavors(self):
        return list(self._flavors)

    def get_num_flavors(self):
        return len(self._flavors)

    def get_size(self):
        return self._size

    def get_total(self):
        base_price = Drink._size_prices.get(self._size.lower())
        flavor_price = len(self._flavors) * Drink._flavor_price
        return base_price + flavor_price

    # Accessor methods
    def set_base(self, base):
        if base.lower() not in Drink._valid_bases:
            raise ValueError(f"Invalid base: {base}. Choose from {Drink._valid_bases}.")
        self._base = base.lower()

    def add_flavor(self, flavor):
        if flavor.lower() not in Drink._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}. Choose from {Drink._valid_flavors}.")
        self._flavors.add(flavor.lower())

    def set_flavors(self, flavors):
        if not isinstance(flavors, (list, set)):
            raise TypeError("Flavors must be a list or set.")
        for flavor in flavors:
            self.add_flavor(flavor)

    def set_size(self, size):
        size = size.lower()
        if size not in Drink._size_prices:
            raise ValueError(f"Invalid size: {size}. Choose from {Drink._size_prices}.")
        self._size = size
