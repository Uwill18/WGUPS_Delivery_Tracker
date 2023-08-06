import csv

import HashMap


class Package:
    def __init__(self, package_id, address, city, state, zipcode, status):
        super.__init__()
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.status = status

        #by comparison, use python datetime for relational operators
        #time loaded
        #time unloaded
        #time delivered


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
