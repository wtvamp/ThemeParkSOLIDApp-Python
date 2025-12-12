from theme_park import ThemePark


def main():
    warwar_land = ThemePark()
    warwar_land.ticket_cost = 90
    warwar_land.average_daily_attendance = 50000
    warwar_land.theme_park_name = "War War Land"

    warwar_land.theme_park_ride_a_name = "Haunted Mansion"
    warwar_land.theme_park_ride_a_speed = 5
    warwar_land.theme_park_ride_b_name = "Teacups"
    warwar_land.theme_park_ride_b_speed = 7
    warwar_land.theme_park_ride_c_name = "Pirates of the Caribbean"
    warwar_land.theme_park_ride_c_speed = 5
    warwar_land.print_rides()

    warwar_land.restaurant_a_name = "Pizzasaurus Rex"
    warwar_land.restaurant_a_income = 5
    warwar_land.restaurant_a_loss = 3
    warwar_land.restaurant_b_name = "Planet Mars Burgers"
    warwar_land.restaurant_b_income = 8
    warwar_land.restaurant_b_loss = 7.5
    warwar_land.restaurant_c_name = "Salads Undersea"
    warwar_land.restaurant_c_income = 3
    warwar_land.restaurant_c_loss = 6
    warwar_land.print_restaurants()

    warwar_land.print_profit()


if __name__ == "__main__":
    main()
