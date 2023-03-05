# This is a sample Python script.
# import csv
import csv
from datetime import timedelta

import LoadCSVData
from LoadCSVData import Load_Packages


from Package import Package
from Truck import Truck
from Hashtable import Hashtable

packagesHashTable = Hashtable()


file = open("CSV Files/Distance Table.csv", "r")
distancedata = list(csv.reader(file, delimiter=","))
file.close()

print(distancedata)

file = open("CSV Files/Address.csv", "r")
addressdata = list(csv.reader(file, delimiter=","))
file.close()

print(addressdata)



LoadCSVData.Load_Packages("CSV Files/WGUPS Package File.csv", packagesHashTable)

Truck1 = Truck(timedelta(hours=10, minutes=30), 16, 18, [10, 9, 26, 28, 11, 12, 17, 22, 23, 24, 33, 35, 39], 0,
               "4001 South 700 East")


Truck2 = Truck(timedelta(hours=9, minutes=5), 16, 18, [3, 18, 36, 37, 38, 8, 30, 6, 31, 32, 5, 29, 7, 40], 0,
               "4001 South 700 East")


Truck3 = Truck(timedelta(hours=8), 16, 18, [1, 13, 14, 15, 16, 19, 20, 21, 34, 27, 2, 4, 25], 0, "4001 South 700 East")



def find_distances_between_addresses(truckaddress, packageaddress):
    distance = distancedata[truckaddress][packageaddress]

    #if distancedata [addressdata[truckaddress]][addressdata[packageaddress]] == "":
    if distance == "":
        return float (distancedata [ addressdata[packageaddress]] [addressdata[truckaddress]])
    return float(distancedata [addressdata[truckaddress]][ addressdata[packageaddress]])

def delivery(truck):
    Upnext = []

    while truck.Packages_loaded:
        NearestAddress = 100
        NextPackage = None
        for packageID in truck.Packages_loaded:
            package = packagesHashTable.search(packageID)

            Upnext.append(package)
            if find_distances_between_addresses(truck.Truck_location, package.Delivery_address) < NearestAddress:
                NearestAddress = find_distances_between_addresses(truck.Truck_location, package.Delivery_address)
                NextPackage = package
        truck.Truck_location = NextPackage.Delivery_address
        Upnext.append(NextPackage.packageID)
        truck.Packages_loaded.remove(NextPackage.packageID)
    truck.Packages_loaded = NextPackage

delivery(Truck1)
delivery(Truck2)
delivery(Truck3)




def main():
    k = Truck.Truck_location



