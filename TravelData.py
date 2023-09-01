import csv

distance_data = []


# def load_distance_data():
#     with open('csv_files/distanceCSV.csv', 'r') as f:
#         reader = list(csv.reader(f))
#         for row in reader[0:]:
#             distance_data.append(row)


def loadDistanceData2(fileName):

    distanceData = []

    with open(fileName) as csv_file:

        csv_reader = csv.reader(csv_file, delimiter = ',')

        for row in csv_reader:

            distList = [float(x) for x in row[0 : :] if x != ""]

            distanceData.append(distList)

    return distanceData


address_data = []


def load_address_data():
    with open('csv_files/addressCSV.csv', 'r') as f:
        reader = list(csv.reader(f))
        for row in reader[0:]:
            address_data.append(row)


# load_distance_data()
load_address_data()
print(loadDistanceData2('csv_files/distanceCSV.csv'))
distance_data = loadDistanceData2('csv_files/distanceCSV.csv')
print(distance_data[10][1])
print(len(distance_data))
print(distance_data[10])
# get adressname, and position for comparison

# Method for finding distance between two addresses


# https://www.linkedin.com/learning/python-object-oriented-programming/equality-and-comparison?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532




# Method to get address number from string literal of address


