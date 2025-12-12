from .interfaces import ISpinningEngine


class SpinningEngineSuperFast(ISpinningEngine):
    def __init__(self):
        self._is_ride_started = False

    def start(self, ride_name: str) -> bool:
        if not self._is_ride_started:
            print(f"The {ride_name} ride is going super fast.")
            self._is_ride_started = True
        return self._is_ride_started

    def stop(self, ride_name: str) -> bool:
        if self._is_ride_started:
            print(f"The {ride_name} ride came to a complete halt!")
            self._is_ride_started = False
        return self._is_ride_started
