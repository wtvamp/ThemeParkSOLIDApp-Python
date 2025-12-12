from .theme_park_ride import ThemeParkRide


class BrokenRide(ThemeParkRide):
    def __init__(self, name: str):
        super().__init__(name, 0)  # Speed is 0 for broken rides

    def extra_details(self) -> str:
        # NOTE: Setting total_speed = None here would violate LSP
        # as it would break the base class contract
        return "This is an example of a broken ride and should not be counted in the total right now"
