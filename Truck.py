class Truck:


    def __init__(self, Depart_time, Truck_capacity, Truck_speed, Packages_loaded, Miles_traveled, Truck_location):
        self.Depart_time = Depart_time
        self.Truck_capacity = Truck_capacity
        self.Truck_speed = Truck_speed
        self.Packages_loaded = Packages_loaded
        self.Miles_traveled = Miles_traveled
        self.Truck_location = Truck_location


    def __str__(self):
        return " %s, %s, %s, %s, %s, %s" %(self.Depart_time, self.Truck_capacity, self.Truck_speed, self.Packages_loaded, self.Miles_traveled, self.Truck_location)