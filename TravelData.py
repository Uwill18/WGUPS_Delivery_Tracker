import csv

distance_data = []


def load_distance_data():
    with open('csv_files/distanceCSV.csv', 'r') as f:
        reader = list(csv.reader(f))
        for row in reader[0:]:
            distance_data.append(row)


address_data = []


def load_address_data():
    with open('csv_files/addressCSV.csv', 'r') as f:
        reader = list(csv.reader(f))
        for row in reader[0:]:
            address_data.append(row)


load_distance_data()
load_address_data()


# get adressname, and position for comparison

# Method for finding distance between two addresses


# https://www.linkedin.com/learning/python-object-oriented-programming/equality-and-comparison?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532

def distance_in_between(xpos, ypos):
    distance = distance_data[xpos][ypos]
    if distance == '':
        distance = distance_data[ypos][xpos]

    return float(distance)


# Method to get address number from string literal of address
def address_index(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])
