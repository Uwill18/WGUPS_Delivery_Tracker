# Name: Uri W. Easter
# Student ID: 001433968
# Date: 10/27/2023

# Proverbs 16:9
# Psalm 32: 8
# Proverbs 3:5-6


# https://realpython.com/python-pep8/#naming-styles
# https://www.linkedin.com/learning/python-essential-training-18764650/csv?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
# https://www.youtube.com/watch?v=efSjcrp87OY
import csv
from datetime import datetime
import datetime
import time
from MyHashMap import MyHashMap
from Package import Package
from Truck import (calc_distance, address_index, Truck)
import os

"""##########################################OBJECT INSTANTIATION START###########################################
This section first instantiates objects through pulling attribute data from class files, csv files, and libraries
 native to python (such as datetime, and time). The objects will be used in the next section for major algorithms
 to deliver packages per the project requisites, and to output data to show that those requisites are met."""
global time


# This block instantiates the series of packages and loads csv column data to package attributes
def load_package_data(csvfile, p_hash_table):
    with open(csvfile) as file:
        reader = list(csv.reader(file))
        for pkg_row in reader[0:]:
            pkg_id = pkg_row[0]
            pkg_address = pkg_row[1]
            pkg_city = pkg_row[2]
            pkg_state = pkg_row[3]
            pkg_zipcode = pkg_row[4]
            pkg_deadline = pkg_row[5]
            pkg_mass = pkg_row[6]
            pkg_msg = pkg_row[7]
            pkg_status = "At Hub"
            pkg_loadtime = datetime.timedelta(hours=8)
            # pkg_dt = pkg_loadtime
            pkg_dt = pkg_loadtime
            pkg_truck = "\033[3mLoading Dock\033[0m"

            pkg = Package(int(pkg_id), pkg_address, pkg_city,
                          pkg_state, pkg_zipcode, pkg_deadline, pkg_mass,
                          pkg_msg, pkg_status, pkg_loadtime, pkg_dt, pkg_truck)
            # print(pkg)
            # instantiate hashtable and call insert f(x) to add packages by id
            p_hash_table.insert(pkg)


pkg_hash_table = MyHashMap()
load_package_data('csv_files/packageCSV.csv', pkg_hash_table)

# The instantiation of the trucks are both O(1) instructions
first_truck = Truck(16, 18, [28, 20, 14, 15, 16, 34, 26, 25, 22, 11, 23, 24, 12, 13, 19],
                    [7, 5, 9, 8, 27, 35, 32], 0.0, 0, "4001 South 700 East",
                    datetime.timedelta(hours=8), datetime.timedelta(hours=8), "\033[3mTruck_One\033[0m")
second_truck = Truck(16, 18, [40, 4, 33, 2, 1, 29, 10, 38, 37, 30, 3, 39, 36, 6, 17, 31],
                     [21, 18], 0.0,
                     0, "4001 South 700 East", datetime.timedelta(hours=8), datetime.timedelta(hours=8),
                     "\033[3mTruck_Two\033[0m")

