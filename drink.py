class Drink:
    _valid_bases = {"water", "sprite", "poke-acola", "Mr. Salt", "hill fog", "leaf wine"}
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}

    def __init__(self):
        self._base = None
        self._flavors = set()

    # Getter methods
    def get_base(self):
        return self._base

    def get_flavors(self):
        return list(self._flavors)

    def get_num_flavors(self):
        return len(self._flavors)

    # Accessor methods
    def set_base(self, base):
        if base not in Drink._valid_bases:
            raise ValueError(f"Invalid base: {base}. Choose from {Drink._valid_bases}.")
        self._base = base

    def add_flavor(self, flavor):
        if flavor not in Drink._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}. Choose from {Drink._valid_flavors}.")
        self._flavors.add(flavor)

    def set_flavors(self, flavors):
        if not isinstance(flavors, (list, set)):
            raise TypeError("Flavors must be a list or set.")
        for flavor in flavors:
            self.add_flavor(flavor)
