import csv

import MyHashMap


class Package:
    def __init__(self, package_id, address, city, state, zipcode, delivery_time, mass, special_msg, status,
                 transit_time):
        # super.__init__()
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_time = delivery_time
        self.mass = mass
        self.special_msg = special_msg
        self.status = status
        self.transit_time = transit_time

    # by comparison, use python datetime for relational operators
    # time loaded
    # time unloaded
    # time delivered

    # runs when debugging
    def __repr__(self):
        return "PACKAGE #" + str(self.package_id) + ": " + self.address

    # runs in prod
    def __str__(self):
        # current_time = self.transit_time.strftime("%H:%M:%S")
        return ("PACKAGE #" + str(self.package_id) + ": < " +
                self.address + " , " +
                self.city + " , " +
                self.zipcode + " , " +
                self.mass + " , " +
                self.status + " > "
                # + "(" + current_time + ")"
                )
        # print(self.transit_time)


# def load_package_data(hashmap):
#     with open('csv_files/packageCSV.csv', 'r') as f:
#         reader = list(csv.reader(f))
#         for row in reader[0:]:
#             print(row)
#
#
# print("\n\n package data below: \n\n")
# load_package_data(HashMap)


def get_package_id(self):
    return self.package_id


class PackageInfo:
    def __init__(self, address, city, state, zipcode, deadline, date, status):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.date = date
        self.status = status