"""""""""###LIST REFACTOR####""""""""""""
THIS INFORMATION SHOWS THE ALIGNMENT OF PACKAGES
TO ASSIGNED ROUTES. THE INFORMATION WAS RECONFIGURED
ACCORDING TO  THE SPECIFICATIONS OF DEADLINES AND 
SPECIAL MESSAGES. ADJUSTING PACKAGES ACCORDING TO
ROUTE ALSO HELPED MAINTAINABILITY OF THE CODE.
I HOPE THIS  NOTE IS HELPFUL FOR THE NEXT DEVELOPER
WHO NEEDS THIS.

route one list:
WGU HUB,4001 South 700 East,84107
 -- 28
3595 S Main St, South Salt Lake, 84115 -- 20 
4300 S 1300 E, Salt Lake City, UT, 84124 -- 14
4580 S 2300 E. Salt Lake City, UT, 84117 -- 15,16 | 34
5383 S 900 E. Salt Lake City, UT 84117 -- 26      | 25
6351 S. 900 E. Salt Lake City, UT, 84121 -- 22
2600 Taylorsville Blvd. Salt Lake City, UT, 84129 -- 11
5100 S 2700 W. Salt Lake City, UT, 84129 -- 23
5025 S State St, Salt Lake City, UT,84107 -- 24
W. Valley Home Avenue, West Valley City, UT, 84119 -- 12
1488 4800 S, 84123 -- 18
177 W Price Avenue,South Salt Lake, 84115  -- 19
WGU HUB,4001 South 700 East,84107 -- 24
[28,20,14,15,
16,26,22,11,
23,24,12,18,
19,24] --t1r1
[34,25] --t2r1
----------------------------------------------------------------
route two list :
3595 S Main St, South Salt Lake, 84115 -- 21
380 W 2880 S, South Salt Lake, 84115 -- 40, 4
2530 S 500 E,  South Salt Lake, 84106 -- 33 , 2
195 W Oakland Ave,South Salt Lake,84115 -- 1
1330 E 2100 S, Salt Lake City, UT,84105 -- 7 | 29
600 S 900 E, Salt Lake City, UT,84102 -- 10
410 S State St, Salt Lake,84111 -- 38,5 | 9
300 S State St, Salt Lake,84111 -- 30, 8 
233 N. Canyon Rd., Salt Lake City, UT,84103 -- 3
2010 W. 500 S., Salt Lake City, UT,84104 -- 13|39
1060 W Dalton Avenue, Salt Lake City, UT,84104 -- | 27,35
2300 W Pkwy Blvd,West Valley City,84119 --36
3060 S Lester St,West Valley City,84119 -- | 6
3148 S 1100 W, South Salt Lake, 84119 -- 17
County Gov't -- 31| 32
177 W Price Avenue,South Salt Lake, 84115
WGU HUB,4001 South 700 East,8410"""
"""""" """"""
"""""""""
TEXT FORMATTING SOURCES:
https://www.sololearn.com/discuss/2359764/how-can-i-put-formated-text-in-python-bold-italic-etc
https://gist.github.com/dnmellen/5584007
https://www.kodeclik.com/how-to-bold-text-in-python/
https://stackoverflow.com/questions/40419276/python-how-to-print-text-to-console-as-hyperlink#:~:text=If%20you%20print%20a%20URL,options%20is%20%22Open%20link%22.&text=You%20just%20print%20it%20syntactically,job%20of%20the%20terminal%20application.
https://docs.python.org/2/library/string.html#format-specification-mini-language
https://i.stack.imgur.com/lZr23.png
https://www.youtube.com/watch?v=LXV53NKfKQI&t=595s
"""""""""

times_list = []

"""##########################################OBJECT INSTANTIATION END###########################################"""

"""##########################################MAJOR ALGORITHM START##########################################"""
"""
Both of these major blocks operate in O (n^2) due to the nested looping. These functions are nearest neighbor
implementations. There are two to allow both trucks to run two different routes at the same time.
I was going to suggest the functions were O (log n) but there are no operations where variables are multiplied
or divided by a constant amount.
"""


