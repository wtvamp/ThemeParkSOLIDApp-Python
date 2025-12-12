from .restaurant import Restaurant


class UnderseaRestaurant(Restaurant):
    def __init__(self, name: str, income: float, loss: float, miles_undersea: int):
        super().__init__(name, income, loss)
        self._miles_undersea = miles_undersea

    def extra_details(self) -> str:
        return f"This restaurant pretends it is {self._miles_undersea} miles under the sea.\n"
