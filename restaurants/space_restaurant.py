from .restaurant import Restaurant


class SpaceRestaurant(Restaurant):
    def __init__(self, name: str, income: float, loss: float, miles_from_earth: int):
        super().__init__(name, income, loss)
        self._miles_from_earth = miles_from_earth

    def extra_details(self) -> str:
        return f"{self.name} pretends it is {self._miles_from_earth} miles from Earth.\n"
