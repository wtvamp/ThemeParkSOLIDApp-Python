from abc import ABC, abstractmethod


class ThemeParkRide(ABC):
    total_speed = 0.0

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed
        ThemeParkRide.total_speed += speed

    def ride_details(self) -> str:
        return f"{self.name} goes {self.speed}mph.\n"

    @abstractmethod
    def extra_details(self) -> str:
        pass
