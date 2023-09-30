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
import tkinter
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

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

            pkg = Package(int(pkg_id), pkg_address, pkg_city,
                          pkg_state, pkg_zipcode, pkg_dt, pkg_mass,
                          pkg_msg, pkg_status)
            print(pkg)
            # instantiate hashtable and call insert f(x) to add packages by id
            p_hash_table.insert(pkg)  # review later

            # print(str(pkg_id))


first_truck = Truck(16, 18, [28, 20, 14, 15, 16, 26, 22, 11, 23, 24, 12, 18, 19, 24, 13],
                    [29, 5, 8, 9, 39, 27, 35, 6, 32], 0.0, 0, "4001 South 700 East",
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

    # defining arrays for tree view
    id_list = []
    city_list = []
    address_list = []
    zip_list = []
    deadline_list = []
    # arrival_list = []

    weight_list = []
    status_list = []
    for pid in truck.pkg_load:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory.append(pkg_item)
        pkg_item.status = "Loaded"
        # print(pkg_item) #this line shows how each package item's status changes from at hub to loaded
        # print(pkg_inventory)
        status_list.append(pkg_item.status)
        weight_list.append(pkg_item.mass)
        deadline_list.append(pkg_item.delivery_time)
        zip_list.append(pkg_item.zipcode)
        address_list.append(pkg_item.address)
        city_list.append(pkg_item.city)
        id_list.append(pkg_item.package_id)

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
                next_pkg.status = "Delivered"
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
        next_pkg.departure_time = truck.depart_time
        print(str(truck.truck_name) + " TIME: " + str(truck.time) + ", DISTANCE: " + str(truck.tot_miles) + "\n" + str(
            next_pkg) + "\n")
        # print(str(pkg_inventory) + "\n")
    print(status_list)
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    print(truck.tot_miles, truck.time)
    # toDo:
    root = tk.Tk()
    root.geometry('1500x400')
    root.iconbitmap('C:/icons/space_owl.jpeg')
    root.title('WGUPS DELIVERY TRACKER')

    style = tkinter.ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                    foreground="#000",
                    rowheight=25,
                    fieldbackground="#003057")
    style.configure("Treeview.Heading", background="#003057", foreground='white')

    style.map('Treeview',
              background=[('selected', "#347083")])

    # tree_frame = tkinter.Frame(root)
    # # tree_frame.pack(pady=10)
    #
    # tree_scroll = tkinter.Scrollbar(tree_frame)
    # tree_scroll.pack(side = RIGHT , fill=Y)
    #
    # my_tree = tkinter.ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    #
    #
    # tree_scroll.config(command=my_tree.yview())

    # data

    # treeview
    # status_list.append(pkg_item.status)
    # weight_list.append(pkg_item.mass)
    # deadline_list.append(pkg_item.delivery_time)
    # zip_list.append(pkg_item.zipcode)
    # address_list.append(pkg_item.address)
    # city_list.append(pkg_item.city)
    # id_list.append(pkg_item.package_id)
    # table = tkinter.ttk.Treeview(root, columns=('ID', 'City', 'Address', 'Zipcode', 'Deadline', 'Status'),
    #                              show='headings')
    table = tkinter.ttk.Treeview(root, show='headings')
    table['columns'] = ('ID', 'City', 'Address', 'Zipcode', 'Deadline', 'Status')
    table.column("#0", width=0, stretch=NO)
    table.column("ID", anchor=CENTER, width=100)
    table.column("City", anchor=CENTER, width=140)
    table.column("Address", anchor=CENTER, width=225)
    table.column("Zipcode", anchor=CENTER, width=140)
    table.column("Deadline", anchor=CENTER, width=100)
    table.column("Status", anchor=CENTER, width=100)

    table.heading('ID', text='ID')
    table.heading('City', text='City')
    table.heading('Address', text='Address')
    table.heading('Zipcode', text='Zipcode')
    table.heading('Deadline', text='Deadline')
    table.heading('Status', text='Status', anchor=CENTER)

    # table.tag_configure('evenrow', background="black")

    # insert values into a table
    # table.insert(parent='', index=0,
    #              values=(id_list[0], city_list[0],
    #                      address_list[0], zip_list[0],
    #                      deadline_list[0], status_list[0]))

    for i in range(len(id_list)):
        #     table.insert(parent='', index=0, values=(id_list[i], city_list[i],
        #                                              address_list[i], zip_list[i], deadline_list[i], status_list[i]),
        #                  tags=('even row', ''))
        if i % 2:
            table.insert(parent='', index=0, values=(id_list[i], city_list[i],
                                                     address_list[i], zip_list[i], deadline_list[i], status_list[i]),
                         tags=('even row', 'lightblue'))
        else:
            table.insert(parent='', index=0, values=(id_list[i], city_list[i],
                                                     address_list[i], zip_list[i], deadline_list[i], status_list[i]),
                         tags=('odd row', 'lightblue'))

    table.tag_configure('even row', background="lightblue")
    table.tag_configure('odd row', background="white")
    table.pack()

    def item_select(_):
        print(table.selection())
        for i in table.selection():
            print(table.item(i)['values'])

    table.bind('<<TreeviewSelect>>', item_select)
    # run
    root.mainloop()



