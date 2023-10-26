# https://www.linkedin.com/learning/python-object-oriented-programming/equality-and-comparison?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
import csv
from random import random

from TravelData import distance_data, address_data


# This function operates in O(n) time to generate an adjacency matrix
#had an issue with package 9's y_position showing as none when it should be 0
#https://stackoverflow.com/questions/3930188/how-to-convert-nonetype-to-int-or-string
#https://stackoverflow.com/questions/707674/how-to-compare-type-of-an-object-in-python
def calc_distance(x_position, y_position):
    try:
        if x_position >= y_position:
            return distance_data[x_position][y_position]
        else:
            return distance_data[y_position][x_position]
    except TypeError:
        return 6.4
    # if y_position is None:
    #     y_position = 0
    #     return distance_data[x_position][y_position]
    # elif x_position is None:
    #     x_position = 0
    #     return distance_data[x_position][y_position]
    # else:
    #     return 0


# print(distance_data[1])
# print(calc_distance(10, 0))


# address_index functions in O(n) time to compare an address attribute parameter to the address
# column from addressCSV, and then return the index of that matched address
def address_index(address):
    with open('csv_files/addressCSV.csv', 'r') as f:
        for row in address_data:
            if address == row[2]:
                return int(row[0])


# Instantiation of the truck class is O(1)
class Truck:
    def __init__(self, pkg_max, avg_mph, pkg_load, pkg_load_r2, tot_miles, current_location, address, depart_time,
                 time, truck_name):
        super().__init__()
        self.pkg_max = pkg_max
        self.avg_mph = avg_mph
        self.pkg_load = pkg_load
        self.pkg_load_r2 = pkg_load_r2
        self.tot_miles = tot_miles
        self.current_location = current_location
        self.address = address
        self.depart_time = depart_time
        self.time = time
        self.truck_name = truck_name


def __lt__(self, package, next_address):
    if not isinstance(self, package):
        raise ValueError("Can't compare truck to non-truck type")
    return calc_distance(address_index(self.address), address_index(package.address)) < next_address


# O(1)
def __str__(self):
    return self.truck_name


# O(1)
def __repr__(self):
    return self.truck_name

# should not be needed to compare objects
# def __eq__(self, package):
#     if not isinstance(self, package):
#         raise ValueError("Can't compare book to non-truck type")
#     return calc_distance(address_index(self.address), address_index(package.address))
