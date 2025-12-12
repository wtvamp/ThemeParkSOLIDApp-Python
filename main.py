from theme_park import ThemePark
from rides import DarkRide, SpinningRide, BrokenRide, SpinningEngine, SpinningEngineSuperFast
from restaurants import SpaceRestaurant, UnderseaRestaurant


def main():
    # Create rides with injected dependencies
    theme_park_rides = [
        SpinningRide("Teacups", 7, 360, 3, SpinningEngine()),
        BrokenRide("Pirates of the Caribbean"),
        DarkRide("Haunted Mansion", 5, 7),
    ]

    # Inject rides into ThemePark
    warwar_land = ThemePark(theme_park_rides)
    warwar_land.ticket_cost = 90
    warwar_land.average_daily_attendance = 50000
    warwar_land.theme_park_name = "War War Land"

    # Can add more rides with different engine implementations
    theme_park_rides.append(SpinningRide("Super Spinner", 10, 720, 5, SpinningEngineSuperFast()))
    theme_park_rides.append(BrokenRide("Old Coaster"))
    warwar_land.print_rides()

    warwar_land.restaurants.append(SpaceRestaurant("Pizzasaurus Rex", 5, 3, 1000))
    warwar_land.restaurants.append(SpaceRestaurant("Planet Mars Burgers", 8, 7.5, 1000))
    warwar_land.restaurants.append(UnderseaRestaurant("Salads Undersea", 3, 6, 1000))
    warwar_land.print_restaurants()

    warwar_land.print_profit()


if __name__ == "__main__":
    main()
