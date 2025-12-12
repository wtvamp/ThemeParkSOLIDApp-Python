from abc import ABC, abstractmethod


class IThemeParkRide(ABC):
    @abstractmethod
    def ride_details(self) -> str:
        pass


class IExtraDetails(ABC):
    @abstractmethod
    def extra_details(self) -> str:
        pass


class ISpinningEngine(ABC):
    @abstractmethod
    def start(self, ride_name: str) -> bool:
        pass

    @abstractmethod
    def stop(self, ride_name: str) -> bool:
        pass
