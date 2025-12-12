from abc import ABC, abstractmethod


class Restaurant(ABC):
    total_income = 0.0
    total_loss = 0.0

    def __init__(self, name: str, income: float, loss: float):
        self.name = name
        self.income = income
        self.loss = loss
        Restaurant.total_income += income
        Restaurant.total_loss += loss

    def restaurant_details(self) -> str:
        return f"{self.name} which generates {self.income} in income and costs {self.loss}\n"

    @abstractmethod
    def extra_details(self) -> str:
        pass
