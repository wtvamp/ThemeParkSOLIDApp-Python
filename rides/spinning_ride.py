from .theme_park_ride import ThemeParkRide
from .interfaces import IExtraDetails, ISpinningEngine


class SpinningRide(ThemeParkRide, IExtraDetails):
    def __init__(self, name: str, speed: float, spinning_degree: float, spinning_speed: float,
                 engine: ISpinningEngine):
        super().__init__(name, speed)
        self._spinning_degree = spinning_degree
        self._spinning_speed = spinning_speed
        self._engine = engine  # Dependency injection of spinning engine

    def extra_details(self) -> str:
        return f"{self.name} is a spinning ride that spins {self._spinning_degree} degrees at {self._spinning_speed}mph.\n"

    def start(self) -> bool:
        return self._engine.start(self.name)

    def stop(self) -> bool:
        return self._engine.stop(self.name)
