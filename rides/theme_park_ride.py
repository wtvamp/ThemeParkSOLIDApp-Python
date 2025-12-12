class ThemeParkRide:
    total_speed = 0.0

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed
        ThemeParkRide.total_speed += speed

    def ride_details(self) -> str:
        return f"{self.name} which goes {self.speed}\n"