def pkg_distribution_r1(truck):
    # Define an array of packages for distribution
    # print("_" * 250)
    pkg_inventory = []
    for pid in truck.pkg_load:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory.append(pkg_item)
        pkg_item.status = "Loaded"
        pkg_item.delivery_time = truck.time
        pkg_item.load_time = truck.depart_time
        pkg_item.truck_name = truck.truck_name

    # Cycle through the pkg_inventory list until no packages remain in the list
    # Adds the nearest package into the truck.pkg_load one by one
    while len(pkg_inventory) > 0:
        truck.current_location = 0
        next_address = 1500
        next_pkg = None

        # Clear the package load of a given truck before ordering them for
        # delivery according to the nearest neighbor algorithm

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
                # next_pkg.truck_name = truck.truck_name
        # Appends the next package to the truck package load using proximity to the nearest address
        truck.pkg_load.append(next_pkg.package_id)

        # Removes the same package from the pkg_inventory
        pkg_inventory.remove(next_pkg)
        # Adds the mileage driven to this package to the current value of the attribute truck.tot_miles
        truck.tot_miles += next_address
        # This line updates the truck's current address to the address where it had last delivered a package
        truck.address = next_pkg.address
        # This reflects the time taken for the truck to drive to the nearest package
        pkg_hash_table.insert(next_pkg)
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_pkg.delivery_time = truck.time
        next_pkg.departure_time = truck.depart_time
        pkg_hash_table.insert(next_pkg)
        time.sleep(1.5)
        final_mileage = "{:.2f}".format(truck.tot_miles)
        print("\033[40m_" * 250)
        print(
            "{:12}".format(f"\033[40m{truck.truck_name}") + "\033[40m TIME: " + "{:10}".format(
                f"{truck.time}") + ", DISTANCE: " + str(
                final_mileage))
        display_header()
        print(str(next_pkg) + "\n")
        print("_" * 250)
        times_list.append(next_pkg.delivery_time)
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    print("\033[32m\033[40m_" * 250)
    print("\n\033[1mTHE CURRENT DELIVERY STATUS OF ALL PACKAGES IS THE RESULT OF " + truck.truck_name +
          "\033[40m\033[32m's FIRST ROUTE")
    print("_" * 250 + "\033[0m\n\n")
    time.sleep(5)
    correction_time = datetime.timedelta(hours=10, minutes=20)
    spc_pkg = pkg_hash_table.lookup(9)
    if truck.time >= correction_time:
        spc_pkg.address = "410 S State St"
        spc_pkg.zipcode = "84111"


times_list.clear()

times_list = []


# Major block O(n^2)
def pkg_distribution_r2(truck):
    # print("_" * 250)
    global time
    pkg_inventory_two = []
    for pid in truck.pkg_load_r2:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory_two.append(pkg_item)
        pkg_item.status = "Loaded"
        pkg_item.delivery_time = truck.time
        pkg_item.load_time = truck.depart_time
        pkg_item.truck_name = truck.truck_name

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
        pkg_hash_table.insert(next_pkg)
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_pkg.delivery_time = truck.time
        next_pkg.departure_time = truck.depart_time
        final_mileage = "{:.2f}".format(truck.tot_miles)
        time.sleep(1.5)
        print("\033[40m_" * 250)
        print("{:12}".format(f"\033[40m{truck.truck_name}") + "\033[40m TIME: " + "{:10}".format(
            f"{truck.time}") + ", DISTANCE: " + str(
            final_mileage) + "\n")
        display_header()
        print(str(next_pkg) + "\n")
        print("_" * 250)

        times_list.append(next_pkg.delivery_time)
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    print("\033[32m\033[40m_" * 250)
    print("\n\033[1mTHE CURRENT DELIVERY STATUS OF ALL PACKAGES IS THE RESULT OF " + truck.truck_name +
          "\033[40m\033[32m's SECOND ROUTE")
    print("_" * 250 + "\033[0m\n\n\n")
    time.sleep(5)
    correction_time = datetime.timedelta(hours=10, minutes=20)
    spc_pkg = pkg_hash_table.lookup(9)
    if truck.time >= correction_time:
        spc_pkg.address = "410 S State St"
        spc_pkg.zipcode = "84111"


"""#############################################MAJOR ALGORITHM END##############################################"""

"""###################################MAJOR USER INTERFACE FUNCTIONS START######################################"""
"""This section is devoted to the functions that comprise the user interface. They have been placed in an order 
similar to how the user will first interact with them when the program runs, then the remaining functions are 
parallel to the options that the user will choose from."""

"""This major block referred to as the greet function has O(1) Time complexity as it outputs strings of text, and asks for minor text input which 
will be passed to another function. These O(1) operations make this function O(1) time complexity."""


