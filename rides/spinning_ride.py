from .theme_park_ride import ThemeParkRide
from .interfaces import IExtraDetails, ISpinningEngine


class SpinningRide(ThemeParkRide, IExtraDetails, ISpinningEngine):
    def __init__(self, name: str, speed: float, spinning_degree: float, spinning_speed: float):
        super().__init__(name, speed)
        self._spinning_degree = spinning_degree
        self._spinning_speed = spinning_speed
        self._is_ride_spinning = False

    def extra_details(self) -> str:
        return f"{self.name} is a spinning ride that spins {self._spinning_degree} degrees at {self._spinning_speed}mph.\n"

    def start(self) -> bool:
        if not self._is_ride_spinning:
            self._is_ride_spinning = True
        return self._is_ride_spinning

    def stop(self) -> bool:
        if self._is_ride_spinning:
            self._is_ride_spinning = False
        return self._is_ride_spinning
