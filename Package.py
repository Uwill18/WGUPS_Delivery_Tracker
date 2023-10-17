import csv

import MyHashMap


# O(1)
class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, mass, special_msg, status,
                 load_time, delivery_time):
        # super.__init__()
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.mass = mass
        self.special_msg = special_msg
        self.status = status
        self.load_time = load_time
        self.delivery_time = delivery_time

    # runs when debugging
    # O(1)
    def __repr__(self):
        return "PACKAGE #" + str(self.package_id) + ": " + self.address

    # runs in prod
    # returning the strings for the package object operate in O(1) time
    def __str__(self):
        # current_time = self.transit_time.strftime("%H:%M:%S")
        return ("PACKAGE #" + str(self.package_id) + ": < -- " +
                self.address + " , " +
                self.city + " , " +
                self.state + ", " +
                self.zipcode + " , " +
                self.mass + " , " +
                str(self.load_time) + " , " +
                str(self.deadline) + " , " +
                str(self.delivery_time) + " , " +
                self.status +
                " -" + self.special_msg + "-" +
                " > "

                )


# timeloaded = time truck takes off

# def load_package_data(hashmap):
#     with open('csv_files/packageCSV.csv', 'r') as f:
#         reader = list(csv.reader(f))
#         for row in reader[0:]:
#             print(row)
#
#
# print("\n\n package data below: \n\n")
# load_package_data(HashMap)

# O(1)
def get_package_id(self):
    return self.package_id


# O(1)
class PackageInfo:
    def __init__(self, address, city, state, zipcode, deadline, date, status):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.date = date
        self.status = status
