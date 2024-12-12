class IceStorm:
    """
    A class representing an Ice Storm dessert item, including flavors and toppings.
    """
    FLAVORS = {
        "Mint Chocolate Chip": 4.00,
        "Chocolate": 3.00,
        "Vanilla Bean": 3.00,
        "Banana": 3.50,
        "Butter Pecan": 3.50,
        "S'more": 4.00
    }

    TOPPINGS = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Storios": 1.00,
        "Dig Dogs": 1.00,
        "T&T's": 1.00,
        "Cookie Dough": 1.00,
        "Pecans": 0.50
    }

    def __init__(self):
        """
        Initializes an Ice Storm with default values.
        """
        self.flavor = None
        self.toppings = []

    def get_flavor(self):
        """Returns the flavor of the Ice Storm."""
        return self.flavor

    def add_flavor(self, flavor):
        """
        Sets the flavor of the Ice Storm.
        
        :param flavor: The flavor to set.
        :raises ValueError: If the flavor is not available.
        """
        if flavor not in self.FLAVORS:
            raise ValueError(f"{flavor} is not a valid flavor.")
        self.flavor = flavor

    def get_toppings(self):
        """Returns the list of toppings added to the Ice Storm."""
        return self.toppings

    def add_topping(self, topping):
        """
        Adds a topping to the Ice Storm.
        
        :param topping: The topping to add.
        :raises ValueError: If the topping is not available.
        """
        if topping not in self.TOPPINGS:
            raise ValueError(f"{topping} is not a valid topping.")
        self.toppings.append(topping)

    def get_total(self):
        """
        Calculates and returns the total price of the Ice Storm.
        """
        total = 0.0
        if self.flavor:
            total += self.FLAVORS[self.flavor]
        total += sum(self.TOPPINGS[topping] for topping in self.toppings)
        return total

    def get_num_toppings(self):
        """Returns the number of toppings on the Ice Storm."""
        return len(self.toppings)

    def __str__(self):
        """
        Returns a string representation of the Ice Storm.
        """
        toppings_str = ", ".join(self.toppings) if self.toppings else "None"
        return f"Ice Storm - Flavor: {self.flavor or 'None'}, Toppings: {toppings_str}, Total: ${self.get_total():.2f}"
