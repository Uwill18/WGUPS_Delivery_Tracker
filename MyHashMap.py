# C950 - Webinar-1 - Let’s Go Hashing
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Modified for Key:Value
import csv


# HashTable class using chaining.
# Develop a hash table, without using any additional libraries or classes,
# that has an insertion function that takes the following components as input and inserts the components into the hash table:
#
# •   package ID number, package_id
# all "delivery properties will  output delivery + property name when called"
# •   delivery address,  address string
# •   delivery deadline, deadline string because of EOD
# •   delivery city    , city string
# •   delivery zip code, zip int
# •   package weight   , weight int
# •   delivery status (e.g., delivered, en route) , status  comparison function
#   special_message
# https://realpython.com/python-pep8/#naming-styles

# 1. pull attributes from csv file
# 2. use Let's go Hashing: https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71
# 3. Modify this using:
# https://www.linkedin.com/learning/programming-foundations-data-structures-2/understanding-hash-functions?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
# https://www.linkedin.com/learning/programming-foundations-data-structures-2/understanding-hash-tables?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
# https://www.linkedin.com/learning/programming-foundations-data-structures-2/using-dictionaries-in-python?autoSkip=true&contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532

# 4. Modify one more time using:
# https://www.linkedin.com/learning/programming-foundations-algorithms/unique-filtering-with-hash-table?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=2045532
# https://learn.zybooks.com/zybook/WGUC950AY20182019/chapter/9/section/3


# https://www.geeksforgeeks.org/implementation-of-hashing-with-chaining-in-python/
# Hashing is a data structure that is used to store a large amount of data,
# which can be accessed in O(1) time by operations such as search, insert and delete.




class MyHashMap:
    def __init__(self):
        self.package_list = []
        # setting up the inner lists for hashmap
        # i.e. for each bucket this function creates ten inner arrays
        for i in range(10):
            self.package_list.append([])

    def insert(self, package):
        # this function is picking the right bucket, then putting the package in that bucket
        hash_index = package.package_id % 10
        self.package_list[hash_index].append(package)

    # the lookup loop through inner bucket to search for object with hash that has been passed

    def lookup(self, packageID: int):
        hashIndex = packageID % 10
        for p in self.package_list[hashIndex]:
            if int(p.package_id) == packageID:
                return p
        return None

    def update_hash(self):
        self.package_list = []
        # setting up the inner lists for hashmap
        # i.e. for each bucket this function creates ten inner arrays
        for i in range(40):
            lookup(i)
        return self.package_list

    def __str__(self):
        retstr = ""
        for i in range(10):
            retstr += str(i) + ":" + str(self.package_list[i])
            retstr += '\n'
        return retstr


# https://www.youtube.com/watch?v=4HKqjENq9OU

# https://www.youtube.com/watch?v=ojjnd5gEMuk

# https://youtu.be/rTEtEy5o3X0

# https://www.youtube.com/watch?v=xtaom__-drE
# https://www.neuralnine.com/k-nearest-neighbors-classification-from-scratch-in-python/


# https://www.youtube.com/watch?v=KURydVL0kGQ
