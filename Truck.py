#https://www.linkedin.com/learning/python-object-oriented-programming/equality-and-comparison?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
class Truck:
    def __init__(self, currentAddress, pkg_load, pkg_max, avg_mph, tot_miles):
        self.currentAddress = currentAddress
        self.pkg_load = pkg_load
        self.pkg_max = pkg_max
        self.avg_mph = avg_mph
        self.tot_miles = tot_miles