def pkg_distribution_r2(truck):
    pkg_inventory_two = []
    for pid in truck.pkg_load_r2:
        pkg_item = pkg_hash_table.lookup(pid)
        pkg_inventory_two.append(pkg_item)
        pkg_item.status = "Loaded"

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
        print(str(truck.truck_name) + " TIME: " + str(truck.time) + ", DISTANCE: " + str(truck.tot_miles) + "\n" + str(next_pkg) +"\n")
    distance_to_hub = calc_distance(address_index(truck.address), 0)
    truck.tot_miles += distance_to_hub
    truck.time += datetime.timedelta(hours=distance_to_hub / 18)
    print(truck.tot_miles, truck.time)


# def pkg_distribution_r1(truckA, truckB):
#     # Define an array of undelivered packages for distribution
#     pkg_inventory = []
#     pkg_inventory_two = []
#
#     # defining arrays for tree view
#     id_list = []
#     city_list = []
#     address_list = []
#     zip_list = []
#     deadline_list = []
#     # arrival_list = []
#
#     weight_list = []
#     status_list = []
#     for pid in truckA.pkg_load:
#         pkg_item = pkg_hash_table.lookup(pid)
#         pkg_inventory.append(pkg_item)
#         pkg_item.status = "Loaded"
#         # print(pkg_item) #this line shows how each package item's status changes from at hub to loaded
#         # print(pkg_inventory)
#         status_list.append(pkg_item.status)
#         weight_list.append(pkg_item.mass)
#         deadline_list.append(pkg_item.delivery_time)
#         zip_list.append(pkg_item.zipcode)
#         address_list.append(pkg_item.address)
#         city_list.append(pkg_item.city)
#         id_list.append(pkg_item.package_id)
#
#     for pid in truckB.pkg_load:
#         pkg_item = pkg_hash_table.lookup(pid)
#         pkg_inventory_two.append(pkg_item)
#         pkg_item.status = "Loaded"
#         # print(pkg_item) #this line shows how each package item's status changes from at hub to loaded
#         # print(pkg_inventory)
#         status_list.append(pkg_item.status)
#         weight_list.append(pkg_item.mass)
#         deadline_list.append(pkg_item.delivery_time)
#         zip_list.append(pkg_item.zipcode)
#         address_list.append(pkg_item.address)
#         city_list.append(pkg_item.city)
#         id_list.append(pkg_item.package_id)
#
#     # Cycle through the list of not_delivered until none remain in the list
#     # Adds the nearest package into the truck.packages list one by one
#     while len(pkg_inventory) > 0:
#         truckA.current_location = 0
#         truckB.current_location = 0
#         tA_next_address = 1500
#         tB_next_address = tA_next_address
#         tA_next_pkg = None
#         tB_next_pkg = tA_next_pkg
#
#         # Clear the package list of a given truck so the packages can be placed back into the truck in the order
#         # of the nearest neighbor
#
#         truckA.pkg_load.clear()
#         truckB.pkg_load.clear()
#
#         for p in pkg_inventory:
#             if calc_distance(address_index(truckA.address),
#                              address_index(p.address)) <= tA_next_address:
#                 tA_next_address = calc_distance(address_index(truckA.address),
#                                                 address_index(p.address))
#
#                 tA_next_pkg = p
#                 tA_next_pkg.status = "Delivered"
#                 # print("next package = { " + str(next_pkg) + "}\n")
#         # Adds next closest package to the truck package list
#         truckA.pkg_load.append(tA_next_pkg.package_id)
#
#         for p in pkg_inventory_two:
#             if calc_distance(address_index(truckB.address),
#                              address_index(p.address)) <= tB_next_address:
#                 tB_next_address = calc_distance(address_index(truckB.address),
#                                                 address_index(p.address))
#
#         # Removes the same package from the not_delivered list
#         pkg_inventory.remove(tA_next_pkg)
#         pkg_inventory_two.remove(tB_next_pkg)
#         # Takes the mileage driven to this packaged into the truck.mileage attribute
#         truckA.tot_miles += next_address
#         truckB.tot_miles += next_address
#         # Updates truck's current address attribute to the package it drove to
#         truckA.address = next_pkg.address
#         truckB.address = next_pkg.address
#         # Updates the time it took for the truck to drive to the nearest package
#         truckA.time += datetime.timedelta(hours=next_address / 18)
#         truckB.time += datetime.timedelta(hours=next_address / 18)
#         tA_next_pkg.delivery_time = truckA.time
#         tA_next_pkg.departure_time = truckA.depart_time
#         tB_next_pkg.delivery_time = truckB.time
#         tB_next_pkg.departure_time = truckB.depart_time
#         print(str(truckA.truck_name) + " TIME: " + str(truckA.time) + ", DISTANCE: " + str(truckA.tot_miles) + "\n" + str(
#             tA_next_pkg) + "\n")
#         print(
#             str(truckB.truck_name) + " TIME: " + str(truckB.time) + ", DISTANCE: " + str(truckB.tot_miles) + "\n" + str(
#                 tB_next_pkg) + "\n")
#         # print(str(pkg_inventory) + "\n")
#     print(status_list)
#     tA_distance_to_hub = calc_distance(address_index(truckA.address), 0)
#     truckA.tot_miles += tA_distance_to_hub
#     truckA.time += datetime.timedelta(hours=tA_distance_to_hub / 18)
#     tB_distance_to_hub = calc_distance(address_index(truckB.address), 0)
#     truckB.tot_miles += tB_distance_to_hub
#     truckB.time += datetime.timedelta(hours=tB_distance_to_hub / 18)
#     print(truckA.tot_miles, truckA.time)
#     print(truckB.tot_miles, truckB.time)






    # toDo:
    root = tk.Tk()
    root.geometry('1500x400')
    root.iconbitmap('C:/icons/space_owl.jpeg')
    root.title('WGUPS DELIVERY TRACKER')

    style = tkinter.ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                    foreground="#000",
                    rowheight=25,
                    fieldbackground="#003057")
    style.configure("Treeview.Heading", background="#003057", foreground='white')

    style.map('Treeview',
              background=[('selected', "#347083")])

    # tree_frame = tkinter.Frame(root)
    # # tree_frame.pack(pady=10)
    #
    # tree_scroll = tkinter.Scrollbar(tree_frame)
    # tree_scroll.pack(side = RIGHT , fill=Y)
    #
    # my_tree = tkinter.ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    #
    #
    # tree_scroll.config(command=my_tree.yview())

    # data

    # treeview
    # status_list.append(pkg_item.status)
    # weight_list.append(pkg_item.mass)
    # deadline_list.append(pkg_item.delivery_time)
    # zip_list.append(pkg_item.zipcode)
    # address_list.append(pkg_item.address)
    # city_list.append(pkg_item.city)
    # id_list.append(pkg_item.package_id)
    # table = tkinter.ttk.Treeview(root, columns=('ID', 'City', 'Address', 'Zipcode', 'Deadline', 'Status'),
    #                              show='headings')
    table = tkinter.ttk.Treeview(root, show='headings')
    table['columns'] = ('ID', 'City', 'Address', 'Zipcode', 'Deadline', 'Status')
    table.column("#0", width=0, stretch=NO)
    table.column("ID", anchor=CENTER, width=100)
    table.column("City", anchor=CENTER, width=140)
    table.column("Address", anchor=CENTER, width=225)
    table.column("Zipcode", anchor=CENTER, width=140)
    table.column("Deadline", anchor=CENTER, width=100)
    table.column("Status", anchor=CENTER, width=100)

    table.heading('ID', text='ID')
    table.heading('City', text='City')
    table.heading('Address', text='Address')
    table.heading('Zipcode', text='Zipcode')
    table.heading('Deadline', text='Deadline')
    table.heading('Status', text='Status', anchor=CENTER)



    # table.tag_configure('evenrow', background="black")

    # insert values into a table
    # table.insert(parent='', index=0,
    #              values=(id_list[0], city_list[0],
    #                      address_list[0], zip_list[0],
    #                      deadline_list[0], status_list[0]))

    for i in range(len(id_list)*2):
        #     table.insert(parent='', index=0, values=(id_list[i], city_list[i],
        #                                              address_list[i], zip_list[i], deadline_list[i], status_list[i]),
        #                  tags=('even row', ''))
        if i % 2:
            table.insert(parent='', index=0, values=(id_list[i], city_list[i],
                                                     address_list[i], zip_list[i], deadline_list[i], status_list[i]),
                         tags=('even row', 'lightblue'))
        else:
            table.insert(parent='', index=0, values=(id_list[i], city_list[i],
                                                     address_list[i], zip_list[i], deadline_list[i], status_list[i]),
                         tags=('odd row', 'lightblue'))

    table.tag_configure('even row', background="lightblue")
    table.tag_configure('odd row', background="white")
    table.pack()

    def item_select(_):
        print(table.selection())
        for i in table.selection():
            print(table.item(i)['values'])

    table.bind('<<TreeviewSelect>>', item_select)
    # run
    root.mainloop()


pkg_distribution_r1(first_truck)  # 36.0
pkg_distribution_r1(second_truck)  # 33.6
# pkg_distribution_r2(first_truck)  # 71.4
# pkg_distribution_r2(second_truck)  # 30.0
# print(first_truck.tot_miles + second_truck.tot_miles)  # 69.6 


# implement rounds of packages  Tuesday x


# get concurrent time working x
# Call package distribution functions x
# continue testing mileage, Monday
# finish final screen of gui, Thursday - Tuesday
# -------------------------------------------------
# test each of the gui pages, Wednesday
# connect the gui pages, Wednesday
# PART F, PART B, Thursday
# PARTS: A, D, I, K, Thursday
# Review project in context of WGU requirements, Friday
# Review project in context of Goodell requirements, Friday
# Review with Instructor, Friday
# Finish last parts of paper, Monday
# Submit Project, Monday
# ----------------------------------------------------------------------------------
# https://stackoverflow.com/questions/63239295/changing-background-color-of-ttk-treeview-heading
# https://stackoverflow.com/questions/61105126/tag-configure-is-not-working-while-using-theme-ttk-treeview
