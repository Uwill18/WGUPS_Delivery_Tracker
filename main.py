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
# from datetime import datetime
from datetime import timedelta
from datetime import datetime
import datetime
import time

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
            pkg_status = "At Hub"
            pkg_transit_time = datetime.timedelta(hours=8)

            pkg = Package(int(pkg_id), pkg_address, pkg_city,
                          pkg_state, pkg_zipcode, pkg_dt, pkg_mass,
                          pkg_msg, pkg_status, pkg_transit_time)
            # print(pkg)
            # instantiate hashtable and call insert f(x) to add packages by id
            p_hash_table.insert(pkg)  # review later


first_truck = Truck(16, 18, [28, 20, 14, 15, 16, 26, 22, 11, 23, 24, 12, 18, 19, 24, 13],
                    [29, 37, 5, 8, 9, 39, 27, 35, 6, 32], 0.0, 0, "4001 South 700 East",
                    datetime.timedelta(hours=8), datetime.timedelta(hours=8), "First_Truck")
second_truck = Truck(16, 18, [21, 40, 4, 33, 2, 1, 7, 10, 38, 30, 3, 39, 36, 17, 31],
                     [34, 25, 18], 0.0,
                     0, "4001 South 700 East", datetime.timedelta(hours=8), datetime.timedelta(hours=8),
                     "Second_Truck")

pkg_hash_table = MyHashMap()
load_package_data('csv_files/packageCSV.csv', pkg_hash_table)

times_list = []


def pkg_distribution_r1(truck):
    # Define an array of undelivered packages for distribution
    global time
    pkg_inventory = []
    for pid in truck.pkg_load:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory.append(pkg_item)
        pkg_item.status = "Loaded"
        pkg_item.delivery_time = truck.time
        pkg_item.load_time = truck.depart_time

        # print(pkg_item) #this line shows how each package item's status changes from at hub to loaded
        # print(pkg_inventory)

    # Cycle through the list of not_delivered until none remain in the list
    # Adds the nearest package into the truck.packages list one by one
    while len(pkg_inventory) > 0:
        truck.current_location = 0
        next_address = 1500
        next_pkg = None

        # Clear the package list of a given truck so the packages can be placed back into the truck in the order
        # of the nearest neighbor

        truck.pkg_load.clear()

        for p in pkg_inventory:
            p.status = "En route"
            p.delivery_time = truck.time
            if calc_distance(address_index(truck.address),
                             address_index(p.address)) <= next_address:
                next_address = calc_distance(address_index(truck.address),
                                             address_index(p.address))
                next_pkg = p
                next_pkg.status = "Delivered"
                # next_pkg.transit_time = truck.time
                # print(next_pkg.transit_time)
                # print("next package = { " + str(next_pkg) + "}\n")
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
        # next_pkg.transit_time += truck.time
        next_pkg.departure_time = truck.depart_time
        pkg_hash_table.insert(next_pkg)
        # time.sleep(2.5)
        print(str(truck.truck_name) + " TIME: " + str(truck.time) + ", DISTANCE: " + str(truck.tot_miles) + "\n" + str(
            next_pkg) + "\n")
        # print("current hash " + str(pkg_hash_table.lookup(next_pkg.package_id)))
        # print(str(pkg_inventory) + "\n")
        times_list.append(next_pkg.delivery_time)
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    # time.sleep(2.5)
    # print(truck.tot_miles, truck.time)


times_list.clear()

# pkg_hash_table.update_hash()

times_list = []


def pkg_distribution_r2(truck):
    pkg_inventory_two = []
    for pid in truck.pkg_load_r2:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory_two.append(pkg_item)
        pkg_item.status = "Loaded"
        pkg_item.delivery_time = truck.time
        pkg_item.load_time = truck.depart_time

    # Cycle through the list of pkg_inventory_two until none remain in the list
    # Adds the nearest package into the truck.pkg_load_r2 list one by one
    while len(pkg_inventory_two) > 0:
        truck.current_location = 0
        next_address = 1500
        next_pkg = None

        # Clear the package list of a given truck so the packages can be placed back into the truck in the order
        # of the nearest neighbor

        truck.pkg_load_r2.clear()

        for p in pkg_inventory_two:
            p.status = "En route"
            if calc_distance(address_index(truck.address),
                             address_index(p.address)) <= next_address:
                next_address = calc_distance(address_index(truck.address),
                                             address_index(p.address))
                next_pkg = p
                # print("next package = { " + str(next_pkg) + "}\n")
        # Adds next closest package to the truck package list
        truck.pkg_load_r2.append(next_pkg.package_id)
        next_pkg.status = "Delivered"

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
        pkg_hash_table.insert(next_pkg)
        # time.sleep(2.5)
        print(str(truck.truck_name) + " TIME: " + str(truck.time) + ", DISTANCE: " + str(truck.tot_miles) + "\n" +
              str(next_pkg) + "\n")
        # print(str(truck.truck_name) + " TIME: " + str(truck.time) + ", DISTANCE: " + str(truck.tot_miles) + "\n" +
        #       str(next_pkg) + " (" + str(next_pkg.delivery_time) + " )" + "\n")
        # print(next_pkg.departure_time)
        times_list.append(next_pkg.delivery_time)
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    # time.sleep(2.5)
    # print(truck.tot_miles, truck.time)


