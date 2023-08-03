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