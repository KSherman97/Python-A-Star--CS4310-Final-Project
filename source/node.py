from math import radians, sin, cos, asin, sqrt

class node:
    def __init__(self, lat, long, parent=None, start=False, goal=False):
        self.lat = lat
        self.long = long

        self.parent = parent
        self.start = start
        self.goal = goal

        self.g = 0
        self.h = 0
        self.f = 0

    def get_distance(node1, node2):
        radius = 6371 # radius of the Earth
        long1 = radians(node1.long)
        long2 = radians(node2.long)
        lat1 = radians(node1.lat)
        lat2 = radians(node2.lat)

        delta_lat = lat2-lat1
        delta_long = long2-long1

        a = pow(sin(delta_lat / 2), 2) + pow(sin(delta_long / 2), 2) * cos(lat1) * cos(lat2)
        c = 2 * asin(sqrt(a))

        return radius * c