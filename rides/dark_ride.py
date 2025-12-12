from .theme_park_ride import ThemeParkRide


class DarkRide(ThemeParkRide):
    def __init__(self, name: str, speed: float, scariness: int):
        super().__init__(name, speed)
        self._scariness = scariness  # Rated from 0-10

    def extra_details(self) -> str:
        return f"{self.name} is a dark ride which is rated {self._scariness} on a scale of 1-10.\n"