def deliver_all():
    pkg_distribution_r1(first_truck)
    pkg_distribution_r1(second_truck)
    delivery_status()
    pkg_distribution_r2(first_truck)
    pkg_distribution_r2(second_truck)
    delivery_status()


def display_all():
    for i in range(1, 41):
        pkg_item = pkg_hash_table.lookup(i)
        print(pkg_item)


# put in a time-loaded attribute, and compare input time to time loaded
def track_one():
    id_searched = input("Please enter the ID of the package you would like to search!")
    pkg_searched = pkg_hash_table.lookup(int(id_searched))
    time_searched = input("Please enter the time you would like to search in HH:mm format :")
    # time_format = datetime.strptime(time_searched, "%H:%M").time()
    # (hh, mm) = time_format.split(":")
    (hh, mm) = time_searched.split(":")
    time_entered = datetime.timedelta(hours=int(hh), minutes=int(mm))
    if time_entered <= pkg_searched.load_time:
        pkg_searched.status = "At Hub"
        print(pkg_searched)

    # if (time_entered > pkg_searched.transit_time) and (time_entered < times_list[0]):
    #     pkg_searched.status = "Loaded"
    #     print(pkg_searched)

    if (time_entered > times_list[0]) and (time_entered < pkg_searched.delivery_time):
        pkg_searched.status = "En route"
        print(pkg_searched)

    if time_entered >= pkg_searched.delivery_time:
        pkg_searched.status = "Delivered"
        print(pkg_searched)


def track_all():
    time_searched = input("Please enter the time you would like to search in HH:mm format :")
    # time_format = datetime.strptime(time_searched, "%H:%M").time()
    # (HH, mm) = time_format.split(":")
    (HH, mm) = time_searched.split(":")
    time_entered = datetime.timedelta(hours=int(HH), minutes=int(mm))
    start_time = datetime.timedelta(hours=8, minutes=0)

    for i in range(1, 41):
        pkg_item = pkg_hash_table.lookup(i)
        if time_entered < pkg_item.load_time:
            pkg_item.status = "At Hub"
            # print(start_time)
            # print(pkg_item.transit)

        elif time_entered < pkg_item.delivery_time:
            pkg_item.status = "En route"
            # print("times_list times")
            # print(times_list[0])
            # print(pkg_item)

        else:
            pkg_item.status = "Delivered"
    display_all()


def delivery_status():
    print("\n")
    display_all()
    print("\n")
    print("🚚DELIVERY STATUS📦:")
    print(str(first_truck.truck_name) + " TIME:" + str(first_truck.time) +
          ", DISTANCE: " + str(first_truck.tot_miles) + "\n")  # format function like pkg_distro
    print(str(second_truck.truck_name) + " TIME:" + str(second_truck.time) +
          ", DISTANCE: " + str(second_truck.tot_miles) + "\n")
    print("TOTAL DISTANCE: " + str(first_truck.tot_miles + second_truck.tot_miles) + "\n")


# O(1) Time complexity
def greet():
    print("-------🦉WGUPS DELIVERY TRACKER🦉---------")
    print("Hello! Welcome to WGUPS DELIVERY TRACKER!!")
    print("Please select from one of the options below:\n")
    print("1. CHECK FULL DELIVERY CYCLE \n"
          "2. TRACK PACKAGE \n"
          "3. TRACK ALL PACKAGES \n"
          "4. CHECK ROUTE ONE OF FIRST TRUCK \n"
          "5. CHECK ROUTE ONE OF SECOND TRUCK \n"
          "6. CHECK ROUTE TWO OF FIRST TRUCK \n"
          "7. CHECK ROUTE TWO OF SECOND TRUCK \n"
          "8. VERIFY DELIVERY STATUS \n"
          "9. DEFINE ALL OPTIONS\n"
          "10. PROGRAM EXIT \n")
    print("-------🦉WGUPS DELIVERY TRACKER🦉---------\n")
    select_option()


# O(1) Time-Complexity
# https://discuss.codechef.com/t/switch-vs-if-else/13183/4
def select_option():
    option = input("Please enter your option here:")
    match option:
        case "1":
            deliver_all()
        case "2":
            track_one()
        case "3":
            track_all()
        case "4":
            pkg_distribution_r1(first_truck)
        case "5":
            pkg_distribution_r1(second_truck)
        case "6":
            pkg_distribution_r2(first_truck)
        case "7":
            pkg_distribution_r2(second_truck)
        case "8":
            delivery_status()
        case "9":
            define_options()
        case "10":
            exit()
        case _:
            again = input("If you would like to select another option enter and underscore:")
            if again == true:
                select_option()
            else:
                exit()


