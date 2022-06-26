from math import radians, sin, cos, asin, sqrt

# Node class attributes
# name - City name
# lat / long - coordinates for the city
# parent - list of parent nodes to the city
class node:
    # node class constructor
    def __init__(self, name:str, parent:str = None, lat = 0, long = 0):
        self.name = name
        self.lat = lat
        self.long = long

        self.parent = parent

        self.h = 0
        self.g = 0
        self.f = 0

    # compare the nodes
    # nodes are compared based on the name
    def __eq__(self, other):
        return self.name == other.name

    # Sort the nodes
    # sort on a total cost basis
    def __lt__(self, other):
        return self.f < other.f

    def get_distance(coord1, coord2):
        radius = 6371 # radius of the Earth
        lat1 = radians(coord1[0])
        long1 = radians(coord1[1])

        lat2 = radians(coord2[0])
        long2 = radians(coord2[1])

        delta_lat = lat2-lat1
        delta_long = long2-long1

        a = pow(sin(delta_lat / 2), 2) + pow(sin(delta_long / 2), 2) * cos(lat1) * cos(lat2)
        c = 2 * asin(sqrt(a))

        return radius * c