def greet():
    try:
        print("")
        print(
            "\033[0;34;40m\033[4m\033[3m-------\033[0m\033[40m\033[1m🦉WGUPS DELIVERY TRACKER🦉\033[0m\033[94m\033[4m\033[40m---------\033[0m\033[40m")
        print("\033[3m\033[1m\033[40mHello! Welcome to WGUPS DELIVERY TRACKER!!")
        print("Please select from one of the options below:\033[0m\033[40m\n")
        print(  # "1. No longer available for evaluators\n"
            "\033[1m\033[40m1. TRACK PACKAGE \n"
            "2. TRACK ALL PACKAGES \n"
            "3. PROGRAM EXIT \033[0m\033[40m\n")
        print("\033[34m------------------------------------------\033[0m\033[40m\n\033[40m")
        select_option()
    except ValueError:
        program_exit_msg()
    except KeyboardInterrupt:
        exit()


"""This major block has O(n^2) Time-Complexity by evaluation of the worst-case. It would be O(1) but it makes a call to
a non-constant time function. The source cited from Geeks for Geeks says that "The time complexity of a function 
(or set of statements) is considered as O(1) if it doesn’t contain a loop, recursion, and call to any other 
non-constant time function. i.e. set of non-recursive and non-loop statements" 
https://discuss.codechef.com/t/switch-vs-if-else/13183/4 
# https://www.geeksforgeeks.org/how-to-analyse-loops-for-complexity-analysis-of-algorithms/"""


def select_option():
    try:
        option = input("\033[0m\033[3m\nPlease enter your option number here:")
        match option:
            # case "1":
            #     deliver_all()
            case "1":
                track_one()
            case "2":
                track_all()
            case "3":
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


"""This major block is O(n^2) by the worst case scenario. The deliver_all() function orchestrates the intended order
for package delivery, and gives a delivery status halfway through the delivery, and then at the end to see the total
mileage between both trucks, and the status of all packages. This function consists mainly of consecutive function calls
and mimics O(1) statements. The pkg_distribution functions are O(n^2), therefore this function by worst-case analysis is
also O(n^2)"""


def deliver_all():
    try:
        spaces = '' * 1000
        print("\rA7 Software presents..", end='')
        time.sleep(5)
        print("\rin Affiliation with H2APPs ", end='')
        time.sleep(5)
        print("\rWGUPS DELIVERY TRACKER v4.0", end='')
        time.sleep(7)
        print('\r' + spaces, end="")
        print("\033[42m\033[30m_" * 250)
        print("\nWGUPS Delivery Tracker simulates delivering 40 packages per each one's delivery requirements"
              "\nand deadlines while also keeping the total travel distance for all delivery trucks under 140 miles.\n")
        print("\033[42m\033[30m_" * 250)
        print("\033[0m")

        print("\033[32m\033[40m_" * 250)
        print("\nTo achieve these objectives two routes were mapped out from the attached SLC downtown map routes,\n"
              "and each truck is assigned a route of delivery for its first round, then both trucks swap routes for\n"
              "their second route.")
        print("\033[32m\033[40m_" * 250)
        print("\033[0m")
        # time.sleep(10)

        print("\033[42m\033[30m_" * 250)
        print("\nThis results in the four sets of output  printed out to show each route traveled by each truck,\n"
              "along with mileage reports, and updates for the delivery status of all 40 packages after each\n"
              "segment.This takes 120 seconds on average to complete and enables the supervisor to see\n"
              "at each assigned point,the progress of each truck and its packages, with the attribute details\n"
              "of each package. Once all four segments are complete,and the fourth mileage report shows the final\n"
              "mileage for both trucks,then the user can select one of three options to continue with the\n"
              "application's execution.\n")
        print("\033[42m\033[30m_" * 250)
        print("\033[0m")
        time.sleep(15)

        print("\033[32m\033[40m_" * 250)
        print("\nThe total distance for all routes will show as 117.10 miles.This is achieved by the usage of the "
              "\nNearest Neighbor Algorithm which finds the minimum distance between a grouping of points before"
              "\nmapping to the next smallest distance in range.This method produces the most optimized paths for"
              "\ndelivering all packages quickly and well within the required distance limit of 140 miles.\n")
        print("\033[32m\033[40m_" * 250)
        print("\033[0m")
        time.sleep(15)

        print("\033[42m\033[30m_" * 250)
        print("\nOnce  all packages have been delivered one can search for any one of forty packages by selecting the\n"
              "option '1.TRACK PACKAGE'. Then enter the PACKAGE ID# for the hashmap to identify the correct package\n"
              "for retrieval by the id number. Finally, input the time you would like to search in military time,\n"
              "also known as 24h format.\n")
        print("\033[42m\033[30m_" * 250)
        print("\033[0m")
        time.sleep(8)

        print("\033[32m\033[40m_" * 250)
        print("\nTo track all packages for any given time you can select the option '2. TRACK ALL PACKAGES'"
              "\nand then enter the time you would like to search in military time a.k.a. 24h format."
              "\nIf you need help with converting to military time/24h time please click the link below:\n"
              "https://helpingwithmath.com/wp-content/uploads/2022/12/image-1024x625.png\n"
              )
        print("\033[32m\033[40m_" * 250)
        print("\033[0m")
        time.sleep(10)

        print('\r' + spaces, end="")
        print("\033[0;34;40m\033[4m\033[3m-------\033[0m\033[40m\033[1m🦉WGUPS DELIVERY TRACKER v4.0🦉\033[0m\033["
              "94m\033[4m\033[40m---------\033[0m\033[40m", end="")

        pkg_distribution_r1(first_truck)
        delivery_status()
        pkg_distribution_r1(second_truck)
        delivery_status()
        pkg_distribution_r2(first_truck)
        delivery_status()
        pkg_distribution_r2(second_truck)
        delivery_status()
    except KeyboardInterrupt:
        exit()


