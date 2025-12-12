from typing import List
from rides import ThemeParkRide, IExtraDetails, ISpinningEngine
from restaurants import Restaurant


class ThemePark:
    def __init__(self):
        self.theme_park_name = None
        self.ticket_cost = 0.0
        self.average_daily_attendance = 0
        self.theme_park_rides: List[ThemeParkRide] = []
        self.restaurants: List[Restaurant] = []
        self._total_income = 0.0
        self._total_cost = 0.0

    def _calculate_total_restaurant_income(self):
        self._total_income += self.average_daily_attendance * (Restaurant.total_income / 3)

    def _calculate_total_restaurant_cost(self):
        self._total_cost += self.average_daily_attendance * (Restaurant.total_loss / 3)

    def _calculate_total_ride_income(self):
        self._total_income += self.ticket_cost * self.average_daily_attendance

    def _calculate_total_ride_cost(self):
        self._total_cost += ThemeParkRide.total_speed * 0.50 * 12

    def _calculate_profit(self):
        self._calculate_total_restaurant_income()
        self._calculate_total_restaurant_cost()
        self._calculate_total_ride_cost()
        self._calculate_total_ride_income()
        return self._total_income - self._total_cost

    def print_rides(self):
        print(f"{self.theme_park_name} contains the following rides:\n")
        for ride in self.theme_park_rides:
            if isinstance(ride, IExtraDetails):
                print(ride.extra_details())
            if isinstance(ride, ISpinningEngine):
                ride.start()
                ride.stop()
            print(ride.ride_details())

    def print_restaurants(self):
        print(f"{self.theme_park_name} contains the following restaurants:\n")
        for restaurant in self.restaurants:
            print(restaurant.extra_details())
            print(restaurant.restaurant_details())

    def print_profit(self):
        print(f"{self.theme_park_name} makes {self._calculate_profit()} in income.")
