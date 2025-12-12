from theme_park import ThemePark
from rides import ThemeParkRide
from restaurants import Restaurant


def main():
    warwar_land = ThemePark()
    warwar_land.ticket_cost = 90
    warwar_land.average_daily_attendance = 50000
    warwar_land.theme_park_name = "War War Land"

    warwar_land.theme_park_rides.append(ThemeParkRide("Haunted Mansion", 5))
    warwar_land.theme_park_rides.append(ThemeParkRide("Teacups", 7))
    warwar_land.theme_park_rides.append(ThemeParkRide("Pirates of the Caribbean", 5))
    warwar_land.print_rides()

    warwar_land.restaurants.append(Restaurant("Pizzasaurus Rex", 5, 3))
    warwar_land.restaurants.append(Restaurant("Planet Mars Burgers", 8, 7.5))
    warwar_land.restaurants.append(Restaurant("Salads Undersea", 3, 6))
    warwar_land.print_restaurants()

    warwar_land.print_profit()


if __name__ == "__main__":
    main()
