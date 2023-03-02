import csv


def Load_Packages(fileName):
    with open(fileName) as package_data:
        packageInfo = csv.reader(package_data, delimiter=',')
        next(packageInfo)
        for package in packageInfo:
            packID = int(package[0])
            packAddress = package[1]
            packCity =  package[2]
            packZip =  package[3]
            packState = package[4]
            packDeadline =  package[5]
            packStatus =  "Waiting to be Loaded"
            packWeight =  package[7]