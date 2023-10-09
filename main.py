# Name: Uri W. Easter
# Student ID: 001433968


# Proverbs 16:9
# Psalm 32: 8
# Proverbs 3:5-6


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# G.  Provide an interface for the user to view the status and info (as listed in part F) of any package at any time,
# and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub,
# en route, or delivered. Delivery status must include the time.)
#
# 1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.
# 2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.
# 3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.

# https://realpython.com/python-pep8/#naming-styles
# https://www.linkedin.com/learning/python-essential-training-18764650/csv?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
# https://www.youtube.com/watch?v=efSjcrp87OY
import csv
# from datetime import datetime
from csv import writer
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
            pkg_loadtime = datetime.timedelta(hours=8)

            pkg = Package(int(pkg_id), pkg_address, pkg_city,
                          pkg_state, pkg_zipcode, pkg_dt, pkg_mass,
                          pkg_msg, pkg_status, pkg_loadtime)
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


# O (n^2)
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
        times_list.append(next_pkg.delivery_time)
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    time.sleep(2.5)
    # print(truck.tot_miles, truck.time)


times_list.clear()

# pkg_hash_table.update_hash()

times_list = []


# O(n^2)
def pkg_distribution_r2(truck):
    global time
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
        times_list.append(next_pkg.delivery_time)
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    time.sleep(2.5)
    # print(truck.tot_miles, truck.time)


# O(1)
def deliver_all():
    pkg_distribution_r1(first_truck)
    pkg_distribution_r1(second_truck)
    delivery_status()
    pkg_distribution_r2(first_truck)
    pkg_distribution_r2(second_truck)
    delivery_status()


# O(n)
def display_all():
    for i in range(1, 41):
        pkg_item = pkg_hash_table.lookup(i)
        print(pkg_item)


# O log n
# https://www.educba.com/python-keyboardinterrupt/

def track_one():
    try:
        id_searched = input("Please enter the ID of the package you would like to search!")
        pkg_searched = pkg_hash_table.lookup(int(id_searched))
        time_searched = input("Please enter the time you would like to search in HH:mm format :")
        (hh, mm) = time_searched.split(":")
        time_limit = datetime.timedelta(hours=23, minutes=59)
        time_entered = datetime.timedelta(hours=int(hh), minutes=int(mm))
        correction_time = datetime.timedelta(hours=10, minutes=20)
        if time_entered <= time_limit:
            if time_entered < pkg_searched.load_time:
                pkg_searched.status = "At Hub"
                print("\n" + str(pkg_searched) + "\n")
            elif time_entered < pkg_searched.delivery_time:
                pkg_searched.status = "En route"
                print(str(pkg_searched) + "\n")
            elif (time_entered >= correction_time) and (time_entered < pkg_searched.delivery_time):
                spc_pkg = pkg_hash_table.lookup(9)
                spc_pkg.address = "410 S. State St."
                spc_pkg.zipcode = "84111"
            else:
                pkg_searched.status = "Delivered"
                spc_pkg = pkg_hash_table.lookup(9)
                spc_pkg.address = "410 S. State St."
                spc_pkg.zipcode = "84111"
                print(str(pkg_searched) + "\n")
        else:
            print("\nInvalid input. Please decide if you would like to try again.")
            select_again()
    except ValueError:
        print("\nInvalid input. Please decide if you would like to try again.")
        select_again()
    except KeyboardInterrupt:
        exit()



# O log n
def track_all():
    try:
        time_searched = input("Please enter the time you would like to search in HH:mm format :")
        (hh, mm) = time_searched.split(":")
        time_entered = datetime.timedelta(hours=int(hh), minutes=int(mm))
        correction_time = datetime.timedelta(hours=10, minutes=20)
        time_limit = datetime.timedelta(hours=23, minutes=59)
        if time_entered <= time_limit:
            for i in range(1, 41):
                pkg_item = pkg_hash_table.lookup(i)
                if time_entered < pkg_item.load_time:
                    pkg_item.status = "At Hub"

                elif time_entered < pkg_item.delivery_time:
                    pkg_item.status = "En route"

                elif time_entered >= correction_time:
                    spc_pkg = pkg_hash_table.lookup(9)
                    spc_pkg.address = "410 S. State St."
                    spc_pkg.zipcode = "84111"
                else:
                    pkg_item.status = "Delivered"
            display_all()
        else:
            print("\nInvalid input. Please decide if you would like to try again.")
            select_again()
    except ValueError:
        print("\nInvalid input. Please decide if you would like to try again.")
        select_again()
    except KeyboardInterrupt:
        exit()


# O(1)
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
    try:
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
        print("-------------------------------------\n")
        select_option()
    except ValueError:
        program_exit_msg()
    except KeyboardInterrupt:
        exit()


# O(1) Time-Complexity
# https://discuss.codechef.com/t/switch-vs-if-else/13183/4
def select_option():
    try:
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
                program_exit_msg()
            case _:
                print("No option has been selected. Exiting program ")
                exit()
        select_again()
    except ValueError:
        print("\nInvalid input. Please decide if you would like to try again.")
        select_again()
    except KeyboardInterrupt:
        exit()