def define_options():
    print("\n1. CHECK FULL DELIVERY CYCLE --  See the total mileage and complete journey of all routes taken  \n\n"
          "2. TRACK PACKAGE -- Use package ID and time to track the status of one package at any time \n\n"
          "3. TRACK ALL PACKAGES -- Enter a time to track the status of all packages at any time \n\n"
          "4. CHECK ROUTE ONE OF FIRST TRUCK --  See the total mileage and journey of truck one of its first route \n\n"
          "5. CHECK ROUTE ONE OF SECOND TRUCK --  See the total mileage and journey of truck two of its first route\n\n"
          "6. CHECK ROUTE TWO OF FIRST TRUCK --  See the total mileage and journey of truck one of its second route\n\n"
          "7. CHECK ROUTE TWO OF SECOND TRUCK --  See the total mileage and journey of truck two of its second "
          "route\n\n"
          "8. VERIFY DELIVERY STATUS -- for any route, check the mileage of all trucks and the status of all "
          "packages\n\n"
          "9. DEFINE ALL OPTIONS -- Descriptions as shown here illuminate the effect of user selections\n\n"
          "10. PROGRAM EXIT -- Exit the Program\n\n")


def program_exit_msg():
    print("----------🦉WGUPS DELIVERY TRACKER🦉-----------\n"
          "Thank you for using the WGUPS DELIVERY TRACKER!\n"
          "This python program  is made by: \n"
          "Author: Uri W. Easter\n"
          "Student ID: 001433968\n"
          "Python Version: 3.10.7\n"
          "-------------------------------------------------\n\n"

          "----------🦉WGUPS DELIVERY TRACKER🦉-----------\n"

          "🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍\n"
          "Special Thanks to Instructors Robert Ferdinand\n"
          "and Amy Antonucci for guiding me through this \n "
          "project, and giving me valuable insights into\n "
          "python!🐍\n"
          "🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍\n"
          "-------------------------------------------------"
          )
    time.sleep(20)
    print("\t\t🐍Exiting Program. Ciao!⛟")

    # track_all()

    # print("STATUS = " + str(pkg_searched.status))
    # print("DELIVERY TIME " + str(pkg_searched.delivery_time))

    # time_searched = input("Please enter the time you would like to search in HH:mm format :")
    # ptime = datetime.strptime(time_searched, "%H:%M").time()
    # ptest = pkg_hash_table.check_timeline(ptime)
    # print("Test " + ptest)
    # exception for no input "Program Exit"
    # exception for incorrect input "Invalid Input. Please Try Again.."


greet()
program_exit_msg()
# deliver_all()
# track_one()
# pkg_distribution_r1(first_truck)  # 36.0
# track_one()


# track_all()
# pkg_distribution_r1(second_truck)  # 33.6
# delivery_status()
# track_all()

# pkg_distribution_r2(first_truck)  # 71.4
# track_one()
# track_all()
# display_all()
# pkg_hash_table.check_timeline(29)
# track_one()
# print("verifying " + str(pkg_hash_table.lookup(14).status))

# track_all()
# pkg_distribution_r2(second_truck)  # 30.0
# track_all()
# print(first_truck.tot_miles + second_truck.tot_miles)  # 69.6
# pkg_distribution_r3(first_truck, second_truck)


# print("🚚🦉WGUPS DELIVERY TRACKER🦉⛟")

# implement rounds of packages  Tuesday x
# get concurrent time working x
# Call package distribution functions x
# reviewing resources x Wednesday
# based on research I think I want to implement multiprocessing techniques for the trucks x  Weekend
# threading could be used for the files x Weekend
# continue testing mileage, Monday x
# find how to get arrival time for each package x
# cast back everything back to time x
# implement the sleep function x
# find out how to search for each package as the function goes x
# find how to print out all packages, with statuses at end of both routes(3) x
# revise track_one() function for pkg_item.loaded comparison Saturday
# decide how you want info to display in the CLI Sunday x
# create an update function to update the delivery address of package #9 Monday
# implement UI, and its exit, and exceptions Monday


# -------------------------------------------------
# Review project in context of WGU requirements, Tuesday
# Review project in context of Goodell requirements, Tuesday
# Review with Instructor, Tuesday
# PARTS: A, D, I, K, Wednesday
# PART F, PART B, Thursday
# Finish last parts of paper, Friday
# Submit Project, Friday
# ----------------------------------------------------------------------------------
# 1. total mileage + final statuses of all packages
# with comments, and time of loading the truck

# 2. status of the package, given a time and package id

# 3. status of all packages at a given time
# 4. exit the program
