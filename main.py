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


first_truck = Truck(16, 18, [28, 20, 14, 15, 16, 26, 22, 11, 23, 24, 12, 18, 19, 24,13],
                    [29,5,8,9,39,27,35,6,32], 0.0, 0, "4001 South 700 East",
                    datetime.timedelta(hours=8), "First_Truck")
second_truck = Truck(16, 18, [21, 40, 4, 33, 2, 1, 7, 10, 38, 30, 3, 39, 36, 17, 31],
                     [34, 25, 18], 0.0,
                     0, "4001 South 700 East", datetime.timedelta(hours=8),
                     "Second_Truck")

pkg_hash_table = MyHashMap()
load_package_data('csv_files/packageCSV.csv', pkg_hash_table)

with open('csv_files/addressCSV.csv', 'r') as f:
    rdr = csv.reader(f)
    address_dict = {int(address_row[0]): address_row[2] for address_row in rdr}
    print(address_dict.keys())


def pkg_distribution_r1(truck):
    # Define an array of undelivered packages for distribution
    pkg_inventory = []
    for pid in truck.pkg_load:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory.append(pkg_item)
        # print(pkg_inventory)

    # Cycle through the list of not_delivered until none remain in the list
    # Adds the nearest package into the truck.packages list one by one
    while len(pkg_inventory) > 0:
        truck.current_location = 0
        next_address = 2000
        next_pkg = None

        # Clear the package list of a given truck so the packages can be placed back into the truck in the order
        # of the nearest neighbor

        truck.pkg_load.clear()

        for p in pkg_inventory:
            if calc_distance(address_index(truck.address),
                             address_index(p.address)) <= next_address:
                next_address = calc_distance(address_index(truck.address),
                                             address_index(p.address))
                next_pkg = p
                print("next package = { " + str(next_pkg) + "}\n")
        # Adds next closest package to the truck package list
        truck.pkg_load.append(next_pkg.package_id)

        # Removes the same package from the not_delivered list
        pkg_inventory.remove(next_pkg)
        # Takes the mileage driven to this packaged into the truck.mileage attribute
        truck.tot_miles += next_address
        # Updates truck's current address attribute to the package it drove to
        truck.address = next_pkg.address
        # Updates the time it took for the truck to drive to the nearest package
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_pkg.delivery_time = truck.time
        next_pkg.departure_time = truck.depart_time
        print(str(truck.truck_name) + " TIME: " + str(truck.time) + ", DISTANCE: " + str(truck.tot_miles) + "\n" + str(
            pkg_inventory))
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    print(truck.tot_miles, truck.time)


def pkg_distribution_r2(truck):
    pkg_inventory_two = []
    for pid in truck.pkg_load_r2:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory_two.append(pkg_item)

    # Cycle through the list of not_delivered until none remain in the list
    # Adds the nearest package into the truck.packages list one by one
    while len(pkg_inventory_two) > 0:
        truck.current_location = 0
        next_address = 2000
        next_pkg = None

        # Clear the package list of a given truck so the packages can be placed back into the truck in the order
        # of the nearest neighbor

        truck.pkg_load_r2.clear()

        for p in pkg_inventory_two:
            if calc_distance(address_index(truck.address),
                             address_index(p.address)) <= next_address:
                next_address = calc_distance(address_index(truck.address),
                                             address_index(p.address))
                next_pkg = p
                print("next package = { " + str(next_pkg) + "}\n")
        # Adds next closest package to the truck package list
        truck.pkg_load_r2.append(next_pkg.package_id)

        # Removes the same package from the not_delivered list
        pkg_inventory_two.remove(next_pkg)
        # Takes the mileage driven to this packaged into the truck.mileage attribute
        truck.tot_miles += next_address
        # Updates truck's current address attribute to the package it drove to
        truck.address = next_pkg.address
        # Updates the time it took for the truck to drive to the nearest package
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_pkg.delivery_time = truck.time
        next_pkg.departure_time = truck.depart_time
        print(str(truck.truck_name) + " TIME: " + str(truck.time) + ", DISTANCE: " + str(truck.tot_miles) + "\n" + str(
            pkg_inventory_two))
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    print(truck.tot_miles, truck.time)


pkg_distribution_r1(first_truck)  # 36.0
pkg_distribution_r1(second_truck)  # 33.6
pkg_distribution_r2(first_truck)  # 71.4
pkg_distribution_r2(second_truck)  # 30.0
print(first_truck.tot_miles + second_truck.tot_miles)  # 69.6

# implement rounds of packages  Tuesday x
# get concurrent time working x
# Call package distribution functions x
# continue testing mileage, Monday
# finish final screen of gui, Wednesday
# PART F, PART B, Wednesday
# test each of the gui pages, Thursday
# connect the gui pages, Thursday
# PARTS: A, D, I, K, Thursday
# Review project in context of WGU requirements, Friday
# Review project in context of Goodell requirements, Friday
# Finish last parts of paper, Friday
# Review with Instructor, Monday
# Submit Project, Monday


# ----------------------------------------------------------------------------------