"""This major block known as track_one() is also O(n^2) due to the nested if statements for time comparisons.
track_one() allows the user to track a package with time and id inputs, and the nested if statements ensure
that the time entered is not out of range.
#The source below was useful to decipher the exact exception needed when stopping the program with the stop button:
 https://www.educba.com/python-keyboardinterrupt/"""


def track_one():
    try:
        print("\nIf you need help with converting to military time/24h format please visit the link below:"
              "\nhttps://helpingwithmath.com/wp-content/uploads/2022/12/image-1024x625.png\n")
        id_searched = input("Please enter the ID of the package you would like to search!")
        pkg_searched = pkg_hash_table.lookup(int(id_searched))
        time_searched = input("Please enter the time you would like to search in military time (HH:mm format):\033[0m")
        print("\n")
        (hh, mm) = time_searched.split(":")
        time_limit = datetime.timedelta(hours=23, minutes=59)
        time_entered = datetime.timedelta(hours=int(hh), minutes=int(mm))
        correction_time = datetime.timedelta(hours=10, minutes=20)
        if time_entered <= time_limit:
            spc_pkg = pkg_hash_table.lookup(9)
            if time_entered < pkg_searched.load_time:
                pkg_searched.status = "\033[90mAt Hub\033[0m"
                spc_pkg.address = "300 State St"
                spc_pkg.zipcode = "84103"
                display_header()
                print("\n" + str(pkg_searched) + "\n")
            elif time_entered < pkg_searched.delivery_time:
                if time_entered < correction_time:
                    pkg_searched.status = "\033[33mEn route\033[0m"
                    spc_pkg.address = "300 State St"
                    spc_pkg.zipcode = "84103"
                    display_header()
                    print(str(pkg_searched) + "\n")
                else:
                    spc_pkg.address = "410 S State St"
                    spc_pkg.zipcode = "84111"
                    spc_pkg.status = "\033[33mEn route\033[0m"
                    display_header()
                    print(str(pkg_searched) + "\n")
            else:
                pkg_searched.status = "\033[92mDelivered\033[0m"
                spc_pkg = pkg_hash_table.lookup(9)
                spc_pkg.address = "410 S. State St."
                spc_pkg.zipcode = "84111"
                display_header()
                print(str(pkg_searched) + "\n")

        else:
            print("\nInvalid input. Please decide if you would like to try again.")
            select_again()
    except ValueError:
        print("\nInvalid input. Please decide if you would like to try again.")
        select_again()
    except KeyboardInterrupt:
        exit()


