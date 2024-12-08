class Food:
    """
    Class representing a food item. A food item has a type (e.g., "hotdog"), a base price, 
    and optional toppings that increase the price.
    """
    _valid_food_items = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice cream": 3.00,
        "onion rings": 1.75,
        "french fries": 1.50,
        "tater tots": 1.70,
        "nacho chips": 1.90,
    }

    _valid_toppings = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "nacho cheese": 0.30,
        "chili": 0.60,
        "bacon bits": 0.30,
        "ketchup": 0.00,
        "mustard": 0.00,
    }

    def __init__(self):
        """
        Initializes a food item with no type and no toppings.
        """
        self._type = None
        self._toppings = set()

    def get_type(self):
        """
        Returns the type of the food item.

        Returns:
            str: The type of food (e.g., "hotdog").
        """
        return self._type

    def set_type(self, food_type):
        """
        Sets the type of food.

        Args:
            food_type (str): The type of food to set.

        Raises:
            ValueError: If the food type is invalid.
        """
        if food_type not in Food._valid_food_items:
            raise ValueError(f"Invalid food type: {food_type}. Choose from {Food._valid_food_items.keys()}.")
        self._type = food_type

    def get_price(self):
        """
        Calculates the total price of the food item, including toppings.

        Returns:
            float: The total price of the food item.
        """
        base_price = Food._valid_food_items.get(self._type, 0.0)
        toppings_price = sum(Food._valid_toppings[topping] for topping in self._toppings)
        return base_price + toppings_price

    def get_toppings(self):
        """
        Returns the list of toppings added to the food.

        Returns:
            list: List of toppings.
        """
        return list(self._toppings)

    def add_topping(self, topping):
        """
        Adds a topping to the food item.

        Args:
            topping (str): The topping to add.

        Raises:
            ValueError: If the topping is invalid.
        """
        if topping not in Food._valid_toppings:
            raise ValueError(f"Invalid topping: {topping}. Choose from {Food._valid_toppings.keys()}.")
        self._toppings.add(topping)

    def get_num_toppings(self):
        """
        Returns the number of toppings added to the food.

        Returns:
            int: Number of toppings.
        """
        return len(self._toppings)
