# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"({self.name}, {self.lat}, {self.lon})"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []
import csv

def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the 
    # `cities` list
    with open('cities.csv', newline='') as cities_csv:
        next(cities_csv)
        cities_reader = csv.reader(cities_csv, delimiter=',')
        for row in cities_reader:
            cities.append(City(row[0], float(row[3]), float(row[4])))
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

### NOTE: I completed the stretch goal in a separate branch, named 'stretch'! :D

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
user_point_1 = input("Please enter a point in the form [latititde] [longitude], where both are floats: ").split(" ")
user_point_2 = input("Please enter a second point in the form [latititde] [longitude], where both are floats: ").split(" ")

# Ensure both are floats:
user_point_1 = list(map(lambda string: float(string), user_point_1))
user_point_2 = list(map(lambda string: float(string), user_point_2))

def cityreader_stretch(lat1 = user_point_1[0], lon1 = user_point_1[1], lat2 = user_point_2[0], lon2 = user_point_2[1], cities=cities):
    point1 = [lat1, lon1]
    point2 = [lat2, lon2]

    lowest_lat = point1 if point1[0] <= point2[0] else point2
    lowest_lon = point1 if point1[1] <= point2[1] else point2

    bottom_left = []
    top_right = []
    if lowest_lat == point1 and lowest_lon == point1:
        bottom_left = point1
        top_right = point2
    elif lowest_lat == point2 and lowest_lon == point2:
        bottom_left = point2
        top_right = point1
    elif lowest_lat == point1 and lowest_lon == point2:
        bottom_left = [point1[0], point2[1]]
        top_right = [point2[0], point1[1]]
    elif lowest_lat == point2 and lowest_lon == point1:
        bottom_left = [point2[0], point1[1]]
        top_right = [point1[0], point2[1]]
    
    # within will hold the cities that fall within the specified region
    within = [city for city in cities if city.lat >= bottom_left[0] and city.lat <= top_right[0] and city.lon >= bottom_left[1] and city.lon <= top_right[1]]

    # TODO Ensure that the lat and lon valuse are all floats
        # Check!
    # Go through each city and check to see if it falls within
    # the specified coordinates.
        # Check!

    return within
