from .theme_park_ride import ThemeParkRide


class SpinningRide(ThemeParkRide):
    def __init__(self, name: str, speed: float, spinning_degree: float, spinning_speed: float):
        super().__init__(name, speed)
        self._spinning_degree = spinning_degree
        self._spinning_speed = spinning_speed

    def extra_details(self) -> str:
        return f"{self.name} is a spinning ride that spins {self._spinning_degree} degrees at {self._spinning_speed}mph.\n"
