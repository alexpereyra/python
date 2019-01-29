#this program will tell a user categroy of hurricane base on wind speed input

wind_speed = eval(input("Wind speed of hurricane: "))

if wind_speed <74:
    print("This is Tropical Storm")

elif wind_speed >= 74 and wind_speed <= 95:
        print("This is a category 1")
elif wind_speed >= 96 and wind_speed <= 110:
        print("This is a category 2")
elif wind_speed >=111 and wind_speed <= 130:
        print("This is a category 3")
elif wind_speed >= 131 and wind_speed <= 155:
        print("This is a category 4")
elif wind_speed >= 156:
        print("This is a category 5")
