from theme_park import ThemePark
from rides import DarkRide, SpinningRide, BrokenRide
from restaurants import SpaceRestaurant, UnderseaRestaurant


def main():
    warwar_land = ThemePark()
    warwar_land.ticket_cost = 90
    warwar_land.average_daily_attendance = 50000
    warwar_land.theme_park_name = "War War Land"

    warwar_land.theme_park_rides.append(DarkRide("Haunted Mansion", 5, 7))
    warwar_land.theme_park_rides.append(SpinningRide("Teacups", 7, 360, 3))
    warwar_land.theme_park_rides.append(BrokenRide("Pirates of the Caribbean"))
    # warwar_land.theme_park_rides.append(DarkRide("Pirates of the Caribbean", 5, 4))
    warwar_land.print_rides()

    warwar_land.restaurants.append(SpaceRestaurant("Pizzasaurus Rex", 5, 3, 1000))
    warwar_land.restaurants.append(SpaceRestaurant("Planet Mars Burgers", 8, 7.5, 1000))
    warwar_land.restaurants.append(UnderseaRestaurant("Salads Undersea", 3, 6, 1000))
    warwar_land.print_restaurants()

    warwar_land.print_profit()


if __name__ == "__main__":
    main()