# O(1)
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
          "10. PROGRAM EXIT -- Exit the Program\n\n"
          "* Special Note : Both trucks have two routes each to meet all requirements for the program.\n\n")


# O(1)
def select_again():
    try:
        new_selection = input("\nIf you would like to make a new selection either 'y' or 'Y'. ")
        match new_selection:
            case "y" | "Y":
                print("\n")
                greet()
            case _:
                program_exit_msg()
                exit()
    except ValueError:
        print("\nInvalid input. Please decide if you would like to try again.")
        select_again()
    except KeyboardInterrupt:
        exit()


# O(1)
def program_exit_msg():
    print("\n----------🦉WGUPS DELIVERY TRACKER🦉-----------\n"
          "Thank you for using the WGUPS DELIVERY TRACKER!\n"
          "This python program  is made by: \n"
          "Author: Uri W. Easter\n"
          "Student ID: 001433968\n"
          "Python Version: 3.10.7\n"
          "-------------------------------------------------\n\n"

          "----------🦉WGUPS DELIVERY TRACKER🦉-----------\n"

          "🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍\n"
          "Special Thanks to Instructors Robert Ferdinand\n"
          "& Amy Antonucci for guiding me through this\n "
          "project, and giving me valuable insights into\n "
          "python!🐍\n"
          "🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍\n"
          "-------------------------------------------------"
          )
    time.sleep(2.5)
    print("\t\t🐍Exiting Program. Ciao!⛟")
    exit()


#
# def add_package():
#     new_selection = input("If you would like to make a new selection either 'y' or 'Y'.")
#     match new_selection:
#         case "y" | "Y":
#             with open('csv_files/packageCSV.csv', 'r') as f:
#                 rdr = csv.reader(f)
#                 address_dict = {int(address_row[0]): address_row[2] for address_row in rdr}
#             # with open('csv_files/packageCSV.csv', 'w') as w:
#                 pkg_id = len(address_dict) + 1
#                 print(pkg_id)
#
#                 pkg_address = input("Enter the destination address")
#                 pkg_city = input("Enter the destination city")
#                 pkg_state = input("Enter the destination state")
#                 pkg_zipcode = input("Enter the destination zipcode")
#                 pkg_dt = input("Enter the destination deadline")
#                 pkg_mass = int(input("Enter the package mass"))
#                 pkg_msg = input("Enter any special notes regarding the delivery")
#                 pkg_status = "Store Location"
#                 pkg_time_entered = input("Enter load time for distribution center in HH:mm format :")
#                 # time_format = datetime.strptime(time_searched, "%H:%M").time()
#                 # (HH, mm) = time_format.split(":")
#                 (HH, mm) = pkg_time_entered.split(":")
#                 pkg_loadtime = datetime.timedelta(hours=int(HH), minutes=int(mm))
#                 added_package = Package(pkg_id, pkg_address, pkg_city,
#                                         pkg_state, pkg_zipcode, pkg_dt, pkg_mass,
#                                         pkg_msg, pkg_status, pkg_loadtime)
#                 print(str(added_package))
#                 display_all()
#                 del added_package
#                 print("deleted added_package")
#                 display_all()
# pkg_hash_table.insert(added_package)
# added_package_list = [int(pkg_id), pkg_address, pkg_city,
#                         pkg_state, pkg_zipcode, pkg_dt, pkg_mass,
#                         pkg_msg, pkg_status, pkg_loadtime]
# Pass this file object to csv.writer()
# and get a writer object
# writer_object = writer(w)

# Pass the list as an argument into
# the writerow()
# writer_object.writerow(added_package_list)
# writer_object.delete()

# Close the file object
# f.close()
# case _:
#     greet()


# add_package()
greet()
# program_exit_msg()
# spc_pkg = pkg_hash_table.lookup(9)
# print(spc_pkg.address)
# print(spc_pkg.city)
# print(spc_pkg.state)
# print(spc_pkg.zipcode)


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
# revise track_one() function for pkg_item.loaded comparison Saturday x
# decide how you want info to display in the CLI Sunday x
# create an update function to update the delivery address of package #9 Monday x
# implement UI, its exit, exceptions next options loop Monday x


# -------------------------------------------------
# Review project in context of WGU requirements, Monday
# Review project in context of Goodell requirements, Monday
# PARTS: A, D,I, J Monday
# PARTS: B, C, G, H, Tuesday
# Review with Instructor, Tuesday
# PARTS:  Tues
# PART F, PART B, Thursday
# Finish last parts of paper, Friday
# Submit Project, Friday
# ----------------------------------------------------------------------------------
# 1. total mileage + final statuses of all packages
# with comments, and time of loading the truck
# 2. status of the package, given a time and package id
# 3. status of all packages at a given time
# 4. exit the program
