import csv
import Truck
import MyHashMap


# O(1)
class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, mass, special_msg, status,
                 load_time, delivery_time, truck_name):
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
        self.truck_name = truck_name

    # runs when debugging
    # O(1)
    def __repr__(self):
        return "PACKAGE #" + str(self.package_id) + ": " + self.address

    # runs in prod
    # returning the strings for the package object operate in O(1) time
    """to format the package output I used the below reference: 
    https://medium.com/@glasshost/format-a-number-to-a-fixed-width-in-python-714685333048?source=rss-------1#:~:text
    =One%20way%20to%20format%20a,and%20precision%20of%20the%20number.&text=In%20the%20example%20above%2C%20the,
    characters%2C%20with%202%20decimal%20places."""

    def __str__(self):
        # current_time = self.transit_time.strftime("%H:%M:%S")
        if self.package_id < 10:
            return ("\033[40m" +
                    "{:16}".format(f"\033[40m\033[3mPACKAGE #0{self.package_id}\033[0m\033[40m |< :") +
                    "{:40}".format(f"{self.address},") +
                    "{:25}".format(f"{self.city}, ") +
                    "{:7}".format(f"{self.state}, ") +
                    "{:9}".format(f"{self.zipcode}, ") +
                    "{:5}".format(f"{self.mass}, ") +
                    "{:12}".format(f"{str(self.load_time)}, ") +
                    "{:12}".format(f"{str(self.deadline)}, ") +
                    "{:25}".format(f"{str(self.delivery_time)},") +
                    "{:30}".format(f"\033[40m{self.status}\033[40m on {self.truck_name}\033[40m:") +
                    "{:55}".format(f"{self.special_msg}>\033[0m")
            )
        else:
            return (
                "\033[40m" +
                "{:16}".format(f"\033[40m\033[3mPACKAGE #{self.package_id}\033[0m\033[40m |< :") +
                "{:40}".format(f"{self.address},") +
                "{:25}".format(f"{self.city}, ") +
                "{:7}".format(f"{self.state}, ") +
                "{:9}".format(f"{self.zipcode}, ") +
                "{:5}".format(f"{self.mass}, ") +
                "{:12}".format(f"{str(self.load_time)}, ") +
                "{:12}".format(f"{str(self.deadline)}, ") +
                "{:25}".format(f"{str(self.delivery_time)},") +
                "{:30}".format(f"\033[40m\033[3m{self.status}\033[40m on {self.truck_name}\033[40m:") +
                "{:55}".format(f"{self.special_msg}>")
                )

        # return (f"PACKAGE #{self.package_id} | < : {self.address}, "
        #         f"{self.city}, {self.state}, {self.zipcode},"
        #         f" {self.mass}, {str(self.load_time)}, "
        #         f"{str(self.deadline)}, {str(self.delivery_time)},"
        #         f"{self.status}:{self.special_msg}>"
        #         )
        # return ("PACKAGE #" + str(self.package_id) + "| < :" +
        #         self.address + " , " +
        #         self.city + " , " +
        #         self.state + ", " +
        #         self.zipcode + " , " +
        #         self.mass + " , " +
        #         str(self.load_time) + " , " +
        #         str(self.deadline) + " , " +
        #         str(self.delivery_time) + " , " +
        #         self.status +
        #         ": " + self.special_msg + "> "
        #         )


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
