class ThemePark:
    def __init__(self):
        self.theme_park_name = None
        self.ticket_cost = 0.0
        self.average_daily_attendance = 0

        self.theme_park_ride_a_name = None
        self.theme_park_ride_b_name = None
        self.theme_park_ride_c_name = None
        self.theme_park_ride_a_speed = 0.0
        self.theme_park_ride_b_speed = 0.0
        self.theme_park_ride_c_speed = 0.0

        self.restaurant_a_name = None
        self.restaurant_b_name = None
        self.restaurant_c_name = None
        self.restaurant_a_income = 0.0
        self.restaurant_b_income = 0.0
        self.restaurant_c_income = 0.0
        self.restaurant_a_loss = 0.0
        self.restaurant_b_loss = 0.0
        self.restaurant_c_loss = 0.0

        self._total_income = 0.0
        self._total_cost = 0.0
        self._theme_park_rides = []
        self._theme_park_food = []

    def _convert_rides_name_to_list(self):
        self._theme_park_rides.append((self.theme_park_ride_a_name, self.theme_park_ride_a_speed))
        self._theme_park_rides.append((self.theme_park_ride_b_name, self.theme_park_ride_b_speed))
        self._theme_park_rides.append((self.theme_park_ride_c_name, self.theme_park_ride_c_speed))
        return self._theme_park_rides

    def _convert_restaurants_to_list(self):
        self._theme_park_food.append((self.restaurant_a_name, self.restaurant_a_income, self.restaurant_a_loss))
        self._theme_park_food.append((self.restaurant_b_name, self.restaurant_b_income, self.restaurant_b_loss))
        self._theme_park_food.append((self.restaurant_c_name, self.restaurant_c_income, self.restaurant_c_loss))
        return self._theme_park_food

    def _calculate_total_restaurant_income(self):
        self._total_income += self.average_daily_attendance * (
            (self.restaurant_a_income + self.restaurant_b_income + self.restaurant_c_income) / 3
        )

    def _calculate_total_restaurant_cost(self):
        self._total_cost += self.average_daily_attendance * (
            (self.restaurant_a_loss + self.restaurant_b_loss + self.restaurant_c_loss) / 3
        )

    def _calculate_total_ride_income(self):
        self._total_income += self.ticket_cost * self.average_daily_attendance

    def _calculate_total_ride_cost(self):
        self._total_cost += (
            self.theme_park_ride_a_speed + self.theme_park_ride_b_speed + self.theme_park_ride_c_speed
        ) * 0.50 * 12

    def _calculate_profit(self):
        self._calculate_total_restaurant_income()
        self._calculate_total_restaurant_cost()
        self._calculate_total_ride_cost()
        self._calculate_total_ride_income()
        return self._total_income - self._total_cost

    def print_rides(self):
        print(f"{self.theme_park_name} contains the following rides:\n")
        for ride in self._convert_rides_name_to_list():
            print(f"{ride[0]} which goes {ride[1]}\n")

    def print_restaurants(self):
        print(f"{self.theme_park_name} contains the following restaurants:\n")
        for restaurant in self._convert_restaurants_to_list():
            print(f"{restaurant[0]} which generates {restaurant[1]} in income and costs {restaurant[2]}\n")

    def print_profit(self):
        print(f"{self.theme_park_name} makes {self._calculate_profit()} in income.")
