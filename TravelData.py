import csv

distance_data = []


# this function operates in O(n^2) time to generate
# a list of lists for all known distances between locations for the adjacency matrix
def load_distance_data(fileName):
    distanceData = []

    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            distList = [float(x) for x in row[0::] if x != ""]

            distanceData.append(distList)

    return distanceData


address_data = []


# This function operates in O(n^2) time to load all rows from the addressCSV file
# def load_address_data():
#     with open('csv_files/addressCSV.csv', 'r') as f:
#         reader = list(csv.reader(f))
#         for row in reader[0:]:
#             address_data.append(row)


def load_address_data(fileName):
    addressData = []

    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            addressData.append(str.strip(row[2]))

    return addressData

address_data = load_address_data("csv_files/addressCSV.csv")


# reads in all rows from the address CSV file
# load_address_data()

# distance data variable stores a list of lists for all known distances between locations for the adjacency matrix
distance_data = load_distance_data('csv_files/distanceCSV.csv')

# print(load_distance_data2('csv_files/distanceCSV.csv'))
# print(distance_data[10][1])
# print(len(distance_data))
# print(distance_data[10])
# get adressname, and position for comparison

# Method for finding distance between two addresses


# https://www.linkedin.com/learning/python-object-oriented-programming/equality-and-comparison?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
# https://stackoverflow.com/questions/42050219/python-how-to-tell-if-a-process-is-i-o-bound


# Method to get address number from string literal of address
