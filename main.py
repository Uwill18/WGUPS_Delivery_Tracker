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


def load_package_data(csvfile, p_hash_table):
    with open(csvfile) as file:
        reader = list(csv.reader(file))
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
            p_hash_table.insert(pkg)  # review later

            # print(str(pkg_id))


first_truck = Truck(16, 18, [20, 13, 14, 15, 16, 19, 34, 26, 22, 11, 23, 31, 36, 24, 17],
                    [18, 25, 32, 6], 0.0, 0, "4001 South 700 East",
                    datetime.timedelta(hours=8), "First_Truck")
second_truck = Truck(16, 18, [3, 36, 20, 40, 29, 10, 38, 5, 8, 27, 40, 4, 1, 19],
                     [3, 36, 20, 40, 29, 10, 38, 5, 8, 27, 36, 40, 4, 1, 19], 0.0,
                     0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20),
                     "Second_Truck")

pkg_hash_table = MyHashMap()
load_package_data('csv_files/packageCSV.csv', pkg_hash_table)

with open('csv_files/addressCSV.csv', 'r') as f:
    rdr = csv.reader(f)
    address_dict = {int(address_row[0]): address_row[2] for address_row in rdr}
    print(address_dict.keys())


def pkg_distribution(truckA, truckB):
    # Define an array of undelivered packages for distribution
    pkg_inventory = []
    for pid in truckA.pkg_load:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory.append(pkg_item)
        # print(pkg_inventory)

    pkg_inventory_two = []
    for pid in truckB.pkg_load_r2:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory_two.append(pkg_item)

    # Cycle through the list of not_delivered until none remain in the list
    # Adds the nearest package into the truck.packages list one by one
    while len(pkg_inventory or pkg_inventory_two) > 0:
        truckA.current_location = 0
        truckB.current_location = 0
        A_next_address = 2000
        A_next_pkg = None
        B_next_address = 2000
        B_next_pkg = None

        # Clear the package list of a given truck so the packages can be placed back into the truck in the order
        # of the nearest neighbor

        truckA.pkg_load.clear()
        truckB.pkg_load_r2.clear()

        for pkgs_a in pkg_inventory:
            if calc_distance(address_index(truckA.address),
                             address_index(pkgs_a.address)) <= A_next_address:
                A_next_address = calc_distance(address_index(truckA.address),
                                               address_index(pkgs_a.address))
                A_next_pkg = pkgs_a
                print("next package = { " + str(A_next_pkg) + "}\n")
        # Adds next closest package to the truck package list
        truckA.pkg_load.append(A_next_pkg.package_id)

        for pkgs_b in pkg_inventory_two:
            if calc_distance(address_index(truckB.address),
                             address_index(pkgs_b.address)) <= B_next_address:
                next_address = calc_distance(address_index(truckB.address),
                                             address_index(pkgs_b.address))
                B_next_pkg = pkgs_b
                print("next package = { " + str(B_next_pkg) + "}\n")
        # Adds next closest package to the truck package list
        truckB.pkg_load.append(B_next_pkg.package_id)

        # Removes the same package from the not_delivered list
        pkg_inventory.remove(A_next_pkg)
        pkg_inventory_two.remove(B_next_pkg)
        # Takes the mileage driven to this packaged into the truck.mileage attribute
        truckA.tot_miles += A_next_address
        truckB.tot_miles += B_next_address
        # Updates truck's current address attribute to the package it drove to
        truckA.address = A_next_pkg.address
        truckB.address = B_next_pkg.address
        # Updates the time it took for the truck to drive to the nearest package
        truckA.time += datetime.timedelta(hours=next_address / 18)
        A_next_pkg.delivery_time = truckA.time
        A_next_pkg.departure_time = truckA.depart_time

        truckB.time += datetime.timedelta(hours=next_address / 18)
        B_next_pkg.delivery_time = truckB.time
        B_next_pkg.departure_time = truckB.depart_time
        print(
            str(truckA.truck_name) + " TIME: " + str(truckA.time) + ", DISTANCE: " + str(truckA.tot_miles) + "\n" + str(
                pkg_inventory))


# def pkg_distribution_r2(truckA, truckB):
#     pkg_inventory_two = []
#     for pid in truck.pkg_load_r2:
#         pkg_item = pkg_hash_table.lookup(pid)
#         pkg_inventory_two.append(pkg_item)
#
#
#     # Cycle through the list of not_delivered until none remain in the list
#     # Adds the nearest package into the truck.packages list one by one
#     while len(pkg_inventory_two) > 0:
#         truck.current_location = 0
#         next_address = 2000
#         next_pkg = None
#
#         # Clear the package list of a given truck so the packages can be placed back into the truck in the order
#         # of the nearest neighbor
#
#         truck.pkg_load_r2.clear()
#
#         for p in pkg_inventory_two:
#             if calc_distance(address_index(truck.address),
#                              address_index(p.address)) <= next_address:
#                 next_address = calc_distance(address_index(truck.address),
#                                              address_index(p.address))
#                 next_pkg = p
#                 print("next package = { " + str(next_pkg) + "}\n")
#         # Adds next closest package to the truck package list
#         truck.pkg_load_r2.append(next_pkg.package_id)
#
#         # Removes the same package from the not_delivered list
#         pkg_inventory_two.remove(next_pkg)
#         # Takes the mileage driven to this packaged into the truck.mileage attribute
#         truck.tot_miles += next_address
#         # Updates truck's current address attribute to the package it drove to
#         truck.address = next_pkg.address
#         # Updates the time it took for the truck to drive to the nearest package
#         truck.time += datetime.timedelta(hours=next_address / 18)
#         next_pkg.delivery_time = truck.time
#         next_pkg.departure_time = truck.depart_time
#         print(str(truck.truck_name) + " TIME: " + str(truck.time) + ", DISTANCE: " + str(truck.tot_miles) + "\n" + str(
#             pkg_inventory_two))


pkg_distribution(first_truck, second_truck)
# pkg_distribution_r2(second_truck,first_truck)
# pkg_distribution_r1(second_truck)
# pkg_distribution_r2(first_truck)

print(first_truck.tot_miles + second_truck.tot_miles)

# implement rounds of packages  Tuesday x
# get concurrent time working
# Call package distribution functions
# Review WGU requirements
# Review Goodell requirements
# finish final screen of gui
# ----------------------------------------------------------------------------------
# try to get results printed to screen
# test each of the gui pages
# connect the gui pages
