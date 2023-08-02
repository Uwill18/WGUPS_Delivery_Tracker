# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# G.  Provide an interface for the user to view the status and info (as listed in part F) of any package at any time, and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
#
# 1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.
# 2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.
# 3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.

#https://realpython.com/python-pep8/#naming-styles
import csv

f = open('WGUPSPackageFile.csv', 'r')
for line in f.readlines():
    print(line.strip())

f = open('WGUPSPackageFileOutput.txt', 'w')
print(f)

with open('WGUPSPackageFile.csv', 'r') as f:
    reader = list(csv.reader(f))
    for row in reader[1:]:
        print(row)
# print(f)
# print(f.readline())
# print(f.readlines())

# with open('10_02_us.csv', 'r') as f:
#     reader = csv.reader(f, delimiter='\t')
#     for row in reader:
#         print(row)
#
# import csv
# with open('some.csv', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)