# https://www.linkedin.com/learning/python-object-oriented-programming/equality-and-comparison?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
from random import random

from TravelData import distance_data, address_data


def calc_distance(x_position, y_position):
    if(x_position >= y_position):
        return distance_data[x_position][y_position]
    else:
        return distance_data[y_position][x_position]


#print(distance_data[1])
calc_distance(10,12)





def address_index(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])


class Truck:
    def __init__(self, pkg_max, avg_mph, pkg_load, tot_miles, address, depart_time):
        super().__init__()
        self.pkg_max = pkg_max
        self.avg_mph = avg_mph
        self.pkg_load = pkg_load
        self.tot_miles = tot_miles
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time


def __lt__(self, package, next_address):
    if not isinstance(self, package):
        raise ValueError("Can't compare truck to non-truck type")
    return calc_distance(address_index(self.address), address_index(package.address)) < next_address

#should not be needed to compare objects
# def __eq__(self, package):
#     if not isinstance(self, package):
#         raise ValueError("Can't compare book to non-truck type")
#     return calc_distance(address_index(self.address), address_index(package.address))
