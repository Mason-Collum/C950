import csv

from Hashtable import Hashtable
from Package import Package


def Load_Packages(fileName,  packagesHashTable):
    with open(fileName) as package_data:
        packageInfo = csv.reader(package_data, delimiter=",")
        next(packageInfo)
        for package in packageInfo:
            packID = int(package[0])
            packAddress = package[1]
            packCity =  package[2]
            packZip =  package[3]
            packState = package[4]
            packDeadline =  package[5]
            packWeight =  package[6]
            packStatus =  "Waiting to be Loaded"

            p = Package(packID, packAddress, packCity, packZip, packState, packDeadline, packWeight, packStatus)



            packagesHashTable.insert(packID, p)






