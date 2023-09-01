# Name: Uri W. Easter
# Student ID: 001433968


# Proverbs 16:9
# Psalm 32: 8
# Proverbs 3:5-6


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# G.  Provide an interface for the user to view the status and info (as listed in part F) of any package at any time, and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
#
# 1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.
# 2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.
# 3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.

# https://realpython.com/python-pep8/#naming-styles
# https://www.linkedin.com/learning/python-essential-training-18764650/csv?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
# https://www.youtube.com/watch?v=efSjcrp87OY
import csv
import datetime
import string
import sys

import TravelData
from MyHashMap import MyHashMap
from Package import Package
from Truck import calc_distance, address_index, Truck


def load_package_data():
    with open('csv_files/packageCSV.csv', 'r') as f:
        reader = list(csv.reader(f))
        for pkg_row in reader[0:]:
            pkg_id = pkg_row[0]
            pkg_address = pkg_row[1]
            pkg_city = pkg_row[2]
            pkg_state = pkg_row[3]
            pkg_zipcode = pkg_row[4]
            pkg_dt = pkg_row[5]
            pkg_mass = pkg_row[6]
            pkg_msg = pkg_row[7]
            pkg_status = "Loaded"

            pkg = Package(int(pkg_id), pkg_address, pkg_city,
                          pkg_state, pkg_zipcode, pkg_dt, pkg_mass,
                          pkg_msg, pkg_status)
            print(pkg)
            # instantiate hashtable and call insert f(x) to add packages by id
            pkg_hash_table.insert(pkg)  # review later

            # print(str(pkg_id))


first_truck = Truck(16, 18, [20, 13, 14, 15,
                             16, 19, 34, 26, 22, 11, 23, 31, 36, 24, 17], 0.0, "4001 South 700 East",
                    datetime.timedelta(hours=8))
second_truck = Truck(16, 18, [3, 36, 20, 40,
                              29, 10, 38, 5, 8, 27, 36, 40, 4, 1, 19], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

print(second_truck.pkg_load)

pkg_hash_table = MyHashMap()
load_package_data()

a = []

#how to get minimum distance formula to return minimum from x-dimension?
def minimum_distance(a):
    # distance = sys.maxsize
    minimum = TravelData.distance_data[26][7]
    for i in range(len(TravelData.distance_data)):
        for j in range(len(TravelData.distance_data[i])):
            if TravelData.distance_data[i][j] < minimum:
                minimum = TravelData.distance_data[i]
        print(minimum)
    #     for j in range(len(TravelData.distance_data[i])):
    #         if a[i] == a[j]:
    #             distance = min(distance, j - i)
    #
    # if distance == sys.maxsize:
    #     return -1
    # else:
    #     return distance


# print(first_truck.pkg_load)
# print(first_truck.tot_miles)
# print(range(len(TravelData.distance_data)))
print(len(TravelData.distance_data[3]))
print(TravelData.distance_data[26])
print(minimum_distance(TravelData.distance_data[5]))

#hub, packages, find address closest to hub, timestamp, and repeat
#with package id, can get string object, feed string address and get indices
#add distance * speed to get time, add time to current time for timestamp