def display_header():
    print("{:12}".format(f"\033[40m" +
                         "{:15}".format(f"PACKAGE ID# |    ") +
                         "{:40}".format(f"ADDRESS") +
                         "{:23}".format(f"CITY") +
                         "{:8}".format(f"STATE") +
                         "{:8}".format(f"ZIPCODE") +
                         "{:5}".format(f"MASS") +
                         "{:15}".format(f"LOADTIME") +
                         "{:22}".format(f"STATUS") +
                         "{:16}".format(f"DELIVERY TIME") +
                         "{:12}".format(f"DEADLINE") +
                         "{:55}".format(f"SPECIAL MESSAGES")))
    print("_" * 250)


"""This major function block known as display_all() is O(n) since it has one for loop in which the output is 
proportional to the length of that for loop's range. I also used the below reference to format the section headers: 
https://medium.com/@glasshost/format-a-number-to-a-fixed-width-in-python-714685333048?source=rss-------1#:~:text=One
%20way%20to%20format%20a,and%20precision%20of%20the%20number.&text=In%20the%20example%20above%2C%20the,
characters%2C%20with%202%20decimal%20places."""


def display_all():
    # print("PACKAGE # |\t\t\tADDRESS\t\t\t|\tCITY\t|STATE|ZIP|"
    #       "MASS| LOAD TIME | DEADLINE | DELIVERY TIME "
    #       "| STATUS | SPECIAL MESSAGE ")
    print("{:15}".format(f"\033[40mALL PACKAGES|    ") +
          "{:40}".format(f"ADDRESS") +
          "{:23}".format(f"CITY") +
          "{:8}".format(f"STATE") +
          "{:8}".format(f"ZIPCODE") +
          "{:5}".format(f"MASS") +
          "{:15}".format(f"LOADTIME") +
          "{:23}".format(f"STATUS") +
          "{:16}".format(f"DELIVERY TIME") +
          "{:12}".format(f"DEADLINE") +
          "{:55}".format(f"SPECIAL MESSAGES"))
    print("\033[40m_" * 250)
    # print("\033[40m\033[0m")
    # place code here for solution 2
    for i in range(1, 41):
        pkg_item = pkg_hash_table.lookup(i)
        print(pkg_item)


"""
#This major function block a.k.a track_all() also classifies as an O(n^2) much like track_one() due to the same
time validation executed by the nested looping. Most technically it is O(n^3), but that is a form of O(n^2).
"""


def track_all():
    try:
        print("\nIf you need help with converting to military time/24h format please visit the link below:"
              "\nhttps://helpingwithmath.com/wp-content/uploads/2022/12/image-1024x625.png\n")
        time_searched = input("Please enter the time you would like to search in military time (HH:mm format):")
        (hh, mm) = time_searched.split(":")
        time_entered = datetime.timedelta(hours=int(hh), minutes=int(mm))
        correction_time = datetime.timedelta(hours=10, minutes=20)
        time_limit = datetime.timedelta(hours=23, minutes=59)
        if time_entered <= time_limit:
            for i in range(1, 41):
                pkg_item = pkg_hash_table.lookup(i)
                spc_pkg = pkg_hash_table.lookup(9)
                if time_entered < pkg_item.load_time:
                    pkg_item.status = "\033[90mAt Hub\033[0m"
                    spc_pkg.address = "300 State St"
                    spc_pkg.zipcode = "84103"

                elif time_entered < pkg_item.delivery_time:
                    pkg_item.status = "\033[33mEn route\033[0m"
                    if time_entered >= correction_time:
                        spc_pkg.address = "410 S State St"
                        spc_pkg.zipcode = "84111"
                    else:
                        spc_pkg.address = "300 State St"
                        spc_pkg.zipcode = "84103"
                else:
                    pkg_item.status = "\033[92mDelivered\033[0m"
                    spc_pkg.address = "410 S State St"
                    spc_pkg.zipcode = "84111"
            print("\n")
            display_all()
        else:
            print("\nInvalid input. Please decide if you would like to try again.")
            select_again()
    except ValueError:
        print("\nInvalid input. Please decide if you would like to try again.")
        select_again()
    except KeyboardInterrupt:
        exit()


