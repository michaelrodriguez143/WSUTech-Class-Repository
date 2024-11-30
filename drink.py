class Drink:
    """
    Class representing a drink. A drink has a base and a set of flavors that can be added to it.
    This class validates the base and flavors to ensure that only valid ones are set.
    """
    
    _valid_bases = {"water", "sprite", "poke-acola", "Mr. Salt", "hill fog", "leaf wine"}
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}

    def __init__(self):
        """
        Initializes a new drink with no base and an empty set of flavors.
        """
        self._base = None
        self._flavors = set()

    def get_base(self):
        """
        Returns the base of the drink.

        Returns:
            str: The base of the drink (e.g., "sprite").
        """
        return self._base

    def get_flavors(self):
        """
        Returns a list of all flavors added to the drink.

        Returns:
            list: List of flavor names.
        """
        return list(self._flavors)

    def get_num_flavors(self):
        """
        Returns the number of flavors added to the drink.

        Returns:
            int: The number of flavors added to the drink.
        """
        return len(self._flavors)

    def set_base(self, base):
        """
        Sets the base for the drink.

        Args:
            base (str): The base to set (must be valid).

        Raises:
            ValueError: If the base is invalid.
        """
        if base not in Drink._valid_bases:
            raise ValueError(f"Invalid base: {base}. Choose from {Drink._valid_bases}.")
        self._base = base

    def add_flavor(self, flavor):
        """
        Adds a flavor to the drink.

        Args:
            flavor (str): The flavor to add (must be valid).

        Raises:
            ValueError: If the flavor is invalid.
        """
        if flavor not in Drink._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}. Choose from {Drink._valid_flavors}.")
        self._flavors.add(flavor)

    def set_flavors(self, flavors):
        """
        Sets multiple flavors for the drink. If the flavors list is not a list or set, it raises a TypeError.

        Args:
            flavors (list or set): A collection of flavors to set for the drink.

        Raises:
            TypeError: If the flavors argument is not a list or set.
        """
        if not isinstance(flavors, (list, set)):
            raise TypeError("Flavors must be a list or set.")
        for flavor in flavors:
            self.add_flavor(flavor)