"""the delivery_status() is a major block that operates in O(1) time. This function outputs strings consisting of
the truck's names, the timing of the trucks to complete a delivery cycle/ route, as well as total mileage of both
trucks since the third truck was not used."""


def delivery_status():
    print("\033[40m\033[1m_" * 250 + "")
    print("📦DELIVERY STATUS📦:")
    print("\033[40m_" * 250)
    display_all()
    print("\033[40m\033[1m_" * 250)
    print("\033[0m")
    time.sleep(5)
    truck_one_mileage = "{:.2f}".format(first_truck.tot_miles)
    truck_two_mileage = "{:.2f}".format(second_truck.tot_miles)
    tot_mileage = "{:.2f}".format(first_truck.tot_miles + second_truck.tot_miles)
    print("\n\033[40m" + "*" * 250)
    print("\n\033[1m🚚MILEAGE REPORT⛟:\033[0m\033[40m\n")
    print("\033[40m\033[3m" + str(first_truck.truck_name) + "\033[40m | TIME:" + str(first_truck.time) +
          ", DISTANCE: " + truck_one_mileage + " MILES \n")  # format function like pkg_distro
    print(str(second_truck.truck_name) + "\033[40m | TIME:" + str(second_truck.time) +
          ", DISTANCE: " + truck_two_mileage + " MILES \n")
    print("TOTAL DISTANCE: " + str(tot_mileage) + " MILES\033[40m\n")
    print("*" * 250 + "\n\033[0m")
    time.sleep(5)


"""This major block define_options() has O(1) Time complexity as it only outputs strings of text.
These O(1) operations make this function O(1) time complexity."""


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


"""This major block select_again() has O(1) Time complexity as it outputs strings of text, and asks for minor text input which 
will be passed to another function. These O(1) operations make this function O(1) time complexity."""


def select_again():
    try:
        new_selection = input("\033[0m\033[1m\nIf you would like to make a new selection type 'Y'."
                              "To exit, type any other key. ")
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


"""This major block program_exit_msg() has O(1) Time complexity as it only outputs strings of text.
These O(1) operations make this function O(1) time complexity."""


def program_exit_msg():
    print("\n\033[40m----------🦉WGUPS DELIVERY TRACKER🦉-----------\n"
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
    print("\t\t🐍Exiting Program. Ciao!⛟\n\033[0m")
    exit()


"""###############################MAJOR USER INTERFACE FUNCTIONS END######################################"""

"""RELEVANT TO PART J OF THE PAPER"""
# SCALING FUNCTION PSEUDOCODE:
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


deliver_all()
greet()

#
# for i in range(10):
#     print("Loading" + "." * i)
#     # sys.stdout.write("\033[F\033[K") # Cursor up one line
#     sys.stdout.flush()
#     time.sleep(1)
# add_package()
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
# Review project in context of WGU requirements, Monday x
# Review project in context of Goodell requirements, Monday x
# PARTS: A,G,H,J Monday,
#        B, C,(L) Tuesday
#        D, K,(L) Wednesday
#        I,(L) Thursday
#
#
# Finish last parts of paper, Friday
# Submit Project, Friday
# ----------------------------------------------------------------------------------
# 1. total mileage + final statuses of all packages
# with comments, and time of loading the truck
# 2. status of the package, given a time and package id
# 3. status of all packages at a given time
# 4. exit the program

# --final tasks
# --input a header X
# --record a panopto - 2
# --rewrite your paper - 1
# --write instructions for the evaluator  - 3
# --input a truck name field x
